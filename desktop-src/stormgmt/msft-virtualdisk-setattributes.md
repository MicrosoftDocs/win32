---
title: SetAttributes method of the MSFT\_VirtualDisk class
description: Sets or updates various attributes for the virtual disk.
ms.assetid: AC57C471-7424-4F01-9C1E-44E523BBC8F2
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_VirtualDisk class
- MSFT_VirtualDisk class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
api_name:
- MSFT_VirtualDisk.SetAttributes
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

# SetAttributes method of the MSFT\_VirtualDisk class

Sets or updates various attributes for the virtual disk.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  Boolean IsManualAttach,
  [in]  UInt16  Access,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*IsManualAttach* \[in\]
</dt> <dd>

If **TRUE**, this virtual disk will only be attached to the system if an explicit call is made to the [**Attach**](msft-virtualdisk-attach.md) method. Note that this property is specific to storage spaces.

</dd> <dt>

*Access* \[in\]
</dt> <dd>

Indicates whether the virtual disk is available for read and write access.

<dl> <dt>

<span id="Readable"></span><span id="readable"></span><span id="READABLE"></span>**Readable** (1)
</dt> <dt>

<span id="Writeable"></span><span id="writeable"></span><span id="WRITEABLE"></span>**Writeable** (2)
</dt> <dt>

<span id="Read_Write"></span><span id="read_write"></span><span id="READ_WRITE"></span>**Read/Write** (3)
</dt> <dt>

<span id="Write_Once"></span><span id="write_once"></span><span id="WRITE_ONCE"></span>**Write Once** (4)
</dt> </dl> </dd> <dt>

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
</dt> <dt>

**The virtual disk could not complete the operation because another computer controls its configuration.** (50002)
</dt> <dt>

**The virtual disk could not complete the operation because its health or operational status does not permit it.** (50003)
</dt> </dl>

## Remarks

Not all parameters must be specified, and only those that are specified will be updated.

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

 

 





