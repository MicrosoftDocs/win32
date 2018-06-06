---
Description: Allows the callback object to merge menu items into the Windows Explorer menus. Used by IShellFolderViewCB::MessageSFVCB.
title: SFVM\_MERGEMENU message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SFVM\_MERGEMENU message

Allows the callback object to merge menu items into the Windows Explorer menus. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/desktop/api/Shlobj/).


```C++
SFVM_MERGEMENU 

    lParam = (LPARAM)(LPQCMINFO) pInfo;

            
```



## Parameters

<dl> <dt>

*pInfo* \[out\]
</dt> <dd>

A [**QCMINFO**](/windows/desktop/api/shlobj_core/ns-shlobj_core-_qcminfo) structure containing the information needed to merge the items into the menu.

</dd> </dl>

## Remarks

This message serves essentially the same purpose as the [**IShellBrowser::InsertMenusSB**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-insertmenussb) and [**IShellBrowser::SetMenuSB**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-setmenusb) in a custom folder view. See the *Using IShellBrowser to Communicate with Windows Explorer* section of [Implementing a Folder View](https://msdn.microsoft.com/8c6712d8-c3cb-4450-8277-3a8675622651) for further discussion.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




