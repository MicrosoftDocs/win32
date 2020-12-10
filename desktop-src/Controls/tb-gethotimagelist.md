---
title: TB_GETHOTIMAGELIST message (Commctrl.h)
description: Retrieves the image list that a toolbar control uses to display hot buttons.
ms.assetid: 63054449-2768-459c-933c-781d31bdcc15
keywords:
- TB_GETHOTIMAGELIST message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETHOTIMAGELIST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETHOTIMAGELIST message

Retrieves the image list that a toolbar control uses to display hot buttons.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle to the image list that the control uses to display hot buttons, or **NULL** if no hot image list is set.

## Remarks

A button is hot when the cursor is over it. Toolbar controls must have the [**TBSTYLE\_FLAT**](toolbar-control-and-button-styles.md) or [**TBSTYLE\_LIST**](toolbar-control-and-button-styles.md) style to have hot items.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





