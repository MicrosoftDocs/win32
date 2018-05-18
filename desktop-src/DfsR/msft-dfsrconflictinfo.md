---
title: MSFT\_DfsrConflictInfo class
description: This class provides details about the files and folders that were moved to the Conflict and Deleted folder due to conflicting updates.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c3661e68-3f6c-4187-872f-733303ae5f78'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_DfsrConflictInfo class Distributed File System Replication", "MSFT_DfsrConflictInfo class Distributed File System Replication , described"]
topic_type:
- apiref
api_name:
- MSFT_DfsrConflictInfo
- MSFT_DfsrConflictInfo.GVsn
- MSFT_DfsrConflictInfo.Uid
- MSFT_DfsrConflictInfo.FileName
- MSFT_DfsrConflictInfo.FileAttributes
- MSFT_DfsrConflictInfo.ConflictFileCount
- MSFT_DfsrConflictInfo.ConflictSizeInBytes
- MSFT_DfsrConflictInfo.ConflictTime
- MSFT_DfsrConflictInfo.ConflictPath
- MSFT_DfsrConflictInfo.ConflictType
- MSFT_DfsrConflictInfo.ReplicatedFolderGuid
- MSFT_DfsrConflictInfo.ReplicationGroupGuid
- MSFT_DfsrConflictInfo.MemberGuid
- MSFT_DfsrConflictInfo.PartnerGuid
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
---

# MSFT\_DfsrConflictInfo class

This class provides details about the files and folders that were moved to the Conflict and Deleted folder due to conflicting updates.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrConflictInfo
{
  string   GVsn;
  string   Uid;
  string   FileName;
  uint32   FileAttributes;
  uint32   ConflictFileCount;
  uint64   ConflictSizeInBytes;
  datetime ConflictTime;
  string   ConflictPath;
  uint8    ConflictType;
  string   ReplicatedFolderGuid;
  string   ReplicationGroupGuid;
  string   MemberGuid;
  string   PartnerGuid;
};
```

## Members

The **MSFT\_DfsrConflictInfo** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DfsrConflictInfo** class has these methods.



| Method                                                         | Description                                                                                         |
|:---------------------------------------------------------------|:----------------------------------------------------------------------------------------------------|
| [**DeleteConflict**](deleteconflict-msft-dfsrconflictinfo.md) | Deletes this conflict from the conflict directory along with its record in the manifest.<br/> |



 

### Properties

The **MSFT\_DfsrConflictInfo** class has these properties.

<dl> <dt>

**ConflictFileCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Conflict File Count")
</dt> </dl>

If the conflict is a folder, this value is the total number of files and folders under the conflicted parent folder.

</dd> <dt>

**ConflictPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Conflict Path")
</dt> </dl>

The original location of the conflicted file or folder.

</dd> <dt>

**ConflictSizeInBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Conflict Size in Bytes")
</dt> </dl>

The size of the file or folder, in bytes.

</dd> <dt>

**ConflictTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Conflict Time")
</dt> </dl>

The time stamp when the conflict was detected.

</dd> <dt>

**ConflictType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Conflict Type")
</dt> </dl>

The type of conflict.

<dt>

<span id="Name_Conflict"></span><span id="name_conflict"></span><span id="NAME_CONFLICT"></span>

**Name Conflict** (1)


</dt> <dd></dd> <dt>

<span id="Remote_Update_Local_Update_Conflict"></span><span id="remote_update_local_update_conflict"></span><span id="REMOTE_UPDATE_LOCAL_UPDATE_CONFLICT"></span>

**Remote Update Local Update Conflict** (2)


</dt> <dd></dd> <dt>

<span id="Remote_Update_Local_Delete_Conflict"></span><span id="remote_update_local_delete_conflict"></span><span id="REMOTE_UPDATE_LOCAL_DELETE_CONFLICT"></span>

**Remote Update Local Delete Conflict** (3)


</dt> <dd></dd> <dt>

<span id="Local_Delete_Remote_Update_Conflict"></span><span id="local_delete_remote_update_conflict"></span><span id="LOCAL_DELETE_REMOTE_UPDATE_CONFLICT"></span>

**Local Delete Remote Update Conflict** (4)


</dt> <dd></dd> <dt>

<span id="Remote_File_Delete"></span><span id="remote_file_delete"></span><span id="REMOTE_FILE_DELETE"></span>

**Remote File Delete** (5)


</dt> <dd></dd> <dt>

<span id="Remote_File_Does_Not_Exist_At_Initial_Sync"></span><span id="remote_file_does_not_exist_at_initial_sync"></span><span id="REMOTE_FILE_DOES_NOT_EXIST_AT_INITIAL_SYNC"></span>

**Remote File Does Not Exist At Initial Sync** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**FileAttributes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File Attributes")
</dt> </dl>

The attributes of the file or folder. For a list of values, see the [**GetFileAttributes**](https://msdn.microsoft.com/library/windows/desktop/aa364944) function.

</dd> <dt>

**FileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File Name")
</dt> </dl>

The name of the file or folder after it is moved to the Conflict and Deleted folder.

</dd> <dt>

**GVsn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Global Version")
</dt> </dl>

The global version of the conflicted file or folder.

</dd> <dt>

**MemberGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member GUID")
</dt> </dl>

The unique identifier of the replication member.

</dd> <dt>

**PartnerGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Partner GUID")
</dt> </dl>

The unique identifier of the partner object in this connection.

</dd> <dt>

**ReplicatedFolderGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder GUID")
</dt> </dl>

The unique identifier of the replicated folder.

</dd> <dt>

**ReplicationGroupGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group GUID")
</dt> </dl>

The unique identifier of the replication group.

</dd> <dt>

**Uid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Conflicted File or Folder GUID-Version Pair")
</dt> </dl>

The unique identifier and version of the conflicted file or folder.

</dd> </dl>

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





