---
title: Flush method of the MSFT\_Volume class
description: Flushes the cached data in the volumes file system to disk.
ms.assetid: 25E48B8F-65C7-46D5-BFFE-6573133148EB
keywords:
- Flush method Windows Storage Management API
- Flush method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , Flush method
topic_type:
- apiref
api_name:
- MSFT_Volume.Flush
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

# Flush method of the MSFT\_Volume class

Flushes the cached data in the volume's file system to disk.

## Syntax


```mof
UInt32 Flush();
```



## Parameters

This method has no parameters.

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
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





