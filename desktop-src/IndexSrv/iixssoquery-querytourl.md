---
Description: Reads the properties of the query object and creates and creates the QueryString portion of a uniform resource locator (URL) string from their values.
ms.assetid: a0efc933-473d-4477-8ff9-3afaf092b8f4
title: IixssoQuery::QueryToURL method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoQuery::QueryToURL method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Reads the properties of the query object and creates and creates the QueryString portion of a uniform resource locator (URL) string from their values.

## Syntax


```C++
HRESULT QueryToURL(
  [out, retval] BSTR *ppwszQuery
);
```



## Parameters

<dl> <dt>

*ppwszQuery* \[out, retval\]
</dt> <dd>

The Common Gateway Interface (CGI) QueryString, which uses certain combinations of character escape sequences for unprintable characters to be used in a URL (for example, "Now" would be %22Now%22).

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Properties read from the query object include [**Catalog**](iixssoquery-catalog.md), [**SortBy**](iixssoquery-sortby.md), [**GroupBy**](iixssoquery-groupby.md), [**Query**](iixssoquery-query.md), [**MaxRecords**](iixssoquery-maxrecords.md), and [**AllowEnumeration**](iixssoquery-allowenumeration.md).

## Examples


```VB
' Take the current property settings on the query object for
'   Q.Query = "Change Notification"
'   Q.SortBy = "rank[d]"
'   Q.Dialect = "1"
'   create an URL version
Dim strURL As String
strURL = Q.QueryToURL( )
Debug.Print "URL Version = " + strURL
' Output is:
'   URL Version = di=1&amp;so=Rank%5Bd%%5D&amp;qu=Change+Notification
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

 

 




