---
Description: Contains the catalog name for a local computer; for example, Web or System.
ms.assetid: 7381e569-57cb-4d5d-a571-636d400d35cf
title: IixssoQuery::Catalog property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoQuery::Catalog property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Contains the catalog name for a local computer; for example, Web or System.

This property is read/write.

## Syntax


```C++
HRESULT put_Catalog(
  [in]          BSTR val
);

HRESULT get_Catalog(
  [out, retval] BSTR *val
);
```



## Property value

Specifies the catalog name. The catalog name can be the name of a directory on the local computer. You can specify more than one catalog name by separating each name with a comma.

The catalog name uses URL-like syntax in the following format: query://*hostname*/*indexname*. The *hostname* is the name of the computer where the catalog can be found. The *hostname* gives the catalog name on that computer. The *hostname* defaults to the local computer. The *hostname* defaults to the default catalog on the computer.

## Remarks

If no name is supplied, Indexing Service uses the default catalog on the computer. If Internet Information Services (IIS) is installed, the default catalog name is Web. The catalog name for Windows is System. For Web clients, the query string variable in URLs associated with this property is ct.

## Examples


```VB
objQuery.Catalog = "query://search.microsoft.com/kb"
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

 

 




