---
title: TB_SETANCHORHIGHLIGHT message (Commctrl.h)
description: Sets the anchor highlight setting for a toolbar.
ms.assetid: d31652d5-e9cf-4bf3-8f90-818eb078fa87
keywords:
- TB_SETANCHORHIGHLIGHT message Windows Controls
topic_type:
- apiref
api_name:
- TB_SETANCHORHIGHLIGHT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_SETANCHORHIGHLIGHT message

Sets the anchor highlight setting for a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

**BOOL** value that specifies if anchor highlighting is enabled or disabled. If this value is nonzero, anchor highlighting will be enabled. If this value is zero, anchor highlighting will be disabled.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the previous anchor highlight setting. If this value is nonzero, anchor highlighting was enabled. If this value is zero, anchor highlighting was disabled.

## Remarks

Anchor highlighting in a toolbar means that the last highlighted item will remain highlighted until another item is highlighted. This occurs even if the cursor leaves the toolbar control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





