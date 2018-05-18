---
title: ClusPartition.MaximumComponentLength property
description: Maximum component length of a storage class resource partition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9b664155-617a-4a3c-9c48-0e9fc9e206ba'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["MaximumComponentLength property Failover Cluster", "MaximumComponentLength property Failover Cluster , ClusPartition object", "ClusPartition object Failover Cluster , MaximumComponentLength property"]
topic_type:
- apiref
api_name:
- ClusPartition.MaximumComponentLength
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusPartition.MaximumComponentLength property

\[The **MaximumComponentLength** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the maximum component length of a [*storage class resource*](s-gly.md#-wolf-storage-class-resource-gly) partition.

This property is read-only.

## Syntax


```VB
ClusPartition.MaximumComponentLength
```



## Property value

**Long** that receives the maximum component length of the partition.

## Remarks

The maximum component length is the maximum number of characters allowed between backslashes in a file or path name.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusPartition is defined as F2E60720-2631-11D1-89F1-00A0C90D061E<br/>    |



## See also

<dl> <dt>

[**ClusPartition**](cluspartition-object.md)
</dt> </dl>

 

 





