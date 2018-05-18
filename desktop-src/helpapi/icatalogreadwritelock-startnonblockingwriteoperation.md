---
title: ICatalogReadWriteLock StartNonBlockingWriteOperation method
description: method StartNonBlockingWriteOperation - creates a non-blocking write lock
ms.assetid: '33d1994d-6b05-4213-b23d-9522f6b1cf75'
keywords: ["StartNonBlockingWriteOperation method HelpAPI", "StartNonBlockingWriteOperation method HelpAPI , ICatalogReadWriteLock interface", "ICatalogReadWriteLock interface HelpAPI , StartNonBlockingWriteOperation method"]
topic_type:
- apiref
api_name:
- ICatalogReadWriteLock.StartNonBlockingWriteOperation
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ICatalogReadWriteLock::StartNonBlockingWriteOperation method

method StartNonBlockingWriteOperation - creates a non-blocking write lock

## Syntax


```C++
HRESULT StartNonBlockingWriteOperation(
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

 

 





