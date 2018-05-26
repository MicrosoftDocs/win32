---
title: CDN\_INCLUDEITEM notification code
description: Sent by an Open or Save As dialog box to determine whether the dialog box should display an item in a shell folders item list.
ms.assetid: 0972a78d-e058-4bac-85bd-fbd4c3885552
keywords:
- CDN_INCLUDEITEM notification code Dialog Boxes
topic_type:
- apiref
api_name:
- CDN_INCLUDEITEM
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

# CDN\_INCLUDEITEM notification code

\[Starting with Windows Vista, the **Open** and **Save As** common dialog boxes have been superseded by the [Common Item Dialog](_shell_common_file_dialog). We recommended that you use the Common Item Dialog API instead of these dialog boxes from the Common Dialog Box Library.\]

Sent by an **Open** or **Save As** dialog box to determine whether the dialog box should display an item in a shell folder's item list. When the user opens a folder, the dialog box sends a **CDN\_INCLUDEITEM** notification for each item in the folder. The dialog box sends this notification only if the **OFN\_ENABLEINCLUDENOTIFY** flag was set when the dialog box was created.

Your [*OFNHookProc*](ofnhookproc.md) hook procedure receives this message in the form of a [**WM\_NOTIFY**](_win32_WM_NOTIFY) message.


```C++
#define CDN_FIRST               (0U-601U)
#define CDN_INCLUDEITEM         (CDN_FIRST - 0x0007)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**OFNOTIFYEX**](/windows/win32/Commdlg/ns-commdlg-_ofnotifyexa?branch=master) structure.

The [**OFNOTIFYEX**](/windows/win32/Commdlg/ns-commdlg-_ofnotifyexa?branch=master) structure contains an [**NMHDR**](https://msdn.microsoft.com/library/windows/desktop/bb775514) structure whose **code** member indicates the **CDN\_INCLUDEITEM** notification message.

The **psf** member of the [**OFNOTIFYEX**](/windows/win32/Commdlg/ns-commdlg-_ofnotifyexa?branch=master) structure is a pointer to an interface for the folder whose items are being enumerated. The **pidl** member is a pointer to an item identifier list that identifies the item relative to the folder.

</dd> </dl>

## Return value

If the [*OFNHookProc*](ofnhookproc.md) hook procedure returns zero, the dialog box excludes the item from the list of items.

To include the item, return a nonzero value from the hook procedure.

## Remarks

The dialog box always includes items that have both the **SFGAO\_FILESYSTEM** and **SFGAO\_FILESYSANCESTOR** attributes, regardless of the value returned by **CDN\_INCLUDEITEM**.

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

[**OFNOTIFYEX**](/windows/win32/Commdlg/ns-commdlg-_ofnotifyexa?branch=master)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

 





