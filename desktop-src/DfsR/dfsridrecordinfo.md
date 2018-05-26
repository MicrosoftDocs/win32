---
title: DfsrIdRecordInfo class
description: This class provides access to ID Table records. The ID Table has a record for each file and folder known to DFSR. In addition, it keeps records of the deleted content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: acdec72e-97ee-44fa-8f2a-481007ee21e9
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DfsrIdRecordInfo class Distributed File System Replication
- DfsrIdRecordInfo class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- DfsrIdRecordInfo
- DfsrIdRecordInfo.Caption
- DfsrIdRecordInfo.Description
- DfsrIdRecordInfo.InstallDate
- DfsrIdRecordInfo.Name
- DfsrIdRecordInfo.Status
- DfsrIdRecordInfo.Uid
- DfsrIdRecordInfo.Flags
- DfsrIdRecordInfo.Attributes
- DfsrIdRecordInfo.GVsn
- DfsrIdRecordInfo.Usn
- DfsrIdRecordInfo.ParentUid
- DfsrIdRecordInfo.Fid
- DfsrIdRecordInfo.Volume
- DfsrIdRecordInfo.Fence
- DfsrIdRecordInfo.Clock
- DfsrIdRecordInfo.CreateTime
- DfsrIdRecordInfo.UpdateTime
- DfsrIdRecordInfo.FileHash
- DfsrIdRecordInfo.FileName
- DfsrIdRecordInfo.FullPathName
- DfsrIdRecordInfo.Index
- DfsrIdRecordInfo.ReplicatedFolderGuid
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DfsrIdRecordInfo class

This class provides access to ID Table records. The ID Table has a record for each file and folder known to DFSR. In addition, it keeps records of the deleted content.

## Syntax

``` syntax
[Dynamic, Provider("DfsrMonitorProv")]
class DfsrIdRecordInfo : CIM_LogicalElement
{
  string       Caption;
  string       Description;
  datetime REF InstallDate;
  string       Name;
  string       Status;
  string       Uid;
  uint8        Flags;
  uint32       Attributes;
  string       GVsn;
  string       Usn;
  string       ParentUid;
  uint64       Fid;
  string       Volume;
  string       Fence;
  datetime     Clock;
  datetime     CreateTime;
  datetime     UpdateTime;
  string       FileHash;
  string       FileName;
  string       FullPathName;
  uint32       Index;
  string       ReplicatedFolderGuid;
};
```

## Members

The **DfsrIdRecordInfo** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **DfsrIdRecordInfo** class has these methods.



| Method                                                      | Description                                                   |
|:------------------------------------------------------------|:--------------------------------------------------------------|
| [**GetFullFilePath**](getfullfilepath-dfsridrecordinfo.md) | Retrieves the complete path to the file or folder.<br/> |



 

### Properties

The **DfsrIdRecordInfo** class has these properties.

<dl> <dt>

**Attributes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Attributes")
</dt> </dl>

