---
title: ICatalog GetReadWriteLock method
description: Method GetReadWriteLock - Return a reference to the catalog read write lock object for a given location
ms.assetid: 4f2be8ba-886c-4d33-8264-63b056bae9eb
keywords:
- GetReadWriteLock method HelpAPI
- GetReadWriteLock method HelpAPI , ICatalog interface
- ICatalog interface HelpAPI , GetReadWriteLock method
topic_type:
- apiref
api_name:
- ICatalog.GetReadWriteLock
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ICatalog::GetReadWriteLock method

Method GetReadWriteLock - Return a reference to the catalog read write lock object for a given location

## Syntax


```C++
HRESULT GetReadWriteLock(
  [in]          BSTR                  catalogPath,
  [out, retval] ICatalogReadWriteLock **pRetVal
);
```



## Parameters

<dl> <dt>

*catalogPath* \[in\]
</dt> <dd></dd> <dt>

*pRetVal* \[out, retval\]
</dt> <dd></dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

 

 





