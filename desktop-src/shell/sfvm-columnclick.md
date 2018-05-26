---
Description: Notifies the callback object that the user has clicked a column header to sort the list of objects in the folder view. Used by IShellFolderViewCBMessageSFVCB.
title: SFVM\_COLUMNCLICK message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_COLUMNCLICK message

Notifies the callback object that the user has clicked a column header to sort the list of objects in the folder view. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/Shlobj/?branch=master).


```C++
SFVM_COLUMNCLICK 

    wParam = (WPARAM)(UINT)iColumn;

            
```



## Parameters

<dl> <dt>

*iColumn* \[in\]
</dt> <dd>

The index of the column that was clicked.

</dd> </dl>

## Remarks

In response to this notification, you should return S\_OK to rearrange the list yourself. To have the system folder view object rearrange the list, return S\_FALSE.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