The file or folder attributes. For a list of values, see the [**GetFileAttributes**](https://msdn.microsoft.com/library/windows/desktop/aa364944) function.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**Clock**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Clock")
</dt> </dl>

The logical clock value assigned to the file or folder.

</dd> <dt>

**CreateTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Create Time")
</dt> </dl>

The creation time stamp of the file or folder. This is the time at which the resource first appears in the replication group.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**Fence**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Fence")
</dt> </dl>

The fence value associated with the file. This property can be one of the following values.

<dt>

<span id="Unfence"></span><span id="unfence"></span><span id="UNFENCE"></span>

<span id="Unfence"></span><span id="unfence"></span><span id="UNFENCE"></span>**Unfence** (0)


</dt> <dd>

This file or folder will lose all conflicts.

</dd> <dt>

<span id="Initial_Sync"></span><span id="initial_sync"></span><span id="INITIAL_SYNC"></span>

<span id="Initial_Sync"></span><span id="initial_sync"></span><span id="INITIAL_SYNC"></span>**Initial Sync** (1)


</dt> <dd>

Initial fence value for non-primary member.

</dd> <dt>

<span id="Initial_Primary"></span><span id="initial_primary"></span><span id="INITIAL_PRIMARY"></span>

<span id="Initial_Primary"></span><span id="initial_primary"></span><span id="INITIAL_PRIMARY"></span>**Initial Primary** (2)


</dt> <dd>

Initial fence value for primary member.

</dd> <dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>**Default** (3)


</dt> <dd>

Default fencing value.

</dd> <dt>

<span id="Fence"></span><span id="fence"></span><span id="FENCE"></span>

<span id="Fence"></span><span id="fence"></span><span id="FENCE"></span>**Fence** (4)


</dt> <dd>

Fence with current time stamp.

</dd> </dl>

</dd> <dt>

**Fid**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File ID")
</dt> </dl>

The file reference number. On NTFS, each file is assigned an identifier which is unique on the volume; it can be used to open a handle to the file.

</dd> <dt>

**FileHash**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File Hash")
</dt> </dl>

A hash value for the file content.

</dd> <dt>

**FileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Relative Name")
</dt> </dl>

The name of the file or folder.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Flags")
</dt> </dl>

A combination of flags for present, authoritative, and file type flags.

<dt>

<span id="PRESENT_FLAG"></span><span id="present_flag"></span>

<span id="PRESENT_FLAG"></span><span id="present_flag"></span>**PRESENT\_FLAG** (0x1)


</dt> <dd>

The resource is not a tombstone; it is available on the computer.

</dd> <dt>

<span id="NAME_CONFLICT_FLAG"></span><span id="name_conflict_flag"></span>

<span id="NAME_CONFLICT_FLAG"></span><span id="name_conflict_flag"></span>**NAME\_CONFLICT\_FLAG** (0x2)


</dt> <dd>

The tombstone was generated because of a name conflict.

This flag is meaningful only for tombstones.

</dd> <dt>

<span id="UID_VISIBLE_FLAG"></span><span id="uid_visible_flag"></span>

<span id="UID_VISIBLE_FLAG"></span><span id="uid_visible_flag"></span>**UID\_VISIBLE\_FLAG** (0x4)


</dt> <dd>

The ID record has already been sent out to other partners; therefore, other partners are aware of this resource.

</dd> <dt>

<span id="JOURNAL_WRAP_FLAG"></span><span id="journal_wrap_flag"></span>

<span id="JOURNAL_WRAP_FLAG"></span><span id="journal_wrap_flag"></span>**JOURNAL\_WRAP\_FLAG** (0x10)


</dt> <dd>

The volume has had a journal wrap and the resource has not been checked to determine if there is any change by the journal wrap recovery process.

</dd> <dt>

<span id="PENDING_TOMBSTONE_FLAG"></span><span id="pending_tombstone_flag"></span>

<span id="PENDING_TOMBSTONE_FLAG"></span><span id="pending_tombstone_flag"></span>**PENDING\_TOMBSTONE\_FLAG** (0x20)


</dt> <dd>

The ID record is in the process of being tombstoned (or deleted.)

</dd> </dl>

</dd> <dt>

**FullPathName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Full Path Name")
</dt> </dl>

The complete path to the file or folder.

**Windows Vista and Windows Server 2008:** This property is not supported until Windows Server 2008 R2.

</dd> <dt>

**GVsn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Global Version")
</dt> </dl>

The global version of the resource (file or folder). The format of this string is {*DatabaseGUID*}-*VersionNumber*, where *DatabaseGUID* is the GUID of the DFSR database and *VersionNumber* is an integer value assigned to each resource that increases when the resource is modified. Because the database GUID uniquely identifies the last computer that the resource was modified on, the GVsn property uniquely identifies a particular version of the resource.

</dd> <dt>

**Index**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Record Index")
</dt> </dl>

The run-time index of the record. This value is used to partition the result of a large query.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates when the object was installed. Lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property.

This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**ParentUid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Parent GUID")
</dt> </dl>

The unique identifier of the parent folder.

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

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File or Folder GUID-Version Pair")
</dt> </dl>

The unique identifier of the resource (file or folder). The format of this string is {*DatabaseGUID*}-*VersionNumber*, where *DatabaseGUID* is the GUID of the DFSR database and *VersionNumber* is an integer value assigned to each resource when it is created. Because the database GUID uniquely identifies the computer that the resource was created on, the Uid property uniquely identifies the resource.

</dd> <dt>

**UpdateTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Update Time")
</dt> </dl>

The last time DFSR updated the record in response to a change in the resource.

</dd> <dt>

**Usn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("USN")
</dt> </dl>

The USN (Update Sequence Number) at the time the resource is updated.

</dd> <dt>

**Volume**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Volume")
</dt> </dl>

The volume where the file or folder is located. The volume format is either \\\\.\\C: or \\\\?\\volume{GUID}.

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

[**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892)
</dt> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





