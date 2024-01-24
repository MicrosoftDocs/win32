---
description: Notfies an application when a selected IME needs information about the candidate window. The application receives this command through the WM\_IME\_REQUEST message with parameter settings as shown below.
ms.assetid: 35849290-a5be-406f-82f5-4a7e2af48586
title: IMR_CANDIDATEWINDOW notification code (Imm.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMR\_CANDIDATEWINDOW notification code

Notfies an application when a selected IME needs information about the candidate window. The application receives this command through the [**WM\_IME\_REQUEST**](wm-ime-request.md) message with parameter settings as shown below.


```C++
LRESULT IMR_CANDIDATEWINDOW
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMR\_CANDIDATEWINDOW.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Pointer to a buffer containing a [**CANDIDATEFORM**](/windows/win32/api/imm/ns-imm-candidateform) structure. Its **dwIndex** member contains the index to the candidate window referenced.

</dd> </dl>

## Return Value

Returns a nonzero value if the application fills in the [**CANDIDATEFORM**](/windows/win32/api/imm/ns-imm-candidateform) structure. Otherwise, the command returns 0.

## Remarks

This command can be sent by the IME to a window that has cleared the ISC\_SHOWUICANDIDATEWINDOW flag in the [**WM\_IME\_SETCONTEXT**](wm-ime-setcontext.md) message handler.

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

[**CANDIDATEFORM**](/windows/win32/api/imm/ns-imm-candidateform)
</dt> <dt>

[**WM\_IME\_REQUEST**](wm-ime-request.md)
</dt> <dt>

[**WM\_IME\_SETCONTEXT**](wm-ime-setcontext.md)
</dt> </dl>

 

 




