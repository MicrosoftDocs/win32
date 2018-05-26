---
Description: Notifies the callback object that the folder view window is being created. Used by IShellFolderViewCBMessageSFVCB.
title: SFVM\_WINDOWCREATED message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_WINDOWCREATED message

Notifies the callback object that the folder view window is being created. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/Shlobj/?branch=master).


```C++
SFVM_WINDOWCREATED 

    wParam = (WPARAM)(HWND) hwndView;

            
```



## Parameters

<dl> <dt>

*hwndView* \[in\]
</dt> <dd>

The folder view's window handle.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




