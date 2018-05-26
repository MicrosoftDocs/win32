---
title: DeleteObject method of the MSFT\_MaskingSet class
description: Deletes the masking set instance.
ms.assetid: 169B2338-3B9C-488F-9BF1-9E64A7915683
keywords:
- DeleteObject method Windows Storage Management API
- DeleteObject method Windows Storage Management API , MSFT_MaskingSet class
- MSFT_MaskingSet class Windows Storage Management API , DeleteObject method
topic_type:
- apiref
api_name:
- MSFT_MaskingSet.DeleteObject
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

# DeleteObject method of the MSFT\_MaskingSet class

Deletes the masking set instance.

## Syntax


```mof
UInt32 DeleteObject(
  [in]  Boolean                 RunAsJob,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String                  ExtendedStatus
);
```



## Parameters

<dl> <dt>

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

**Cache out of date** (40003)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
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

[**MSFT\_MaskingSet**](msft-maskingset.md)
</dt> </dl>

 

 





