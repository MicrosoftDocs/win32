---
title: UpdateHostStorageCache method of the MSFT\_StorageSetting class
description: Updates the internal cache of software objects (that is, Disks, Partitions, Volumes) for the storage setting.
ms.assetid: A4B49108-44F2-4BD0-A642-9A0755DCFC81
keywords:
- UpdateHostStorageCache method Windows Storage Management API
- UpdateHostStorageCache method Windows Storage Management API , MSFT_StorageSetting class
- MSFT_StorageSetting class Windows Storage Management API , UpdateHostStorageCache method
topic_type:
- apiref
api_name:
- MSFT_StorageSetting.UpdateHostStorageCache
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

# UpdateHostStorageCache method of the MSFT\_StorageSetting class

Updates the internal cache of software objects (that is, Disks, Partitions, Volumes) for the storage setting. This is useful if there was extensive change to the storage layout exposed to that computer.

## Syntax


```mof
UInt32 UpdateHostStorageCache();
```



## Parameters

This method has no parameters.

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

 

 





