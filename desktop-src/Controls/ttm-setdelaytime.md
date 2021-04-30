---
title: TTM_SETDELAYTIME message (Commctrl.h)
description: Sets the initial, pop-up, and reshow durations for a tooltip control.
ms.assetid: 0a73def0-550c-4d01-9cb1-1eb1f4356fa3
keywords:
- TTM_SETDELAYTIME message Windows Controls
topic_type:
- apiref
api_name:
- TTM_SETDELAYTIME
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_SETDELAYTIME message

Sets the initial, pop-up, and reshow durations for a tooltip control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Flag that specifies which time value to set. This parameter can be one of the following values



| Value                                                                                                                                                            | Meaning                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TTDT_AUTOPOP"></span><span id="ttdt_autopop"></span><dl> <dt>**TTDT\_AUTOPOP**</dt> </dl>       | Set the amount of time a tooltip window remains visible if the pointer is stationary within a tool's bounding rectangle. To return the autopop delay time to its default value, set *lParam* to -1.<br/>                                                                                                                                                         |
| <span id="TTDT_INITIAL"></span><span id="ttdt_initial"></span><dl> <dt>**TTDT\_INITIAL**</dt> </dl>       | Set the amount of time a pointer must remain stationary within a tool's bounding rectangle before the tooltip window appears. To return the initial delay time to its default value, set *lParam* to -1.<br/>                                                                                                                                                    |
| <span id="TTDT_RESHOW"></span><span id="ttdt_reshow"></span><dl> <dt>**TTDT\_RESHOW**</dt> </dl>          | Set the amount of time it takes for subsequent tooltip windows to appear as the pointer moves from one tool to another. To return the reshow delay time to its default value, set *lParam* to -1.<br/>                                                                                                                                                           |
| <span id="TTDT_AUTOMATIC"></span><span id="ttdt_automatic"></span><dl> <dt>**TTDT\_AUTOMATIC**</dt> </dl> | Set all three delay times to default proportions. The autopop time will be ten times the initial time and the reshow time will be one fifth the initial time. If this flag is set, use a positive value of *lParam* to specify the initial time, in milliseconds. Set *lParam* to a negative value to return all three delay times to their default values.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies the delay time, in milliseconds. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) must be zero.

</dd> </dl>

## Return value

The return value for this message is not used.

## Remarks

The default delay times are based on the double-click time. For the default double-click time of 500 ms, the initial, autopop, and reshow delay times are 500ms, 5000ms, and 100ms respectively. The following code fragment uses the [**GetDoubleClickTime**](/windows/desktop/api/winuser/nf-winuser-getdoubleclicktime) function to determine the three delay times for any system.


```
initial = GetDoubleClickTime();

autopop = GetDoubleClickTime() * 10;

reshow = GetDoubleClickTime() / 5;
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TTM\_GETDELAYTIME**](ttm-getdelaytime.md)
</dt> </dl>

 

