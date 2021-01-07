---
description: SFVM\_QUERYFSNOTIFY may be altered or unavailable.
ms.assetid: 5d777115-bae3-47c4-9edc-c99c40a4f926
title: SFVM_QUERYFSNOTIFY message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SFVM\_QUERYFSNOTIFY message

\[**SFVM\_QUERYFSNOTIFY** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Allows the callback object to register a folder so that changes to that folder's view will generate notifications. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/api/shlobj_core/nf-shlobj_core-ishellfolderviewcb-messagesfvcb).


```C++
SFVM_QUERYFSNOTIFY 
    lParam = (LPARAM)(SHChangeNotifyEntry*) shcne;
            
```



## Parameters

<dl> <dt>

*shcne* \[in, out\]
</dt> <dd>

A structure to hold the PIDL of the item to watch for events and an indication whether subfolders of that item should also be watched.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| End of client support<br/>    | Windows XP with SP2<br/>                                                      |
| End of server support<br/>    | Windows Server 2003<br/>                                                      |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
