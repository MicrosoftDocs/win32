---
title: IixssoQuery AllowEnumeration property
description: Determines whether the query engine can use enumeration queries to resolve the result set. This property is used when resolving a query for properties that involve recursively searching directories for property information.
ms.assetid: b591bb31-994c-4a83-b1c0-abaa6aaf8d82
keywords:
- AllowEnumeration property Indexing Service
- AllowEnumeration property Indexing Service , IixssoQuery interface
- IixssoQuery interface Indexing Service , AllowEnumeration property
topic_type:
- apiref
api_name:
- IixssoQuery.AllowEnumeration
- IixssoQuery.get_AllowEnumeration
- IixssoQuery.put_AllowEnumeration
api_location:
- Ixsso.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoQuery::AllowEnumeration property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Determines whether the query engine can use enumeration queries to resolve the result set. This property is used when resolving a query for properties that involve recursively searching directories for property information.

This property is read/write.

## Syntax


```C++
HRESULT put_AllowEnumeration(
  [in]          VARIANT_BOOL val
);

HRESULT get_AllowEnumeration(
  [out, retval] VARIANT_BOOL *val
);
```



## Property value

When set to **VARIANT\_TRUE**, allows queries to use enumeration to resolve the result set. Otherwise, queries are forced to use indexes only for resolution. The default value is **VARIANT\_FALSE**.

## Remarks

This property expresses the inverse of the .idq parameter CiForceUseCI. For Web clients, the query string variable in URLs associated with this property is ae.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ixsso.dll</dt> </dl> |



## See also

<dl> <dt>

[**IixssoQuery**](iixssoquery.md)
</dt> </dl>

 

 





