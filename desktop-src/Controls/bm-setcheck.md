---
title: BM_SETCHECK message (Winuser.h)
description: Sets the check state of a radio button or check box. You can send this message explicitly or by using the Button\_SetCheck macro.
ms.assetid: 8294e6c4-caac-4c60-85ff-38698a1d2ae4
keywords:
- BM_SETCHECK message Windows Controls
topic_type:
- apiref
api_name:
- BM_SETCHECK
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BM\_SETCHECK message

Sets the check state of a radio button or check box. You can send this message explicitly or by using the [**Button\_SetCheck**](/windows/desktop/api/Windowsx/nf-windowsx-button_setcheck) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The check state. This parameter can be one of the following values.



| Value                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="BST_CHECKED"></span><span id="bst_checked"></span><dl> <dt>**BST\_CHECKED**</dt> </dl>                   | Sets the button state to checked.<br/>                                                                                                                                                                                           |
| <span id="BST_INDETERMINATE"></span><span id="bst_indeterminate"></span><dl> <dt>**BST\_INDETERMINATE**</dt> </dl> | Sets the button state to grayed, indicating an indeterminate state. Use this value only if the button has the [**BS\_3STATE**](button-styles.md) or [**BS\_AUTO3STATE**](button-styles.md) style.<br/> |
| <span id="BST_UNCHECKED"></span><span id="bst_unchecked"></span><dl> <dt>**BST\_UNCHECKED**</dt> </dl>             | Sets the button state to cleared.<br/>                                                                                                                                                                                           |



 

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

This message always returns zero.

## Remarks

The **BM\_SETCHECK** message has no effect on push buttons.

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

[**BM\_GETCHECK**](bm-getcheck.md)
</dt> <dt>

[**BM\_GETSTATE**](bm-getstate.md)
</dt> <dt>

[**BM\_SETSTATE**](bm-setstate.md)
</dt> </dl>

 

 





