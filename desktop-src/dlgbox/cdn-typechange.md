---
title: CDN\_TYPECHANGE notification code
description: Sent by an Explorer-style Open or Save As dialog box when the user selects a new file type from the file types combo box.
ms.assetid: 'fb8324db-e435-4ef2-aac5-506a6b7adb2c'
keywords: ["CDN_TYPECHANGE notification code Dialog Boxes"]
topic_type:
- apiref
api_name:
- CDN_TYPECHANGE
api_location:
- Commdlg.h
api_type:
- HeaderDef
---

# CDN\_TYPECHANGE notification code

\[Starting with Windows Vista, the **Open** and **Save As** common dialog boxes have been superseded by the [Common Item Dialog](_shell_common_file_dialog). We recommended that you use the Common Item Dialog API instead of these dialog boxes from the Common Dialog Box Library.\]

Sent by an Explorer-style **Open** or **Save As** dialog box when the user selects a new file type from the file types combo box.

Your [*OFNHookProc*](ofnhookproc.md) hook procedure receives this message in the form of a [**WM\_NOTIFY**](_win32_WM_NOTIFY) message.


```C++
#define CDN_FIRST               (0U-601U)
#define CDN_TYPECHANGE          (CDN_FIRST - 0x0006)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**OFNOTIFY**](ofnotify-str.md) structure.

The [**OFNOTIFY**](ofnotify-str.md) structure contains an [**NMHDR**](_win32_nmhdr_str) structure whose **code** member indicates the **CDN\_TYPECHANGE** notification message.

The [**OFNOTIFY**](ofnotify-str.md) structure also contains a pointer to an [**OPENFILENAME**](openfilename-str.md) structure whose **nFilterIndex** member indicates the one-based index of the newly selected file type filter.

</dd> </dl>

## Return value

This message has no return value.

## Remarks

The system sends this notification only if the dialog box was created using the **OFN\_EXPLORER** value.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Commdlg.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**GetOpenFileName**](getopenfilename.md)
</dt> <dt>

[**GetSaveFileName**](getsavefilename.md)
</dt> <dt>

[*OFNHookProc*](ofnhookproc.md)
</dt> <dt>

[**OFNOTIFY**](ofnotify-str.md)
</dt> <dt>

[**OPENFILENAME**](openfilename-str.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

 





