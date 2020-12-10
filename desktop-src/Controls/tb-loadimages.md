---
title: TB_LOADIMAGES message (Commctrl.h)
description: Loads system-defined button images into a toolbar control's image list.
ms.assetid: 61146f43-9fd9-4fe3-b85c-cf465f2de769
keywords:
- TB_LOADIMAGES message Windows Controls
topic_type:
- apiref
api_name:
- TB_LOADIMAGES
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_LOADIMAGES message

Loads system-defined button images into a toolbar control's image list.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Identifier of a system-defined button image list. This parameter can be set to one of the following values.



| Value                                                                                                                                                                                | Meaning                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <span id="IDB_HIST_LARGE_COLOR"></span><span id="idb_hist_large_color"></span><dl> <dt>**IDB\_HIST\_LARGE\_COLOR**</dt> </dl> | Windows Explorer bitmaps in large size.<br/>                                  |
| <span id="IDB_HIST_SMALL_COLOR"></span><span id="idb_hist_small_color"></span><dl> <dt>**IDB\_HIST\_SMALL\_COLOR**</dt> </dl> | Windows Explorer bitmaps in small size.<br/>                                  |
| <span id="IDB_STD_LARGE_COLOR"></span><span id="idb_std_large_color"></span><dl> <dt>**IDB\_STD\_LARGE\_COLOR**</dt> </dl>    | Standard bitmaps in large size.<br/>                                          |
| <span id="IDB_STD_SMALL_COLOR"></span><span id="idb_std_small_color"></span><dl> <dt>**IDB\_STD\_SMALL\_COLOR**</dt> </dl>    | Standard bitmaps in small size.<br/>                                          |
| <span id="IDB_VIEW_LARGE_COLOR"></span><span id="idb_view_large_color"></span><dl> <dt>**IDB\_VIEW\_LARGE\_COLOR**</dt> </dl> | View bitmaps in large size.<br/>                                              |
| <span id="IDB_VIEW_SMALL_COLOR"></span><span id="idb_view_small_color"></span><dl> <dt>**IDB\_VIEW\_SMALL\_COLOR**</dt> </dl> | View bitmaps in small size.<br/>                                              |
| <span id="IDB_HIST_NORMAL"></span><span id="idb_hist_normal"></span><dl> <dt>**IDB\_HIST\_NORMAL**</dt> </dl>                 | Windows Explorer travel buttons and favorites bitmaps in normal state.<br/>   |
| <span id="IDB_HIST_HOT"></span><span id="idb_hist_hot"></span><dl> <dt>**IDB\_HIST\_HOT**</dt> </dl>                          | Windows Explorer travel buttons and favorites bitmaps in hot state.<br/>      |
| <span id="IDB_HIST_DISABLED"></span><span id="idb_hist_disabled"></span><dl> <dt>**IDB\_HIST\_DISABLED**</dt> </dl>           | Windows Explorer travel buttons and favorites bitmaps in disabled state.<br/> |
| <span id="IDB_HIST_PRESSED"></span><span id="idb_hist_pressed"></span><dl> <dt>**IDB\_HIST\_PRESSED**</dt> </dl>              | Windows Explorer travel buttons and favorites bitmaps in pressed state.<br/>  |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Instance handle. This parameter must be set to HINST\_COMMCTRL.

</dd> </dl>

## Return value

The count of images in the image list. Returns zero if the toolbar has no image list or if the existing image list is empty.

## Remarks

You must use the proper image index values when you prepare [**TBBUTTON**](/windows/desktop/api/Commctrl/ns-commctrl-tbbutton) structures prior to sending the [**TB\_ADDBUTTONS**](tb-addbuttons.md) message. For a list of image index values for these preset bitmaps, see [Toolbar Standard Button Image Index Values](toolbar-standard-button-image-index-values.md).

## Examples

The following sample code loads the system standard small color images.


```C++
// hWndToobar is the window handle of the toolbar control.
SendMessage(hWndToolbar, TB_LOADIMAGES, (WPARAM)IDB_STD_SMALL_COLOR, (LPARAM)HINST_COMMCTRL);
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TB\_ADDBITMAP**](tb-addbitmap.md)
</dt> </dl>

 

 





