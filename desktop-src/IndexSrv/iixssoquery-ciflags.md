---
error-parsing-yaml: 
---

# IixssoQuery::CiFlags property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Represents the Indexing Service flags that control whether the queries are resolved by searching recursively through the scope hierarchy or through only the scope directory itself. This property is for internal use only and is used in conjunction with [**CiScope**](iixssoquery-ciscope.md).

This is a deprecated property. Use [**AddScopeToQuery**](iixssoquery-addscopetoquery.md) instead.

This property is write-only.

## Syntax


```C++
HRESULT put_CiFlags(
  [in] BSTR val
);
```



## Property value

"DEEP" indicates to Indexing Service that it needs to use the directory given in [**CiScope**](iixssoquery-ciscope.md) and recursively search through all directories within it. "SHALLOW" means search only the directory specified in **CiScope**.

## Remarks

The **CiFlags** and [**CiScope**](iixssoquery-ciscope.md) properties are used primarily for debugging and are always used together. Use the [**AddScopeToQuery**](iixssoquery-addscopetoquery.md) method to add this restriction to the query object.

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

 

 





