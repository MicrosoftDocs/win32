---
title: DfsrConflictInfo class
description: This class provides details about the files and folders that were moved to the Conflict and Deleted folder due to conflicting updates.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '14b21820-9631-435e-8990-ef518a52bea8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DfsrConflictInfo class Distributed File System Replication", "DfsrConflictInfo class Distributed File System Replication , described"]
topic_type:
- apiref
api_name:
- DfsrConflictInfo
- DfsrConflictInfo.Caption
- DfsrConflictInfo.Description
- DfsrConflictInfo.InstallDate
- DfsrConflictInfo.Name
- DfsrConflictInfo.Status
- DfsrConflictInfo.GVsn
- DfsrConflictInfo.Uid
- DfsrConflictInfo.FileName
- DfsrConflictInfo.FileAttributes
- DfsrConflictInfo.ConflictFileCount
- DfsrConflictInfo.ConflictSizeInBytes
- DfsrConflictInfo.ConflictTime
- DfsrConflictInfo.ConflictPath
- DfsrConflictInfo.ConflictType
- DfsrConflictInfo.ReplicatedFolderGuid
- DfsrConflictInfo.ReplicationGroupGuid
- DfsrConflictInfo.MemberGuid
- DfsrConflictInfo.PartnerGuid
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
---

# DfsrConflictInfo class

This class provides details about the files and folders that were moved to the Conflict and Deleted folder due to conflicting updates.

## Syntax

``` syntax
[Dynamic, Provider("DfsrMonitorProv")]
class DfsrConflictInfo : CIM_LogicalElement
{
  string       Caption;
  string       Description;
  datetime REF InstallDate;
  string       Name;
  string       Status;
  string       GVsn;
  string       Uid;
  string       FileName;
  uint32       FileAttributes;
  uint32       ConflictFileCount;
  uint64       ConflictSizeInBytes;
  datetime     ConflictTime;
  string       ConflictPath;
  uint8        ConflictType;
  string       ReplicatedFolderGuid;
  string       ReplicationGroupGuid;
  string       MemberGuid;
  string       PartnerGuid;
};
```

## Members

The **DfsrConflictInfo** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **DfsrConflictInfo** class has these methods.



| Method                                    | Description                                                                                         |
|:------------------------------------------|:----------------------------------------------------------------------------------------------------|
| [**Delete**](delete-dfsrconflictinfo.md) | Deletes this conflict from the conflict directory along with its record in the manifest.<br/> |



 

### Properties

The **DfsrConflictInfo** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64)
</dt> </dl>

A short textual description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

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

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

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

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Global Version")
</dt> </dl>

The global version of the conflicted file or folder.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates when the object was installed. Lack of a value does not indicate that the object is not installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**MemberGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The unique identifier of the member.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**PartnerGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Partner GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The unique identifier of the partner object in this connection.

</dd> <dt>

**ReplicatedFolderGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The unique identifier of the replicated folder.

</dd> <dt>

**ReplicationGroupGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The unique identifier of the replication group.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

String that indicates the current status of the object. Operational and non-operational status can be defined. Operational status can include "OK", "Degraded", and "Pred Fail". "Pred Fail" indicates that an element is functioning properly, but is predicting a failure (for example, a SMART-enabled hard disk drive).

Non-operational status can include "Error", "Starting", "Stopping", and "Service". "Service" can apply during disk mirror-resilvering, reloading a user permissions list, or other administrative work. Not all such work is online, but the managed element is neither "OK" nor in one of the other states. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

Values include the following:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

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
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| End of client support<br/>    | Windows Vista<br/>                                                                 |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>DfsRProvs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892)
</dt> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





