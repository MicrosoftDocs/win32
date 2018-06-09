---
title: CDN\_TYPECHANGE notification code
description: Sent by an Explorer-style Open or Save As dialog box when the user selects a new file type from the file types combo box.
ms.assetid: fb8324db-e435-4ef2-aac5-506a6b7adb2c
keywords:
- CDN_TYPECHANGE notification code Dialog Boxes
topic_type:
- apiref
api_name:
- CDN_TYPECHANGE
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

# CDN\_TYPECHANGE notification code

\[Starting with Windows Vista, the **Open** and **Save As** common dialog boxes have been superseded by the [Common Item Dialog](f8846148-89a5-4b9b-ad68-56137a5c2f65). We recommended that you use the Common Item Dialog API instead of these dialog boxes from the Common Dialog Box Library.\]

Sent by an Explorer-style **Open** or **Save As** dialog box when the user selects a new file type from the file types combo box.

Your [*OFNHookProc*](https://www.bing.com/search?q=*OFNHookProc*) hook procedure receives this message in the form of a [**WM\_NOTIFY**](23ff9dc1-3d92-4e94-8df5-7a645039ce27) message.


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

A pointer to an [**OFNOTIFY**](/windows/desktop/api/Commdlg/ns-commdlg-_ofnotifya) structure.

The [**OFNOTIFY**](/windows/desktop/api/Commdlg/ns-commdlg-_ofnotifya) structure contains an [**NMHDR**](0c8b116b-82ad-495a-b19d-8c172e0b2608) structure whose **code** member indicates the **CDN\_TYPECHANGE** notification message.

The [**OFNOTIFY**](/windows/desktop/api/Commdlg/ns-commdlg-_ofnotifya) structure also contains a pointer to an [**OPENFILENAME**](/windows/desktop/api/Commdlg/ns-commdlg-tagofna) structure whose **nFilterIndex** member indicates the one-based index of the newly selected file type filter.

</dd> </dl>

## Return value

This message has no return value.

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

[**GetOpenFileName**](/windows/desktop/api/Commdlg/nf-commdlg-getopenfilenamea)
</dt> <dt>

[**GetSaveFileName**](/windows/desktop/api/Commdlg/nf-commdlg-getsavefilenamea)
</dt> <dt>

[*OFNHookProc*](https://www.bing.com/search?q=*OFNHookProc*)
</dt> <dt>

[**OFNOTIFY**](/windows/desktop/api/Commdlg/ns-commdlg-_ofnotifya)
</dt> <dt>

[**OPENFILENAME**](/windows/desktop/api/Commdlg/ns-commdlg-tagofna)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

 





