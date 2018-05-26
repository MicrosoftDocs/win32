---
title: SetDedupMode method of the MSFT\_Volume class
description: Enables or disables deduplication on the volume.
ms.assetid: A37E60BA-914A-4876-B411-138B8D9335B3
keywords:
- SetDedupMode method Windows Storage Management API
- SetDedupMode method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , SetDedupMode method
topic_type:
- apiref
api_name:
- MSFT_Volume.SetDedupMode
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

# SetDedupMode method of the MSFT\_Volume class

Enables or disables deduplication on the volume.

## Syntax


```mof
UInt32 SetDedupMode(
  [in]  UInt32 SetDedupMode,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*SetDedupMode* \[in\]
</dt> <dd>

New deduplication mode of the volume.

<dl> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (0)
</dt> <dt>

<span id="GeneralPurpose"></span><span id="generalpurpose"></span><span id="GENERALPURPOSE"></span>**GeneralPurpose** (1)
</dt> <dt>

<span id="HyperV"></span><span id="hyperv"></span><span id="HYPERV"></span>**HyperV** (2)
</dt> <dt>

<span id="Backup"></span><span id="backup"></span><span id="BACKUP"></span>**Backup** (3)
</dt> <dt>

<span id="NotAvailable"></span><span id="notavailable"></span><span id="NOTAVAILABLE"></span>**NotAvailable** (4)
</dt> </dl> </dd> <dt>

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

 

 





