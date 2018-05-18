---
title: IScopeAdm Logon property
description: Retrieves the case-insensitive logon name.
ms.assetid: '0c59070a-59f2-42b3-b8d2-9036de52ca77'
keywords: ["Logon property Indexing Service", "Logon property Indexing Service , IScopeAdm interface", "IScopeAdm interface Indexing Service , Logon property"]
topic_type:
- apiref
api_name:
- IScopeAdm.Logon
- IScopeAdm.get_Logon
api_type:
- COM
---

# IScopeAdm::Logon property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Retrieves the case-insensitive logon name.

This property is read-only.

## Syntax


```C++
HRESULT get_Logon(
  [out, retval] BSTR *pVal
);
```



## Property value

Receives the case-insensitive logon name.

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

 

 





