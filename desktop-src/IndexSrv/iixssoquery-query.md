---
title: IixssoQuery Query property
description: Retrieves or sets the query string (also known as the restriction or query restriction).
ms.assetid: e4a2a88f-9f1c-4dce-8dd3-3015dceebe8e
keywords:
- Query property Indexing Service
- Query property Indexing Service , IixssoQuery interface
- IixssoQuery interface Indexing Service , Query property
topic_type:
- apiref
api_name:
- IixssoQuery.Query
- IixssoQuery.get_Query
- IixssoQuery.put_Query
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

# IixssoQuery::Query property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Retrieves or sets the query string (also known as the restriction or query restriction).

This property is read/write.

## Syntax


```C++
HRESULT put_Query(
  [in]          BSTR val
);

HRESULT get_Query(
  [out, retval] BSTR *val
);
```



## Property value

Specifies the query string.

## Remarks

The combination of words or phrases or properties to search for that determines the documents to be returned in a search For Web clients, the query string variable in URLs associated with this property is qu.

The [**Dialect**](iixssoquery-dialect.md) property defines the version of query language contained in the **Query** property. The [**LocaleID**](iixssoquery-localeid.md) determines the language components (English (US), Japanese, French, and any one of the other supported languages) to use to break the query string into words, to remove noise words, and to create the appropriate stemming variations of the words in the query string.

## Examples


```VB
' Search for the word "dog" near the word "cat" in .htm files
objQuery.Query = "#filename *.htm and dog near cat"
```



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

 

 





