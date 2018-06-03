---
Description: Stops the collector. If the collector is running as a service, stopping the service is the better approach.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fab3e060-156f-46f5-98a2-d47a23d64552
ms.prod: windows-server-dev
ms.technology:
- boot-event-collector
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Shutdown method of the Control class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shutdown method of the Control class

Stops the collector. If the collector is running as a service, stopping the service is the better approach.

## Syntax


```mof
void Shutdown();
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
| MOF<br/>                      | <dl> <dt>BootEventCollectorWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>BEvtCol.exe</dt> </dl>               |



## See also

<dl> <dt>

[**Control**](control.md)
</dt> </dl>

 

 




