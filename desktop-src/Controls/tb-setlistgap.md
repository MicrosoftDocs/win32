---
title: TB_SETLISTGAP message (Commctrl.h)
description: Sets the distance between the toolbar buttons on a specific toolbar.
ms.assetid: ca8ba6e4-cf70-41ca-ac61-cd13671d4010
keywords:
- TB_SETLISTGAP message Windows Controls
topic_type:
- apiref
api_name:
- TB_SETLISTGAP
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_SETLISTGAP message

Sets the distance between the toolbar buttons on a specific toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The gap, in pixels, between buttons on the toolbar.

</dd> <dt>

*lParam* 
</dt> <dd>

Ignored.

</dd> </dl>

## Return value

No return value.

## Remarks

The gap between buttons only applies to the toolbar control window that receives this message. Receipt of this message triggers a repaint of the toolbar, if the toolbar is currently visible.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





