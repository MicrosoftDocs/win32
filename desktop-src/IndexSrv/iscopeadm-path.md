---
Description: Retrieves or sets the case-insensitive scope path to the directory for Indexing Service to index.
ms.assetid: 8b328539-5bea-47e3-b1d2-72b96ee1ab71
title: IScopeAdm::Path property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IScopeAdm::Path property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Retrieves or sets the case-insensitive scope path to the directory for Indexing Service to index.

This property is read/write.

## Syntax


```C++
HRESULT put_Path(
  [in]          BSTR newVal
);

HRESULT get_Path(
  [out, retval] BSTR *pVal
);
```



## Property value

Specifies the scope path. For example, "c:\\".

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

 

 




