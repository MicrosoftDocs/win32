---
Description: Notifies an application when the selected IME needs information about the coordinates of a character in the composition string. The application receives this command through the WM\_IME\_REQUEST message with parameter settings as shown below.
ms.assetid: cae7e5b3-8aaf-452d-80df-fb0ae04a342c
title: IMR_QUERYCHARPOSITION notification code
ms.author: windowssdkdev
ms.topic: article
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

Pointer to an [**IMECHARPOSITION**](/windows/desktop/api/Imm/ns-imm-tagimecharposition) structure that contains the position of the character in the composition window.

</dd> </dl>

## Return Value

Returns a nonzero value if the application fills the [**IMECHARPOSITION**](/windows/desktop/api/Imm/ns-imm-tagimecharposition) structure. Otherwise, the command returns 0.

## Remarks

An application that draws the composition string itself, instead of relying on the IME, is responsible for filling in all the members of the [**IMECHARPOSITION**](/windows/desktop/api/Imm/ns-imm-tagimecharposition) structure. Otherwise, the application should pass the command to [**DefWindowProc**](https://msdn.microsoft.com/library/ms633572(v=VS.85).aspx) or [**ImmIsUIMessage**](/windows/desktop/api/Imm/nf-imm-immisuimessagea) if it has its own IME user interface window.

## Requirements



|                                     |                                                                                                      |
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

[**IMECHARPOSITION**](/windows/desktop/api/Imm/ns-imm-tagimecharposition)
</dt> <dt>

[**ImmIsUIMessage**](/windows/desktop/api/Imm/nf-imm-immisuimessagea)
</dt> <dt>

[**WM\_IME\_REQUEST**](wm-ime-request.md)
</dt> </dl>

 

 




