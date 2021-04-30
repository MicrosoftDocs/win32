---
title: TCM_HIGHLIGHTITEM message (Commctrl.h)
description: Sets the highlight state of a tab item. You can send this message explicitly or by using the TabCtrl\_HighlightItem macro.
ms.assetid: b0d0850a-62d9-46a1-8846-81f67a886ea8
keywords:
- TCM_HIGHLIGHTITEM message Windows Controls
topic_type:
- apiref
api_name:
- TCM_HIGHLIGHTITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCM\_HIGHLIGHTITEM message

Sets the highlight state of a tab item. You can send this message explicitly or by using the [**TabCtrl\_HighlightItem**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_highlightitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

An **INT** value that specifies the zero-based index of a tab control item.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is a **BOOL** specifying the highlight state to be set. If this value is **TRUE**, the tab is highlighted; if **FALSE**, the tab is set to its default state. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) must be zero.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Remarks

In Comctl32.dll version 6.0, this message has no visible effect when a theme is active.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

