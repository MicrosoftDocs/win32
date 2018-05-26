---
Description: Sets the position of an item in the Shell view. Used by SHShellFolderView\_Message.
title: SFVM\_SETITEMPOS message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_SETITEMPOS message

Sets the position of an item in the Shell view. Used by [**SHShellFolderView\_Message**](/windows/win32/shlobj_core/nf-shlobj_core-shshellfolderview_message?branch=master).


```C++

                SFVM_SETITEMPOS 

    lParam = (LPSFV_SETITEMPOS)&amp;sip;

            
```



## Parameters

<dl> <dt>

*sip* \[in\]
</dt> <dd>

A pointer to an [**SFV\_SETITEMPOS**](/windows/win32/Shlobj/ns-shlobj-_sfv_setitempos?branch=master) structure.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




