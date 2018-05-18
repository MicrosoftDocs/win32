---
title: StartService method of the CIM\_Service class
description: Places the service in the started state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c1c450dc-2dda-40cd-b75b-7cbc78043525'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["StartService method", "StartService method, CIM_Service class", "CIM_Service class, StartService method"]
topic_type:
- apiref
api_name:
- CIM_Service.StartService
api_location:
- WlbsProv.dll
api_type:
- COM
---

# StartService method of the CIM\_Service class

Places the service in the started state.

## Syntax


```mof
uint32 StartService();
```



## Parameters

This method has no parameters.

## Return value

Returns an integer value of 0 if the service was successfully started, 1 if the request is not supported and any other number to indicate an error.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Service**](cim-service.md)
</dt> </dl>

 

 





