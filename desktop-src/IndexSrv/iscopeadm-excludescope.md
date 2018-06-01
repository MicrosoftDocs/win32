---
Description: Indicates whether to index this scope.
ms.assetid: d2bb7eb4-c9c7-4f33-aecc-0ee10b362e81
title: IScopeAdm::ExcludeScope property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IScopeAdm::ExcludeScope property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Indicates whether to index this scope.

This property is read/write.

## Syntax


```C++
HRESULT put_ExcludeScope(
  [in]          VARIANT_BOOL newVal
);

HRESULT get_ExcludeScope(
  [out, retval] VARIANT_BOOL *pVal
);
```



## Property value

If **VARIANT\_TRUE**, indexing is disabled for this scope. If **VARIANT\_FALSE**, indexing is enabled for this scope.

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

 

 




