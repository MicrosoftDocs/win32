---
description: Instructs the IME window to hide the status window. To send this command, the application uses the WM\_IME\_CONTROL message with the parameter settings shown below.
ms.assetid: e3da5962-a652-409e-b0ec-eb93671049b4
title: IMC_CLOSESTATUSWINDOW command (Imm.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMC\_CLOSESTATUSWINDOW command

Instructs the IME window to hide the status window. To send this command, the application uses the [**WM\_IME\_CONTROL**](wm-ime-control.md) message with the parameter settings shown below.


```C++
LRESULT IMC_CLOSESTATUSWINDOW
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMC\_CLOSESTATUSWINDOW.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Not used.

</dd> </dl>

## Return Value

Returns 0 if successful, or a nonzero value otherwise.

## Remarks

When the IME status window is already hidden, this command does nothing. Although an application can send this command to the IME window, the application does not receive the corresponding [IMN\_CLOSESTATUSWINDOW](imn-closestatuswindow.md) command.

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
</dt> </dl>

 

 




