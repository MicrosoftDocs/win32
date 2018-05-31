---
error-parsing-yaml: 
---

# IixssoQuery::QueryIncomplete property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Warns when the Indexing Service could not resolve the query because of a very complicated regular expression query, or some prefix query that matched too many terms in an index.

This property is read-only.

## Syntax


```C++
HRESULT get_QueryIncomplete(
  [out, retval] VARIANT_BOOL *val
);
```



## Property value

**VARIANT\_TRUE** if the query could not be resolved using the Content Index and if the [**AllowEnumeration**](iixssoquery-allowenumeration.md) property was **VARIANT\_FALSE**; **VARIANT\_FALSE** otherwise.

## Remarks

A query can be incomplete when it becomes too complex or expands to an unreasonable number of query restriction nodes. This can happen for a variety of reasons. You must call the [**CreateRecordset**](iixssoquery-createrecordset.md) method before using this property.

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
</dt> <dt>

[MaxRestrictionNodes](maxrestrictionnodes.md)
</dt> </dl>

 

 





