---
title: RB_PUSHCHEVRON message (Commctrl.h)
description: Sent to a rebar control to programmatically push a chevron.
ms.assetid: 00a8ce10-1fb2-488a-a6f9-1814f73f82bd
keywords:
- RB_PUSHCHEVRON message Windows Controls
topic_type:
- apiref
api_name:
- RB_PUSHCHEVRON
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RB\_PUSHCHEVRON message

Sent to a rebar control to programmatically push a chevron.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the band whose chevron is to be pushed.

</dd> <dt>

*lParam* 
</dt> <dd>

An application defined 32-bit value. It will be passed back to the application as the **lParamNM** member of the [**NMREBARCHEVRON**](/windows/win32/api/commctrl/ns-commctrl-nmrebarchevron) structure that is passed with the [RBN\_CHEVRONPUSHED](rbn-chevronpushed.md) notification.

</dd> </dl>

## Return value

The return value for this message is not used.

## Remarks

When this message is sent, the rebar control will send the application an [RBN\_CHEVRONPUSHED](rbn-chevronpushed.md) notification code, prompting it to display the chevron menu.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





