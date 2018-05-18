---
title: IixssoQuery Catalog property
description: Contains the catalog name for a local computer; for example, Web or System.
ms.assetid: '7381e569-57cb-4d5d-a571-636d400d35cf'
keywords: ["Catalog property Indexing Service", "Catalog property Indexing Service , IixssoQuery interface", "IixssoQuery interface Indexing Service , Catalog property"]
topic_type:
- apiref
api_name:
- IixssoQuery.Catalog
- IixssoQuery.get_Catalog
- IixssoQuery.put_Catalog
api_location:
- Ixsso.dll
api_type:
- COM
---

# IixssoQuery::Catalog property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

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

 

 





