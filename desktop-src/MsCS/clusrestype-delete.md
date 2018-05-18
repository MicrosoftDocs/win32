---
title: ClusResType.Delete method
description: Deletes the resource type from the cluster and unregisters the type with the Cluster service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b71789a5-7e88-418e-acf4-f28f60b03e3a'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Delete method Failover Cluster", "Delete method Failover Cluster , ClusResType object", "ClusResType object Failover Cluster , Delete method"]
topic_type:
- apiref
api_name:
- ClusResType.Delete
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResType.Delete method

\[The **Delete** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes the [resource type](resource-types.md) from the [*cluster*](c-gly.md#-wolf-cluster-gly) and unregisters the type with the [*Cluster service*](c-gly.md#-wolf-cluster-service-gly).

## Syntax


```VB
ClusResType.Delete()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method will fail if any resources of the specified type exist in the cluster. Once a resource type is deleted, no resources of that type can be created in the cluster until the resource type is re-created.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResType is defined as F2E60710-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[**ClusResType**](clusrestype-object.md)
</dt> </dl>

 

 





