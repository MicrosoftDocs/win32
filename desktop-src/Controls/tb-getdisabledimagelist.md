---
title: TB_GETDISABLEDIMAGELIST message (Commctrl.h)
description: Retrieves the image list that a toolbar control uses to display inactive buttons.
ms.assetid: 8f6782d5-488b-4906-908a-e4bf8d512e0a
keywords:
- TB_GETDISABLEDIMAGELIST message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETDISABLEDIMAGELIST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETDISABLEDIMAGELIST message

Retrieves the image list that a toolbar control uses to display inactive buttons.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle to the inactive image list, or **NULL** if no inactive image list is set.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





