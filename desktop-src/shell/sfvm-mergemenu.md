---
Description: 'Allows the callback object to merge menu items into the Windows Explorer menus. Used by IShellFolderViewCB::MessageSFVCB.'
title: 'SFVM\_MERGEMENU message'
---

# SFVM\_MERGEMENU message

Allows the callback object to merge menu items into the Windows Explorer menus. Used by [**IShellFolderViewCB::MessageSFVCB**](ishellfolderviewcb-messagesfvcb.md).


```C++
SFVM_MERGEMENU 

    lParam = (LPARAM)(LPQCMINFO) pInfo;

            
```



## Parameters

<dl> <dt>

*pInfo* \[out\]
</dt> <dd>

A [**QCMINFO**](qcminfo-str.md) structure containing the information needed to merge the items into the menu.

</dd> </dl>

## Remarks

This message serves essentially the same purpose as the [**IShellBrowser::InsertMenusSB**](ishellbrowser-insertmenussb.md) and [**IShellBrowser::SetMenuSB**](ishellbrowser-setmenusb.md) in a custom folder view. See the *Using IShellBrowser to Communicate with Windows Explorer* section of [Implementing a Folder View](lwef.nse_folderview) for further discussion.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




