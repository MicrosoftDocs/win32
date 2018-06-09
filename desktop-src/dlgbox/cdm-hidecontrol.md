---
title: CDM\_HIDECONTROL message
description: Hides the specified control in an Explorer-style Open or Save As dialog box.
ms.assetid: 5bf7f861-d38c-491a-89f0-5b3dfce8abfc
keywords:
- CDM_HIDECONTROL message Dialog Boxes
topic_type:
- apiref
api_name:
- CDM_HIDECONTROL
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CDM\_HIDECONTROL message

\[Starting with Windows Vista, the **Open** and **Save As** common dialog boxes have been superseded by the [Common Item Dialog](f8846148-89a5-4b9b-ad68-56137a5c2f65). We recommended that you use the Common Item Dialog API instead of these dialog boxes from the Common Dialog Box Library.\]

Hides the specified control in an Explorer-style **Open** or **Save As** dialog box. The dialog box must have been created with the **OFN\_EXPLORER** flag; otherwise, the message fails.


```C++
#define WM_USER                  0x0400
#define CDM_FIRST               (WM_USER + 100)
#define CDM_HIDECONTROL         (CDM_FIRST + 0x0005)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The identifier of the control to be hidden.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

This message has no return value.

## Remarks

The corresponding macro is as follows:

``` syntax
void CommDlg_OpenSave_HideControl(hwnd, wparam);
```

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

[**GetOpenFileName**](/windows/desktop/api/Commdlg/nf-commdlg-getopenfilenamea)
</dt> <dt>

[**GetSaveFileName**](/windows/desktop/api/Commdlg/nf-commdlg-getsavefilenamea)
</dt> <dt>

[**OPENFILENAME**](/windows/desktop/api/Commdlg/ns-commdlg-tagofna)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

 





