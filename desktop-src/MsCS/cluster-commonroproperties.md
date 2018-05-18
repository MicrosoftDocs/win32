---
title: Cluster.CommonROProperties property
description: Returns the read-only common properties of a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fcd27e3b-4895-445f-a578-f08ccd110a99'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CommonROProperties property Failover Cluster", "CommonROProperties property Failover Cluster , Cluster object", "Cluster object Failover Cluster , CommonROProperties property"]
topic_type:
- apiref
api_name:
- Cluster.CommonROProperties
- ISCluster.get_CommonROProperties
api_location:
- MsClus.dll
api_type:
- COM
---

# Cluster.CommonROProperties property

\[The **CommonROProperties** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the read-only [common properties](common-properties.md) of a [*cluster*](c-gly.md#-wolf-cluster-gly).

This property is read-only.

## Syntax


```VB
Cluster.CommonROProperties
```



## Property value

A [**ClusProperties**](clusproperties-collection.md) collection that receives the read-only common properties of the cluster.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCluster is defined as F2E606E4-2631-11D1-89F1-00A0C90D061E<br/>          |



## See also

<dl> <dt>

[**ClusProperties**](clusproperties-collection.md)
</dt> <dt>

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





