---
title: ClusResType.Resources property
description: Returns a ClusResTypeResources collection providing access to the resources of a particular type in the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2fa27a3c-c340-478a-af05-1583efb420b4'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Resources property Failover Cluster", "Resources property Failover Cluster , ClusResType object", "ClusResType object Failover Cluster , Resources property"]
topic_type:
- apiref
api_name:
- ClusResType.Resources
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResType.Resources property

\[The **Resources** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusResTypeResources**](clusrestyperesources-collection.md) collection providing access to the [resources](resources.md) of a particular [type](resource-types.md) in the [*cluster*](c-gly.md#-wolf-cluster-gly).

This property is read-only.

## Syntax


```VB
ClusResType.Resources
```



## Property value

A [**ClusResTypeResources**](clusrestyperesources-collection.md) collection that receives the resources.

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
</dt> <dt>

[**ClusResTypeResources**](clusrestyperesources-collection.md)
</dt> </dl>

 

 





