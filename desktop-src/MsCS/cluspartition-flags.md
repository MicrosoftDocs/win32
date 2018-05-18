---
title: ClusPartition.Flags property
description: Flags set for a storage class resource partition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '19a69c92-495c-486d-9f42-6b0531dfb992'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Flags property Failover Cluster", "Flags property Failover Cluster , ClusPartition object", "ClusPartition object Failover Cluster , Flags property"]
topic_type:
- apiref
api_name:
- ClusPartition.Flags
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusPartition.Flags property

\[The **Flags** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the flags set for a [*storage class resource*](s-gly.md#-wolf-storage-class-resource-gly) partition.

This property is read-only.

## Syntax


```VB
ClusPartition.Flags
```



## Property value

**Long** that receives the flags of the storage class resource, enumerated by the [**CLUSPROP\_PIFLAGS**](clusprop-piflags.md) enumeration.

<dt>

<span id="CLUSPROP_PIFLAG_STICKY"></span><span id="clusprop_piflag_sticky"></span>

<span id="CLUSPROP_PIFLAG_STICKY"></span><span id="clusprop_piflag_sticky"></span>**CLUSPROP\_PIFLAG\_STICKY** (0x00000001)


</dt> <dd>

The drive letter is sticky.

</dd> <dt>

<span id="CLUSPROP_PIFLAG_REMOVABLE"></span><span id="clusprop_piflag_removable"></span>

<span id="CLUSPROP_PIFLAG_REMOVABLE"></span><span id="clusprop_piflag_removable"></span>**CLUSPROP\_PIFLAG\_REMOVABLE** (0x00000002)


</dt> <dd>

The storage class resource is removable.

</dd> <dt>

<span id="CLUSPROP_PIFLAG_USABLE"></span><span id="clusprop_piflag_usable"></span>

<span id="CLUSPROP_PIFLAG_USABLE"></span><span id="clusprop_piflag_usable"></span>**CLUSPROP\_PIFLAG\_USABLE** (0x00000004)


</dt> <dd>

The storage class resource is formatted with a file system that is usable by the [Cluster service](cluster-service.md).

</dd> <dt>

<span id="CLUSPROP_PIFLAG_DEFAULT_QUORUM"></span><span id="clusprop_piflag_default_quorum"></span>

<span id="CLUSPROP_PIFLAG_DEFAULT_QUORUM"></span><span id="clusprop_piflag_default_quorum"></span>**CLUSPROP\_PIFLAG\_DEFAULT\_QUORUM** (0x00000008)


</dt> <dd>

The partition should be used to store quorum files if no partition is specified in the [**SetClusterQuorumResource**](setclusterquorumresource.md) function. For [Physical Disk](physical-disk.md) resources, the smallest NTFS partition larger than 50MB automatically receives this flag.

</dd> </dl>

## Remarks

For information on making constants defined by the Cluster Automation Server type library (MsClus.tlb) available to scripts, see [Creating a Cluster Automation Server Script](creating-a-cluster-automation-server-script.md).

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
</dt> <dt>

[**CLUSPROP\_PIFLAGS**](clusprop-piflags.md)
</dt> </dl>

 

 





