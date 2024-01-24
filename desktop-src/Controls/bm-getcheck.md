---
title: BM_GETCHECK message (Winuser.h)
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
ms.topic: reference
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

The return value from a button created with the [**BS\_AUTOCHECKBOX**](button-styles.md), [**BS\_AUTORADIOBUTTON**](button-styles.md), [**BS\_AUTO3STATE**](button-styles.md), [**BS\_CHECKBOX**](button-styles.md), [**BS\_RADIOBUTTON**](button-styles.md), or [**BS\_3STATE**](button-styles.md) style can be one of the following.



| Return code                                                                                       | Description                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**BST\_CHECKED**</dt> </dl>       | Button is checked.<br/>                                                                                                                                                                                     |
| <dl> <dt>**BST\_INDETERMINATE**</dt> </dl> | Button is grayed, indicating an indeterminate state (applies only if the button has the [**BS\_3STATE**](button-styles.md) or [**BS\_AUTO3STATE**](button-styles.md) style).<br/> |
| <dl> <dt>**BST\_UNCHECKED**</dt> </dl>     | Button is cleared<br/>                                                                                                                                                                                      |



 

## Remarks

If the button has a style other than those listed, the return value is zero.

## Requirements



| Requirement | Value |
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

 

 





