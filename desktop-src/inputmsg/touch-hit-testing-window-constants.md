---
title: Touch Hit Testing Window Constants
description: Indicates how messages for touch hit testing are processed by windows that are registered through the RegisterTouchHitTestingWindow function.
ms.assetid: CC6CCD0B-882F-4DA7-B886-D4BD18D6060C
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
ms.topic: article
ms.date: 02/03/2020
---

# Touch Hit Testing Window Constants

Indicates how messages for touch hit testing are processed by windows that are registered through the [**RegisterTouchHitTestingWindow**](/windows/win32/api/winuser/nf-winuser-registertouchhittestingwindow) function.



| Constant/value                                                                                                                                                                                                                                                   | Description                                                                                                                            |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TOUCH_HIT_TESTING_DEFAULT"></span><span id="touch_hit_testing_default"></span><dl> <dt>**TOUCH_HIT_TESTING_DEFAULT**</dt> <dt>0 (0x0)</dt> </dl> | [**WM_TOUCHHITTESTING**](wm-touchhittesting.md) messages are not sent to the target window but are sent to child windows.<br/> |
| <span id="TOUCH_HIT_TESTING_CLIENT"></span><span id="touch_hit_testing_client"></span><dl> <dt>**TOUCH_HIT_TESTING_CLIENT**</dt> <dt>1 (0x1)</dt> </dl>    | [**WM_TOUCHHITTESTING**](wm-touchhittesting.md) messages are sent to the target window.<br/>                                   |
| <span id="TOUCH_HIT_TESTING_NONE"></span><span id="touch_hit_testing_none"></span><dl> <dt>**TOUCH_HIT_TESTING_NONE**</dt> <dt>2 (0x2)</dt> </dl>          | [**WM_TOUCHHITTESTING**](wm-touchhittesting.md) messages are not sent to the target window or child windows.<br/>              |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



## See also

<dl> <dt>

[Constants](constants.md)
</dt> <dt>

[**POINTER_INFO**](/windows/win32/api/winuser/ns-winuser-pointer_info)
</dt> </dl>

 

