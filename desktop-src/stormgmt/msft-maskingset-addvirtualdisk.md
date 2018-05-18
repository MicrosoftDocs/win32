---
title: AddVirtualDisk method of the MSFT\_MaskingSet class
description: Adds one or more virtual disks to the masking set.
ms.assetid: 'D81ED854-CF77-4C55-9A2D-D17D7E64FD3B'
keywords: ["AddVirtualDisk method Windows Storage Management API", "AddVirtualDisk method Windows Storage Management API , MSFT_MaskingSet class", "MSFT_MaskingSet class Windows Storage Management API , AddVirtualDisk method"]
topic_type:
- apiref
api_name:
- MSFT_MaskingSet.AddVirtualDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# AddVirtualDisk method of the MSFT\_MaskingSet class

Adds one or more virtual disks to the masking set.

Adding a virtual disk allows the disk to be shown to the initiators contained in the set.

## Syntax


```mof
UInt32 AddVirtualDisk(
  [in]  String                  VirtualDiskNames[],
  [in]  UInt16                  DeviceNumbers[],
  [in]  UInt16                  DeviceAccesses[],
  [in]  Boolean                 RunAsJob,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String                  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*VirtualDiskNames* \[in\]
</dt> <dd>

Array of strings containing virtual disk names. This parameter is required and cannot be NULL.

</dd> <dt>

*DeviceNumbers* \[in\]
</dt> <dd>

Array of device numbers for the virtual disks. This parameter is required.

</dd> <dt>

*DeviceAccesses* \[in\]
</dt> <dd>

Array of device accesses for the virtual disks.

<dl> <dt>

<span id="Read_Write"></span><span id="read_write"></span><span id="READ_WRITE"></span>**Read Write** (2)
</dt> <dt>

<span id="Read-Only"></span><span id="read-only"></span><span id="READ-ONLY"></span>**Read-Only** (3)
</dt> <dt>

<span id="No_Access"></span><span id="no_access"></span><span id="NO_ACCESS"></span>**No Access** (4)
</dt> </dl> </dd> <dt>

*RunAsJob* \[in\]
</dt> <dd>

This parameter controls the asynchronous behavior the method will follow.

**TRUE** to use the *CreatedStorageJob* out parameter when the request takes a long time to service; otherwise **FALSE**.

If a storage job has been created to track the operation, this method will return 4096 - 'Method Parameters Checked - Job Started'. Note, even if *RunAsJob* is **TRUE**, the method can still return a result if it finishes in sufficient time.

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation (i.e. synchronous unless requested otherwise).

</dd> <dt>

*CreatedStorageJob* \[out\]
</dt> <dd>

If *RunAsJob* is set to **TRUE** and this method takes a while to execute, this parameter returns a reference to the storage job used to track the long running operation.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**The specified virtual disk could not be found.** (50000)
</dt> <dt>

**The device number specified is not valid.** (52000)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_MaskingSet**](msft-maskingset.md)
</dt> </dl>

 

 





