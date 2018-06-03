---
title: Detach method of the MSFT\_VirtualDisk class
description: Detaches a storage spaces-based virtual disk from a computer.
ms.assetid: ED70182D-C5FF-4BB7-9CDC-FDA4C60BB36D
keywords:
- Detach method Windows Storage Management API
- Detach method Windows Storage Management API , MSFT_VirtualDisk class
- MSFT_VirtualDisk class Windows Storage Management API , Detach method
topic_type:
- apiref
api_name:
- MSFT_VirtualDisk.Detach
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

# Detach method of the MSFT\_VirtualDisk class

Detaches a storage spaces-based virtual disk from a computer.

## Syntax


```mof
UInt32 Detach(
  [in]  String StorageNodeName,
  [out] String ExtendedStatus
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
</dt> <dt>

**The virtual disk could not complete the operation because its Manual Attach status does not permit it.** (50004)
</dt> </dl>

## Remarks

This operation is similar to [**Hide**](msft-virtualdisk-hide.md). However, there is no need for target and initiator configuration, because everything is done locally. Detaching a storage space will cause its corresponding disk object to be surprise-removed from the system. Note that detaching can happen in response to certain failure and warning conditions (such as failing redundancy, or thin provisioning capacity limits being reached).

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

 

 





