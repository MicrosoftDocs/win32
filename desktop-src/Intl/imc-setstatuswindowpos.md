---
description: Instructs an IME window to set the position of the status window. To send this command, the application uses the WM\_IME\_CONTROL message with parameter settings as shown below.
ms.assetid: d77de7ab-1fbc-42f4-829e-e9fb51668d21
title: IMC_SETSTATUSWINDOWPOS command (Imm.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMC\_SETSTATUSWINDOWPOS command

Instructs an IME window to set the position of the status window. To send this command, the application uses the [**WM\_IME\_CONTROL**](wm-ime-control.md) message with parameter settings as shown below.


```C++
LRESULT IMC_SETSTATUSWINDOWPOS
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMC\_SETSTATUSWINDOWPOS.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Pointer to a [**POINTS**](/previous-versions//dd162808(v=vs.85)) structure that contains the x coordinate and y coordinate of the position of the status window. The coordinates are in screen coordinates, relative to the upper left corner of the display.

</dd> </dl>

## Return Value

Returns 0 if successful, or a nonzero value otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>Imm.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Input Method Manager](input-method-manager.md)
</dt> <dt>

[Input Method Manager Commands](input-method-manager-commands.md)
</dt> <dt>

[**WM\_IME\_CONTROL**](wm-ime-control.md)
</dt> </dl>

 

 
