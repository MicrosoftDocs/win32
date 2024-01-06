---
title: HKM_GETHOTKEY message (Commctrl.h)
description: Gets the virtual key code and modifier flags of a hot key from a hot key control.
ms.assetid: 8b061411-604d-46ea-a082-3eca2d47d992
keywords:
- HKM_GETHOTKEY message Windows Controls
topic_type:
- apiref
api_name:
- HKM_GETHOTKEY
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HKM\_GETHOTKEY message

Gets the virtual key code and modifier flags of a hot key from a hot key control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the virtual key code and modifier flags. The [**LOBYTE**](../winmsg/lobyte.md) of the [**LOWORD**](../winmsg/loword.md) is the virtual key code of the hot key. The [**HIBYTE**](../winmsg/hibyte.md) of the **LOWORD** is the key modifier that specifies the keys that define a hot key combination. The modifier flags can be a combination of the following values.

| Value            | Meaning      |
|------------------|--------------|
| HOTKEYF\_ALT     | ALT key      |
| HOTKEYF\_CONTROL | CONTROL key  |
| HOTKEYF\_EXT     | Extended key |
| HOTKEYF\_SHIFT   | SHIFT key    |

## Remarks

The 16-bit value returned by this message can be used as the *wParam* parameter in the [**WM\_SETHOTKEY**](/windows/desktop/inputdev/wm-sethotkey) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

