---
title: The Profile Action
description: The Profile Action
ms.assetid: '07112e9d-8ad9-498d-81ae-6f20666cd865'
---

# The Profile Action

The profile action produces a text file that summarizes the various metrics regarding profiles. The usage for this action is:


```
-a profile [-util [n]] [-detail] [-range T1 [T2]] 
```





| Option                      | Description                                                                                                                                                 |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| util \[n\] <br/>      | Show CPU utilization for *n* second intervals, default 1 second<br/>                                                                                  |
| detail <br/>          | Show CPU samples bucketed by process and module if symbol decoding is not enabled and by process and function name if symbol decoding is enabled<br/> |
| range T1 \[T2\] <br/> | Show data between times T1 and T2, both in use. If T2 is not present, the end of the trace is used instead<br/>                                       |
| freq <br/>            | Show constant sampling frequency zones in the trace<br/>                                                                                              |



 

If no report type is selected, default is to show the CPU utilization report.

 

 





