---
title: TTM_ADDTOOL message (Commctrl.h)
description: Registers a tool with a tooltip control.
ms.assetid: c974866b-20e7-45bc-914e-9dcf9af161e0
keywords:
- TTM_ADDTOOL message Windows Controls
topic_type:
- apiref
api_name:
- TTM_ADDTOOL
- TTM_ADDTOOLA
- TTM_ADDTOOLW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_ADDTOOL message

Registers a tool with a tooltip control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure containing information that the tooltip control needs to display text for the tool. The **cbSize** member of this structure must be filled in before sending this message.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remakrs

Although the name of the message implicitly indicates the "addition of a tool", it must be made clear that this message merely records a set of specific settings for what is called "a tool", however a ToolTip can be displayed even when there is no "tool" itself (a visual control with a handle), for this reason this message should be interpreted as "add a set of specific settings for the display of a ToolTip ". A ToolTip window can be displayed in several different ways and each of these ways can be registered via the TTM_ADDTOOL message.

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TTM\_ADDTOOLW** (Unicode) and **TTM\_ADDTOOLA** (ANSI)<br/>                   |

## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TTM\_DELTOOL**](ttm-deltool.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[About Tooltip Controls](tooltip-controls.md)
</dt> </dl>

 

 





