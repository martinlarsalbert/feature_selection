---
title: ICSOS Conference
toc: true
layout: post
description: I presented the paper *Analysis of roll damping model scale data* on the [ICSOS 2020 conference](https://www.icsos.info/). Here are my notes from this conference.
categories: [markdown]
branch: master
comments: true
categories: [dynamics, kalman filter]
image: https://le-cdn.website-editor.net/a88a366fb4174f939aa349fe67bc7d1e/dms3rep/multi/opt/ICSOS-640w.png
hide: false
search_exclude: true
metadata_key1: metadata_value1
metadata_key2: metadata_value2
---
# ICSOS Conference
I presented the paper *Analysis of roll damping model scale data* on the [ICSOS 2020 conference](https://www.icsos.info/). Here are my notes from this conference.

## Notes about papers/presenations

### A dockin simulation framework: model evaluation and expert knowledge data harvesting
A paper by Marco Mirkulec et.al. They have used (pygame)[https://www.pygame.org/] to make a simple simulation for docking simulations, very cool.

### Parameter identification of nonlinear ship maneuvering model using support vector machine method
A paper by Tongtong Wang et.al. about system identification of manoeuvring tests using Support Vector Machine regression (SVR).
* SVM is better than Least Square Fit in handling initial values and noise.
* 3DOF Abkowitz model i used
* Linear kernel in SVM
* The system identification works extremly good (I'm impressed).

### Fast Virtual Prototyping a case study with the RV Gunnerus reaseach vessel
A paper by Pierre Major et.al.
* Digital twin = predictin an existing ship (usually a lot of measurement data avaliable)
* Virtual prototype = Nonexistong ship (usually less data avaliable)
* (opensimulationplatform)[https://opensimulationplatform.com/]
* (fhsim)[https://fhsim.no/docs/licence.html]
* (fmi-standard)[https://fmi-standard.org/]
