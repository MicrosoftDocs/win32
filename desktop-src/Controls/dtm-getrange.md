---
title: DTM_GETRANGE message
description: Gets the current minimum and maximum allowable system times for a date and time picker (DTP) control. You can send this message explicitly or use the DateTime\_GetRange macro.
ms.assetid: 190cada6-49ee-483f-a464-d3d789127159
keywords:
- DTM_GETRANGE message Windows Controls
topic_type:
- apiref
api_name:
- DTM_GETRANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DTM\_GETRANGE message

Gets the current minimum and maximum allowable system times for a date and time picker (DTP) control. You can send this message explicitly or use the [**DateTime\_GetRange**](/windows/desktop/api/Commctrl/nf-commctrl-datetime_getrange) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a two-element array of [**SYSTEMTIME**](https://msdn.microsoft.com/library/windows/desktop/ms724950) structures.

</dd> </dl>

## Return value

Returns a **DWORD** value that is a combination of GDTR\_MIN or GDTR\_MAX. The first element of the [**SYSTEMTIME**](https://msdn.microsoft.com/library/windows/desktop/ms724950) array contains the minimum allowable time if GDTR\_MIN is set. The second element of the **SYSTEMTIME** array contains the maximum allowable time if GDTR\_MAX is set.

## Remarks

The date and time picker displays only dates/times that fall within the specified range, preventing the user from selecting a date and time that falls outside the range. If the [**DTM\_SETSYSTEMTIME**](dtm-setsystemtime.md) message specifies a date and time that falls outside the range, it will fail.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





