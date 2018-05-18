---
title: Cluster.QuorumLogSize property
description: Returns or sets the maximum size of the log file maintained by the quorum resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '38dff875-1fb9-4173-9d47-a9a9643770fe'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["QuorumLogSize property Failover Cluster", "QuorumLogSize property Failover Cluster , Cluster object", "Cluster object Failover Cluster , QuorumLogSize property"]
topic_type:
- apiref
api_name:
- Cluster.QuorumLogSize
- ISCluster.get_QuorumLogSize
- ISCluster.put_QuorumLogSize
api_location:
- MsClus.dll
api_type:
- COM
---

# Cluster.QuorumLogSize property

\[The **QuorumLogSize** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns or sets the maximum size of the log file maintained by the [quorum resource](quorum-resource.md).

This property is read/write.

## Syntax


```VB
Cluster.QuorumLogSize
```



## Property value

**Long** specifying the maximum log file size.

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

[**Cluster.QuorumResource**](cluster-quorumresource.md)
</dt> </dl>

 

 





