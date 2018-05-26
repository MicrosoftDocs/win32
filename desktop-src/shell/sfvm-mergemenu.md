---
Description: Allows the callback object to merge menu items into the Windows Explorer menus. Used by IShellFolderViewCBMessageSFVCB.
title: SFVM\_MERGEMENU message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_MERGEMENU message

Allows the callback object to merge menu items into the Windows Explorer menus. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/Shlobj/?branch=master).


```C++
SFVM_MERGEMENU 

    lParam = (LPARAM)(LPQCMINFO) pInfo;

            
```



## Parameters

<dl> <dt>

*pInfo* \[out\]
</dt> <dd>

A [**QCMINFO**](/windows/win32/shlobj_core/ns-shlobj_core-_qcminfo?branch=master) structure containing the information needed to merge the items into the menu.

</dd> </dl>

## Remarks

This message serves essentially the same purpose as the [**IShellBrowser::InsertMenusSB**](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellbrowser-insertmenussb?branch=master) and [**IShellBrowser::SetMenuSB**](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellbrowser-setmenusb?branch=master) in a custom folder view. See the *Using IShellBrowser to Communicate with Windows Explorer* section of [Implementing a Folder View](lwef.nse_folderview) for further discussion.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




