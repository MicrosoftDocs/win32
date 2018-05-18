---
title: Attach method of the MSFT\_VirtualDisk class
description: Attaches a storage spaces-based virtual disk to the system.
ms.assetid: '1B2768DB-EDDF-406E-B88B-FEA4F471D37C'
keywords: ["Attach method Windows Storage Management API", "Attach method Windows Storage Management API , MSFT_VirtualDisk class", "MSFT_VirtualDisk class Windows Storage Management API , Attach method"]
topic_type:
- apiref
api_name:
- MSFT_VirtualDisk.Attach
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# Attach method of the MSFT\_VirtualDisk class

Attaches a storage spaces-based virtual disk to the system.

## Syntax


```mof
UInt32 Attach(
  [in]  String StorageNodeName,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*StorageNodeName* \[in\]
</dt> <dd>

The name of the storage node.

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
</dt> <dt>

**The virtual disk could not complete the operation because another computer controls its configuration.** (50002)
</dt> <dt>

**The virtual disk could not complete the operation because its health or operational status does not permit it.** (50003)
</dt> </dl>

## Remarks

This operation is similar to [**Show**](msft-virtualdisk-show.md) and [**Hide**](msft-virtualdisk-hide.md). However, there is no need for target and initiator configuration, because everything is done locally. Depending on the computer's **NewDiskPolicy** (formerly SAN policy), a storage space may need to be attached by calling this method before it can be used.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
</dt> </dl>

 

 





