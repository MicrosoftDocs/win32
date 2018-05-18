---
Description: 'Notifies the callback object that the folder view window is being created. Used by IShellFolderViewCB::MessageSFVCB.'
title: 'SFVM\_WINDOWCREATED message'
---

# SFVM\_WINDOWCREATED message

Notifies the callback object that the folder view window is being created. Used by [**IShellFolderViewCB::MessageSFVCB**](ishellfolderviewcb-messagesfvcb.md).


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



 

 




