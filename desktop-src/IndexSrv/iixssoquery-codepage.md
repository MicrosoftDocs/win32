---
Description: Contains the code page to be used for this query.
ms.assetid: d113297e-f77a-4418-9656-52d266421fe2
title: IixssoQuery::CodePage property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoQuery::CodePage property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Contains the code page to be used for this query.

This property is read/write.

## Syntax


```C++
HRESULT put_CodePage(
  [in]          LONG val
);

HRESULT get_CodePage(
  [out, retval] LONG *val
);
```



## Property value

Sets the code page identifier.

## Remarks

A code page is a set of typographical characters used to represent text, which can differ by language or locale. Code pages are designated by numbers such as ANSI code page 1252 for American English and OEM code page 932 for Japanese Kanji. Code pages are used to parse the query string and other strings such as column names, and to convert back and forth between URL sequences and query strings in the [**SetQueryFromURL**](iixssoquery-setqueryfromurl.md) and [**QueryToURL**](iixssoquery-querytourl.md) methods.

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

 

 




