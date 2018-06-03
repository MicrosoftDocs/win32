---
title: Introduction
description: Introduction
ms.assetid: 8dfb15eb-6505-4afd-9036-a449f3ceedc3
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Introduction

The On/Off Transition Trace Capture tool collects information during the on/off transition phases of Windows Vista. Data can be captured during any of the following phases:

-   Boot

-   Shutdown

-   Standby and resume

-   Hibernate and resume

> [!Note]  
> Be aware that On/Off Transition Trace Capture tool automates state transitions. After issuing a trace command, the test computer resets within five seconds.

 

The On/Off Transition Trace Capture tool can capture data during all of these phases and additionally can automate a *reboot cycle* during which the Windows Vista system is shut down and rebooted multiple times. You can analyze the captured data by using the Xperf and Xperfview tools.

The following table lists the options that you should use to capture and analyze traces from each of the transitions. For more information, see the [Reference](reference.md) section later in this documentation.



| Power state transition to examine  | To create the trace, type:xbootmgrfollowed by | To analyze the trace, type:xperf -i \[filename\]followed by       |
|------------------------------------|-----------------------------------------------|-------------------------------------------------------------------|
| Boot<br/>                    | -trace boot<br/>                        | -a boot<br/>                                                |
| Shutdown<br/>                | -trace shutdown<br/>                    | -a shutdown<br/>                                            |
| Standby and resume<br/>      | -trace standby<br/>                     | -a suspend<br/>                                             |
| Hibernate and resume<br/>    | -trace hibernate<br/>                   | -a suspend<br/>                                             |
| Boot and shutdown cycle<br/> | -trace rebootCycle<br/>                 | -a boot<br/> Followed by:<br/> -a shutdown<br/> |



 

 

 





