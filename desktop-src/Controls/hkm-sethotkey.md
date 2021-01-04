---
title: HKM_SETHOTKEY message (Commctrl.h)
description: Sets the hot key combination for a hot key control.
ms.assetid: 372a7b2f-d9d5-43a8-9c06-730f2f5dc56e
keywords:
- HKM_SETHOTKEY message Windows Controls
topic_type:
- apiref
api_name:
- HKM_SETHOTKEY
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HKM\_SETHOTKEY message

Sets the hot key combination for a hot key control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOBYTE**](/previous-versions/windows/desktop/legacy/ms632658(v=vs.85)) of the [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is the virtual key code of the hot key. The [**HIBYTE**](/previous-versions/windows/desktop/legacy/ms632656(v=vs.85)) of the **LOWORD** is the key modifier that indicates the keys that define a hot key combination. For a list of modifier flag values, see the description of the [**HKM\_GETHOTKEY**](hkm-gethotkey.md) message.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

Always returns zero.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

