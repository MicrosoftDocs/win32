---
Description: Sets the font that a control is to use when drawing text.
ms.assetid: 7db6b8af-dbec-4c29-8bf7-d7e95d9813c3
title: WM\_SETFONT message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

The best time for the owner of a dialog box control to set the font of the control is when it receives the [**WM\_INITDIALOG**](dlgbox.wm_initdialog) message. The application should call the [**DeleteObject**](gdi.deleteobject) function to delete the font when it is no longer needed; for example, after it destroys the control.

The size of the control does not change as a result of receiving this message. To avoid clipping text that does not fit within the boundaries of the control, the application should correct the size of the control window before it sets the font.

When a dialog box uses the [DS\_SETFONT](dlgbox.about_dialog_boxes#templates) style to set the text in its controls, the system sends the **WM\_SETFONT** message to the dialog box procedure before it creates the controls. An application can create a dialog box that contains the DS\_SETFONT style by calling any of the following functions:

-   [**CreateDialogIndirect**](dlgbox.createdialogindirect)
-   [**CreateDialogIndirectParam**](dlgbox.createdialogindirectparam)
-   [**DialogBoxIndirect**](dlgbox.dialogboxindirect)
-   [**DialogBoxIndirectParam**](dlgbox.dialogboxindirectparam)

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

[**CreateDialogIndirect**](dlgbox.createdialogindirect)
</dt> <dt>

[**CreateDialogIndirectParam**](dlgbox.createdialogindirectparam)
</dt> <dt>

[**DialogBoxIndirect**](dlgbox.dialogboxindirect)
</dt> <dt>

[**DialogBoxIndirectParam**](dlgbox.dialogboxindirectparam)
</dt> <dt>

[**DLGTEMPLATE**](dlgbox.dlgtemplate)
</dt> <dt>

[**MAKELPARAM**](/windows/win32/Winuser/nf-winuser-makelparam?branch=master)
</dt> <dt>

[**WM\_GETFONT**](wm-getfont.md)
</dt> <dt>

[**WM\_INITDIALOG**](dlgbox.wm_initdialog)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**DeleteObject**](gdi.deleteobject)
</dt> </dl>

 

 




