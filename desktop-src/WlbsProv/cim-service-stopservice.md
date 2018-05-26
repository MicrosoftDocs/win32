---
title: StopService method of the CIM\_Service class
description: Places the service in the stopped state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 652b7fe8-1563-4903-ae24-dfedffb2b41b
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- StopService method
- StopService method, CIM_Service class
- CIM_Service class, StopService method
topic_type:
- apiref
api_name:
- CIM_Service.StopService
api_location:
- WlbsProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# StopService method of the CIM\_Service class

Places the service in the stopped state.

## Syntax


```mof
uint32 StopService();
```



## Parameters

This method has no parameters.

## Return value

Returns an integer value of 0 if the service was successfully started, 1 if the request is not supported and any other number to indicate an error.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| Header<br/>                   | <dl> <dt>Sdoias.h</dt> </dl>     |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Service**](cim-service.md)
</dt> </dl>

 

 





