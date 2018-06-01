---
Description: Defines the maximum number of records (rows) to use in the query result set, which is an ADO Rowset object.
ms.assetid: 9e09e861-d970-4956-bc91-35a95e9b7f63
title: IixssoQuery::MaxRecords property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoQuery::MaxRecords property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Defines the maximum number of records (rows) to use in the query result set, which is an ADO Rowset object.

This property is read/write.

## Syntax


```C++
HRESULT put_MaxRecords(
  [in]          LONG val
);

HRESULT get_MaxRecords(
  [out, retval] LONG *val
);
```



## Property value

Specifies the maximum number of hits to allow for in the query result set.

## Remarks

This property limits the number of records in the Rowset object the Indexing Service OLE DB provider retrieves from its data source object, which is the group of indexes defined by the current catalog. The default setting of zero requests all records. **MaxRecords** is read/write when the recordset is closed and read-only when it is open.

For Web clients, the query string variables in URLs associated with this property is mh (MaxHits).

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

 

 




