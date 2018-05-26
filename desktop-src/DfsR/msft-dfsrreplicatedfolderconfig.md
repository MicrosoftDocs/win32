---
title: MSFT\_DfsrReplicatedFolderConfig class
description: An instance of this class is available for each replicated folder that is hosted on this computer. This class provides read-only access to the configuration parameters for the replicated folder.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9ff53a9a-dd1d-4b86-ba8d-9c849dba003e
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DfsrReplicatedFolderConfig class Distributed File System Replication
- MSFT_DfsrReplicatedFolderConfig class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- MSFT_DfsrReplicatedFolderConfig
- MSFT_DfsrReplicatedFolderConfig.ReplicatedFolderGuid
- MSFT_DfsrReplicatedFolderConfig.ReplicatedFolderName
- MSFT_DfsrReplicatedFolderConfig.ReplicatedFolderDn
- MSFT_DfsrReplicatedFolderConfig.ReplicationGroupGuid
- MSFT_DfsrReplicatedFolderConfig.MemberGuid
- MSFT_DfsrReplicatedFolderConfig.VolumeGuid
- MSFT_DfsrReplicatedFolderConfig.RootPath
- MSFT_DfsrReplicatedFolderConfig.RootSizeInMb
- MSFT_DfsrReplicatedFolderConfig.StagingPath
- MSFT_DfsrReplicatedFolderConfig.StagingSizeInMb
- MSFT_DfsrReplicatedFolderConfig.StagingFileSizeThreshold
- MSFT_DfsrReplicatedFolderConfig.ConflictPath
- MSFT_DfsrReplicatedFolderConfig.ConflictSizeInMb
- MSFT_DfsrReplicatedFolderConfig.FileFilter
- MSFT_DfsrReplicatedFolderConfig.DirectoryFilter
- MSFT_DfsrReplicatedFolderConfig.Ghosted
- MSFT_DfsrReplicatedFolderConfig.CacheObeyConnectionSchedule
- MSFT_DfsrReplicatedFolderConfig.MinAgeInCacheInMin
- MSFT_DfsrReplicatedFolderConfig.MaxAgeInCacheInMin
- MSFT_DfsrReplicatedFolderConfig.Enabled
- MSFT_DfsrReplicatedFolderConfig.IsPrimary
- MSFT_DfsrReplicatedFolderConfig.ReadOnly
- MSFT_DfsrReplicatedFolderConfig.DisableSaveDeletes
- MSFT_DfsrReplicatedFolderConfig.DisableReanimateDeletes
- MSFT_DfsrReplicatedFolderConfig.SharedStaging
- MSFT_DfsrReplicatedFolderConfig.CompressedExtensions
- MSFT_DfsrReplicatedFolderConfig.Description
- MSFT_DfsrReplicatedFolderConfig.UsnCreated
- MSFT_DfsrReplicatedFolderConfig.ContainerComputerName
- MSFT_DfsrReplicatedFolderConfig.IsClustered
- MSFT_DfsrReplicatedFolderConfig.VcoResourceName
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_DfsrReplicatedFolderConfig class

