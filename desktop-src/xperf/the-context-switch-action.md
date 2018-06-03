---
title: The Context Switch Action
description: The Context Switch Action
ms.assetid: ca40312e-6916-49d0-8943-2a9ce6522471
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# The Context Switch Action

The context switch action produces a report file that summarizes the various metrics regarding context switches. The usage for this action is:


```
-a cswitch [-util [n] -process -thread -exc_dpcisr -range T1 T2] 
```





| Option                  | Description                                                                                                                                                                        |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| avail \[n\] <br/> | Show CPU availability for n second intervals, default 1 second <br/>                                                                                                         |
| util \[n\] <br/>  | Show CPU utilization for n second intervals, default 1 second <br/>                                                                                                          |
| process <br/>     | Show CPU usage per process as deduced from context switch data <br/>                                                                                                         |
| thread <br/>      | Show CPU usage per thread as deduced from context switch data <br/>                                                                                                          |
| exc\_dpcisr <br/> | Exclude time spent in DPC/ISR in availability, utilization process and thread reports. DPC/Interrupt tracing must have been enabled for this option to have any effect <br/> |
| range T1 T2 <br/> | Show data between times T1 and T2, both in use <br/>                                                                                                                         |



 

If no report type is selected, default is to show CPU availability report.

 

 





