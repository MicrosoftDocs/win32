---
title: WM_PSD_YAFULLPAGERECT message
description: Notifies the hook procedure of a Page Setup dialog box, PagePaintHook, that the dialog box is about to draw the return address portion of an envelope sample page.
ms.assetid: 1f6aea69-a1bd-41ea-b508-44b4f5c38757
keywords:
- WM_PSD_YAFULLPAGERECT message Dialog Boxes
topic_type:
- apiref
api_name:
- WM_PSD_YAFULLPAGERECT
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

# WM\_PSD\_YAFULLPAGERECT message

Notifies the hook procedure of a **Page Setup** dialog box, [*PagePaintHook*](https://msdn.microsoft.com/en-us/library/ms646935(v=VS.85).aspx), that the dialog box is about to draw the return address portion of an envelope sample page.


```C++
#define WM_USER                  0x0400
#define WM_PSD_YAFULLPAGERECT   (WM_USER+6)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the device context for the sample page.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897) structure that contains the coordinates, in pixels, of the sample page.

</dd> </dl>

## Return value

If the hook procedure returns **TRUE**, the dialog box does not draw the return address portion of an envelope sample page.

If the hook procedure returns **FALSE**, the dialog box draws the return address portion of an envelope sample page.

If the paper type is not an envelope, the return value has no effect.

## Remarks

The **Page Setup** dialog box includes an image of a sample page that shows how the user's selections affect the appearance of the printed output. When you call the [**PageSetupDlg**](https://msdn.microsoft.com/en-us/library/ms646937(v=VS.85).aspx) function, you can provide a [*PagePaintHook*](https://msdn.microsoft.com/en-us/library/ms646935(v=VS.85).aspx) hook procedure to customize the appearance of the sample page. Whenever the dialog box is about to draw the contents of the sample page, the dialog box sends a sequence of messages to the hook procedure.

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

[*PagePaintHook*](https://msdn.microsoft.com/en-us/library/ms646935(v=VS.85).aspx)
</dt> <dt>

[**PageSetupDlg**](https://msdn.microsoft.com/en-us/library/ms646937(v=VS.85).aspx)
</dt> <dt>

[**WM\_PSD\_PAGESETUPDLG**](wm-psd-pagesetupdlg.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Common Dialog Box Library](common-dialog-box-library.md)
</dt> </dl>

 

 





