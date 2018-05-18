---
title: AddTargetPort method of the MSFT\_MaskingSet class
description: Adds one or more target ports to the masking set.
ms.assetid: '36FAC871-02AF-4913-9E46-87F4DED0AAC2'
keywords: ["AddTargetPort method Windows Storage Management API", "AddTargetPort method Windows Storage Management API , MSFT_MaskingSet class", "MSFT_MaskingSet class Windows Storage Management API , AddTargetPort method"]
topic_type:
- apiref
api_name:
- MSFT_MaskingSet.AddTargetPort
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# AddTargetPort method of the MSFT\_MaskingSet class

Adds one or more target ports to the masking set.

## Syntax


```mof
UInt32 AddTargetPort(
  [in]  String                  TargetPortAddresses[],
  [in]  Boolean                 RunAsJob,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String                  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*TargetPortAddresses* \[in\]
</dt> <dd>

An array of strings containing target port addresses. This parameter is required and cannot be NULL.

</dd> <dt>

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

**The target port address specified is not valid.** (54000)
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

 

 





