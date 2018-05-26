---
title: The Dumper Action
description: The Dumper Action
ms.assetid: 2a0eaa98-3bb3-4b90-a649-98e90d058ca5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# The Dumper Action

The dumper action produces an ANSI text file of the ETL trace log. The usage for this action is:


```
-a dumper [-range T1 T2] [-exc_dpcisr] [-stacktimeshifting] 
```





| Option                        | Description                                                                                                                                                                           |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| range T1 T2 <br/>       | Dump only data between times T1 and T2 <br/>                                                                                                                                    |
| stacktimeshifting <br/> | Time shift stacks right after trigger event <br/>                                                                                                                               |
| exc\_dpcisr <br/>       | Add reports excluding time spent in DPCs/ISRs. DPC/Interrupt tracing must have been enabled for this option to have any effect. Currently this effects only CSwitch events<br/> |



 

 

 





