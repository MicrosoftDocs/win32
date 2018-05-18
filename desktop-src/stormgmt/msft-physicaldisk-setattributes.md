---
title: SetAttributes method of the MSFT\_PhysicalDisk class
description: Updates the attributes of the physical disk.
ms.assetid: '8A7194B5-345D-43F1-933D-6061C7107D80'
keywords: ["SetAttributes method Windows Storage Management API", "SetAttributes method Windows Storage Management API , MSFT_PhysicalDisk class", "MSFT_PhysicalDisk class Windows Storage Management API , SetAttributes method"]
topic_type:
- apiref
api_name:
- MSFT_PhysicalDisk.SetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# SetAttributes method of the MSFT\_PhysicalDisk class

Updates the attributes of the physical disk.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  UInt16 MediaType,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*MediaType* \[in\]
</dt> <dd>

The media type of the physical disk.



| Value                                                                                                | Meaning                |
|------------------------------------------------------------------------------------------------------|------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | Unspecified<br/> |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | HDD<br/>         |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | SSD<br/>         |
| <span id="5"></span><dl> <dt>**5**</dt> </dl> | SCM<br/>         |



 

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

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
</dt> <dt>

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
</dt> </dl>

 

 





