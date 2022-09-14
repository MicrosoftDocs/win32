---
description: Notifies an application when the style or position of the composition window is updated. The application receives this command through the WM\_IME\_NOTIFY message with parameter settings as shown below.
ms.assetid: 07a9f0f6-587e-47c6-8f18-b48bdab0a541
title: IMN_SETCOMPOSITIONWINDOW notification code (Imm.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMN\_SETCOMPOSITIONWINDOW notification code

Notifies an application when the style or position of the composition window is updated. The application receives this command through the [**WM\_IME\_NOTIFY**](wm-ime-notify.md) message with parameter settings as shown below.


```C++
IMN_SETCOMPOSITIONWINDOW
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMN\_SETCOMPOSITIONWINDOW.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Not used.

</dd> </dl>

## Return Value

This command has no return value.

## Remarks

The application can get information about the composition form by using the [**IMC\_GETCOMPOSITIONWINDOW**](imc-getcompositionwindow.md) command.

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

[**IMC\_GETCOMPOSITIONWINDOW**](imc-getcompositionwindow.md)
</dt> <dt>

[**WM\_IME\_NOTIFY**](wm-ime-notify.md)
</dt> </dl>

 

 




