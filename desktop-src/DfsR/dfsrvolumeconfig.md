---
title: DfsrVolumeConfig class
description: This class stores the per-volume settings for each volume on the system that hosts one or more replicated folders.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c501ada0-6c5c-44f5-8fb3-c4850b2d5463
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DfsrVolumeConfig class Distributed File System Replication
- DfsrVolumeConfig class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- DfsrVolumeConfig
- DfsrVolumeConfig.Caption
- DfsrVolumeConfig.Description
- DfsrVolumeConfig.SettingID
- DfsrVolumeConfig.VolumeGuid
- DfsrVolumeConfig.SerialNumber
- DfsrVolumeConfig.VolumePath
- DfsrVolumeConfig.LastChangeNumber
- DfsrVolumeConfig.LastChangeTime
- DfsrVolumeConfig.LastChangeSource
- DfsrVolumeConfig.DatabasePath
- DfsrVolumeConfig.MinNtfsJournalSizeInMb
- DfsrVolumeConfig.UsnCheckPoint
- DfsrVolumeConfig.MaxJetSessions
- DfsrVolumeConfig.IsClustered
- DfsrVolumeConfig.ClusterDiskResName
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DfsrVolumeConfig class

This class stores the per-volume settings for each volume on the system that hosts one or more replicated folders.

## Syntax

``` syntax
[Dynamic, Provider("DfsrConfigProv")]
class DfsrVolumeConfig : CIM_Setting
{
  string   Caption;
  string   Description;
  string   SettingID;
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

The **DfsrVolumeConfig** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **DfsrVolumeConfig** class has these methods.



| Method                                                          | Description                                                                                                                                                                                                  |
|:----------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ResumeReplication**](resumereplication-dfsrvolumeconfig.md) | Resumes replication for the volume.<br/> **Windows Server 2012, Windows Server 2008 R2, Windows Server 2008 and Windows Vista:** This method is not supported until Windows Server 2012 R2.<br/> |



 

### Properties

The **DfsrVolumeConfig** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Short textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

This property is inherited from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

</dd> <dt>

**ClusterDiskResName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Clustered Volume Physical Disk Resource Name")
</dt> </dl>

If the volume is a cluster shared volume, this property specifies the physical disk resource name.

**Windows Vista and Windows Server 2008:** This property is not supported until Windows Server 2008 R2.

</dd> <dt>

**DatabasePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Database Path"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (2600)
</dt> </dl>

The full path to the database. This database contains metadata about the files and folders in the replicated folder.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

This property is inherited from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

</dd> <dt>

**IsClustered**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Is a clustered Volume")
</dt> </dl>

This property is **TRUE** if the volume is a cluster shared volume, or **FALSE** if it is a local volume.

**Windows Vista and Windows Server 2008:** This property is not supported until Windows Server 2008 R2.

</dd> <dt>

**LastChangeNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Change Number"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1)
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

Information about the originator of the last configuration change. This is the name of the DC that provided the configuration information.

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

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Maximum number of Jet Sessions"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (16)
</dt> </dl>

The maximum number of concurrent Jet database sessions for this volume. Every volume has its own database, and therefore this parameter is defined per-volume.

**Windows Vista and Windows Server 2008:** This property is not supported until Windows Server 2008 R2.

</dd> <dt>

**MinNtfsJournalSizeInMb**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Minimum USN Journal Size in MB"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("MB"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (4), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (10000)
</dt> </dl>

The minimum size of the journal to allocate on the volume, in megabytes. If no journal exists, the DFSR creates a new journal with the specified size; otherwise, it increases the existing journal size to this minimum size. The DFSR will not change the existing journal size if it is already larger than the new minimum size.

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

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Identifier by which the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object is known.

This property is inherited from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

</dd> <dt>

**UsnCheckPoint**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Usn Check Point"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The number of journal updates to accumulate before committing a transaction.

**Windows Vista and Windows Server 2008:** This property is not supported until Windows Server 2008 R2.

</dd> <dt>

**VolumeGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Volume GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
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
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| End of client support<br/>    | Windows Vista<br/>                                                                 |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>DfsRProvs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461)
</dt> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





