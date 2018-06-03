---
title: GetCorruptionCount method of the MSFT\_Volume class
description: Retrieves the corruption count for the volume.
ms.assetid: 30F417D9-A4E3-49A3-A86E-79AFF5CC9D1C
keywords:
- GetCorruptionCount method Windows Storage Management API
- GetCorruptionCount method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , GetCorruptionCount method
topic_type:
- apiref
api_name:
- MSFT_Volume.GetCorruptionCount
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

# GetCorruptionCount method of the MSFT\_Volume class

Retrieves the corruption count for the volume.

## Syntax


```mof
UInt32 GetCorruptionCount(
  [out] UInt32 CorruptionCount,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*CorruptionCount* \[out\]
</dt> <dd>

The corruption count for the volume.

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

 

 





