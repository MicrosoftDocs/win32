---
description: Allows the callback object to request enumeration on a background thread. Used by IShellFolderViewCB::MessageSFVCB.
title: SFVM_BACKGROUNDENUM message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 8428179c-2ec9-4979-9281-c2439e58beb6
api_name: 
 - SFVM_BACKGROUNDENUM
api_type: 
 - HeaderDef
api_location: 
 - Shlobj.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SFVM\_BACKGROUNDENUM message

Allows the callback object to request enumeration on a background thread. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/api/shlobj_core/nf-shlobj_core-ishellfolderviewcb-messagesfvcb).


```C++

                SFVM_BACKGROUNDENUM

            
```



## Parameters

This message has no parameters.

## Remarks

In response to this notification, return S\_OK to enable background enumeration. By default, the system folder object will display the "flashlight" animation while the enumeration is taking place. To specify a custom animation, handle [**SFVM\_GETANIMATION**](sfvm-getanimation.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
