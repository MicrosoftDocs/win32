---
title: CDN\_HELP notification code
description: Sent by an Explorer-style Open or Save As dialog box when the user clicks the Help button.
ms.assetid: 18ee86b2-3446-4de4-a47a-2e44e677f4f7
keywords:
- CDN_HELP notification code Dialog Boxes
topic_type:
- apiref
api_name:
- CDN_HELP
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

# CDN\_HELP notification code

\[Starting with Windows Vista, the **Open** and **Save As** common dialog boxes have been superseded by the [Common Item Dialog](f8846148-89a5-4b9b-ad68-56137a5c2f65). We recommended that you use the Common Item Dialog API instead of these dialog boxes from the Common Dialog Box Library.\]

Sent by an Explorer-style **Open** or **Save As** dialog box when the user clicks the **Help** button.

Your [*OFNHookProc*](https://www.bing.com/search?q=*OFNHookProc*) hook procedure receives this message in the form of a [**WM\_NOTIFY**](23ff9dc1-3d92-4e94-8df5-7a645039ce27) message.


```C++
#define CDN_FIRST               (0U-601U)
#define CDN_HELP                (CDN_FIRST - 0x0004)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**OFNOTIFY**](/windows/desktop/api/Commdlg/ns-commdlg-_ofnotifya) structure. The **OFNOTIFY** structure contains an [**NMHDR**](0c8b116b-82ad-495a-b19d-8c172e0b2608) structure whose **code** member indicates the **CDN\_HELP** notification message.

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

 

 





