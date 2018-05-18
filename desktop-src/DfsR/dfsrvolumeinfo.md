---
title: DfsrVolumeInfo class
description: This class provides statistical and operational information for each volume that has or had replicated folders.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd74be5aa-0250-4362-b6d8-d05664a05a9b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DfsrVolumeInfo class Distributed File System Replication", "DfsrVolumeInfo class Distributed File System Replication , described"]
topic_type:
- apiref
api_name:
- DfsrVolumeInfo
- DfsrVolumeInfo.Caption
- DfsrVolumeInfo.Description
- DfsrVolumeInfo.InstallDate
- DfsrVolumeInfo.Name
- DfsrVolumeInfo.Status
- DfsrVolumeInfo.VolumeGuid
- DfsrVolumeInfo.VolumeSerialNumber
- DfsrVolumeInfo.VolumePath
- DfsrVolumeInfo.DatabaseGuid
- DfsrVolumeInfo.State
- DfsrVolumeInfo.LastConfigChangeTime
- DfsrVolumeInfo.LastErrorCode
- DfsrVolumeInfo.LastErrorMessageId
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
---

# DfsrVolumeInfo class

This class provides statistical and operational information for each volume that has or had replicated folders.

## Syntax

``` syntax
[Dynamic, Provider("DfsrMonitorProv")]
class DfsrVolumeInfo : CIM_LogicalElement
{
  string       Caption;
  string       Description;
  datetime REF InstallDate;
  string       Name;
  string       Status;
  string       VolumeGuid;
  uint64       VolumeSerialNumber;
  string       VolumePath;
  string       DatabaseGuid;
  uint8        State;
  datetime     LastConfigChangeTime;
  uint32       LastErrorCode;
  uint32       LastErrorMessageId;
};
```

## Members

The **DfsrVolumeInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **DfsrVolumeInfo** class has these properties.

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

**DatabaseGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Database GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The identifier of the database on this volume.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates when the object was installed. Lack of a value does not indicate that the object is not installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

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

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>

**Success** (0)


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

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>

**Success** (0)


</dt> <dd></dd> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

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

**VolumeGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Volume GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
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

The volume path format; this is either "\\\\.\\C:" or "\\\\?\\volume{*GUID*}".

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

 

 





