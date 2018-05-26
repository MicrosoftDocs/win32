---
title: IScopeAdm VirtualScope property
description: Indicates whether this scope is a virtual path.
ms.assetid: eaaaa459-7b1d-4f4c-a00d-8eadfb19dede
keywords:
- VirtualScope property Indexing Service
- VirtualScope property Indexing Service , IScopeAdm interface
- IScopeAdm interface Indexing Service , VirtualScope property
topic_type:
- apiref
api_name:
- IScopeAdm.VirtualScope
- IScopeAdm.get_VirtualScope
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IScopeAdm::VirtualScope property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Indicates whether this scope is a virtual path.

This property is read-only.

## Syntax


```C++
HRESULT get_VirtualScope(
  [out, retval] VARIANT_BOOL *pVal
);
```



## Property value

If **VARIANT\_TRUE**, the scope is virtual.

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

 

 





