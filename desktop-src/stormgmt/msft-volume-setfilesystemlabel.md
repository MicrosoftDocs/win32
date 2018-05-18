---
title: SetFileSystemLabel method of the MSFT\_Volume class
description: Sets the file system label for the volume.
ms.assetid: 'BD93DE04-A779-49DC-8764-75A98F8B8AF8'
keywords: ["SetFileSystemLabel method Windows Storage Management API", "SetFileSystemLabel method Windows Storage Management API , MSFT_Volume class", "MSFT_Volume class Windows Storage Management API , SetFileSystemLabel method"]
topic_type:
- apiref
api_name:
- MSFT_Volume.SetFileSystemLabel
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# SetFileSystemLabel method of the MSFT\_Volume class

Sets the file system label for the volume.

## Syntax


```mof
UInt32 SetFileSystemLabel(
  [in]  String FileSystemLabel,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FileSystemLabel* \[in\]
</dt> <dd>

The file system label.

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

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





