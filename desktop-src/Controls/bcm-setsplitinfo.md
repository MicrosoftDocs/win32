---
title: BCM\_SETSPLITINFO message
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BCM\_SETSPLITINFO message

Sets information for a split button control. Send this message explicitly or by using the [**Button\_SetSplitInfo**](/windows/win32/Commctrl/nf-commctrl-button_setsplitinfo?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

A pointer to a [**BUTTON\_SPLITINFO**](/windows/win32/Commctrl/ns-commctrl-tagbutton_splitinfo?branch=master) structure containing information about the split button.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

Use this message only with the [**BS\_SPLITBUTTON**](button-styles.md#bs-splitbutton) and [**BS\_DEFSPLITBUTTON**](button-styles.md#bs-defsplitbutton) button styles.

## Requirements



|                                     |                                                                                       |
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

 

 





