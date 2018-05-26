---
Description: Allows the callback object to specify an HTML Help file and a topic within it. Used by IShellFolderViewCBMessageSFVCB.
title: SFVM\_GETHELPTOPIC message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_GETHELPTOPIC message

Allows the callback object to specify an HTML Help file and a topic within it. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/Shlobj/?branch=master).


```C++
SFVM_GETHELPTOPIC 

    lParam = (LPARAM)(SFVM_HELPTOPIC_DATA*) phtd;

            
```



## Parameters

<dl> <dt>

*phtd* \[out\]
</dt> <dd>

The address of a [**SFVM\_HELPTOPIC\_DATA**](/windows/win32/shlobj_core/ns-shlobj_core-_sfvm_helptopic_data?branch=master) structure that specifies the HTML Help file and topic.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




