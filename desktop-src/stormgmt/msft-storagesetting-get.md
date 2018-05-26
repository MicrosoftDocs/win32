---
title: Get method of the MSFT\_StorageSetting class
description: Retrieves the current state of all storage settings for the computer.
ms.assetid: 044A260C-65A0-462B-8C2D-1553E17493D0
keywords:
- Get method Windows Storage Management API
- Get method Windows Storage Management API , MSFT_StorageSetting class
- MSFT_StorageSetting class Windows Storage Management API , Get method
topic_type:
- apiref
api_name:
- MSFT_StorageSetting.Get
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

# Get method of the MSFT\_StorageSetting class

Retrieves the current state of all storage settings for the computer.

## Syntax


```mof
UInt32 Get(
  [out] String StorageSettings
);
```



## Parameters

<dl> <dt>

*StorageSettings* \[out\]
</dt> <dd>

A string that contains an embedded instance of the [**MSFT\_StorageSetting**](msft-storagesetting.md) class that contains the storage settings.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageSetting**](msft-storagesetting.md)
</dt> </dl>

 

 





