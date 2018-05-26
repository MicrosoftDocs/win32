---
title: GetAttributes method of the MSFT\_Volume class
description: Retrieves the volume attributes.
ms.assetid: 82CA68FB-0394-4816-A8EA-510D8D926B1E
keywords:
- GetAttributes method Windows Storage Management API
- GetAttributes method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , GetAttributes method
topic_type:
- apiref
api_name:
- MSFT_Volume.GetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetAttributes method of the MSFT\_Volume class

Retrieves the volume attributes.

Only one attribute can be retrieved.

## Syntax


```mof
UInt32 GetAttributes(
  [out] Boolean VolumeScrubEnabled
);
```



## Parameters

<dl> <dt>

*VolumeScrubEnabled* \[out\]
</dt> <dd>

Indicates whether the automatic data integrity scanner should scrub files.

**TRUE** if files on this volume will be scrubbed, or **FALSE** otherwise.

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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





