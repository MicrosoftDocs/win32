---
description: Notifies an application when a selected IME needs information about the composition window. The application receives this command through the WM\_IME\_REQUEST message with parameters set as shown below.
ms.assetid: 08fd7119-d225-4a78-b2cd-8b58887c9139
title: IMR_COMPOSITIONWINDOW notification code (Imm.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMR\_COMPOSITIONWINDOW notification code

Notifies an application when a selected IME needs information about the composition window. The application receives this command through the [**WM\_IME\_REQUEST**](wm-ime-request.md) message with parameters set as shown below.


```C++
LRESULT IMR_COMPOSITIONWINDOW
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMR\_COMPOSITIONWINDOW.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Pointer to a buffer containing a [**COMPOSITIONFORM**](/windows/win32/api/imm/ns-imm-compositionform) structure.

</dd> </dl>

## Return Value

Returns a nonzero value if the application fills in the [**COMPOSITIONFORM**](/windows/win32/api/imm/ns-imm-compositionform) structure. Otherwise, the command returns 0.

## Remarks

This command can be sent by the IME to a window that has cleared the ISC\_SHOWUICOMPOSITIONWINDOW flag in the [**WM\_IME\_SETCONTEXT**](wm-ime-setcontext.md) message handler.

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

[**WM\_IME\_REQUEST**](wm-ime-request.md)
</dt> <dt>

[**WM\_IME\_SETCONTEXT**](wm-ime-setcontext.md)
</dt> </dl>

 

 




