---
title: WM_CHOOSEFONT_SETFLAGS message (Commdlg.h)
description: An application sends the WM\_CHOOSEFONT\_SETFLAGS message to a Font dialog box to set the display options for the dialog box.
ms.assetid: 945ebc07-440d-4466-8255-ad344bdc568a
keywords:
- WM_CHOOSEFONT_SETFLAGS message Dialog Boxes
topic_type:
- apiref
api_name:
- WM_CHOOSEFONT_SETFLAGS
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CHOOSEFONT\_SETFLAGS message

An application sends the **WM\_CHOOSEFONT\_SETFLAGS** message to a **Font** dialog box to set the display options for the dialog box.


```C++
#define WM_USER                        0x0400
#define WM_CHOOSEFONT_SETFLAGS        (WM_USER + 102)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**CHOOSEFONT**](/windows/win32/api/commdlg/ns-commdlg-choosefonta) structure that contains new settings in the **Flags** member.

</dd> </dl>

## Return value

No return value.

## Remarks

The [**ChooseFont**](/windows/win32/api/commdlg/ns-commdlg-choosefonta) function creates a **Font** dialog box and uses a [**CHOOSEFONT**](/windows/win32/api/commdlg/ns-commdlg-choosefonta) structure to specify the initial values for the **Flags** member. Use the **WM\_CHOOSEFONT\_SETFLAGS** message to specify different values for the **Flags** member while the **Font** dialog box is open.

Typically, you should send the **WM\_CHOOSEFONT\_SETFLAGS** message from a [**CFHookProc**](/windows/win32/api/commdlg/nc-commdlg-lpcfhookproc) hook procedure.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Commdlg.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CFHookProc**](/windows/win32/api/commdlg/nc-commdlg-lpcfhookproc)
</dt> <dt>

[**ChooseFont**](/windows/win32/api/commdlg/ns-commdlg-choosefonta)
</dt> <dt>

[**CHOOSEFONT**](/windows/win32/api/commdlg/ns-commdlg-choosefonta)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

