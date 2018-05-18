---
title: What's New in DFSR in Windows Server 2008 R2
description: Changes to the Distributed File System Replication (DFSR) WMI provider in Windows Server 2008 R2.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6c936db6-e15f-4f10-be90-0d36a4b80115'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# What's New in DFSR in Windows Server 2008 R2

Windows Server 2008 R2 introduces the following changes to the Distributed File System Replication (DFSR) WMI provider.

## Removal of DFSR Client Support

Beginning with Windows Server 2008 R2, DFSR is available only on Windows Server operating systems. The only client version that supports DFSR is Windows Vista.

## New DFSR WMI Classes

<dl>

[**DfsrIdUpdateInfo**](dfsridupdateinfo.md)  
</dl>

## Existing DFSR WMI Class Modifications

<dl>

[**DfsrReplicatedFolderConfig**](dfsrreplicatedfolderconfig.md) class  
Added methods:  
<dl>

[**Offline**](dfsrreplicatedfolderconfig-offline.md) [**Online**](dfsrreplicatedfolderconfig-online.md)  
</dl>

Added properties:

<dl> **ContainerComputerName**  
**IsClustered**  
**UsnCreated**  
**VcoResourceName**  
</dl> </dd> [**DfsrIdRecordInfo**](dfsridrecordinfo.md) class  
Added properties:  
<dl> **FullPathName** </dl> </dd> <dd>

[**DfsrReplicationGroupConfig**](dfsrreplicationgroupconfig.md) class

Added properties:

<dl> **ContainerComputerName**  
**IsClustered**  
**ReplicationGroupType**  
**VcoResourceName**  
</dl> </dd> [**DfsrVolumeConfig**](dfsrvolumeconfig.md)  
Added properties:  
<dl> **ClusterDiskResName** **IsClustered**  
**MaxJetSessions**  
**UsnCheckPoint**  
</dl> </dd> </dl>

 

 




