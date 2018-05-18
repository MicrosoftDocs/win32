---
Description: 'Notifies the callback object that an event has taken place that affects one of its items. Used by IShellFolderViewCB::MessageSFVCB.'
title: 'SFVM\_FSNOTIFY message'
---

# SFVM\_FSNOTIFY message

Notifies the callback object that an event has taken place that affects one of its items. Used by [**IShellFolderViewCB::MessageSFVCB**](ishellfolderviewcb-messagesfvcb.md).


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

A SHCNE value that indicates which event occurred. For a list of possible values, see [**SHChangeNotify**](shchangenotify.md).

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




