---
title: DfsrReplicatedFolderConfig class
description: An instance of this class is available for each replicated folder that this hosted on this computer. This class provides read-only access to the configuration parameters for the replicated folder.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 056d61f1-7b7d-4fa0-bed0-c23763277617
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DfsrReplicatedFolderConfig class Distributed File System Replication
- DfsrReplicatedFolderConfig class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- DfsrReplicatedFolderConfig
- DfsrReplicatedFolderConfig.Caption
- DfsrReplicatedFolderConfig.SettingID
- DfsrReplicatedFolderConfig.ReplicatedFolderGuid
- DfsrReplicatedFolderConfig.ReplicatedFolderName
- DfsrReplicatedFolderConfig.ReplicatedFolderDn
- DfsrReplicatedFolderConfig.ReplicationGroupGuid
- DfsrReplicatedFolderConfig.MemberGuid
- DfsrReplicatedFolderConfig.VolumeGuid
- DfsrReplicatedFolderConfig.RootPath
- DfsrReplicatedFolderConfig.RootSizeInMb
- DfsrReplicatedFolderConfig.StagingPath
- DfsrReplicatedFolderConfig.StagingSizeInMb
- DfsrReplicatedFolderConfig.ConflictPath
- DfsrReplicatedFolderConfig.ConflictSizeInMb
- DfsrReplicatedFolderConfig.FileFilter
- DfsrReplicatedFolderConfig.DirectoryFilter
- DfsrReplicatedFolderConfig.Ghosted
- DfsrReplicatedFolderConfig.CacheObeyConnectionSchedule
- DfsrReplicatedFolderConfig.MinAgeInCacheInMin
- DfsrReplicatedFolderConfig.MaxAgeInCacheInMin
- DfsrReplicatedFolderConfig.Enabled
- DfsrReplicatedFolderConfig.IsPrimary
- DfsrReplicatedFolderConfig.ReadOnly
- DfsrReplicatedFolderConfig.DisableSaveDeletes
- DfsrReplicatedFolderConfig.DisableReanimateDeletes
- DfsrReplicatedFolderConfig.SharedStaging
- DfsrReplicatedFolderConfig.CompressedExtensions
- DfsrReplicatedFolderConfig.Description
- DfsrReplicatedFolderConfig.UsnCreated
- DfsrReplicatedFolderConfig.ContainerComputerName
- DfsrReplicatedFolderConfig.IsClustered
- DfsrReplicatedFolderConfig.VcoResourceName
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DfsrReplicatedFolderConfig class

An instance of this class is available for each replicated folder that this hosted on this computer. This class provides read-only access to the configuration parameters for the replicated folder.

## Syntax

``` syntax
[Dynamic, Provider("DfsrConfigProv")]
class DfsrReplicatedFolderConfig : CIM_Setting
{
  string  Caption;
  string  SettingID;
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
  boolean CompressedExtensions;
  string  Description;
  uint64  UsnCreated;
  string  ContainerComputerName;
  boolean IsClustered;
  string  VcoResourceName;
};
```

## Members

The **DfsrReplicatedFolderConfig** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **DfsrReplicatedFolderConfig** class has these methods.



| Method                                                | Description                                        |
|:------------------------------------------------------|:---------------------------------------------------|
| [**Offline**](dfsrreplicatedfolderconfig-offline.md) | This method is reserved for system use.<br/> |
| [**Online**](dfsrreplicatedfolderconfig-online.md)   | This method is reserved for system use.<br/> |



 

### Properties

The **DfsrReplicatedFolderConfig** class has these properties.

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

**CompressedExtensions**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File extensions that are compressed")
</dt> </dl>

File extensions that are compressed, contain the \* wildcard, are empty strings, or are comma-separated extensions.

</dd> <dt>

**ConflictPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Conflict and Deleted Folder Path"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (2600)
</dt> </dl>

The local path of the Conflict and Deleted folder for the replicated folder.

</dd> <dt>

**ConflictSizeInMb**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Conflict and Deleted Folder Quota In MB"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

The quota size of the Conflict and Deleted folder assigned to the replicated folder, in megabytes.

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

**Windows Vista and Windows Server 2008:** This property is not supported until Windows Server 2008 R2.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-defined description of the content or purpose of the current replicated folder.

</dd> <dt>

**DirectoryFilter**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Subfolder Exclusion Filter"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (2600)
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

Indicates whether this replicated folder is enabled. DFSR will ignore disabled replicated folder; however, they will remain in the configuration files.

</dd> <dt>

**FileFilter**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File Exclusion Filter"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (2600)
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

**Windows Vista and Windows Server 2008:** This property is not supported until Windows Server 2008 R2.

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

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Maximum Age Time In Cache In Minutes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0)
</dt> </dl>

Reserved for system use.

</dd> <dt>

**MemberGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The GUID of the member that hosts this replicated folder.

</dd> <dt>

**MinAgeInCacheInMin**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Minimum Age Time In Cache In Minutes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0)
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

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
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

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The GUID of the replication group that contains this replicated folder.

</dd> <dt>

**RootPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Local Path"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (2600)
</dt> </dl>

The full path to the replicated folder.

</dd> <dt>

**RootSizeInMb**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Root Quota In MB"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

The quota size of the root folder, in megabytes, assigned to the replicated folder.

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

**StagingPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Staging Folder Path"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (2600)
</dt> </dl>

The full path to the staging folder for the replicated folder.

</dd> <dt>

**StagingSizeInMb**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Staging Quota In MB"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

The maximum size of the staging space assigned to the replicated folder, in megabytes. Note that DFSR can allow the staging space to exceed this value temporarily.

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

**Windows Vista and Windows Server 2008:** This property is not supported until Windows Server 2008 R2.

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

**Windows Vista and Windows Server 2008:** This property is not supported until Windows Server 2008 R2.

</dd> <dt>

**VolumeGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Volume GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The GUID of the volume that contains the replicated folder.

</dd> </dl>

## Examples

The [Get-DFSRBacklog](https://Gallery.TechNet.Microsoft.Com/dac62790-219d-4325-a57b-e79c2aa6b58e) PowerShell code sample on TechNet Gallery uses **DfsrReplicatedFolderConfig** to retrieve DFSR backlog for replication groups of the targeted server.

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

 

 





