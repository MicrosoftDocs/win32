---
title: MSFT\_DfsrVolumeInfo class
description: This class provides statistical and operational information for each volume that has or had replicated folders.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 30467101-f5b7-4856-aa03-fee98d8e8df0
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DfsrVolumeInfo class Distributed File System Replication
- MSFT_DfsrVolumeInfo class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- MSFT_DfsrVolumeInfo
- MSFT_DfsrVolumeInfo.VolumeGuid
- MSFT_DfsrVolumeInfo.VolumeSerialNumber
- MSFT_DfsrVolumeInfo.VolumePath
- MSFT_DfsrVolumeInfo.DatabaseGuid
- MSFT_DfsrVolumeInfo.State
- MSFT_DfsrVolumeInfo.LastConfigChangeTime
- MSFT_DfsrVolumeInfo.LastErrorCode
- MSFT_DfsrVolumeInfo.LastErrorMessageId
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_DfsrVolumeInfo class

This class provides statistical and operational information for each volume that has or had replicated folders.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrVolumeInfo
{
  string   VolumeGuid;
  uint64   VolumeSerialNumber;
  string   VolumePath;
  string   DatabaseGuid;
  uint8    State;
  datetime LastConfigChangeTime;
  uint32   LastErrorCode;
  uint32   LastErrorMessageId;
};
```

## Members

The **MSFT\_DfsrVolumeInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DfsrVolumeInfo** class has these properties.

<dl> <dt>

**DatabaseGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Database GUID")
</dt> </dl>

The identifier of the database on this volume.

</dd> <dt>

**LastConfigChangeTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Configuration Change Time")
</dt> </dl>

The last time the volume configuration was changed.

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Error Code")
</dt> </dl>

The last error code.

<dt>



 (0)


</dt> <dd></dd> </dl>

</dd> <dt>

**LastErrorMessageId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Error Message ID")
</dt> </dl>

Event log message identifier that corresponds to the last error code.

<dt>



 (0)


</dt> <dd></dd> </dl>

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Volume State")
</dt> </dl>

The current volume state.

<dt>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>

**Initialized** (0)


</dt> <dd></dd> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>

**Shutting Down** (1)


</dt> <dd></dd> <dt>

<span id="In_Error"></span><span id="in_error"></span><span id="IN_ERROR"></span>

**In Error** (2)


</dt> <dd></dd> <dt>

<span id="Auto_Recovery"></span><span id="auto_recovery"></span><span id="AUTO_RECOVERY"></span>

**Auto Recovery** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**VolumeGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Volume GUID")
</dt> </dl>

The volume identifier.

</dd> <dt>

**VolumePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group GUID")
</dt> </dl>

The volume path format; this is either "\\\\.\\C:" or "\\\\?\\volume{*GUID*}\\".

</dd> <dt>

**VolumeSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Volume Serial Number")
</dt> </dl>

The volume serial number.

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

 

 





