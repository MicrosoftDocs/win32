---
title: Touch Hit Testing Behaviors
description: The following constants are used by applications or UI frameworks to identify how messages for touch hit testing are processed by windows that are registered through the RegisterTouchHitTestingWindow function.
ms.assetid: D1ECCBFA-CD01-401E-A42E-4F954F5F0A32
topic_type:
- apiref
api_name:
- TOUCH_HIT_TESTING_DEFAULT
- TOUCH_HIT_TESTING_CLIENT
- TOUCH_HIT_TESTING_NONE
api_location:
- winuser.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Touch Hit Testing Behaviors

The following constants are used by applications or UI frameworks to identify how messages for touch hit testing are processed by windows that are registered through the [**RegisterTouchHitTestingWindow**](https://msdn.microsoft.com/library/windows/desktop/hh437252) function.



| Constant/value                                                                                                                                                                                                                                                   | Description                                                                                                                                                |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TOUCH_HIT_TESTING_DEFAULT"></span><span id="touch_hit_testing_default"></span><dl> <dt>**TOUCH\_HIT\_TESTING\_DEFAULT**</dt> <dt>0 (0x0)</dt> </dl> | Indicates that [**WM\_TOUCHHITTESTING**](https://msdn.microsoft.com/library/windows/desktop/hh454931) messages are not sent to the target window but are sent to child windows.<br/> |
| <span id="TOUCH_HIT_TESTING_CLIENT"></span><span id="touch_hit_testing_client"></span><dl> <dt>**TOUCH\_HIT\_TESTING\_CLIENT**</dt> <dt>1 (0x1)</dt> </dl>    | Indicates that [**WM\_TOUCHHITTESTING**](https://msdn.microsoft.com/library/windows/desktop/hh454931) messages are sent to the target window.<br/>                                   |
| <span id="TOUCH_HIT_TESTING_NONE"></span><span id="touch_hit_testing_none"></span><dl> <dt>**TOUCH\_HIT\_TESTING\_NONE**</dt> <dt>2 (0x2)</dt> </dl>          | Indicates that [**WM\_TOUCHHITTESTING**](https://msdn.microsoft.com/library/windows/desktop/hh454931) messages are not sent to the target window or child windows.<br/>              |



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



## See also

<dl> <dt>

[Constants](constants.md)
</dt> </dl>

 

 





