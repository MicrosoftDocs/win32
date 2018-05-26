---
title: ClusPartition.FileSystemFlags property
description: Flags describing the file system of a storage class resource partition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 311e011a-3617-4659-b6cc-777cd57384d7
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- FileSystemFlags property Failover Cluster
- FileSystemFlags property Failover Cluster , ClusPartition object
- ClusPartition object Failover Cluster , FileSystemFlags property
topic_type:
- apiref
api_name:
- ClusPartition.FileSystemFlags
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusPartition.FileSystemFlags property

\[The **FileSystemFlags** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns flags describing the file system of a [*storage class resource*](s-gly.md#-wolf-storage-class-resource-gly) partition.

This property is read-only.

## Syntax


```VB
ClusPartition.FileSystemFlags
```



## Property value

Long that receives the file system flags of the partition. The following flags are valid.

<dt>

<span id="FS_CASE_IS_PRESERVED"></span><span id="fs_case_is_preserved"></span>

<span id="FS_CASE_IS_PRESERVED"></span><span id="fs_case_is_preserved"></span>**FS\_CASE\_IS\_PRESERVED** (0x00000002)


</dt> <dd>

The file system preserves the case of file names when it places a name on the storage class resource.

</dd> <dt>

<span id="FS_CASE_SENSITIVE"></span><span id="fs_case_sensitive"></span>

<span id="FS_CASE_SENSITIVE"></span><span id="fs_case_sensitive"></span>**FS\_CASE\_SENSITIVE** (0x00000001)


</dt> <dd>

The file system supports case-sensitive file names.

</dd> <dt>

<span id="FS_UNICODE_STORED_ON_DISK"></span><span id="fs_unicode_stored_on_disk"></span>

<span id="FS_UNICODE_STORED_ON_DISK"></span><span id="fs_unicode_stored_on_disk"></span>**FS\_UNICODE\_STORED\_ON\_DISK** (0x00000004)


</dt> <dd>

The file system supports Unicode in file names as they appear on storage class resource.

</dd> <dt>

<span id="FS_PERSISTENT_ACLS"></span><span id="fs_persistent_acls"></span>

<span id="FS_PERSISTENT_ACLS"></span><span id="fs_persistent_acls"></span>**FS\_PERSISTENT\_ACLS** (0x00000008)


</dt> <dd>

The file system preserves and enforces access control lists (ACLs).

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusPartition is defined as F2E60720-2631-11D1-89F1-00A0C90D061E<br/>    |



## See also

<dl> <dt>

[**ClusPartition**](cluspartition-object.md)
</dt> </dl>

 

 





