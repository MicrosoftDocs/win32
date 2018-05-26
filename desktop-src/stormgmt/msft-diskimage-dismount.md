---
title: Dismount method of the MSFT\_DiskImage class
description: Dismounts the disk image.
ms.assetid: 67E66529-1B2C-4F53-A7C5-03FC4E671D7A
keywords:
- Dismount method Windows Storage Management API
- Dismount method Windows Storage Management API , MSFT_DiskImage class
- MSFT_DiskImage class Windows Storage Management API , Dismount method
topic_type:
- apiref
api_name:
- MSFT_DiskImage.Dismount
api_location:
- vds.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Dismount method of the MSFT\_DiskImage class

Dismounts the disk image.

## Syntax


```mof
UInt32 Dismount();
```



## Parameters

This method has no parameters.

## Return value

This method returns [**OpenVirtualDisk**](https://msdn.microsoft.com/library/windows/desktop/dd323680) and [**DetachVirtualDisk**](https://msdn.microsoft.com/library/windows/desktop/dd323696) error codes converted to **HRESULT** codes.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| Header<br/>                   | <dl> <dt>Vds.h</dt> </dl>          |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DiskImage**](msft-diskimage.md)
</dt> </dl>

 

 





