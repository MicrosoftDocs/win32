---
title: IScopeAdm Alias property
description: Retrieves or sets the case-insensitive name of the alias or friendly name for this scope.
ms.assetid: 'ecd53410-a7ce-4c99-b572-bffb180c2514'
keywords: ["Alias property Indexing Service", "Alias property Indexing Service , IScopeAdm interface", "IScopeAdm interface Indexing Service , Alias property"]
topic_type:
- apiref
api_name:
- IScopeAdm.Alias
- IScopeAdm.get_Alias
- IScopeAdm.put_Alias
api_type:
- COM
---

# IScopeAdm::Alias property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Retrieves or sets the case-insensitive name of the alias or friendly name for this scope.

This property is read/write.

## Syntax


```C++
HRESULT put_Alias(
  [in]          BSTR newVal
);

HRESULT get_Alias(
  [out, retval] BSTR *pVal
);
```



## Property value

Specifies the name.

## Requirements



|                                     |                                                            |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |
| End of client support<br/>    | Windows 7<br/>                                       |
| End of server support<br/>    | Windows Server 2008 R2<br/>                          |



## See also

<dl> <dt>

[**IScopeAdm**](iscopeadm.md)
</dt> </dl>

 

 





