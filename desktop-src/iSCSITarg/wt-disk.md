---
title: WT\_Disk class
description: Describes an iSCSI virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 518f9d66-043b-4b14-b4fe-f6c88f828526
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WT_Disk class iSCSI Software Target API
- WT_Disk class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- WT_Disk
- WT_Disk.WTD
- WT_Disk.Type
- WT_Disk.Flags
- WT_Disk.Status
- WT_Disk.Description
- WT_Disk.DevicePath
- WT_Disk.ActiveDevicePath
- WT_Disk.ParentPath
- WT_Disk.ParentWTD
- WT_Disk.Size
- WT_Disk.AllocatedSize
- WT_Disk.SerialNumber
- WT_Disk.DVMountStatus
- WT_Disk.DVTimeStamp
- WT_Disk.DVDeviceId
- WT_Disk.AsyncOpStartTime
- WT_Disk.AsyncOpEndTime
- WT_Disk.ResourceGroup
- WT_Disk.Enabled
- WT_Disk.Guid
- WT_Disk.DeviceVolumeGuid
- WT_Disk.VdsLunInfo
- WT_Disk.LMSnapshotId
- WT_Disk.InternalCode
- WT_Disk.BlockSize
- WT_Disk.IsBasedOnUnderlyingRedundancy
api_location:
- WtWmiProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WT\_Disk class

