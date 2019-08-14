---
title: WM_CHOOSEFONT_SETLOGFONT message
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
ms.topic: article
ms.date: 05/31/2018
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

A pointer to a [**LOGFONT**](https://docs.microsoft.com/windows/win32/api/wingdi/ns-wingdi-logfonta) structure that contains information about the current logical font.

</dd> </dl>

## Return value

This message has no return value.

## Remarks

When you call the [**ChooseFont**](/windows/win32/api/commdlg/ns-commdlg-choosefonta) function to create a **Font** dialog box, you can use the **lpLogFont** member of the [**CHOOSEFONT**](/windows/win32/api/commdlg/ns-commdlg-choosefonta) structure to specify a [**LOGFONT**](https://docs.microsoft.com/windows/win32/api/wingdi/ns-wingdi-logfonta) structure containing initial values for the dialog box. Use the **WM\_CHOOSEFONT\_SETLOGFONT** message to specify a **LOGFONT** structure with different values while the **Font** dialog box is open.

Typically, you would send the **WM\_CHOOSEFONT\_SETLOGFONT** message from a [**CFHookProc**](https://msdn.microsoft.com/en-us/library/ms646909(v=VS.85).aspx) hook procedure. The hook procedure can also send the [**WM\_CHOOSEFONT\_GETLOGFONT**](wm-choosefont-getlogfont.md) and [**WM\_CHOOSEFONT\_SETFLAGS**](wm-choosefont-setflags.md) messages.

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

[**CFHookProc**](https://msdn.microsoft.com/en-us/library/ms646909(v=VS.85).aspx)
</dt> <dt>

[**ChooseFont**](/windows/win32/api/commdlg/ns-commdlg-choosefonta)
</dt> <dt>

[**CHOOSEFONT**](/windows/win32/api/commdlg/ns-commdlg-choosefonta)
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

[**LOGFONT**](https://docs.microsoft.com/windows/win32/api/wingdi/ns-wingdi-logfonta)
</dt> </dl>

 

 





