---
title: MSFT\_DfsrIdRecordInfo class
description: This class provides access to ID Table records. The ID Table has a record for each file and folder known to DFSR. In addition, it keeps records of the deleted content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 173c3262-0ed1-420b-a8ec-ac722a1fb9de
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DfsrIdRecordInfo class Distributed File System Replication
- MSFT_DfsrIdRecordInfo class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- MSFT_DfsrIdRecordInfo
- MSFT_DfsrIdRecordInfo.Uid
- MSFT_DfsrIdRecordInfo.Flags
- MSFT_DfsrIdRecordInfo.Attributes
- MSFT_DfsrIdRecordInfo.GVsn
- MSFT_DfsrIdRecordInfo.Usn
- MSFT_DfsrIdRecordInfo.ParentUid
- MSFT_DfsrIdRecordInfo.Fid
- MSFT_DfsrIdRecordInfo.Volume
- MSFT_DfsrIdRecordInfo.Fence
- MSFT_DfsrIdRecordInfo.Clock
- MSFT_DfsrIdRecordInfo.CreateTime
- MSFT_DfsrIdRecordInfo.UpdateTime
- MSFT_DfsrIdRecordInfo.FileHash
- MSFT_DfsrIdRecordInfo.FileName
- MSFT_DfsrIdRecordInfo.FullPathName
- MSFT_DfsrIdRecordInfo.Index
- MSFT_DfsrIdRecordInfo.ReplicatedFolderGuid
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DfsrIdRecordInfo class

This class provides access to ID Table records. The ID Table has a record for each file and folder known to DFSR. In addition, it keeps records of the deleted content.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrIdRecordInfo
{
  string   Uid;
  uint8    Flags;
  uint32   Attributes;
  string   GVsn;
  sint64   Usn;
  string   ParentUid;
  uint64   Fid;
  string   Volume;
  string   Fence;
  uint64   Clock;
  datetime CreateTime;
  datetime UpdateTime;
  string   FileHash;
  string   FileName;
  string   FullPathName;
  uint32   Index;
  string   ReplicatedFolderGuid;
};
```

## Members

The **MSFT\_DfsrIdRecordInfo** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DfsrIdRecordInfo** class has these methods.



| Method                                                               | Description                                                           |
|:---------------------------------------------------------------------|:----------------------------------------------------------------------|
| [**GetFullFilePath**](getfullfilepath-msft-dfsridrecordinfo.md)     | Retrieves the complete path to the file or folder.<br/>         |
| [**GetIdRecordByPath**](msft-dfsridrecordinfo-getidrecordbypath.md) | Retrieves a specified **MSFT\_DfsrIdRecordInfo** instance.<br/> |



 

### Properties

The **MSFT\_DfsrIdRecordInfo** class has these properties.

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

**Clock**
</dt> <dd> <dl> <dt>

Data type: **uint64**
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

</dd> <dt>

**GVsn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Global Version")
</dt> </dl>

The global version of the resource (file or folder). The format of this string is "{*DatabaseGUID*}-*VersionNumber*", where "*DatabaseGUID*" is the **GUID** of the DFSR database and "*VersionNumber*" is an integer value assigned to each resource that increases when the resource is modified. Because the database **GUID** uniquely identifies the last computer that the resource was modified on, the GVsn property uniquely identifies a particular version of the resource.

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

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder GUID")
</dt> </dl>

The unique identifier of the replicated folder.

</dd> <dt>

**Uid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File or Folder GUID-Version Pair")
</dt> </dl>

The unique identifier of the resource (file or folder). The format of this string is "{*DatabaseGUID*}-*VersionNumber*", where "*DatabaseGUID*" is the **GUID** of the DFSR database and "*VersionNumber*" is an integer value assigned to each resource when it is created. Because the database **GUID** uniquely identifies the computer that the resource was created on, the Uid property uniquely identifies the resource.

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

Data type: **sint64**
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

The volume where the file or folder is located. The volume format is either "\\\\.\\C:" or "\\\\?\\volume{GUID}".

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

 

 





