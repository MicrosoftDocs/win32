---
title: MCM_GETMAXTODAYWIDTH message (Commctrl.h)
description: Retrieves the maximum width of the \ 0034;today \ 0034; string in a month calendar control. This includes the label text and the date text. You can send this message explicitly or by using the MonthCal\_GetMaxTodayWidth macro.
ms.assetid: bb55c24e-ba04-4a57-97b0-ff04d77e1d43
keywords:
- MCM_GETMAXTODAYWIDTH message Windows Controls
topic_type:
- apiref
api_name:
- MCM_GETMAXTODAYWIDTH
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCM\_GETMAXTODAYWIDTH message

Retrieves the maximum width of the "today" string in a month calendar control. This includes the label text and the date text. You can send this message explicitly or by using the [**MonthCal\_GetMaxTodayWidth**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_getmaxtodaywidth) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the width of the "today" string, in pixels.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





