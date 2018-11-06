---
Description: Allows the callback object to request enumeration on a background thread. Used by IShellFolderViewCB::MessageSFVCB.
title: SFVM_BACKGROUNDENUM message
ms.topic: article
ms.date: 05/31/2018
---

# SFVM\_BACKGROUNDENUM message

Allows the callback object to request enumeration on a background thread. Used by [**IShellFolderViewCB::MessageSFVCB**](https://msdn.microsoft.com/en-us/library/Bb774968(v=VS.85).aspx).


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



 

 




