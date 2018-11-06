---
Description: The WM\_CTLCOLOR message is used in 16-bit versions of Windows to change the color scheme of list boxes, the list boxes of combo boxes, message boxes, button controls, edit controls, static controls, and dialog boxes.Note  For information related to this message and 32-bit versions of Windows, see Remarks. 
ms.assetid: e654cf48-550f-4210-9952-20470b9a397a
title: WM_CTLCOLOR message
ms.topic: article
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

-   [**WM\_CTLCOLORBTN**](https://msdn.microsoft.com/library/Bb761849(v=VS.85).aspx)
-   [**WM\_CTLCOLOREDIT**](https://msdn.microsoft.com/library/Bb761691(v=VS.85).aspx)
-   [**WM\_CTLCOLORDLG**](https://msdn.microsoft.com/library/ms645417(v=VS.85).aspx)
-   [**WM\_CTLCOLORLISTBOX**](https://msdn.microsoft.com/library/Bb761360(v=VS.85).aspx)
-   [**WM\_CTLCOLORSCROLLBAR**](https://msdn.microsoft.com/library/Bb787573(v=VS.85).aspx)
-   [**WM\_CTLCOLORSTATIC**](https://msdn.microsoft.com/library/Bb787524(v=VS.85).aspx)

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>WindowsX.h</dt> </dl> |



 

 




