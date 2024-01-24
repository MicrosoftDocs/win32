---
title: RB_INSERTBAND message (Commctrl.h)
description: Inserts a new band in a rebar control.
ms.assetid: ac621f65-b8ab-41d6-928d-a48fbea572e7
keywords:
- RB_INSERTBAND message Windows Controls
topic_type:
- apiref
api_name:
- RB_INSERTBAND
- RB_INSERTBANDA
- RB_INSERTBANDW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RB\_INSERTBAND message

Inserts a new band in a rebar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the location where the band will be inserted. If you set this parameter to -1, the control will add the new band at the last location.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**REBARBANDINFO**](/windows/win32/api/commctrl/ns-commctrl-rebarbandinfoa) structure that defines the band to be inserted. You must set the **cbSize** member of this structure to **sizeof**(REBARBANDINFO) before sending this message.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **RB\_INSERTBANDW** (Unicode) and **RB\_INSERTBANDA** (ANSI)<br/>               |



 

 





