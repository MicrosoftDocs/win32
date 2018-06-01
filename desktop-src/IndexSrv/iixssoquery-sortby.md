---
Description: Indicates how to sort the results set of a query, by listing column names and sorting order.
ms.assetid: c48136f9-f8b5-44a8-8491-2d253a24d93a
title: IixssoQuery::SortBy property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoQuery::SortBy property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Indicates how to sort the results set of a query, by listing column names and sorting order.

This property is read/write.

## Syntax


```C++
HRESULT put_SortBy(
  [in]          BSTR val
);

HRESULT get_SortBy(
  [out, retval] BSTR *val
);
```



## Property value

One or more existing result set column names, separated by commas. Each column name can be followed by an optional sort order identifier: \[a\] for ascending and \[d\] for descending order. The column names must already exist in the ADO recordset object.

## Remarks

This property sorts results in ascending order ( \[a\] ) by default. The query string variables associated with this property are so (sort order) and sd (sort descending).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ixsso.dll</dt> </dl> |



## See also

<dl> <dt>

[**IixssoQuery**](iixssoquery.md)
</dt> </dl>

 

 




