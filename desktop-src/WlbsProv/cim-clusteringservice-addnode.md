---
title: AddNode method of the CIM\_ClusteringService class
description: Brings a new computer system into a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '972b39d6-3464-47fb-9caf-c4b078f30142'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddNode method", "AddNode method, CIM_ClusteringService class", "CIM_ClusteringService class, AddNode method"]
---

# AddNode method of the CIM\_ClusteringService class

Brings a new computer system into a cluster. The node to be added is specified as a parameter to the method. The return value should be 0 if the computer system is successfully added, 1 if the method is not supported and any other number if an error occurred.

## Syntax


```mof
uint32 AddNode(
  [in] CIM_ComputerSystem REF CS
);
```



## Parameters

<dl> <dt>

*CS* \[in\]
</dt> <dd>

TBD

</dd> </dl>

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

[**CIM\_ClusteringService**](cim-clusteringservice.md)
</dt> </dl>

 

 





