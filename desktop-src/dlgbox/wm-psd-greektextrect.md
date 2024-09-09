---
title: WM_PSD_GREEKTEXTRECT message (Commdlg.h)
description: Notifies the hook procedure of a Page Setup dialog box, PagePaintHook, that the dialog box is about to draw Greek text inside the margin rectangle of the sample page.
ms.assetid: ad0a200d-5626-4768-b3bd-73d4e3f0d548
keywords:
- WM_PSD_GREEKTEXTRECT message Dialog Boxes
topic_type:
- apiref
api_name:
- WM_PSD_GREEKTEXTRECT
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_PSD\_GREEKTEXTRECT message

Notifies the hook procedure of a **Page Setup** dialog box, [*PagePaintHook*](/windows/win32/api/commdlg/nc-commdlg-lppagepainthook), that the dialog box is about to draw Greek text inside the margin rectangle of the sample page.


```C++
#define WM_USER                  0x0400
#define WM_PSD_GREEKTEXTRECT    (WM_USER+4)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the device context for the sample page.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure that contains the coordinates, in pixels, of the Greek text rectangle.

</dd> </dl>

## Return value

If the hook procedure returns **TRUE**, the dialog box does not draw the Greek text portion of the sample page.

If the hook procedure returns **FALSE**, the dialog box draws the Greek text portion of the sample page.

## Remarks

The **Page Setup** dialog box includes an image of a sample page that shows how the user's selections affect the appearance of the printed output. When you call the [**PageSetupDlg**](/previous-versions/windows/desktop/legacy/ms646937(v=vs.85)) function, you can provide a [*PagePaintHook*](/windows/win32/api/commdlg/nc-commdlg-lppagepainthook) hook procedure to customize the appearance of the sample page. Whenever the dialog box is about to draw the contents of the sample page, the dialog box sends a sequence of messages to the hook procedure.

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

[*PagePaintHook*](/windows/win32/api/commdlg/nc-commdlg-lppagepainthook)
</dt> <dt>

[**PageSetupDlg**](/previous-versions/windows/desktop/legacy/ms646937(v=vs.85))
</dt> <dt>

[**WM\_PSD\_PAGESETUPDLG**](wm-psd-pagesetupdlg.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

