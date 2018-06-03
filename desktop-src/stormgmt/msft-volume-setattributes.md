---
title: SetAttributes method of the MSFT\_Volume class
description: Sets or changes the volume attributes.
ms.assetid: 526F2E01-6E34-4891-ACF9-A8A87FDF0271
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
api_name:
- MSFT_Volume.SetAttributes
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

# SetAttributes method of the MSFT\_Volume class

Sets or changes the volume attributes.

Only one attribute can be set or changed.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  Boolean EnableVolumeScrub,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*EnableVolumeScrub* \[in\]
</dt> <dd>

Specifies whether the automatic data integrity scanner should repair files.

**TRUE** if files on this volume will be scrubbed, or **FALSE** otherwise.

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

**This setting may not be changed due to the group policy setting** (43015)
</dt> <dt>

**This setting may not be changed due to the global registry setting** (43016)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





