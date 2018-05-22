---
title: BM\_GETCHECK message
description: Gets the check state of a radio button or check box. You can send this message explicitly or use the Button\_GetCheck macro.
ms.assetid: 'a25b2c8d-0b32-4807-bfb4-e277675924f1'
keywords: ["BM_GETCHECK message Windows Controls"]
topic_type:
- apiref
api_name:
- BM_GETCHECK
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# BM\_GETCHECK message

Gets the check state of a radio button or check box. You can send this message explicitly or use the [**Button\_GetCheck**](button-getcheck.md) macro.

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

The return value from a button created with the [**BS\_AUTOCHECKBOX**](button-styles.md#bs-autocheckbox), [**BS\_AUTORADIOBUTTON**](button-styles.md#bs-autoradiobutton), [**BS\_AUTO3STATE**](button-styles.md#bs-auto3state), [**BS\_CHECKBOX**](button-styles.md#bs-checkbox), [**BS\_RADIOBUTTON**](button-styles.md#bs-radiobutton), or [**BS\_3STATE**](button-styles.md#bs-3state) style can be one of the following.



| Return code                                                                                       | Description                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**BST\_CHECKED**</dt> </dl>       | Button is checked.<br/>                                                                                                                                                                                     |
| <dl> <dt>**BST\_INDETERMINATE**</dt> </dl> | Button is grayed, indicating an indeterminate state (applies only if the button has the [**BS\_3STATE**](button-styles.md#bs-3state) or [**BS\_AUTO3STATE**](button-styles.md#bs-auto3state) style).<br/> |
| <dl> <dt>**BST\_UNCHECKED**</dt> </dl>     | Button is cleared<br/>                                                                                                                                                                                      |



 

## Remarks

If the button has a style other than those listed, the return value is zero.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**BM\_GETSTATE**](bm-getstate.md)
</dt> <dt>

[**BM\_SETCHECK**](bm-setcheck.md)
</dt> </dl>

 

 





