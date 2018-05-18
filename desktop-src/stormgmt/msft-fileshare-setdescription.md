---
title: SetDescription method of the MSFT\_FileShare class
description: Allows a user to set the description field of the file share.
ms.assetid: '09CEA9ED-198E-4163-8981-8B164BDB8E34'
keywords: ["SetDescription method Windows Storage Management API", "SetDescription method Windows Storage Management API , MSFT_FileShare class", "MSFT_FileShare class Windows Storage Management API , SetDescription method"]
topic_type:
- apiref
api_name:
- MSFT_FileShare.SetDescription
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# SetDescription method of the MSFT\_FileShare class

Allows a user to set the description field of the file share.

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

A user settable description of the file share. This field can be used to store extra free-form information, such as notes or details about the intended usage.

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
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_FileShare**](msft-fileshare.md)
</dt> </dl>

 

 





