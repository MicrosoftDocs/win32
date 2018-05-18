---
title: SetAttributes method of the MSFT\_StorageSubSystem class
description: Sets the SupportsAutomaticObjectClustering field of the storage subsystem object instance.
ms.assetid: '226BCD54-EA3A-4917-9688-7293C1C049EA'
keywords: ["SetAttributes method Windows Storage Management API", "SetAttributes method Windows Storage Management API , MSFT_StorageSubSystem class", "MSFT_StorageSubSystem class Windows Storage Management API , SetAttributes method"]
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.SetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# SetAttributes method of the MSFT\_StorageSubSystem class

Sets the **SupportsAutomaticObjectClustering** field of the storage subsystem object instance.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  Boolean AutomaticClusteringEnabled,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*AutomaticClusteringEnabled* \[in\]
</dt> <dd>

**TRUE** to enable automatic object clustering; otherwise, **FALSE**. This parameter is required and cannot be **NULL**.

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

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





