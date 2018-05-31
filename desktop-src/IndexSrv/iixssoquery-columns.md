---
error-parsing-yaml: 
---

# IixssoQuery::Columns property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Contains the list of case-insensitive column names used in formatting the query result set.

This property is read/write.

## Syntax


```C++
HRESULT put_Columns(
  [in]          BSTR val
);

HRESULT get_Columns(
  [out, retval] BSTR *val
);
```



## Property value

Specifies a list of column names, separated by commas.

## Remarks

This property gives a list of column names, each separated by commas. The column names can be enclosed in quotation marks if they contain characters other than alphabetic and numeric characters.

## Examples


```VB
objQuery.Columns = "DocAuthor, vpath, doctitle"
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

 

 





