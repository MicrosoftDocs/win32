---
title: Cluster.CommonProperties property
description: Returns the read/write common properties of a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 99de61b9-2979-404a-bbed-94d6f5eea2da
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CommonProperties property Failover Cluster
- CommonProperties property Failover Cluster , Cluster object
- Cluster object Failover Cluster , CommonProperties property
topic_type:
- apiref
api_name:
- Cluster.CommonProperties
- ISCluster.get_CommonProperties
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Cluster.CommonProperties property

\[The **CommonProperties** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the read/write [common properties](common-properties.md) of a [*cluster*](c-gly.md#-wolf-cluster-gly).

This property is read-only.

## Syntax


```VB
Cluster.CommonProperties
```



## Property value

[**ClusProperties**](clusproperties-collection.md) collection that receives the read/write common properties of the cluster.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCluster is defined as F2E606E4-2631-11D1-89F1-00A0C90D061E<br/>          |



## See also

<dl> <dt>

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





