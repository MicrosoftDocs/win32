---
title: Cluster.Name property
description: Retrieves or sets the name of the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8d42bb44-f4af-49f3-b6c9-055625739557
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Name property Failover Cluster
- Name property Failover Cluster , Cluster object
- Cluster object Failover Cluster , Name property
topic_type:
- apiref
api_name:
- Cluster.Name
- ISCluster.get_Name
- ISCluster.put_Name
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Cluster.Name property

\[The **Name** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves or sets the name of the [*cluster*](c-gly.md#-wolf-cluster-gly).

This property is read/write.

## Syntax


```VB
Cluster.Name
```



## Property value

**String** containing the new name of the cluster.

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

 

 





