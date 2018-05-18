---
title: SetDescription method of the MSFT\_StorageSubSystem class
description: Sets the Description property of the storage subsystem object instance.
ms.assetid: 'F0EDAB49-15C0-442C-A8A7-37567060FC5F'
keywords: ["SetDescription method Windows Storage Management API", "SetDescription method Windows Storage Management API , MSFT_StorageSubSystem class", "MSFT_StorageSubSystem class Windows Storage Management API , SetDescription method"]
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.SetDescription
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# SetDescription method of the MSFT\_StorageSubSystem class

Sets the **Description** property of the storage subsystem object instance.

## Syntax


```mof
UInt32 SetDescription(
  [in]  String Description,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Description* \[in\]
</dt> <dd>

The description to be set for the storage subsystem. This parameter is required and cannot be **NULL**.

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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





