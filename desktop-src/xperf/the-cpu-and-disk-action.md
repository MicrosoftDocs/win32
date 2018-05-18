---
title: The CPU and Disk Action
description: The CPU and Disk Action
ms.assetid: '86371865-858a-4119-be91-42207db22c03'
---

# The CPU and Disk Action

The CPU and disk action produces a text report that summarizes the various metrics regarding the CPU and disk. The command line options for CPU and disk are:


```
-a cpudisk [-thread] [-exc_dpcisr]  [-pids ...] [-exes ..] [-marks ..] [-times ..] 
```





| Option                  | Description                     |
|-------------------------|---------------------------------|
| thread <br/>      | Thread-level report <br/> |
| exc\_dpcisr <br/> | Exclude DPC/ISR time<br/> |



 

DPC/ISR times are excluded from process/thread time if DPC/ISR events are present in the trace. For process filtering, the options in the following table are available.



| Option                        | Description                                       |
|-------------------------------|---------------------------------------------------|
| pids &lt;pid&gt; <br/>  | Process Ids to include in the report <br/>  |
| exes &lt;name&gt; <br/> | Process names to include in the report<br/> |



 

If no **-pids** or **-exes** is specified, all processes will be included in the report. For time filtering, the options in the following table are available.



| Option                                  | Description                                                            |
|-----------------------------------------|------------------------------------------------------------------------|
| marks &lt;mark&gt; <br/>          | Marks that determine the time intervals in the report <br/>      |
| times &lt;ts&gt; &lt;ts&gt; <br/> | Timestamps that determine the time intervals in the report <br/> |



 

If no **-marks** or **-times** are specified, all marks in the traces, or the trace start and end time if less than two marks are present in the trace, will be used to determine the report time intervals.

 

 





