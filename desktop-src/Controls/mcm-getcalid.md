---
title: MCM\_GETCALID message
description: Gets the calendar ID for the given calendar control. You can send this message explicitly or by using the MonthCal\_GetCALID macro.
ms.assetid: 'ecfab4f3-a5af-445d-8b90-243b646524a6'
keywords: ["MCM_GETCALID message Windows Controls"]
topic_type:
- apiref
api_name:
- MCM_GETCALID
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# MCM\_GETCALID message

Gets the calendar ID for the given calendar control. You can send this message explicitly or by using the [**MonthCal\_GetCALID**](monthcal-getcalid.md) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

ID of the current calendar. One of the [Calendar Identifiers](https://msdn.microsoft.com/library/windows/desktop/dd317732) constants.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





