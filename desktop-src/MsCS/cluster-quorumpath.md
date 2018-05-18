---
title: Cluster.QuorumPath property
description: Retrieves or sets the path to the log file maintained by the quorum resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5f1c6a47-5f28-40b7-9b36-551335ac72d4'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["QuorumPath property Failover Cluster", "QuorumPath property Failover Cluster , Cluster object", "Cluster object Failover Cluster , QuorumPath property"]
topic_type:
- apiref
api_name:
- Cluster.QuorumPath
- ISCluster.get_QuorumPath
- ISCluster.put_QuorumPath
api_location:
- MsClus.dll
api_type:
- COM
---

# Cluster.QuorumPath property

\[The **QuorumPath** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves or sets the path to the log file maintained by the [quorum resource](quorum-resource.md).

This property is read/write.

## Syntax


```VB
Cluster.QuorumPath
```



## Property value

**String** containing the path to the quorum log file.

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

[**Cluster**](cluster-object.md)
</dt> <dt>

[**Cluster.QuorumLogSize**](cluster-quorumlogsize.md)
</dt> <dt>

[**Cluster.QuorumResource**](cluster-quorumresource.md)
</dt> </dl>

 

 





