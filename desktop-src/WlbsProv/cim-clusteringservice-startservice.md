---
title: StartService method of the CIM\_ClusteringService class
description: Places the service in the started state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c0d6b833-0662-4fd8-853c-40bf8cf45f02'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["StartService method", "StartService method, CIM_ClusteringService class", "CIM_ClusteringService class, StartService method"]
topic_type:
- apiref
api_name:
- CIM_ClusteringService.StartService
api_location:
- WlbsProv.dll
api_type:
- COM
---

# StartService method of the CIM\_ClusteringService class

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
</dt> <dt>

[**CIM\_ClusteringService**](cim-clusteringservice.md)
</dt> </dl>

 

 





