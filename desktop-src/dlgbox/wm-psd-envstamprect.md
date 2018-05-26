---
title: WM\_PSD\_ENVSTAMPRECT message
description: Notifies the hook procedure of a Page Setup dialog box, PagePaintHook, that the dialog box is about to draw the envelope-stamp rectangle of the sample page.
ms.assetid: f193baa0-a084-416e-90c9-9c838758a3d3
keywords:
- WM_PSD_ENVSTAMPRECT message Dialog Boxes
topic_type:
- apiref
api_name:
- WM_PSD_ENVSTAMPRECT
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

# WM\_PSD\_ENVSTAMPRECT message

Notifies the hook procedure of a **Page Setup** dialog box, [*PagePaintHook*](pagepainthook.md), that the dialog box is about to draw the envelope-stamp rectangle of the sample page.


```C++
#define WM_USER                  0x0400
#define WM_PSD_ENVSTAMPRECT     (WM_USER+5)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the device context for the sample page.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897) structure that contains the coordinates, in pixels, of the envelope-stamp rectangle.

</dd> </dl>

## Return value

If the hook procedure returns **TRUE**, the dialog box does not draw the envelope-stamp portion of the sample page.

If the hook procedure returns **FALSE**, the dialog box draws the envelope-stamp portion of the sample page.

## Remarks

The **Page Setup** dialog box includes an image of a sample page that shows how the user's selections affect the appearance of the printed output. When you call the [**PageSetupDlg**](pagesetupdlg.md) function, you can provide a [*PagePaintHook*](pagepainthook.md) hook procedure to customize the appearance of the sample page. Whenever the dialog box is about to draw the contents of the sample page, the dialog box sends a sequence of messages to the hook procedure.

A hook procedure receives this message only if the selected paper type is an envelope.

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

[*PagePaintHook*](pagepainthook.md)
</dt> <dt>

[**PageSetupDlg**](pagesetupdlg.md)
</dt> <dt>

[**WM\_PSD\_PAGESETUPDLG**](wm-psd-pagesetupdlg.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

 





