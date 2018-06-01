---
Description: Sets the properties on the query object of a Web client request.
ms.assetid: ae284340-7b1d-4be9-a9d9-d2d7ee3c2d87
title: IixssoQuery::SetQueryFromURL method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoQuery::SetQueryFromURL method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Sets the properties on the query object of a Web client request.

## Syntax


```C++
HRESULT SetQueryFromURL(
  [in] BSTR pwszQuery
);
```



## Parameters

<dl> <dt>

*pwszQuery* \[in\]
</dt> <dd>

The CGI QueryString that is URL-encoded. See [QUERY\_STRING Variables](query-string-variables.md).

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The state of the query object is not reset before loading the query string values. Unrecognized tag names in the query string are ignored.

Query string and form variables can also be parsed from a script without calling this method.

## Examples


```VB
' Take the URL query string that specifies files > 10,000, 
'     sort order by rank in descending alphabetical order, 
'     and the maximum hit count = 200 
' Set the corresponding query object properties
objQuery.SetQueryFromURL("qu=%40size+%3E+10000&amp;so=rank%5bd%5d&amp;mh=200") 
' results are:
' objQuery.Query = "@size > 10,000"
' objQuery.SortBy = "rank[d]"
' objQuery.MaxRecords = 200
```



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

 

 




