---
title: WT\_Snapshot class
description: Represents a volume shadow copy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '22858e35-6480-4f33-9550-eeb6a79b7b71'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["WT_Snapshot class iSCSI Software Target API", "WT_Snapshot class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- WT_Snapshot
- WT_Snapshot.Id
- WT_Snapshot.Description
- WT_Snapshot.OrigWTD
- WT_Snapshot.Status
- WT_Snapshot.TimeStamp
- WT_Snapshot.ExportedWTD
- WT_Snapshot.VdsLunInfo
- WT_Snapshot.ResourceGroup
api_location:
- WtWmiProv.dll
api_type:
- DllExport
---

# WT\_Snapshot class

Represents a volume shadow copy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_Snapshot
{
  string               Id;
  string               Description;
  uint32               OrigWTD;
  sint32               Status;
  string               TimeStamp;
  sint32               ExportedWTD;
  WT_VDSLunInformation VdsLunInfo;
  string               ResourceGroup;
};
```

## Members

The **WT\_Snapshot** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **WT\_Snapshot** class has these methods.



| Method                                             | Description                                                                                                                                                                                 |
|:---------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AbortRollback**](abortrollback-wt-snapshot.md) | Aborts the rollback of the virtual disk.<br/>                                                                                                                                         |
| [**Create**](create-wt-snapshot.md)               | Creates a shadow copy of the specified virtual disk.<br/>                                                                                                                             |
| [**Delete**](delete-wt-snapshot.md)               | Deletes a shadow copy.<br/>                                                                                                                                                           |
| [**DVDismount**](dvdismount-wt-snapshot.md)       | Dismounts the shadow copy that was mounted locally.<br/> **Windows Server 2012 R2:** This method is deprecated. Use iSCSI loopback instead.<br/>                                |
| [**DVMount**](dvmount-wt-snapshot.md)             | Mounts the current shadow copy in read-only mode on the local iSCSI Target server.<br/> **Windows Server 2012 R2:** This method is deprecated. Use iSCSI loopback instead.<br/> |
| [**Export**](export-wt-snapshot.md)               | Exports the current shadow copy as a virtual disk.<br/>                                                                                                                               |
| [**Rollback**](rollback-wt-snapshot.md)           | Rolls back the virtual disk to the current shadow copy.<br/>                                                                                                                          |



 

### Properties

The **WT\_Snapshot** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A user-friendly description of the shadow copy.

</dd> <dt>

**ExportedWTD**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains the index of the disk in the event that the shadow copy is exported as a virtual disk.

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

A GUID that uniquely identifies this shadow copy

</dd> <dt>

**OrigWTD**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The iSCSI disk index of the virtual disk that this shadow copy belongs to.

</dd> <dt>

**ResourceGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The resource group. Valid only in a cluster.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Status of the current shadow copy. This property is a bitmask and can contain one or more of the following values.

<dt>

<span id="Idle"></span><span id="idle"></span><span id="IDLE"></span>

**Idle** (0x0)


</dt> <dd></dd> <dt>

<span id="Exposed"></span><span id="exposed"></span><span id="EXPOSED"></span>

**Exposed** (0x1)


</dt> <dd></dd> <dt>

<span id="DVMounted"></span><span id="dvmounted"></span><span id="DVMOUNTED"></span>

**DVMounted** (0x2)


</dt> <dd></dd> <dt>

<span id="RollbackInProgress"></span><span id="rollbackinprogress"></span><span id="ROLLBACKINPROGRESS"></span>

**RollbackInProgress** (0x4)


</dt> <dd></dd> </dl>

</dd> <dt>

**TimeStamp**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when this shadow copy was created.

</dd> <dt>

**VdsLunInfo**
</dt> <dd> <dl> <dt>

Data type: **[**WT\_VDSLunInformation**](wt-vdsluninformation.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

LUN information for an exported shadow copy.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



 

 





