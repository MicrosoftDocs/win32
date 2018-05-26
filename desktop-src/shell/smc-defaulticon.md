---
Description: Return the default icon for the item specified by the accompanying SMDATA structure.
title: SMC\_DEFAULTICON message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SMC\_DEFAULTICON message

Return the default icon for the item specified by the accompanying [**SMDATA**](/windows/win32/Shobjidl_core/ns-shobjidl_core-tagsmdata?branch=master) structure.


```C++
SMC_DEFAULTICON 
    wParam = (WPARAM) (LPWSTR) pwszIcon;
    lParam = (LPARAM) (int) iIcon
            
```



## Parameters

<dl> <dt>

*pwszIcon* 
</dt> <dd>

A pointer to a string that receives the fully qualified path of the file that contains the default icon.

</dd> <dt>

*iIcon* 
</dt> <dd>

A pointer to an integer that receives the index of the icon in the file specified by *pwszIcon*.

</dd> </dl>

## Return value

Return S\_OK.

## Remarks

This notification is received by the [**IShellMenuCallback::CallbackSM**](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellmenucallback-callbacksm?branch=master) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 




