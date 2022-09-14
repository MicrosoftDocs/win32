---
title: TB_GETCOLORSCHEME message (Commctrl.h)
description: Retrieves the color scheme information from the toolbar control.
ms.assetid: af172631-309e-4181-a690-05946cd6e143
keywords:
- TB_GETCOLORSCHEME message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETCOLORSCHEME
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETCOLORSCHEME message

Retrieves the color scheme information from the toolbar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**COLORSCHEME**](/windows/win32/api/commctrl/ns-commctrl-colorscheme) structure that will receive the color scheme information. You must set the **cbSize** member of this structure to **sizeof**(COLORSCHEME) before sending this message.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TB\_SETCOLORSCHEME**](tb-setcolorscheme.md)
</dt> </dl>

 

 





