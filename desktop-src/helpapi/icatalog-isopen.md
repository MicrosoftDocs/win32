---
title: ICatalog IsOpen property
description: Returns true if a catalog is currently open, else false
ms.assetid: 872f02b9-677a-4c40-ace3-649f9d5fbadf
keywords:
- IsOpen property HelpAPI
- IsOpen property HelpAPI , ICatalog interface
- ICatalog interface HelpAPI , IsOpen property
topic_type:
- apiref
api_name:
- ICatalog.IsOpen
- ICatalog.get_IsOpen
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ICatalog::IsOpen property

Returns true if a catalog is currently open, else false

This property is read-only.

## Syntax


```C++
HRESULT get_IsOpen(
  [out, retval] VARIANT_BOOL *pRetVal
);
```



## Property value

True if a catalog is currently open, otherwise false.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**ICatalog**](icatalog.md)
</dt> </dl>

 

 





