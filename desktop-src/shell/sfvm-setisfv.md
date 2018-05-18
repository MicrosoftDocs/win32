---
Description: 'Notifies the callback object of the container site. This is used only when IObjectWithSite::SetSite is not supported and SHCreateShellFolderViewEx is used. Used by IShellFolderViewCB::MessageSFVCB.'
ms.assetid: 'a4aa40f8-1d98-4686-86e2-87280e470aac'
title: 'SFVM\_SETISFV message'
---

# SFVM\_SETISFV message

\[This notification is supported through Windows XP Service Pack 2 (SP2) and Windows Server 2003. It might be unsupported in subsequent versions of Windows.\]

Notifies the callback object of the container site. This is used only when [**IObjectWithSite::SetSite**](_inet_IObjectWithSite_SetSite_Method) is not supported and [**SHCreateShellFolderViewEx**](shcreateshellfolderviewex.md) is used. Used by [**IShellFolderViewCB::MessageSFVCB**](ishellfolderviewcb-messagesfvcb.md).


```C++
SFVM_SETISFV
    lParam = (LPARAM)(IUnknown*) site;
            
```



## Parameters

<dl> <dt>

*site* \[in\]
</dt> <dd>

A pointer to the container site's [**IUnknown**](com.iunknown) interface.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




