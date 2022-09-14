---
title: BM_GETSTATE message (Winuser.h)
description: Retrieves the state of a button or check box. You can send this message explicitly or use the Button\_GetState macro.
ms.assetid: ca4c2f1a-b657-490a-ac8b-5f0cfef64d76
keywords:
- BM_GETSTATE message Windows Controls
topic_type:
- apiref
api_name:
- BM_GETSTATE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BM\_GETSTATE message

Retrieves the state of a button or check box. You can send this message explicitly or use the [**Button\_GetState**](/windows/desktop/api/Windowsx/nf-windowsx-button_getstate) macro.

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

The return value specifies the current state of the button. It is a combination of the following values.



| Return code                                                                                        | Description                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**BST\_CHECKED**</dt> </dl>        | The button is checked.<br/>                                                                                                                                                                                        |
| <dl> <dt>**BST\_DROPDOWNPUSHED**</dt> </dl> | [Windows Vista](common-control-versions.md). The button is in the drop-down state. Applies only if the button has the [**TBSTYLE\_DROPDOWN**](toolbar-control-and-button-styles.md) style.<br/> |
| <dl> <dt>**BST\_FOCUS**</dt> </dl>          | The button has the keyboard focus.<br/>                                                                                                                                                                            |
| <dl> <dt>**BST\_HOT**</dt> </dl>            | The button is hot; that is, the mouse is hovering over it.<br/>                                                                                                                                                    |
| <dl> <dt>**BST\_INDETERMINATE**</dt> </dl>  | The state of the button is indeterminate. Applies only if the button has the [**BS\_3STATE**](button-styles.md) or [**BS\_AUTO3STATE**](button-styles.md) style.<br/>                    |
| <dl> <dt>**BST\_PUSHED**</dt> </dl>         | The button is being shown in the pushed state.<br/>                                                                                                                                                                |
| <dl> <dt>**BST\_UNCHECKED**</dt> </dl>      | No special state. Equivalent to zero.<br/>                                                                                                                                                                         |



 

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

[**BM\_SETSTATE**](bm-setstate.md)
</dt> </dl>

 

 





