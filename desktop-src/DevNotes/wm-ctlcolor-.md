---
description: The WM\_CTLCOLOR message is used in 16-bit versions of Windows to change the color scheme of list boxes, the list boxes of combo boxes, message boxes, button controls, edit controls, static controls, and dialog boxes.Note  For information related to this message and 32-bit versions of Windows, see Remarks.
ms.assetid: e654cf48-550f-4210-9952-20470b9a397a
title: WM_CTLCOLOR message (WindowsX.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CTLCOLOR message

The **WM\_CTLCOLOR** message is used in 16-bit versions of Windows to change the color scheme of list boxes, the list boxes of combo boxes, message boxes, button controls, edit controls, static controls, and dialog boxes.

> [!Note]  
> For information related to this message and 32-bit versions of Windows, see Remarks.

 


```C++
  WM_CTLCOLOR

  WPARAM wParam;
  LPARAM lParam;
    
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

A handle to destination window.

</dd> <dt>

*wParam* 
</dt> <dd>

A handle to a display context (DC).

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to a child window (control).

</dd> </dl>

## Return value

If an application processes this message, it returns a handle to a brush. The system uses the brush to paint the background of the control.

## Remarks

The **WM\_CTLCOLOR** message from 16-bit Windows has been replaced by more specific notifications. These replacements include the following:

-   [**WM\_CTLCOLORBTN**](../controls/wm-ctlcolorbtn.md)
-   [**WM\_CTLCOLOREDIT**](../controls/wm-ctlcoloredit.md)
-   [**WM\_CTLCOLORDLG**](../dlgbox/wm-ctlcolordlg.md)
-   [**WM\_CTLCOLORLISTBOX**](../controls/wm-ctlcolorlistbox.md)
-   [**WM\_CTLCOLORSCROLLBAR**](../controls/wm-ctlcolorscrollbar.md)
-   [**WM\_CTLCOLORSTATIC**](../controls/wm-ctlcolorstatic.md)

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>WindowsX.h</dt> </dl> |



 

 
