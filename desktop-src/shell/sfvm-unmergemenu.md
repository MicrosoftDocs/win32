---
Description: 'Notifies the callback object that a menu is being removed. Used by IShellFolderViewCB::MessageSFVCB.'
title: 'SFVM\_UNMERGEMENU message'
---

# SFVM\_UNMERGEMENU message

Notifies the callback object that a menu is being removed. Used by [**IShellFolderViewCB::MessageSFVCB**](ishellfolderviewcb-messagesfvcb.md).


```C++
SFVM_UNMERGEMENU 

    lParam = (LPARAM)(HMENU) hmenuCurrent;

            
```



## Parameters

<dl> <dt>

*hmenuCurrent* \[in\]
</dt> <dd>

The handle of the menu that is being removed.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




