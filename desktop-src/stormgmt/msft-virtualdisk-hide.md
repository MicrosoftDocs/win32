---
title: Hide method of the MSFT\_VirtualDisk class
description: Hides a virtual disk from an initiator.
ms.assetid: E47716E5-9397-4AAB-B33F-CB39188A683A
keywords:
- Hide method Windows Storage Management API
- Hide method Windows Storage Management API , MSFT_VirtualDisk class
- MSFT_VirtualDisk class Windows Storage Management API , Hide method
topic_type:
- apiref
api_name:
- MSFT_VirtualDisk.Hide
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Hide method of the MSFT\_VirtualDisk class

Hides a virtual disk from an initiator.

This operation is also known as "unexposing" or "masking" a virtual disk.

## Syntax


```mof
UInt32 Hide(
  [in]  String              TargetPortAddresses[],
  [in]  String              InitiatorAddress,
  [in]  Boolean             RunAsJob,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*TargetPortAddresses* \[in\]
</dt> <dd>

An array of target port addresses for which the virtual disk should be hidden. Note: This array may contain a subset of the addresses originally given in the [**Show**](msft-virtualdisk-show.md) method.

This parameter is required and cannot be **NULL**.

</dd> <dt>

*InitiatorAddress* \[in\]
</dt> <dd>

The address of the initiator from which the virtual disk should be hidden.

This parameter is required and cannot be **NULL**.

</dd> <dt>

*RunAsJob* \[in\]
</dt> <dd>

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

</dd> <dt>

*CreatedStorageJob* \[out\]
</dt> <dd>

If *RunAsJob* is set to **TRUE** and this method takes a long time to execute, this parameter receives a reference to the storage job object that is used to track the long-running operation.

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

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**The HostType requested is not supported.** (52001)
</dt> <dt>

**The initiator address specified is not valid** (53000)
</dt> <dt>

**The target port address specified is not valid.** (54000)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
</dt> </dl>

 

 





