---
title: Calculating Usage Graphs
description: Calculating Usage Graphs
ms.assetid: '4540401a-aa63-46f1-a083-f6fa659c3dde'
---

# Calculating Usage Graphs

When computing graph values, WPA calculates a weighted average of the data points within a given time interval. Weights are taken to be the proportion of the intersection of the interval with the size of the bucket. For instance, if in time slot T, data point P1 takes 80% of the time and data point P2 takes 20% of the time then we add them as (80% x *Y value of P1*) + (20% x *Y value of P2*). For sampled graphs, interval is taken to be the distance between two adjacent samples.

 

 




