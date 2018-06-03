---
title: MSFT\_DfsrVolumeConfig class
description: This class stores the per-volume settings for each volume on the system that hosts one or more replicated folders.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 767e0ed1-fbc0-410d-801c-eb221a60b454
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DfsrVolumeConfig class Distributed File System Replication
- MSFT_DfsrVolumeConfig class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- MSFT_DfsrVolumeConfig
- MSFT_DfsrVolumeConfig.VolumeGuid
- MSFT_DfsrVolumeConfig.SerialNumber
- MSFT_DfsrVolumeConfig.VolumePath
- MSFT_DfsrVolumeConfig.LastChangeNumber
- MSFT_DfsrVolumeConfig.LastChangeTime
- MSFT_DfsrVolumeConfig.LastChangeSource
- MSFT_DfsrVolumeConfig.DatabasePath
- MSFT_DfsrVolumeConfig.MinNtfsJournalSizeInMb
- MSFT_DfsrVolumeConfig.UsnCheckPoint
- MSFT_DfsrVolumeConfig.MaxJetSessions
- MSFT_DfsrVolumeConfig.IsClustered
- MSFT_DfsrVolumeConfig.ClusterDiskResName
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DfsrVolumeConfig class

This class stores the per-volume settings for each volume on the system that hosts one or more replicated folders.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrVolumeConfig
{
  string   VolumeGuid;
  uint64   SerialNumber;
  string   VolumePath;
  uint32   LastChangeNumber;
  datetime LastChangeTime;
  string   LastChangeSource;
  string   DatabasePath;
  uint32   MinNtfsJournalSizeInMb;
  uint32   UsnCheckPoint;
  uint32   MaxJetSessions;
  boolean  IsClustered;
  string   ClusterDiskResName;
};
```

## Members

The **MSFT\_DfsrVolumeConfig** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DfsrVolumeConfig** class has these methods.



| Method                                                               | Description                                                                                                                  |
|:---------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| [**ExportDBClone**](msft-dfsrvolumeconfig-exportdbclone.md)         | Starts the process of exporting the Distributed File System Replication (DFSR) database for the specified volume.<br/> |
| [**GetDBCloneState**](msft-dfsrvolumeconfig-getdbclonestate.md)     | Returns the current state of the database export or import process.<br/>                                               |
| [**ImportDBClone**](msft-dfsrvolumeconfig-importdbclone.md)         | Starts the process of importing the specified Distributed File System Replication (DFSR) volume database.<br/>         |
| [**ResetDBClone**](msft-dfsrvolumeconfig-resetdbclone.md)           | Stops the current database export or import operation and returns the database to its previous state.<br/>             |
| [**ResumeReplication**](resumereplication-msft-dfsrvolumeconfig.md) | Resumes replication for the volume.<br/>                                                                               |



 

### Properties

The **MSFT\_DfsrVolumeConfig** class has these properties.

<dl> <dt>

**ClusterDiskResName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Clustered Volume Physical Disk Resource Name")
</dt> </dl>

If the volume is a cluster shared volume, this property specifies the physical disk resource name.

</dd> <dt>

**DatabasePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (2600), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Database Path")
</dt> </dl>

The full path to the database. This database contains metadata about the files and folders in the replicated folder.

</dd> <dt>

**IsClustered**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Is a clustered Volume")
</dt> </dl>

This property is **TRUE** if the volume is a cluster shared volume; it is **FALSE** if it is a local volume.

</dd> <dt>

**LastChangeNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("1"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Change Number")
</dt> </dl>

The configuration sequence number. This value is incremented each time the volume configuration changes.

</dd> <dt>

**LastChangeSource**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Change Source")
</dt> </dl>

Information about the originator of the last configuration change. The originator is the name of the domain controller that provided the configuration information.

</dd> <dt>

**LastChangeTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Change Time")
</dt> </dl>

The time stamp of the last configuration change.

</dd> <dt>

**MaxJetSessions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("16"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Maximum number of Jet Sessions")
</dt> </dl>

The maximum number of concurrent Jet database sessions for this volume. Every volume has its own database, and therefore this parameter is defined per-volume.

</dd> <dt>

**MinNtfsJournalSizeInMb**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("4"), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) ("10000"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("MB"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Minimum USN Journal Size in MB")
</dt> </dl>

The minimum size of the journal to allocate on the volume, in megabytes. If no journal exists, the DFSR creates a new journal with the specified size; otherwise, it increases the existing journal size to this minimum size. The DFSR does not change the existing journal size if it is already larger than the new minimum size.

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Volume Serial Number")
</dt> </dl>

The volume serial number.

</dd> <dt>

**UsnCheckPoint**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("1"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Usn Check Point")
</dt> </dl>

The number of journal updates to accumulate before committing a transaction.

</dd> <dt>

**VolumeGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Volume GUID")
</dt> </dl>

The unique volume identifier.

</dd> <dt>

**VolumePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Volume Path")
</dt> </dl>

The volume path name.

This string has one of the following formats: "\\\\.\\*drive*:" or "\\\\?\\*volume*{*GUID*}".

</dd> </dl>

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





