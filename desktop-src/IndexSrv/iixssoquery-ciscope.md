---
title: IixssoQuery CiScope property
description: Specifies where to search to resolve the query defined in Query. Scope contains the starting directory or list of directories as physical or virtual path names.
ms.assetid: d50e9f19-b56c-45db-add3-9b10778555a4
keywords:
- CiScope property Indexing Service
- CiScope property Indexing Service , IixssoQuery interface
- IixssoQuery interface Indexing Service , CiScope property
topic_type:
- apiref
api_name:
- IixssoQuery.CiScope
- IixssoQuery.put_CiScope
api_location:
- Ixsso.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IixssoQuery::CiScope property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Specifies where to search to resolve the query defined in Query. Scope contains the starting directory or list of directories as physical or virtual path names.

This is a deprecated property. Use [**AddScopeToQuery**](iixssoquery-addscopetoquery.md) instead.

This property is write-only.

## Syntax


```C++
HRESULT put_CiScope(
  [in] BSTR val
);
```



## Property value

A list of scopes separated by commas (,). The scope / (forward slash) matches every page in all virtual directories and the scope \\ (backslash) matches every page on every physical directory. To use **CiScope** in a URL with a query expression, see [HTML Extension Files](html-extension-files.md).

## Remarks

Use [**CiFlags**](iixssoquery-ciflags.md) to indicate the type of searching to perform, whether deep or shallow. Use the [**AddScopeToQuery**](iixssoquery-addscopetoquery.md) method to add this restriction and **CiScope** on the query object.

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

 

 





