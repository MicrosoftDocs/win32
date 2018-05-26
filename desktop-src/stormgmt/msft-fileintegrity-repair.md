---
title: Repair method of the MSFT\_FileIntegrity class
description: Repairs the data for the specified file.
ms.assetid: 09FF3AEB-4BD2-4A53-B46D-B3B84CAB02A5
keywords:
- Repair method Windows Storage Management API
- Repair method Windows Storage Management API , MSFT_FileIntegrity class
- MSFT_FileIntegrity class Windows Storage Management API , Repair method
topic_type:
- apiref
api_name:
- MSFT_FileIntegrity.Repair
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

# Repair method of the MSFT\_FileIntegrity class

Repairs the data for the specified file.

## Syntax


```mof
UInt32 Repair(
  [in]  String FileName,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FileName* \[in\]
</dt> <dd>

The file to repair.

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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_FileIntegrity**](msft-fileintegrity.md)
</dt> </dl>

 

 





