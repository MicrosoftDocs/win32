---
Description: Notifies the callback object that an event has taken place that affects one of its items. Used by IShellFolderViewCBMessageSFVCB.
title: SFVM\_FSNOTIFY message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_FSNOTIFY message

Notifies the callback object that an event has taken place that affects one of its items. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/Shlobj/?branch=master).


```C++
SFVM_FSNOTIFY 

    wParam = (WPARAM)(LPCITEMIDLIST) pidl;

    lParam = (LPARAM)(DWORD) lEvent;

            
```



## Parameters

<dl> <dt>

*pidl* \[in\]
</dt> <dd>

The PIDL of the affected item.

</dd> <dt>

*lEvent* \[in\]
</dt> <dd>

A SHCNE value that indicates which event occurred. For a list of possible values, see [**SHChangeNotify**](/windows/win32/shlobj_core/nf-shlobj_core-shchangenotify?branch=master).

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




