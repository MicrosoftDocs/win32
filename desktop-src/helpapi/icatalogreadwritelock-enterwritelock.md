---
title: ICatalogReadWriteLock EnterWriteLock method
description: method EnterWriteLock - creates a write lock
ms.assetid: 3cafb431-6fce-4052-aac4-bb97a903c671
keywords:
- EnterWriteLock method HelpAPI
- EnterWriteLock method HelpAPI , ICatalogReadWriteLock interface
- ICatalogReadWriteLock interface HelpAPI , EnterWriteLock method
topic_type:
- apiref
api_name:
- ICatalogReadWriteLock.EnterWriteLock
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

# ICatalogReadWriteLock::EnterWriteLock method

method EnterWriteLock - creates a write lock

## Syntax


```C++
HRESULT EnterWriteLock(
  [in]          long         timeout,
  [out, retval] VARIANT_BOOL *pRetVal
);
```



## Parameters

<dl> <dt>

*timeout* \[in\]
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

[**ICatalogReadWriteLock**](icatalogreadwritelock.md)
</dt> </dl>

 

 





