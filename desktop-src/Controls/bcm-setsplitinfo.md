---
title: BCM_SETSPLITINFO message (Commctrl.h)
description: Sets information for a split button control. Send this message explicitly or by using the Button\_SetSplitInfo macro.
ms.assetid: 609b8972-9616-4850-a72c-2f87ce19f563
keywords:
- BCM_SETSPLITINFO message Windows Controls
topic_type:
- apiref
api_name:
- BCM_SETSPLITINFO
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BCM\_SETSPLITINFO message

Sets information for a split button control. Send this message explicitly or by using the [**Button\_SetSplitInfo**](/windows/desktop/api/Commctrl/nf-commctrl-button_setsplitinfo) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

A pointer to a [**BUTTON\_SPLITINFO**](/windows/win32/api/commctrl/ns-commctrl-button_splitinfo) structure containing information about the split button.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

Use this message only with the [**BS\_SPLITBUTTON**](button-styles.md) and [**BS\_DEFSPLITBUTTON**](button-styles.md) button styles.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[Button Styles](button-styles.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Button Types](button-types-and-styles.md)
</dt> </dl>

 

 





