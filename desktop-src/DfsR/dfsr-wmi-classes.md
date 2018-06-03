---
title: DFSR WMI Classes
description: The DfsrWmiV2.mof file defines the Distributed File System Replication (DFSR) WMI V2 provider, including association and registration classes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 202ff6cf-c964-4bdd-b87c-7b835ebf1ddb
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Distributed File System Replication Files , reference
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DFSR WMI Classes

The DfsrWmiV2.mof file defines the Distributed File System Replication (DFSR) WMI V2 provider, including association and registration classes. The DfsRProvs.mof file defines the DFSR WMI V1 provider, including association and registration classes. You can access the DFSR provider classes in the "Root\\MicrosoftDfs" namespace. For more information about WMI, see [Windows Management Instrumentation](https://msdn.microsoft.com/library/aa394582).

## In this section

<dl> <dt>

[CONFIG\_STATUS Return Codes](config-status-return-codes.md)
</dt> <dd>

The following error codes can be returned by the configuration WMI classes for DFSR.

</dd> <dt>

[MONITOR\_STATUS Return Codes](monitor-status-return-codes.md)
</dt> <dd>

The following error codes can be returned by the information WMI classes for DFSR.

</dd> <dt>

[**DfsrConfig**](dfsrconfig.md)
</dt> <dd>

This class is a DFSR configuration provider class. It includes provider-specific settings in addition to computer-wide service configuration parameters and methods.

</dd> <dt>

[**DfsrConflictInfo**](dfsrconflictinfo.md)
</dt> <dd>

This class provides details about the files and folders that were moved to the Conflict and Deleted folder due to conflicting updates.

</dd> <dt>

[**DfsrConnectionConfig**](dfsrconnectionconfig.md)
</dt> <dd>

This class provides the configuration settings for a replication group connection. Each connection links a local and remote member, establishing a partnership. Only the connections of the direct partners to the local member have instances of this class.

</dd> <dt>

[**DfsrConnectionInfo**](dfsrconnectioninfo.md)
</dt> <dd>

This class provides statistical and operational information for each incoming and outgoing connection of the local replication group members.

</dd> <dt>

[**DfsrIdRecordInfo**](dfsridrecordinfo.md)
</dt> <dd>

This class provides access to ID Table records. The ID Table has a record for each file and folder known to DFSR. In addition, it keeps records of the deleted content.

</dd> <dt>

[**DfsrIdUpdateInfo**](dfsridupdateinfo.md)
</dt> <dd>

This class provides statistical and operational information about updates that are being transferred by this computer.

</dd> <dt>

[**DfsrInfo**](dfsrinfo.md)
</dt> <dd>

The DFSR monitoring provider class. This singleton class has provider-specific settings in addition to computer-wide service properties and methods.

</dd> <dt>

[**DfsrLocalMemberConfig**](dfsrlocalmemberconfig.md)
</dt> <dd>

This class is for replication group membership. An instance of this class is available for each replication group hosted on this computer. This class maps to the DFSR2-Member class in the Active Directory Domain Services.

</dd> <dt>

[**DfsrLocalMemberInfo**](dfsrlocalmemberinfo.md)
</dt> <dd>

This class provides statistical and operational information for each replication group member hosted on the local computer.

</dd> <dt>

[**DfsrMachineConfig**](dfsrmachineconfig.md)
</dt> <dd>

This class provides service-wide settings on the local computer.

</dd> <dt>

[**DfsrReplicatedFolderConfig**](dfsrreplicatedfolderconfig.md)
</dt> <dd>

An instance of this class is available for each replicated folder that this hosted on this computer. This class provides read-only access to the configuration parameters for the replicated folder.

</dd> <dt>

[**DfsrReplicatedFolderInfo**](dfsrreplicatedfolderinfo.md)
</dt> <dd>

This class provides statistical and operational information for each replicated folder hosted on the local computer.

</dd> <dt>

[**DfsrReplicationGroupConfig**](dfsrreplicationgroupconfig.md)
</dt> <dd>

This class provides read-only access to the replication group configuration parameters.

</dd> <dt>

[**DfsrSyncInfo**](dfsrsyncinfo.md)
</dt> <dd>

This class provides statistical and operational information for active synchronization sessions between the local replication group member and one of its partners.

</dd> <dt>

[**DfsrVolumeConfig**](dfsrvolumeconfig.md)
</dt> <dd>

This class stores the per-volume settings for each volume on the system that hosts one or more replicated folders.

</dd> <dt>

[**DfsrVolumeInfo**](dfsrvolumeinfo.md)
</dt> <dd>

This class provides statistical and operational information for each volume that has or had replicated folders.

</dd> <dt>

[**MSFT\_DfsrConflictInfo**](msft-dfsrconflictinfo.md)
</dt> <dd>

This class provides details about the files and folders that were moved to the Conflict and Deleted folder due to conflicting updates.

</dd> <dt>

[**MSFT\_DfsrConnectionConfig**](msft-dfsrconnectionconfig.md)
</dt> <dd>

This class provides the configuration settings for a replication group connection. Each connection links a local and remote member, establishing a partnership. Only the connections of the direct partners to the local member have instances of this class.

</dd> <dt>

[**MSFT\_DfsrConnectionInfo**](msft-dfsrconnectioninfo.md)
</dt> <dd>

This class provides statistical and operational information for each incoming and outgoing connection of the local replication group members.

</dd> <dt>

[**MSFT\_DfsrIdRecordInfo**](msft-dfsridrecordinfo.md)
</dt> <dd>

This class provides access to ID Table records. The ID Table has a record for each file and folder known to DFSR. In addition, it keeps records of the deleted content.

</dd> <dt>

[**MSFT\_DfsrIdUpdateInfo**](msft-dfsridupdateinfo.md)
</dt> <dd>

This class provides statistical and operational information about updates that are being transferred by this computer.

</dd> <dt>

[**MSFT\_DfsrLocalMemberConfig**](msft-dfsrlocalmemberconfig.md)
</dt> <dd>

This class is for replication group membership. An instance of this class is available for each replication group hosted on this computer. This class maps to the DFSR2-Member class in the Active Directory Domain Services.

</dd> <dt>

[**MSFT\_DfsrLocalMemberInfo**](msft-dfsrlocalmemberinfo.md)
</dt> <dd>

This class provides statistical and operational information for each replication group member hosted on the local computer.

</dd> <dt>

[**MSFT\_DfsrMachineConfig**](msft-dfsrmachineconfig.md)
</dt> <dd>

This class provides service-wide settings on the local computer.

</dd> <dt>

[**MSFT\_DfsrReplicatedFolderConfig**](msft-dfsrreplicatedfolderconfig.md)
</dt> <dd>

An instance of this class is available for each replicated folder that is hosted on this computer. This class provides read-only access to the configuration parameters for the replicated folder.

</dd> <dt>

[**MSFT\_DfsrReplicatedFolderInfo**](msft-dfsrreplicatedfolderinfo.md)
</dt> <dd>

This class provides statistical and operational information for each replicated folder hosted on the local computer.

</dd> <dt>

[**MSFT\_DfsrReplicationGroupConfig**](msft-dfsrreplicationgroupconfig.md)
</dt> <dd>

An instance of this class is available for each replication group that contains this computer. This class provides read-only access to the replication group configuration parameters.

</dd> <dt>

[**MSFT\_DfsrServiceConfig**](msft-dfsrserviceconfig.md)
</dt> <dd>

This class is a DFSR configuration provider class. It includes provider-specific settings in addition to computer-wide service configuration parameters and methods.

</dd> <dt>

[**MSFT\_DfsrServiceInfo**](msft-dfsrserviceinfo.md)
</dt> <dd>

This class is a DFS Replication monitoring provider class. This is a singleton class that has provider-specific settings in addition to computer-wide service configuration parameters and methods.

</dd> <dt>

[**MSFT\_DfsrSyncInfo**](msft-dfsrsyncinfo.md)
</dt> <dd>

This class provides statistical and operational information for active synchronization sessions between the local replication group member and one of its partners.

</dd> <dt>

[**MSFT\_DfsrVolumeConfig**](msft-dfsrvolumeconfig.md)
</dt> <dd>

This class stores the per-volume settings for each volume on the system that hosts one or more replicated folders.

</dd> <dt>

[**MSFT\_DfsrVolumeInfo**](msft-dfsrvolumeinfo.md)
</dt> <dd>

This class provides statistical and operational information for each volume that has or had replicated folders.

</dd> </dl>

## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> </dl>

 

 




