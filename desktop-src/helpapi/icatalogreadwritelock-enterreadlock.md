---
title: ICatalogReadWriteLock EnterReadLock method
description: method EnterReadLock - creates a read lock
ms.assetid: '304f396b-84af-4d96-9181-26f30c7191a2'
keywords: ["EnterReadLock method HelpAPI", "EnterReadLock method HelpAPI , ICatalogReadWriteLock interface", "ICatalogReadWriteLock interface HelpAPI , EnterReadLock method"]
topic_type:
- apiref
api_name:
- ICatalogReadWriteLock.EnterReadLock
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ICatalogReadWriteLock::EnterReadLock method

method EnterReadLock - creates a read lock

## Syntax


```C++
HRESULT EnterReadLock(
  [in]          long         timeout,
  [out, retval] VARIANT_BOOL *pRetVal
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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**ICatalogReadWriteLock**](icatalogreadwritelock.md)
</dt> </dl>

 

 





