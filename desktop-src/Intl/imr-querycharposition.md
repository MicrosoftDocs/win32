---
description: Notifies an application when the selected IME needs information about the coordinates of a character in the composition string. The application receives this command through the WM\_IME\_REQUEST message with parameter settings as shown below.
ms.assetid: cae7e5b3-8aaf-452d-80df-fb0ae04a342c
title: IMR_QUERYCHARPOSITION notification code (Imm.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMR\_QUERYCHARPOSITION notification code

Notifies an application when the selected IME needs information about the coordinates of a character in the composition string. The application receives this command through the [**WM\_IME\_REQUEST**](wm-ime-request.md) message with parameter settings as shown below.


```C++
LRESULT IMR_QUERYCHARPOSITION
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMR\_QUERYCHARPOSITION.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Pointer to an [**IMECHARPOSITION**](/windows/win32/api/imm/ns-imm-imecharposition) structure that contains the position of the character in the composition window.

</dd> </dl>

## Return Value

Returns a nonzero value if the application fills the [**IMECHARPOSITION**](/windows/win32/api/imm/ns-imm-imecharposition) structure. Otherwise, the command returns 0.

## Remarks

An application that draws the composition string itself, instead of relying on the IME, is responsible for filling in all the members of the [**IMECHARPOSITION**](/windows/win32/api/imm/ns-imm-imecharposition) structure. Otherwise, the application should pass the command to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) or [**ImmIsUIMessage**](/windows/desktop/api/Imm/nf-imm-immisuimessagea) if it has its own IME user interface window.

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

[**IMECHARPOSITION**](/windows/win32/api/imm/ns-imm-imecharposition)
</dt> <dt>

[**ImmIsUIMessage**](/windows/desktop/api/Imm/nf-imm-immisuimessagea)
</dt> <dt>

[**WM\_IME\_REQUEST**](wm-ime-request.md)
</dt> </dl>

 

 
