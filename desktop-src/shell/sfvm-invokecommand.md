---
description: Notifies the callback object that one of its toolbar or menu commands has been invoked by the user. Used by IShellFolderViewCB::MessageSFVCB.
ms.assetid: 6b9e4a4d-ec45-489c-bbff-d123d5756b75
title: SFVM_INVOKECOMMAND message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SFVM\_INVOKECOMMAND message

Notifies the callback object that one of its toolbar or menu commands has been invoked by the user. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/api/shlobj_core/nf-shlobj_core-ishellfolderviewcb-messagesfvcb).


```C++
SFVM_INVOKECOMMAND 

    wParam = (WPARAM)(UINT) idCmd;

            
```



## Parameters

<dl> <dt>

*idCmd* \[in\]
</dt> <dd>

The command ID of the selected toolbar or menu item.

</dd> </dl>

## Remarks

This message serves essentially the same function as a [**WM\_COMMAND**](../menurc/wm-command.md) message in a conventional window procedure. It allows the callback object to handle any items that it has added to the Windows Explorer tool or menu bar.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
