---
title: ICatalogReadWriteLock IsCurrentlyNonBlockingWriteLocked property
description: Returns true if a catalog is currently non-blocking write locked, else false
ms.assetid: '34fd1773-be85-4cb8-b8d6-efcd99103954'
keywords: ["IsCurrentlyNonBlockingWriteLocked property HelpAPI", "IsCurrentlyNonBlockingWriteLocked property HelpAPI , ICatalogReadWriteLock interface", "ICatalogReadWriteLock interface HelpAPI , IsCurrentlyNonBlockingWriteLocked property"]
topic_type:
- apiref
api_name:
- ICatalogReadWriteLock.IsCurrentlyNonBlockingWriteLocked
- ICatalogReadWriteLock.get_IsCurrentlyNonBlockingWriteLocked
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ICatalogReadWriteLock::IsCurrentlyNonBlockingWriteLocked property

Returns true if a catalog is currently non-blocking write locked, else false

This property is read-only.

## Syntax


```C++
HRESULT get_IsCurrentlyNonBlockingWriteLocked(
  [out, retval] VARIANT_BOOL *pRetVal
);
```



## Property value

True if a catalog is currently non-blocking write locked, otherwise false.

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

 

 





