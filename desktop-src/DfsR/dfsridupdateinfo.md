---
title: DfsrIdUpdateInfo class
description: This class provides statistical and operational information about updates that are being transferred by this computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6734dbcc-b512-45e5-a89b-e7676cae5e8c
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DfsrIdUpdateInfo class Distributed File System Replication
- DfsrIdUpdateInfo class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- DfsrIdUpdateInfo
- DfsrIdUpdateInfo.UpdateGuid
- DfsrIdUpdateInfo.Uid
- DfsrIdUpdateInfo.GVsn
- DfsrIdUpdateInfo.ParentUid
- DfsrIdUpdateInfo.UpdateState
- DfsrIdUpdateInfo.FileName
- DfsrIdUpdateInfo.FullPathName
- DfsrIdUpdateInfo.ReplicatedFolderGuid
- DfsrIdUpdateInfo.ConnectionGuid
- DfsrIdUpdateInfo.PartnerName
- DfsrIdUpdateInfo.Inbound
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DfsrIdUpdateInfo class

This class provides statistical and operational information about updates that are being transferred by this computer.

## Syntax

``` syntax
[Dynamic, Provider("DfsrMonitorProv")]
class DfsrIdUpdateInfo
{
  string  UpdateGuid;
  string  Uid;
  string  GVsn;
  string  ParentUid;
  uint32  UpdateState;
  string  FileName;
  string  FullPathName;
  string  ReplicatedFolderGuid;
  string  ConnectionGuid;
  string  PartnerName;
  boolean Inbound;
};
```

## Members

The **DfsrIdUpdateInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **DfsrIdUpdateInfo** class has these properties.

<dl> <dt>

**ConnectionGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Connection GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The unique connection identifier of the connection that this update is being transferred on. This string is in the format of a globally unique identifier (**GUID**), for example "{95ee9fff-3436-11d1-b2b0-d15ae3ac8436}".

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

**FullPathName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Full Path Name")
</dt> </dl>

The full path to the file or folder.

</dd> <dt>

**GVsn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Global Version")
</dt> </dl>

The global version of the resource (file or folder). The format of this string is {*DatabaseGUID*}-*VersionNumber*, where *DatabaseGUID* is the **GUID** of the DFSR database and *VersionNumber* is an integer value assigned to each resource that increases when the resource is modified. Because the database GUID uniquely identifies the last computer that the resource was modified on, the **GVsn** property uniquely identifies a particular version of the resource.

</dd> <dt>

**Inbound**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Incoming Connection")
</dt> </dl>

Indicates the direction of the connection between the local computer and this partner. The value is **TRUE** if the connection is inbound (coming from the partner) and **FALSE** if the connection is outbound (going to the partner).

</dd> <dt>

**ParentUid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Parent GUID")
</dt> </dl>

The unique identifier of the parent folder. This string is in **GUID** format, for example "{95ee9fff-3436-11d1-b2b0-d15ae3ac8436}".

</dd> <dt>

**PartnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Partner Name")
</dt> </dl>

The partner name for the connection. This is typically the unqualified DNS name of the partner computer.

</dd> <dt>

**ReplicatedFolderGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replicated Folder GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The unique identifier of the replicated folder. This string is in **GUID** format, for example "{95ee9fff-3436-11d1-b2b0-d15ae3ac8436}".

</dd> <dt>

**Uid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("File or Folder GUID-Version Pair")
</dt> </dl>

The unique identifier of the resource (file or folder). The format of this string is {*DatabaseGUID*}-*VersionNumber*, where *DatabaseGUID* is the **GUID** of the DFSR database and *VersionNumber* is an integer value assigned to each resource when it is created. Because the database GUID uniquely identifies the computer that the resource was created on, the **Uid** property uniquely identifies the resource.

</dd> <dt>

**UpdateGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("The unique identifier guid of the update"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

A GUID for the update that is downloaded or uploaded.

</dd> <dt>

**UpdateState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Update State")
</dt> </dl>

The current state of the update. The following values are supported.

<dt>

<span id="SCHEDULED"></span><span id="scheduled"></span>

<span id="SCHEDULED"></span><span id="scheduled"></span>**SCHEDULED** (1)


</dt> <dd>

The update has been created and is scheduled to be processed.

</dd> <dt>

<span id="RUNNING"></span><span id="running"></span>

<span id="RUNNING"></span><span id="running"></span>**RUNNING** (2)


</dt> <dd>

The update is being processed.

</dd> <dt>

<span id="DOWNLOADING"></span><span id="downloading"></span>

<span id="DOWNLOADING"></span><span id="downloading"></span>**DOWNLOADING** (3)


</dt> <dd>

The update is being downloaded.

</dd> <dt>

<span id="WAIT"></span><span id="wait"></span>

<span id="WAIT"></span><span id="wait"></span>**WAIT** (4)


</dt> <dd>

The update failed to be processed and is in wait state. The update will be processed again later.

</dd> <dt>

<span id="BLOCKED"></span><span id="blocked"></span>

<span id="BLOCKED"></span><span id="blocked"></span>**BLOCKED** (5)


</dt> <dd>

The update is blocked, because it depends on another update which has not been processed yet.

</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                        |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>Dfsrprovs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





