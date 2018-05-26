---
title: Get method of the MSFT\_FileIntegrity class
description: Retrieves the file integrity information for the specified file.
ms.assetid: C376D77A-1AB6-4000-AB5E-814104B9751B
keywords:
- Get method Windows Storage Management API
- Get method Windows Storage Management API , MSFT_FileIntegrity class
- MSFT_FileIntegrity class Windows Storage Management API , Get method
topic_type:
- apiref
api_name:
- MSFT_FileIntegrity.Get
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

# Get method of the MSFT\_FileIntegrity class

Retrieves the file integrity information for the specified file.

## Syntax


```mof
UInt32 Get(
  [in]  FileName String,
  [out] String   FileIntegrity,
  [out] String   ExtendedStatus
);
```



## Parameters

<dl> <dt>

*String* \[in\]
</dt> <dd>

The file to get the integrity information for.

</dd> <dt>

*FileIntegrity* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_FileIntegrity**](msft-fileintegrity.md) object that contains the file integrity information.

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

 

 





