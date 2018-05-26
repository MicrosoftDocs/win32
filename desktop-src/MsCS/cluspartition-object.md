---
title: ClusPartition object
description: Provides information about a partition on a Physical Disk resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b7af8ab1-83dc-4164-bf59-901cc9fae56f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusPartition object Failover Cluster
- ClusPartition object Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusPartition
- ISClusPartition
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ClusPartition object

\[The **ClusPartition** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides information about a partition on a [Physical Disk](physical-disk.md) resource.

## Members

The **ClusPartition** object has these types of members:

-   [Properties](#properties)

### Properties

The **ClusPartition** object has these properties.



| Property                                                                          | Access type          | Description                                                                                 |
|:----------------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------|
| [**DeviceName**](cluspartition-devicename.md)<br/>                         | Read-only<br/> | Returns the partition's device name.<br/>                                             |
| [**FileSystem**](cluspartition-filesystem.md)<br/>                         | Read-only<br/> | Returns the partition's file system.<br/>                                             |
| [**FileSystemFlags**](cluspartition-filesystemflags.md)<br/>               | Read-only<br/> | Returns any descriptive flags associated with the partition's file system.<br/>       |
| [**Flags**](cluspartition-flags.md)<br/>                                   | Read-only<br/> | Returns any descriptive flags associated with the partition.<br/>                     |
| [**MaximumComponentLength**](cluspartition-maximumcomponentlength.md)<br/> | Read-only<br/> | Returns the maximum length allowed by the file system for a file name component.<br/> |
| [**SerialNumber**](cluspartition-serialnumber.md)<br/>                     | Read-only<br/> | Returns the partition's serial number.<br/>                                           |
| [**VolumeLabel**](cluspartition-volumelabel.md)<br/>                       | Read-only<br/> | Returns the volume label of the partition.<br/>                                       |



 

## Remarks

A **ClusPartition** object:

-   Is obtained from [**ClusPartitions.Item**](cluspartitions-item.md).

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

[Resource Management Objects](resource-management-objects.md)
</dt> </dl>

 

 





