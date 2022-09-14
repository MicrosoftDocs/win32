---
title: TB_GETIMAGELIST message (Commctrl.h)
description: Retrieves the image list that a toolbar control uses to display buttons in their default state. A toolbar control uses this image list to display buttons when they are not hot or disabled.
ms.assetid: 21edde99-019b-495c-a38b-4d686e124f8e
keywords:
- TB_GETIMAGELIST message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETIMAGELIST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETIMAGELIST message

Retrieves the image list that a toolbar control uses to display buttons in their default state. A toolbar control uses this image list to display buttons when they are not hot or disabled.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

Returns the handle to the image list, or **NULL** if no image list is set.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





