---
title: Resize method of the MSFT\_VirtualDisk class
description: Resizes a virtual disk.
ms.assetid: 6672EB31-A5CE-49E0-8F4F-6874BC95F0DD
keywords:
- Resize method Windows Storage Management API
- Resize method Windows Storage Management API , MSFT_VirtualDisk class
- MSFT_VirtualDisk class Windows Storage Management API , Resize method
topic_type:
- apiref
api_name:
- MSFT_VirtualDisk.Resize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resize method of the MSFT\_VirtualDisk class

Resizes a virtual disk.

## Syntax


```mof
UInt32 Resize(
  [in, out] UInt64              Size,
  [in]      Boolean             RunAsJob,
  [out]     MSFT_StorageJob REF CreatedStorageJob,
  [out]     String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Size* \[in, out\]
</dt> <dd>

On input, this parameter is the requested new size, in bytes, for the virtual disk.

On output, this parameter receives actual new size of the virtual disk after the resize operation.

This parameter is required.

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

**Size Not Supported** (4097)
</dt> <dt>

**Not enough free space** (40000)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
</dt> <dt>

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
</dt> <dt>

**The virtual disk could not complete the operation because another computer controls its configuration.** (50002)
</dt> <dt>

**The virtual disk could not complete the operation because its health or operational status does not permit it.** (50003)
</dt> </dl>

## Remarks

The new size must be in the range of valid values given by the [**GetSupportedSize**](msft-storagepool-getsupportedsize.md) method of the [**MSFT\_StoragePool**](msft-storagepool.md) object.

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

 

 





