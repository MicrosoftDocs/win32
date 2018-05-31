---
error-parsing-yaml: 
---

# IScopeAdm::ExcludeScope property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Indicates whether to index this scope.

This property is read/write.

## Syntax


```C++
HRESULT put_ExcludeScope(
  [in]          VARIANT_BOOL newVal
);

HRESULT get_ExcludeScope(
  [out, retval] VARIANT_BOOL *pVal
);
```



## Property value

If **VARIANT\_TRUE**, indexing is disabled for this scope. If **VARIANT\_FALSE**, indexing is enabled for this scope.

## Requirements



|                                     |                                                            |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |
| End of client support<br/>    | Windows 7<br/>                                       |
| End of server support<br/>    | Windows Server 2008 R2<br/>                          |



## See also

<dl> <dt>

[**IScopeAdm**](iscopeadm.md)
</dt> </dl>

 

 





