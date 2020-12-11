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
ms.topic: article
ms.date: 02/07/2020
---

# Touch Hit Testing Behaviors

The following constants are used by applications or UI frameworks to identify how messages for touch hit testing are processed by windows that are registered through the [**RegisterTouchHitTestingWindow**](/windows/win32/api/winuser/nf-winuser-registertouchhittestingwindow) function.

| Constant/value | Description |
|---|---|
| **TOUCH_HIT_TESTING_DEFAULT**</dt> <dt>0 (0x0) | Indicates that [WM_TOUCHHITTESTING](../inputmsg/wm-touchhittesting.md) messages are not sent to the target window but are sent to child windows.<br/> |
| **TOUCH_HIT_TESTING_CLIENT**</dt> <dt>1 (0x1)    | Indicates that [WM_TOUCHHITTESTING](../inputmsg/wm-touchhittesting.md) messages are sent to the target window.<br/>                                   |
| **TOUCH_HIT_TESTING_NONE**</dt> <dt>2 (0x2)          | Indicates that [WM_TOUCHHITTESTING](../inputmsg/wm-touchhittesting.md) messages are not sent to the target window or child windows.<br/>              |

## Requirements

| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Winuser.h |

## See also

<dl> <dt>

[Constants](constants.md)
