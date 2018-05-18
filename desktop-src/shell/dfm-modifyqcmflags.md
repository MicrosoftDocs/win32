---
Description: 'Allows the callback to modify the CFM\_XXX values passed to IContextMenu::QueryContextMenu.'
title: 'DFM\_MODIFYQCMFLAGS message'
---

# DFM\_MODIFYQCMFLAGS message

Allows the callback to modify the CFM\_XXX values passed to [**IContextMenu::QueryContextMenu**](icontextmenu-querycontextmenu.md).


```C++
DFM_MODIFYQCMFLAGS

    lParam = (LPARAM)(UINT) *puNewFlags;

    wParam = (WPARAM)(UINT) uFlags;         

            
```



## Parameters

<dl> <dt>

*puNewFlags* \[in\]
</dt> <dd>

A pointer to the new flag values.

</dd> <dt>

*uFlags* \[in\]
</dt> <dd>

Flags that specify how the context menu can be changed. This parameter uses the CMF\_XXX values described in [**IContextMenu::QueryContextMenu**](icontextmenu-querycontextmenu.md).

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




