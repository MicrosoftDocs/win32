---
title: EvictNode method of the CIM\_ClusteringService class
description: Removes a computer system from a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e3629ecc-0cd5-4995-a09b-62e43b6faa0e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["EvictNode method", "EvictNode method, CIM_ClusteringService class", "CIM_ClusteringService class, EvictNode method"]
topic_type:
- apiref
api_name:
- CIM_ClusteringService.EvictNode
api_location:
- WlbsProv.dll
api_type:
- COM
---

# EvictNode method of the CIM\_ClusteringService class

Removes a computer system from a cluster. The node to be evicted is specified as a parameter to the method. The return value should be 0 if the computer system is successfully evicted, 1 if the method is not supported and any other number if an error occurred.

## Syntax


```mof
uint32 EvictNode(
  [in] CIM_ComputerSystem REF CS
);
```



## Parameters

<dl> <dt>

*CS* \[in\]
</dt> <dd>

An embedded instance of a [**CIM\_ComputerSystem**](cim-computersystem.md) class that represents the node to be evicted.

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

 

 





