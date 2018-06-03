---
title: GetDedupProperties method of the MSFT\_Volume class
description: Gets deduplication properties of the volume.
ms.assetid: 94B6A3CD-7D52-468F-9E6C-54870C97A383
keywords:
- GetDedupProperties method Windows Storage Management API
- GetDedupProperties method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , GetDedupProperties method
topic_type:
- apiref
api_name:
- MSFT_Volume.GetDedupProperties
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

# GetDedupProperties method of the MSFT\_Volume class

Gets deduplication properties of the volume.

## Syntax


```mof
UInt32 GetDedupProperties(
  [out] String DedupProperties,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*DedupProperties* \[out\]
</dt> <dd>

An array of strings containing embedded [**MSFT\_DedupProperties**](msft-dedupproperties.md) objects specifying the deduplication properties of the volume.

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

**Object Not Found** (8)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**Deduplication feature is not available** (43020)
</dt> <dt>

**Deduplication is not enabled for the volume** (43021)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





