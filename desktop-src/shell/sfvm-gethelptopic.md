---
Description: Allows the callback object to specify an HTML Help file and a topic within it. Used by IShellFolderViewCB::MessageSFVCB.
title: SFVM_GETHELPTOPIC message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SFVM\_GETHELPTOPIC message

Allows the callback object to specify an HTML Help file and a topic within it. Used by [**IShellFolderViewCB::MessageSFVCB**](https://msdn.microsoft.com/en-us/library/Bb774968(v=VS.85).aspx).


```C++
SFVM_GETHELPTOPIC 

    lParam = (LPARAM)(SFVM_HELPTOPIC_DATA*) phtd;

            
```



## Parameters

<dl> <dt>

*phtd* \[out\]
</dt> <dd>

The address of a [**SFVM\_HELPTOPIC\_DATA**](/windows/desktop/api/shlobj_core/ns-shlobj_core-_sfvm_helptopic_data) structure that specifies the HTML Help file and topic.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




