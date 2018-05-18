---
title: IixssoQuery Dialect property
description: Contains the dialect of the Indexing Service Query Language being used in the Query property for this query.
ms.assetid: '47fa8f6d-ad22-4b63-975f-82aae0033086'
keywords: ["Dialect property Indexing Service", "Dialect property Indexing Service , IixssoQuery interface", "IixssoQuery interface Indexing Service , Dialect property"]
topic_type:
- apiref
api_name:
- IixssoQuery.Dialect
- IixssoQuery.get_Dialect
- IixssoQuery.put_Dialect
api_location:
- Ixsso.dll
api_type:
- COM
---

# IixssoQuery::Dialect property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Contains the dialect of the Indexing Service Query Language being used in the Query property for this query.

This property is read/write.

## Syntax


```C++
HRESULT put_Dialect(
  [in]          BSTR val
);

HRESULT get_Dialect(
  [out, retval] BSTR *val
);
```



## Property value

Specifies the dialect. The literal value "1" indicates Indexing Service Query Language Dialect 1, and "2" refers to Indexing Service Query Language Dialect 2 (default value).

## Remarks

For Web clients, the query string variable in URLs associated with this property is di. Scripts written with the previous version of the Query object may behave differently due to the change in dialect.

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

 

 





