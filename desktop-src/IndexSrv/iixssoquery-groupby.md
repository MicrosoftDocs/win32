---
Description: Groups search results by value within a column. For example, searches could group, in the result table, all documents written by one author.
ms.assetid: 2eb71ec5-66eb-4796-950d-6cc9562a6bc8
title: IixssoQuery::GroupBy property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoQuery::GroupBy property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Groups search results by value within a column. For example, searches could group, in the result table, all documents written by one author.

This property is read/write.

## Syntax


```C++
HRESULT put_GroupBy(
  [in]          BSTR val
);

HRESULT get_GroupBy(
  [out, retval] BSTR *val
);
```



## Property value

A grouping specification made up of a type (currently only \[unique\] is supported), a property name, and a sort order (\[a\] for ascending or \[d\] for descending). In unique grouping, unique values of the column set form the individual categories. The syntax for the unique grouping term is:

unique *fname* \[ {\[a\]\|\[d\]} \] \[ , *fname2* {\[a\]\|\[d\]} ... \]

where *fname*, or *fname2*, is the friendly name assigned by the [**DefineColumn**](iixssoquery-definecolumn.md) method.

Because the initial default value for a type is also unique, you can omit this term. Column names separated by a plus sign (+) are grouped in individual categories, and column names following a comma (,) are grouped together into subgroups of the previous grouping.

## Remarks

For Web clients, the query string variables in URLs associated with this property are gr (group) and gd (group in descending order).

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

 

 




