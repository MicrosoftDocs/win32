---
description: Notifies an application when an IME is about to close the status window. The application receives this command through the WM\_IME\_NOTIFY message with parameter settings as shown below.
ms.assetid: d59fdf76-50e7-4a59-b1bd-a12cdb0026f6
title: IMN_CLOSESTATUSWINDOW notification code (Imm.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMN\_CLOSESTATUSWINDOW notification code

Notifies an application when an IME is about to close the status window. The application receives this command through the [**WM\_IME\_NOTIFY**](wm-ime-notify.md) message with parameter settings as shown below.


```C++
IMN_CLOSESTATUSWINDOW
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMN\_CLOSESTATUSWINDOW.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Not used.

</dd> </dl>

## Return Value

This command has no return value.

## Remarks

An application should process this command if it displays the status window for the IME.

The IME window closes the status window when it processes this command.

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

[**WM\_IME\_NOTIFY**](wm-ime-notify.md)
</dt> </dl>

 

 




