import pandas as pd
import numpy as np
from scipy.integrate import solve_ivp

class ShipData():

    def __init__(self,t_max=10000, dt=0.1, seed=42):
        self.t_max = t_max
        self.dt=dt
        self.seed=seed
        self.data_real = self.generate_data()
        self.data_measure = self.measure()

    def measure(self,accuracy=0.005, measured=['u','u_w','P']):

        data_real = self.data_real
        df_noise = pd.DataFrame(index=data_real.index)
        np.random.seed(self.seed)
        for key in data_real:

            scale = accuracy*data_real[key].abs().max()
            noise = np.random.normal(loc=0, scale=scale, size=len(data_real))
            df_noise[key]=noise

        data_noise = data_real + df_noise
        self.data_measure = data_noise[measured]
        
        return self.data_measure

    def generate_data(self):
        """Load data from mysterious ship

        Args:
            n (int, optional): [description]. Defaults to 1000.
        """

        np.random.seed(self.seed)

        ship_data = pd.Series()
        ship_data['m'] = 10000
        ship_data['B'] = 20
        ship_data['H'] = 30
        ship_data['A_t'] = ship_data.B*ship_data.H
        ship_data['cx'] = 0.01

        t = np.arange(0,self.t_max, self.dt)

        controls = pd.DataFrame(index=t)
        controls['T'] = 1000

        df_wind = wind(t=t, u_mean=10, gust_mean=0.1,  gust_std=0.5, t_mean=300, t_std=100, components=10, seed=self.seed)
        controls['u_w'] = df_wind['u']
        controls['fx_wind'] = -ship_data.cx*controls['u_w']**2

        df = simulate(t=t, controls=controls, ship_data=ship_data)
        df['P'] = controls['T']*df['u']
        data = pd.concat([df,controls], axis=1)

        return data

def simulate(t, controls, ship_data):

    y0 = [
        7,  # u
    ]
    solution = solve_ivp(fun=step, t_span=[t[0],t[-1]], y0=y0, t_eval=t, args=(controls, ship_data))
    df = pd.DataFrame(data=solution.y.T, columns=['u'], index=t)

    return df

def wind(t, u_mean, gust_mean, gust_std, t_mean, t_std, components=10, seed=42):

    np.random.seed(seed)

    u_amplitudes = np.random.normal(loc=gust_mean/components, scale=gust_std, size=components)
    ts = np.random.normal(loc=t_mean, scale=t_std, size=components)

    phase_limits = t[-1]
    phases = phase_limits*np.random.rand(components)
    
    df = pd.DataFrame(index=t)
    for i,(u_amplitude,T,phase) in enumerate(zip(u_amplitudes,ts,phases)):
        omega = 2*np.pi/T

        df[i] = u_amplitude*np.sin(omega*t - phase)

    df['u'] = u_mean+df.sum(axis=1)
    
    return df


def resistance(u):
    return 10*u**2

def step(t,states, controls, ship_data):

    u = states

    index = np.argmin(np.abs(np.array(controls.index)-t))
    control = controls.iloc[index]
    T = control['T']
    fx_wind = control['fx_wind']*ship_data.A_t

    fx = T - resistance(u) + fx_wind
    u1d = fx/ship_data.m

    dstates = [u1d]

    return dstates









