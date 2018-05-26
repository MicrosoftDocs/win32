---
title: WM\_CHOOSEFONT\_SETLOGFONT message
description: An application sends the WM\_CHOOSEFONT\_SETLOGFONT message to a Font dialog box to set the current logical font information.
ms.assetid: ad169eca-a3ae-45bd-90df-821a93a7a764
keywords:
- WM_CHOOSEFONT_SETLOGFONT message Dialog Boxes
topic_type:
- apiref
api_name:
- WM_CHOOSEFONT_SETLOGFONT
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_CHOOSEFONT\_SETLOGFONT message

An application sends the **WM\_CHOOSEFONT\_SETLOGFONT** message to a **Font** dialog box to set the current logical font information.


```C++
#define WM_USER                        0x0400
#define WM_CHOOSEFONT_SETLOGFONT      (WM_USER + 101)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**LOGFONT**](https://msdn.microsoft.com/library/windows/desktop/dd145037) structure that contains information about the current logical font.

</dd> </dl>

## Return value

This message has no return value.

## Remarks

When you call the [**ChooseFont**](/windows/win32/Commdlg/ns-commdlg-tagchoosefonta?branch=master) function to create a **Font** dialog box, you can use the **lpLogFont** member of the [**CHOOSEFONT**](/windows/win32/Commdlg/ns-commdlg-tagchoosefonta?branch=master) structure to specify a [**LOGFONT**](https://msdn.microsoft.com/library/windows/desktop/dd145037) structure containing initial values for the dialog box. Use the **WM\_CHOOSEFONT\_SETLOGFONT** message to specify a **LOGFONT** structure with different values while the **Font** dialog box is open.

Typically, you would send the **WM\_CHOOSEFONT\_SETLOGFONT** message from a [**CFHookProc**](cfhookproc.md) hook procedure. The hook procedure can also send the [**WM\_CHOOSEFONT\_GETLOGFONT**](wm-choosefont-getlogfont.md) and [**WM\_CHOOSEFONT\_SETFLAGS**](wm-choosefont-setflags.md) messages.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Commdlg.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CFHookProc**](cfhookproc.md)
</dt> <dt>

[**ChooseFont**](/windows/win32/Commdlg/ns-commdlg-tagchoosefonta?branch=master)
</dt> <dt>

[**CHOOSEFONT**](/windows/win32/Commdlg/ns-commdlg-tagchoosefonta?branch=master)
</dt> <dt>

[**WM\_CHOOSEFONT\_GETLOGFONT**](wm-choosefont-getlogfont.md)
</dt> <dt>

[**WM\_CHOOSEFONT\_SETFLAGS**](wm-choosefont-setflags.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**LOGFONT**](https://msdn.microsoft.com/library/windows/desktop/dd145037)
</dt> </dl>

 

 





