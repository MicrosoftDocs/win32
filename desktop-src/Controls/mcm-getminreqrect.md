---
title: MCM_GETMINREQRECT message (Commctrl.h)
description: Retrieves the minimum size required to display a full month in a month calendar control. You can send this message explicitly or by using the MonthCal\_GetMinReqRect macro.
ms.assetid: f0378338-4809-48e9-9387-ed8b79356f95
keywords:
- MCM_GETMINREQRECT message Windows Controls
topic_type:
- apiref
api_name:
- MCM_GETMINREQRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCM\_GETMINREQRECT message

Retrieves the minimum size required to display a full month in a month calendar control. You can send this message explicitly or by using the [**MonthCal\_GetMinReqRect**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_getminreqrect) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure that will receive bounding rectangle information. This parameter must be a valid address and cannot be **NULL**.

</dd> </dl>

## Return value

Returns nonzero and *lParam* receives the applicable bounding information if successful. Otherwise, the message returns zero.

## Remarks

The minimum required window size for a month calendar control depends on the currently selected font, control styles, system metrics, and regional settings. When an application changes anything that affects the minimum window size, or processes a [**WM\_SETTINGCHANGE**](/windows/desktop/winmsg/wm-settingchange) message, it should send **MCM\_GETMINREQRECT** to determine the new minimum size.

> [!Note]  
> The rectangle returned by **MCM\_GETMINREQRECT** does not include the width of the "Today" string, if it is present. If the [**MCS\_NOTODAY**](month-calendar-control-styles.md) style is not set, your application should also retrieve the rectangle that defines the "Today" string width by sending a [**MCM\_GETMAXTODAYWIDTH**](mcm-getmaxtodaywidth.md) message. Use the larger of the two rectangles to ensure that the "Today" string is not clipped.

 

The **top** and **left** members of the structure pointed to by *lParam* will always be zero. The **right** and **bottom** members represent the minimum *cx* and *cy* required for the control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

