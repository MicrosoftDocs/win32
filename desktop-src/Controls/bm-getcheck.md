---
title: BM\_GETCHECK message
description: Gets the check state of a radio button or check box. You can send this message explicitly or use the Button\_GetCheck macro.
ms.assetid: a25b2c8d-0b32-4807-bfb4-e277675924f1
keywords:
- BM_GETCHECK message Windows Controls
topic_type:
- apiref
api_name:
- BM_GETCHECK
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BM\_GETCHECK message

Gets the check state of a radio button or check box. You can send this message explicitly or use the [**Button\_GetCheck**](/windows/desktop/api/Windowsx/nf-windowsx-button_getcheck) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

The return value from a button created with the [**BS\_AUTOCHECKBOX**](https://www.bing.com/search?q=**BS\_AUTOCHECKBOX**), [**BS\_AUTORADIOBUTTON**](https://www.bing.com/search?q=**BS\_AUTORADIOBUTTON**), [**BS\_AUTO3STATE**](https://www.bing.com/search?q=**BS\_AUTO3STATE**), [**BS\_CHECKBOX**](https://www.bing.com/search?q=**BS\_CHECKBOX**), [**BS\_RADIOBUTTON**](https://www.bing.com/search?q=**BS\_RADIOBUTTON**), or [**BS\_3STATE**](https://www.bing.com/search?q=**BS\_3STATE**) style can be one of the following.



| Return code                                                                                       | Description                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**BST\_CHECKED**</dt> </dl>       | Button is checked.<br/>                                                                                                                                                                                     |
| <dl> <dt>**BST\_INDETERMINATE**</dt> </dl> | Button is grayed, indicating an indeterminate state (applies only if the button has the [**BS\_3STATE**](https://www.bing.com/search?q=**BS\_3STATE**) or [**BS\_AUTO3STATE**](https://www.bing.com/search?q=**BS\_AUTO3STATE**) style).<br/> |
| <dl> <dt>**BST\_UNCHECKED**</dt> </dl>     | Button is cleared<br/>                                                                                                                                                                                      |



 

## Remarks

If the button has a style other than those listed, the return value is zero.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**BM\_GETSTATE**](bm-getstate.md)
</dt> <dt>

[**BM\_SETCHECK**](bm-setcheck.md)
</dt> </dl>

 

 





