---
title: Clear method of the MSFT\_FileStorageTier class
description: Unpins a volume or file from a storage tier.
ms.assetid: 771004D8-8D11-4B34-8CF4-F6DF785C6634
keywords:
- Clear method Windows Storage Management API
- Clear method Windows Storage Management API , MSFT_FileStorageTier class
- MSFT_FileStorageTier class Windows Storage Management API , Clear method
topic_type:
- apiref
api_name:
- MSFT_FileStorageTier.Clear
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

# Clear method of the MSFT\_FileStorageTier class

Unpins a volume or file from a storage tier.

## Syntax


```mof
UInt32 Clear(
  [in] String FilePath
);
```



## Parameters

<dl> <dt>

*FilePath* \[in\]
</dt> <dd>

The path of a file to unpin.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_FileStorageTier**](msft-filestoragetier.md)
</dt> </dl>

 

 