An instance of this class is available for each replicated folder that is hosted on this computer. This class provides read-only access to the configuration parameters for the replicated folder.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrReplicatedFolderConfig
{
  string  ReplicatedFolderGuid;
  string  ReplicatedFolderName;
  string  ReplicatedFolderDn;
  string  ReplicationGroupGuid;
  string  MemberGuid;
  string  VolumeGuid;
  string  RootPath;
  uint32  RootSizeInMb;
  string  StagingPath;
  uint32  StagingSizeInMb;
  uint64  StagingFileSizeThreshold;
  string  ConflictPath;
  uint32  ConflictSizeInMb;
  string  FileFilter;
  string  DirectoryFilter;
  boolean Ghosted;
  boolean CacheObeyConnectionSchedule;
  uint32  MinAgeInCacheInMin;
  uint32  MaxAgeInCacheInMin;
  boolean Enabled;
  boolean IsPrimary;
  boolean ReadOnly;
  boolean DisableSaveDeletes;
  boolean DisableReanimateDeletes;
  boolean SharedStaging;
  string  CompressedExtensions;
  string  Description;
  uint64  UsnCreated;
  string  ContainerComputerName;
  boolean IsClustered;
  string  VcoResourceName;
};
```

## Members

The **MSFT\_DfsrReplicatedFolderConfig** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DfsrReplicatedFolderConfig** class has these methods.



| Method                                                     | Description                                        |
|:-----------------------------------------------------------|:---------------------------------------------------|
| [**Offline**](offline-msft-dfsrreplicatedfolderconfig.md) | This method is reserved for system use.<br/> |
| [**Online**](online-msft-dfsrreplicatedfolderconfig.md)   | This method is reserved for system use.<br/> |



 

### Properties

The **MSFT\_DfsrReplicatedFolderConfig** class has these properties.

<dl> <dt>

**CacheObeyConnectionSchedule**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Obey Connection Schedule In Cache")
</dt> </dl>

Obey the connection schedule for on-demand replication.

</dd> <dt>

**CompressedExtensions**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File extensions that are compressed")
</dt> </dl>

File extensions that are compressed, contain the \* wildcard, are empty strings, or are comma-separated lists of file extensions.

</dd> <dt>

**ConflictPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (2600), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Conflict and Deleted Folder Path")
</dt> </dl>

The local path of the Conflict and Deleted folder for the replicated folder.

</dd> <dt>

**ConflictSizeInMb**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("10"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Conflict and Deleted Folder Quota In MB")
</dt> </dl>

The quota size of the Conflict and Deleted folder that is assigned to the replicated folder, in megabytes.

</dd> <dt>

**ContainerComputerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Content Set AD computer name")
</dt> </dl>

The name of the Active Directory computer object that holds the replicated folder information. Normally this name is same as the NETBIOS name of the local computer.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder Description")
</dt> </dl>

The user-defined description of the content or purpose of the current replicated folder.

</dd> <dt>

**DirectoryFilter**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (2600), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Subfolder Exclusion Filter")
</dt> </dl>

The directory exclusion filter list. A comma-separated list of filter strings to be applied to subfolders under the local path of the replicated folder.

</dd> <dt>

**DisableReanimateDeletes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Disable Reanimation of Remote Deletions")
</dt> </dl>

Indicates whether remote deletions should be reanimated.

</dd> <dt>

**DisableSaveDeletes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Disable Saving Deletes")
</dt> </dl>

Disables the feature that moves deleted files to the Conflict and Deleted folder.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder Status")
</dt> </dl>

Indicates whether this replicated folder is enabled. DFSR ignores the disabled replicated folder; however, they remain in the configuration files.

</dd> <dt>

**FileFilter**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (2600), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File Exclusion Filter")
</dt> </dl>

The file exclusion filter list. This is a comma-separated list of filter strings to be applied to files under the local path of the replicated folder.

</dd> <dt>

**Ghosted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Ghosted Content")
</dt> </dl>

This property is not used.

</dd> <dt>

**IsClustered**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Is content set part of a VCO")
</dt> </dl>

This property is **TRUE** if the Active Directory server that holds the replicated folder is a virtual computer in a cluster, or **FALSE** if it is a local computer.

</dd> <dt>

**IsPrimary**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Is Primary")
</dt> </dl>

Indicates whether the data in the replicated folder is authoritative during the initial synchronization operation.

</dd> <dt>

**MaxAgeInCacheInMin**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("0"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Maximum Age Time In Cache In Minutes")
</dt> </dl>

Reserved for system use.

</dd> <dt>

**MemberGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member GUID")
</dt> </dl>

The **GUID** of the member that hosts this replicated folder.

</dd> <dt>

**MinAgeInCacheInMin**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("0"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Minimum Age Time In Cache In Minutes")
</dt> </dl>

Minimum time a candidate ghosted resource remains un-ghosted before it is considered for ghosting.

</dd> <dt>

**ReadOnly**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Read-only")
</dt> </dl>

Indicates whether this replicated folder is read-only.

</dd> <dt>

**ReplicatedFolderDn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder Distinguished Name")
</dt> </dl>

The distinguished name of the corresponding object in the Active Directory Domain Services.

</dd> <dt>

**ReplicatedFolderGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder GUID")
</dt> </dl>

The unique identifier for the replicated folder.

</dd> <dt>

**ReplicatedFolderName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder Name")
</dt> </dl>

The friendly name of the replicated folder. The name is not required to be unique.

</dd> <dt>

**ReplicationGroupGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group GUID")
</dt> </dl>

The **GUID** of the replication group that contains this replicated folder.

</dd> <dt>

**RootPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (2600), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Local Path")
</dt> </dl>

The full path to the replicated folder.

</dd> <dt>

**RootSizeInMb**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("10"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Root Quota In MB")
</dt> </dl>

The quota size of the root folder, in megabytes, assigned to the replicated folder.

</dd> <dt>

**SharedStaging**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Shared Staging Folder")
</dt> </dl>

Specifies whether the staging folder is private or shared.

</dd> <dt>

**StagingFileSizeThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Minimum File Staging Size")
</dt> </dl>

The minimum size in bytes of files to stage during outbound replication.

</dd> <dt>

**StagingPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (2600), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Staging Folder Path")
</dt> </dl>

The full path to the staging folder for the replicated folder.

</dd> <dt>

**StagingSizeInMb**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("10"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Staging Quota In MB")
</dt> </dl>

The maximum size of the staging space assigned to the replicated folder, in megabytes. Note that DFSR can enable the staging space to exceed this value temporarily.

</dd> <dt>

**UsnCreated**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder USN Created")
</dt> </dl>

The USN-created value of the object that represents the replicated folder in Active Directory.

</dd> <dt>

**VcoResourceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Content Set VCO Resource Name")
</dt> </dl>

If the replicated folder is configured against a virtual computer, this property specifies the Network Name resource of the clustered replicated folder.

</dd> <dt>

**VolumeGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Volume GUID")
</dt> </dl>

The **GUID** of the volume that contains the replicated folder.

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

 

 





