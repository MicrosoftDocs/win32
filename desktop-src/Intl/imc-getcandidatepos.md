---
description: Instructs an IME window to get the position of the candidate window. To send this command, the application uses the WM\_IME\_CONTROL message with the parameter settings shown below.
ms.assetid: e582dbc2-8081-424c-a972-1a182a477293
title: IMC_GETCANDIDATEPOS command (Imm.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMC\_GETCANDIDATEPOS command

Instructs an IME window to get the position of the candidate window. To send this command, the application uses the [**WM\_IME\_CONTROL**](wm-ime-control.md) message with the parameter settings shown below.


```C++
LRESULT IMC_GETCANDIDATEPOS
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMC\_GETCANDIDATEPOS.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Pointer to a [**CANDIDATEFORM**](/windows/win32/api/imm/ns-imm-candidateform) structure that contains the position of the candidate window.

</dd> </dl>

## Return Value

Returns 0 if successful, or a nonzero value otherwise.

## Remarks

Because the IME might adjust the position of a candidate window, an application uses this command to get the actual position to decide whether to reposition the window. The retrieved position is in window coordinates relative to the window having the current input focus.

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
</dt> </dl>

 

 




