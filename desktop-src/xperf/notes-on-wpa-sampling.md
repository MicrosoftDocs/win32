---
title: Notes on WPA Sampling
description: Notes on WPA Sampling
ms.assetid: d1624adf-e9da-4738-826a-5cac82c8ab38
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Notes on WPA Sampling

By default, sampling occurs every millisecond. The usage graph is then aggregated based on these samples. To verify the sampling rate enter the command:


```
xperf -ProfInt 
```



The sampling rate can be changed by using the -SetProfInt option. For example:


```
xperf -on PROC_THREAD+PROFILE -SetProfInt 20000 [cached] 
```



The units of SetProfInt are 100 nanosecond time intervals, or a ten-thousandth of a millisecond. This command will set the sampling interval to 2 milliseconds. If "cached" is specified, that sampling interval is cached by WPA. The cached value is applied to all kernel loggers that are subsequently started. \[Default: &lt;n&gt; = 10000; not cached\].

 

 




