---
title: CDN\_INITDONE notification code
description: Sent by an Explorer-style Open or Save As dialog box when the system has finished arranging the controls in the dialog box. The system moves the standard controls to make room for the controls of the child dialog box.
ms.assetid: 337fccac-5444-442d-92f0-862c5302fa21
keywords:
- CDN_INITDONE notification code Dialog Boxes
topic_type:
- apiref
api_name:
- CDN_INITDONE
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

# CDN\_INITDONE notification code

\[Starting with Windows Vista, the **Open** and **Save As** common dialog boxes have been superseded by the [Common Item Dialog](_shell_common_file_dialog). We recommended that you use the Common Item Dialog API instead of these dialog boxes from the Common Dialog Box Library.\]

Sent by an Explorer-style **Open** or **Save As** dialog box when the system has finished arranging the controls in the dialog box. The system moves the standard controls to make room for the controls of the child dialog box.

Your [*OFNHookProc*](ofnhookproc.md) hook procedure receives this message in the form of a [**WM\_NOTIFY**](_win32_WM_NOTIFY) message.


```C++
#define CDN_FIRST               (0U-601U)
#define CDN_INITDONE            (CDN_FIRST - 0x0000)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**OFNOTIFY**](/windows/win32/Commdlg/ns-commdlg-_ofnotifya?branch=master) structure. The **OFNOTIFY** structure contains an [**NMHDR**](_win32_nmhdr_str) structure whose **code** member indicates the **CDN\_INITDONE** notification message.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

The system sends this notification only if the dialog box was created using the **OFN\_EXPLORER** value.

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

[**GetOpenFileName**](/windows/win32/Commdlg/nf-commdlg-getopenfilenamea?branch=master)
</dt> <dt>

[**GetSaveFileName**](/windows/win32/Commdlg/nf-commdlg-getsavefilenamea?branch=master)
</dt> <dt>

[*OFNHookProc*](ofnhookproc.md)
</dt> <dt>

[**OFNOTIFY**](/windows/win32/Commdlg/ns-commdlg-_ofnotifya?branch=master)
</dt> <dt>

[**OPENFILENAME**](/windows/win32/Commdlg/ns-commdlg-tagofna?branch=master)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

 





