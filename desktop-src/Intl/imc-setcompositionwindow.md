---
description: Instructs an IME window to set the style of the composition window. To send this command, the application uses the WM\_IME\_CONTROL message with the parameter settings shown below.
ms.assetid: 19b99228-a1fc-4cd5-8f37-5462bf767f85
title: IMC_SETCOMPOSITIONWINDOW command (Imm.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMC\_SETCOMPOSITIONWINDOW command

Instructs an IME window to set the style of the composition window. To send this command, the application uses the [**WM\_IME\_CONTROL**](wm-ime-control.md) message with the parameter settings shown below.


```C++
LRESULT IMC_SETCOMPOSITIONWINDOW
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMC\_SETCOMPOSITIONWINDOW.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Pointer to a [**COMPOSITIONFORM**](/windows/win32/api/imm/ns-imm-compositionform) structure that contains the style information.

</dd> </dl>

## Return Value

Returns 0 if successful, or a nonzero value otherwise.

## Remarks

This command sets the style in the current input context, and the style is subsequently applied to each IME window that receives that input context.

By default, the IME window has the CFS\_POINT style. With this style, the IME window uses the current caret position and window client area when it opens any composition window.

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

[**COMPOSITIONFORM**](/windows/win32/api/imm/ns-imm-compositionform)
</dt> <dt>

[**WM\_IME\_CONTROL**](wm-ime-control.md)
</dt> </dl>

 

 




