---
title: ICatalogReadWriteLock IsCurrentlyWriteLocked property
description: Returns true if a catalog is currently write locked, else false
ms.assetid: '91a57649-3296-4017-84f9-1398690f566e'
keywords: ["IsCurrentlyWriteLocked property HelpAPI", "IsCurrentlyWriteLocked property HelpAPI , ICatalogReadWriteLock interface", "ICatalogReadWriteLock interface HelpAPI , IsCurrentlyWriteLocked property"]
topic_type:
- apiref
api_name:
- ICatalogReadWriteLock.IsCurrentlyWriteLocked
- ICatalogReadWriteLock.get_IsCurrentlyWriteLocked
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ICatalogReadWriteLock::IsCurrentlyWriteLocked property

Returns true if a catalog is currently write locked, else false

This property is read-only.

## Syntax


```C++
HRESULT get_IsCurrentlyWriteLocked(
  [out, retval] VARIANT_BOOL *pRetVal
);
```



## Property value

True if a catalog is currently write locked, otherwise false.

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

 

 





