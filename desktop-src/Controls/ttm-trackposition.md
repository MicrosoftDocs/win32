---
title: TTM_TRACKPOSITION message (Commctrl.h)
description: Sets the position of a tracking tooltip.
ms.assetid: 9eb7c86c-78e6-442a-ad77-5fb919cab591
keywords:
- TTM_TRACKPOSITION message Windows Controls
topic_type:
- apiref
api_name:
- TTM_TRACKPOSITION
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_TRACKPOSITION message

Sets the position of a tracking tooltip.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies the x-coordinate of the point at which the tracking tooltip will be displayed, in screen coordinates. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the y-coordinate of the point at which the tracking tooltip will be displayed, in screen coordinates.

</dd> </dl>

## Return value

The return value for this message is not used.

## Remarks

The tooltip control chooses where to display the tooltip window based on the coordinates you provide with this message. This causes the tooltip window to appear beside the tool to which it corresponds. To have tooltip windows displayed at specific coordinates, include the TTF\_ABSOLUTE flag in the **uFlags** member of the [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure when adding the tool.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TTM\_TRACKACTIVATE**](ttm-trackactivate.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Using Tooltip Controls](using-tooltip-contro.md)
</dt> </dl>

 