Describes an iSCSI virtual disk.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_Disk
{
  uint32               WTD;
  sint32               Type;
  sint32               Flags;
  sint32               Status;
  string               Description;
  string               DevicePath;
  string               ActiveDevicePath;
  string               ParentPath;
  uint32               ParentWTD;
  uint32               Size;
  uint32               AllocatedSize;
  string               SerialNumber;
  sint32               DVMountStatus;
  datetime             DVTimeStamp;
  string               DVDeviceId;
  datetime             AsyncOpStartTime;
  datetime             AsyncOpEndTime;
  string               ResourceGroup;
  boolean              Enabled;
  string               Guid;
  string               DeviceVolumeGuid;
  WT_VDSLunInformation VdsLunInfo;
  string               LMSnapshotId;
  uint32               InternalCode;
  uint64               BlockSize;
  boolean              IsBasedOnUnderlyingRedundancy;
};
```

## Members

The **WT\_Disk** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **WT\_Disk** class has these methods.



| Method                                                                 | Description                                                                                                                                                                                                                                                                                            |
|:-----------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CancelAsyncOperation**](cancelasyncoperation-wt-disk.md)           | **Windows Server 2012:** This method is not supported until Windows Server 2012 R2.<br/> Cancel any asynchronous operation on this disk.<br/>                                                                                                                                              |
| [**CreateRamWTDisk**](createramwtdisk-wt-disk.md)                     | **Windows Server 2012:** This method is not supported until Windows Server 2012 R2.<br/> Create a new RAM-based iSCSI virtual disk.<br/>                                                                                                                                                   |
| [**CreateVhdWTDisk**](createvhdwtdisk-wt-disk.md)                     | **Windows Server 2012:** This method is not supported until Windows Server 2012 R2.<br/> Create a new VHDX-based iSCSI virtual disk.<br/>                                                                                                                                                  |
| [**Extend**](extend-wt-disk.md)                                       | **Windows Server 2012 R2:** This method is deprecated. Use the [**Resize**](resize-wt-disk.md) method instead.<br/> Extends a virtual disk.<br/>                                                                                                                                          |
| [**GetAsyncOperationProgress**](getasyncoperationprogress-wt-disk.md) | **Windows Server 2012:** This method is not supported until Windows Server 2012 R2.<br/> Get the asynchronous operation progress information for this iSCSI virtual disk.<br/>                                                                                                             |
| [**GetDVMountPoints**](getdvmountpoints-wt-disk.md)                   | **Windows Server 2012 R2:** This method is deprecated.<br/> Returns a list of all mount points that belong to the virtual disk. This is used for locally mounted shadow copies.<br/>                                                                                                       |
| [**GetRollbackProgress**](wt-disk-getrollbackprogress.md)             | **Windows Server 2012 R2:** This method is deprecated. Use [**GetAsyncOperationProgress**](getasyncoperationprogress-wt-disk.md) instead.<br/> Retrieves the rollback progress information for the disk.<br/>                                                                             |
| [**ImportWTDisk**](importwtdisk-wt-disk.md)                           | **Windows Server 2012:** This method is not supported until Windows Server 2012 R2.<br/> Import an existing VHD or SCSI device as a iSCSI virtual disk.<br/>                                                                                                                               |
| [**NewDiffWTDisk**](wt-disk-newdiffwtdisk.md)                         | **Windows Server 2012 R2:** This method is deprecated. Use the [**CreateRamWTDisk**](createramwtdisk-wt-disk.md), [**CreateVhdWTDisk**](createvhdwtdisk-wt-disk.md), or [**ImportWTDisk**](importwtdisk-wt-disk.md) methods instead.<br/> Creates a new differencing virtual disk.<br/> |
| [**NewWTDisk**](newwtdisk-wt-disk.md)                                 | **Windows Server 2012 R2:** This method is deprecated. Use the [**CreateRamWTDisk**](createramwtdisk-wt-disk.md), [**CreateVhdWTDisk**](createvhdwtdisk-wt-disk.md), or [**ImportWTDisk**](importwtdisk-wt-disk.md) methods instead.<br/> Creates a new virtual disk.<br/>              |
| [**Resize**](resize-wt-disk.md)                                       | **Windows Server 2012:** This method is not supported until Windows Server 2012 R2.<br/> Resize iSCSI virtual disk.<br/>                                                                                                                                                                   |



 

### Properties

The **WT\_Disk** class has these properties.

<dl> <dt>

**ActiveDevicePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Full active device path to the VHD file on the Microsoft iSCSI Target Server.

For a pass-through device, this is a decorated active Win32 device path in the form "SCSI:&lt;*win32\_device\_path*&gt;". For other device types, this property always has the same value as the *DevicePath* property.

**Windows Server 2012:** This property is not supported until Windows Server 2012 R2.

</dd> <dt>

**AllocatedSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Allocated size of the virtual disk, in megabytes.

</dd> <dt>

**AsyncOpEndTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When an asynchronous operation ended, whether it ended successfully or not.

**Windows Server 2012:** This property is not supported until Windows Server 2012 R2.

</dd> <dt>

**AsyncOpStartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When an asynchronous operation started.

**Windows Server 2012:** This property is not supported until Windows Server 2012 R2.

</dd> <dt>

**BlockSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Logical block or sector size of the virtual disk, in bytes.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A user-friendly description of the virtual disk.

</dd> <dt>

**DevicePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Full path to the VHD file on the Microsoft iSCSI Target Server.

</dd> <dt>

**DeviceVolumeGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier of the volume where the disk resides.

</dd> <dt>

**DVDeviceId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Windows Server 2012 R2:** This property is deprecated.

Reserved for system use.

</dd> <dt>

**DVMountStatus**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (NotMounted, MountSnapshot), **ValueMap** (0, 1)
</dt> </dl>

**Windows Server 2012 R2:** This property is deprecated.

The current data view mount status.

</dd> <dt>

**DVTimeStamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Windows Server 2012 R2:** This property is deprecated.

If the value of *DVMountStatus* is **MountSnapshot**, *DVTimeStamp* contains the date and time when the snapshot was taken. Otherwise, *DVTimeStamp* is an empty string.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the disk is enabled.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Flags that indicate characteristics of the disk. This property is a bitmask and may contain one of the following possible values.

<dt>

<span id="ReadOnlyWTDisk"></span><span id="readonlywtdisk"></span><span id="READONLYWTDISK"></span>

<span id="ReadOnlyWTDisk"></span><span id="readonlywtdisk"></span><span id="READONLYWTDISK"></span>**ReadOnlyWTDisk** (0x00000001)


</dt> <dd>

The disk is a read-only disk.

**Windows Server 2012:** This property value is not supported before Windows Server 2012 R2.

</dd> <dt>

<span id="ShadowWTDisk"></span><span id="shadowwtdisk"></span><span id="SHADOWWTDISK"></span>

<span id="ShadowWTDisk"></span><span id="shadowwtdisk"></span><span id="SHADOWWTDISK"></span>**ShadowWTDisk** (0x00000002)


</dt> <dd>

The disk is a shadow copy disk.

</dd> </dl>

</dd> <dt>

**Guid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for system use.

</dd> <dt>

**InternalCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for system use.

</dd> <dt>

**IsBasedOnUnderlyingRedundancy**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the device is based on the underlying storage redundancy.

</dd> <dt>

**LMSnapshotId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the disk contains a volume shadow copy that is locally mounted, this property contains the shadow copy identifier.

</dd> <dt>

**ParentPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Full path to the parent VHD file on the Microsoft iSCSI Target Server. The parent VHD is the base virtual disk file that the differencing VHD links to.

</dd> <dt>

**ParentWTD**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Parent iSCSI Disk Index.

</dd> <dt>

**ResourceGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the cluster group that this virtual disk belongs to. If the Microsoft iSCSI Target Server service is not running on a Microsoft Failover Cluster, this property is an empty string.

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Serial number of the virtual disk.

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size of the virtual disk, in megabytes.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (Not Connected, Connected, Reverting), **ValueMap** (0, 1, 2)
</dt> </dl>

Status of the virtual disk.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

VHD type.

**Windows Server 2012:** The following property values are not supported before Windows Server 2012 R2.

<dt>

<span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span>

**Fixed** (2)


</dt> <dd></dd> <dt>

<span id="Dynamic"></span><span id="dynamic"></span><span id="DYNAMIC"></span>

**Dynamic** (3)


</dt> <dd></dd> <dt>

<span id="Differencing"></span><span id="differencing"></span><span id="DIFFERENCING"></span>

**Differencing** (4)


</dt> <dd></dd> <dt>

<span id="ReadOnlySnapshot"></span><span id="readonlysnapshot"></span><span id="READONLYSNAPSHOT"></span>

**ReadOnlySnapshot** (30000)


</dt> <dd></dd> <dt>

<span id="WritableSnapshot"></span><span id="writablesnapshot"></span><span id="WRITABLESNAPSHOT"></span>

**WritableSnapshot** (30001)


</dt> <dd></dd> <dt>

<span id="RamDisk"></span><span id="ramdisk"></span><span id="RAMDISK"></span>

**RamDisk** (30002)


</dt> <dd></dd> <dt>

<span id="PassThrough"></span><span id="passthrough"></span><span id="PASSTHROUGH"></span>

**PassThrough** (30003)


</dt> <dd></dd> </dl>

**Windows Server 2012:** The following property values are the only ones supported on Windows Server 2012.

<dt>

<span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span>

**Fixed** (1)


</dt> <dd></dd> <dt>

<span id="Differencing"></span><span id="differencing"></span><span id="DIFFERENCING"></span>

**Differencing** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**VdsLunInfo**
</dt> <dd> <dl> <dt>

Data type: **[**WT\_VDSLunInformation**](wt-vdsluninformation.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

LUN information for the disk, used by the [Virtual Disk Service](https://msdn.microsoft.com/library/windows/desktop/bb986750) (VDS).

</dd> <dt>

**WTD**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

An iSCSI disk identifier that uniquely identifies the virtual disk. This index is automatically assigned by Microsoft iSCSI Target Server during the creation process and cannot be changed.

</dd> </dl>

## Remarks

It is possible for one or more property values to return **NULL** intermittently due to transient issues. In this case, re-querying may return all property values correctly.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



 

 





