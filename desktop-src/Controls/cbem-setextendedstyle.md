---
title: CBEM_SETEXTENDEDSTYLE message (Commctrl.h)
description: Sets extended styles within a ComboBoxEx control.
ms.assetid: 00848bd0-5a2f-4bfb-ae1f-ee3aa88ac57a
keywords:
- CBEM_SETEXTENDEDSTYLE message Windows Controls
topic_type:
- apiref
api_name:
- CBEM_SETEXTENDEDSTYLE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CBEM\_SETEXTENDEDSTYLE message

Sets extended styles within a ComboBoxEx control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A **DWORD** value that indicates which styles in *lParam* are to be affected. Only the extended styles in *wParam* will be changed. If this parameter is zero, then all of the styles in *lParam* will be affected.

</dd> <dt>

*lParam* 
</dt> <dd>

A **DWORD** value that contains the [ComboBoxEx Control Extended Styles](comboboxex-control-extended-styles.md) to set for the control.

</dd> </dl>

## Return value

Returns a **DWORD** value that contains the extended styles previously used for the control.

## Remarks

*wParam* enables you to modify one or more extended styles without having to retrieve the existing styles first. For example, if you pass [**CBES\_EX\_NOEDITIMAGE**](comboboxex-control-extended-styles.md) for *wParam* and 0 for *lParam*, the **CBES\_EX\_NOEDITIMAGE** style will be cleared, but all other styles will remain the same.

If you try to set an extended style for a ComboBoxEx control created with the [**CBS\_SIMPLE**](combo-box-styles.md) style, it may not repaint properly.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





