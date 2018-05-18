---
title: SetFriendlyName method of the MSFT\_FileServer class
description: Allows the file server to be renamed.
ms.assetid: 'B9E430B6-36B2-4370-ABCE-E6DF2F395DD4'
keywords: ["SetFriendlyName method Windows Storage Management API", "SetFriendlyName method Windows Storage Management API , MSFT_FileServer class", "MSFT_FileServer class Windows Storage Management API , SetFriendlyName method"]
topic_type:
- apiref
api_name:
- MSFT_FileServer.SetFriendlyName
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# SetFriendlyName method of the MSFT\_FileServer class

Allows the file server to be renamed.

## Syntax


```mof
UInt32 SetFriendlyName(
  [in]  String FriendlyName,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in\]
</dt> <dd>

The friendly name to be set for the file server. This parameter is required and cannot be **NULL**.

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

[**MSFT\_FileServer**](msft-fileserver.md)
</dt> </dl>

 

 





