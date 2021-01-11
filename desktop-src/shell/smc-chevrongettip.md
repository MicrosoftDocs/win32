---
description: Requests the title and text for a chevron infotip for the item specified by the accompanying SMDATA structure.
ms.assetid: 7bce4079-994c-4eb0-ab86-9044701d85a1
title: SMC_CHEVRONGETTIP message (Shobjidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SMC\_CHEVRONGETTIP message

Requests the title and text for a chevron infotip for the item specified by the accompanying [**SMDATA**](/windows/win32/api/shobjidl_core/ns-shobjidl_core-smdata) structure.


```C++
SMC_CHEVRONGETTIP 
    wParam = (WPARAM) (LPWSTR) pwszTipTitle;
    lParam = (LPARAM) (LPWSTR) pwszTipText
            
```



## Parameters

<dl> <dt>

*pwszTipTitle* 
</dt> <dd>

A pointer to a buffer that receives a **NULL**-terminated Unicode string that contains the infotip's title. This string must be no longer than MAX\_PATH characters long, including the terminating **NULL** character.

</dd> <dt>

*pwszTipText* 
</dt> <dd>

A pointer to a buffer that receives a **NULL**-terminated Unicode string that contains the infotip's text. This string must be no longer than MAX\_PATH characters long, including the terminating **NULL** character.

</dd> </dl>

## Return value

Return S\_OK.

## Remarks

This notification is received by the [**IShellMenuCallback::CallbackSM**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellmenucallback-callbacksm) method.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 




