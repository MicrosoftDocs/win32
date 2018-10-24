---
Description: Stop the collector quickly, discarding all the queued data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9d96a94b-21ae-40bd-9c7f-b466ca38dce3
- boot-event-collector
- windows-management-instrumentation
ms.tgt_platform: multiple
title: FastShutdown method of the Control class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Control.FastShutdown
api_type: 
- COM
api_location: 
- BEvtCol.exe
---

# FastShutdown method of the Control class

Stop the collector quickly, discarding all the queued data.

## Syntax


```mof
void FastShutdown();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                       |
| Namespace<br/>                | Root\\Microsoft\\Windows\\BootEventCollector<br/>                                              |
| MOF<br/>                      | <dl> <dt>BootEventCollectorWMI.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>BEvtCol.exe</dt> </dl>               |



## See also

<dl> <dt>

[**Control**](control.md)
</dt> </dl>

 

 




