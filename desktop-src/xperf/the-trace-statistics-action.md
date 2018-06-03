---
title: The Trace Statistics Action
description: The Trace Statistics Action
ms.assetid: 657115df-bc14-4782-ae0b-d72411955f5d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# The Trace Statistics Action

The trace statistics action produces a text file that summarizes the various metrics regarding trace statistics. The usage for this action is:


```
-a tracestats [-timespan [actual]] 
              [-detail]  
              [-timezone {utc | local}] 
```





| Option                               | Description                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| timespan \[actual\] <br/>      | Show information about session and traces. Without parameters, -timespan requires inspection of trace headers only; no pass is performed through the traces in the session. When the parameter "actual" is specified, the actual times of the first event and the last event in the session are added to the report. In this case, a pass through the traces in the session is required. <br/> |
| detail <br/>                   | Show detailed information about providers, IDs, tasks, opcodes, versions, channels, and levels of events in the session along with provider and opcode friendly names. Requires a full pass through the traces in the session. <br/>                                                                                                                                                           |
| timezone {utc \| local } <br/> | Show timestamps in specified time zone. <br/>                                                                                                                                                                                                                                                                                                                                                  |



 

If no time zone is specified, the local time zone is used by default.

 

 





