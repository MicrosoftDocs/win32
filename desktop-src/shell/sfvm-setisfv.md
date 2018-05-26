---
Description: Notifies the callback object of the container site. This is used only when IObjectWithSiteSetSite is not supported and SHCreateShellFolderViewEx is used. Used by IShellFolderViewCBMessageSFVCB.
ms.assetid: a4aa40f8-1d98-4686-86e2-87280e470aac
title: SFVM\_SETISFV message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_SETISFV message

\[This notification is supported through Windows XP Service Pack 2 (SP2) and Windows Server 2003. It might be unsupported in subsequent versions of Windows.\]

Notifies the callback object of the container site. This is used only when [**IObjectWithSite::SetSite**](_inet_IObjectWithSite_SetSite_Method) is not supported and [**SHCreateShellFolderViewEx**](/windows/win32/shlobj_core/nf-shlobj_core-shcreateshellfolderviewex?branch=master) is used. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/Shlobj/?branch=master).


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



 

 




