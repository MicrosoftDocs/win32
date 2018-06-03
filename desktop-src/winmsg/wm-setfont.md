---
Description: Sets the font that a control is to use when drawing text.
ms.assetid: 7db6b8af-dbec-4c29-8bf7-d7e95d9813c3
title: WM\_SETFONT message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_SETFONT message

Sets the font that a control is to use when drawing text.


```C++
#define WM_SETFONT                      0x0030
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the font (**HFONT**). If this parameter is **NULL**, the control uses the default system font to draw text.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word of *lParam* specifies whether the control should be redrawn immediately upon setting the font. If this parameter is **TRUE**, the control redraws itself.

</dd> </dl>

## Return value

Type: **LRESULT**

This message does not return a value.

## Remarks

The **WM\_SETFONT** message applies to all controls, not just those in dialog boxes.

The best time for the owner of a dialog box control to set the font of the control is when it receives the [**WM\_INITDIALOG**](https://msdn.microsoft.com/windows/desktop/bc4f4718-1dab-48db-ae3b-5a81a7be2644) message. The application should call the [**DeleteObject**](https://msdn.microsoft.com/windows/desktop/cc679af0-6839-4c83-9c42-39d7ededda40) function to delete the font when it is no longer needed; for example, after it destroys the control.

The size of the control does not change as a result of receiving this message. To avoid clipping text that does not fit within the boundaries of the control, the application should correct the size of the control window before it sets the font.

When a dialog box uses the [DS\_SETFONT](https://www.bing.com/search?q=DS\_SETFONT) style to set the text in its controls, the system sends the **WM\_SETFONT** message to the dialog box procedure before it creates the controls. An application can create a dialog box that contains the DS\_SETFONT style by calling any of the following functions:

-   [**CreateDialogIndirect**](https://msdn.microsoft.com/windows/desktop/b3bddf88-be6d-4aa3-9e23-257126bdfc15)
-   [**CreateDialogIndirectParam**](https://msdn.microsoft.com/windows/desktop/f8ed581b-992e-41b8-a2f5-906b9bafa578)
-   [**DialogBoxIndirect**](https://msdn.microsoft.com/windows/desktop/0af783b3-804d-4075-8046-5109f37e275d)
-   [**DialogBoxIndirectParam**](https://msdn.microsoft.com/windows/desktop/ce241d7b-8775-4c0d-bb4b-87df5f58f8a8)

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CreateDialogIndirect**](https://msdn.microsoft.com/windows/desktop/b3bddf88-be6d-4aa3-9e23-257126bdfc15)
</dt> <dt>

[**CreateDialogIndirectParam**](https://msdn.microsoft.com/windows/desktop/f8ed581b-992e-41b8-a2f5-906b9bafa578)
</dt> <dt>

[**DialogBoxIndirect**](https://msdn.microsoft.com/windows/desktop/0af783b3-804d-4075-8046-5109f37e275d)
</dt> <dt>

[**DialogBoxIndirectParam**](https://msdn.microsoft.com/windows/desktop/ce241d7b-8775-4c0d-bb4b-87df5f58f8a8)
</dt> <dt>

[**DLGTEMPLATE**](https://msdn.microsoft.com/windows/desktop/e6164c92-51ec-48ea-9a61-80e55de7a6d8)
</dt> <dt>

[**MAKELPARAM**](/windows/desktop/api/Winuser/nf-winuser-makelparam)
</dt> <dt>

[**WM\_GETFONT**](wm-getfont.md)
</dt> <dt>

[**WM\_INITDIALOG**](https://msdn.microsoft.com/windows/desktop/bc4f4718-1dab-48db-ae3b-5a81a7be2644)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**DeleteObject**](https://msdn.microsoft.com/windows/desktop/cc679af0-6839-4c83-9c42-39d7ededda40)
</dt> </dl>

 

 




