---
Description: Allows the callback object to request enumeration on a background thread. Used by IShellFolderViewCBMessageSFVCB.
title: SFVM\_BACKGROUNDENUM message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_BACKGROUNDENUM message

Allows the callback object to request enumeration on a background thread. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/Shlobj/?branch=master).


```C++

                SFVM_BACKGROUNDENUM

            
```



## Parameters

This message has no parameters.

## Remarks

In response to this notification, return S\_OK to enable background enumeration. By default, the system folder object will display the "flashlight" animation while the enumeration is taking place. To specify a custom animation, handle [**SFVM\_GETANIMATION**](sfvm-getanimation.md).

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




