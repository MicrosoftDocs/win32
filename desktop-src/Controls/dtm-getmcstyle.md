---
title: DTM\_GETMCSTYLE message
description: Gets the style of a date and time picker (DTP) control. Send this message explicitly or by using the DateTime\_GetMonthCalStyle macro.
ms.assetid: 8983898f-e23a-4247-838c-56364f695429
keywords:
- DTM_GETMCSTYLE message Windows Controls
topic_type:
- apiref
api_name:
- DTM_GETMCSTYLE
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

# DTM\_GETMCSTYLE message

Gets the style of a date and time picker (DTP) control. Send this message explicitly or by using the [**DateTime\_GetMonthCalStyle**](/windows/win32/Commctrl/nf-commctrl-datetime_getmonthcalstyle?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the style value of the control. For more information see [Month Calendar Control Styles](month-calendar-control-styles.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





