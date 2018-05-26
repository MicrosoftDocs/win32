---
title: WM\_INPUT message
description: Sent to the window that is getting raw input. A window receives this message through its WindowProc function.
ms.assetid: a014d68c-841c-4120-b752-4b3fac60e12d
keywords:
- WM_INPUT message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_INPUT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_INPUT message

Sent to the window that is getting raw input.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


```C++
#define WM_INPUT                        0x00FF
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The input code. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                | Meaning                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RIM_INPUT"></span><span id="rim_input"></span><dl> <dt>**RIM\_INPUT**</dt> <dt>0</dt> </dl>             | Input occurred while the application was in the foreground. The application must call [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) so the system can perform cleanup.<br/>         |
| <span id="RIM_INPUTSINK"></span><span id="rim_inputsink"></span><dl> <dt>**RIM\_INPUTSINK**</dt> <dt>1</dt> </dl> | Input occurred while the application was not in the foreground. The application must call [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) so the system can perform the cleanup.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the [**RAWINPUT**](rawinput.md) structure that contains the raw input from the device.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

To get the *wParam* value, use the [**GET\_RAWINPUT\_CODE\_WPARAM**](get-rawinput-code-wparam.md) macro.

Note that *lParam* has the handle to the [**RAWINPUT**](rawinput.md) structure, not a pointer to it. To get the raw data, use the handle in the call to [**GetRawInputData**](getrawinputdata.md).

Raw input is available only when the application calls [**RegisterRawInputDevices**](registerrawinputdevices.md) with valid device specifications

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**GetRawInputData**](getrawinputdata.md)
</dt> <dt>

[**RegisterRawInputDevices**](registerrawinputdevices.md)
</dt> <dt>

[**RAWINPUT**](rawinput.md)
</dt> <dt>

[**GET\_RAWINPUT\_CODE\_WPARAM**](get-rawinput-code-wparam.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Raw Input](raw-input.md)
</dt> </dl>

 

 





