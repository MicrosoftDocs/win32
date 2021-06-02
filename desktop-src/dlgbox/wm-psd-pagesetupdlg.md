---
title: WM_PSD_PAGESETUPDLG message (Commdlg.h)
description: Notifies a PagePaintHook hook procedure that the Page Setup dialog box is about to draw the contents of the sample page. The hook procedure can use this message to carry out initialization tasks related to drawing the contents of the sample page.
ms.assetid: 0d95240b-7d77-4819-8e5c-cc25cd1b30f2
keywords:
- WM_PSD_PAGESETUPDLG message Dialog Boxes
topic_type:
- apiref
api_name:
- WM_PSD_PAGESETUPDLG
api_location:
- Commdlg.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_PSD\_PAGESETUPDLG message

Notifies a [**PagePaintHook**](/windows/win32/api/commdlg/nc-commdlg-lppagepainthook) hook procedure that the **Page Setup** dialog box is about to draw the contents of the sample page. The hook procedure can use this message to carry out initialization tasks related to drawing the contents of the sample page.


```C++
#define WM_USER                  0x0400
#define WM_PSD_PAGESETUPDLG     (WM_USER  )
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The low-order word specifies a value that indicates the paper size. This value can be one of the **DMPAPER\_** values listed in the description of the structure. The high-order word specifies the orientation of the paper or envelope, and whether the printer is a dot matrix or HPPCL (Hewlett Packard Printer Control Language) device. This parameter can be one of the following values.



| Value                                                                             | Meaning                                            |
|-----------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>0x0001</dt> </dl> | Paper in landscape mode (dot matrix)<br/>    |
| <dl> <dt>0x0003</dt> </dl> | Paper in landscape mode (HPPCL)<br/>         |
| <dl> <dt>0x0005</dt> </dl> | Paper in portrait mode (dot matrix)<br/>     |
| <dl> <dt>0x0007</dt> </dl> | Paper in portrait mode (HPPCL)<br/>          |
| <dl> <dt>0x000b</dt> </dl> | Envelope in landscape mode (HPPCL)<br/>      |
| <dl> <dt>0x000d</dt> </dl> | Envelope in portrait mode (dot matrix)<br/>  |
| <dl> <dt>0x0019</dt> </dl> | Envelope in landscape mode (dot matrix)<br/> |
| <dl> <dt>0x001f</dt> </dl> | Envelope in portrait mode (HPPCL)<br/>       |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**PAGESETUPDLG**](/windows/win32/api/commdlg/ns-commdlg-pagesetupdlga) structure that contains information used to initialize the **Page Setup** dialog box.

</dd> </dl>

## Return value

If the hook procedure returns **TRUE**, the dialog box sends no more messages and does not draw in the sample page until the next time the system needs to redraw the sample page.

If the hook procedure returns **FALSE**, the dialog box sends the remaining messages of the drawing sequence.

## Remarks

The **Page Setup** dialog box includes an image of a sample page that shows how the user's selections affect the appearance of the printed output. When you call the [**PageSetupDlg**](/previous-versions/windows/desktop/legacy/ms646937(v=vs.85)) function, you can provide a [*PagePaintHook*](/windows/win32/api/commdlg/nc-commdlg-lppagepainthook) hook procedure to customize the appearance of the sample page. Whenever the dialog box is about to draw the contents of the sample page, the dialog box sends a sequence of messages to the hook procedure.

The first three messages of a drawing sequence (**WM\_PSD\_PAGESETUPDLG**, [**WM\_PSD\_FULLPAGERECT**](wm-psd-fullpagerect.md), or [**WM\_PSD\_MINMARGINRECT**](wm-psd-minmarginrect.md)) provide information that the hook procedure can use to draw the contents of the sample page. The remaining messages ([**WM\_PSD\_MARGINRECT**](wm-psd-marginrect.md), [**WM\_PSD\_GREEKTEXTRECT**](wm-psd-greektextrect.md), [**WM\_PSD\_ENVSTAMPRECT**](wm-psd-envstamprect.md), [**WM\_PSD\_YAFULLPAGERECT**](wm-psd-yafullpagerect.md)) notify the hook procedure that the dialog box is about to draw a specific portion of the sample page. This allows the hook procedure to selectively draw portions of the sample page.

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

[**PAGESETUPDLG**](/windows/win32/api/commdlg/ns-commdlg-pagesetupdlga)
</dt> <dt>

[**WM\_PSD\_ENVSTAMPRECT**](wm-psd-envstamprect.md)
</dt> <dt>

[**WM\_PSD\_FULLPAGERECT**](wm-psd-fullpagerect.md)
</dt> <dt>

[**WM\_PSD\_GREEKTEXTRECT**](wm-psd-greektextrect.md)
</dt> <dt>

[**WM\_PSD\_MARGINRECT**](wm-psd-marginrect.md)
</dt> <dt>

[**WM\_PSD\_MINMARGINRECT**](wm-psd-minmarginrect.md)
</dt> <dt>

[**WM\_PSD\_YAFULLPAGERECT**](wm-psd-yafullpagerect.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

