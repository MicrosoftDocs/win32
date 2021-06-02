---
description: Notifies the callback object that the status bar is being updated. Used by IShellFolderViewCB::MessageSFVCB.
title: SFVM_UPDATESTATUSBAR message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: f1bac364-1011-4308-8b9b-8ed1800dd30d
api_name: 
 - SFVM_UPDATESTATUSBAR
api_type: 
 - HeaderDef
api_location: 
 - Shlobj.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SFVM\_UPDATESTATUSBAR message

Notifies the callback object that the status bar is being updated. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/api/shlobj_core/nf-shlobj_core-ishellfolderviewcb-messagesfvcb).


```C++
SFVM_UPDATESTATUSBAR 

    wParam = (WPARAM)(BOOL) fInitialize;

            
```



## Parameters

<dl> <dt>

*fInitialize* \[in\]
</dt> <dd>

A **BOOL** value that is set to **TRUE** if the status bar is being initialized.

</dd> </dl>

## Remarks

When you receive this notification:

-   Return S\_OK if you will handle the update.
-   Return MAKE\_HRESULT(SEVERITY\_SUCCESS,0,1) to have the system folder view object set the status bar text.
-   Return E\_FAIL to have the system folder view object handle the status bar.

The default status bar text is as follows.



| Status                      | Status bar text                         |
|-----------------------------|-----------------------------------------|
| No items selected           | "\#\# objects" (in the folder)          |
| One item selected           | The infotip for the item, if available. |
| More than one item selected | "\#\# objects selected"                 |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
