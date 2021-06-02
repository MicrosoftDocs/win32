---
title: TB_SETHOTITEM2 message (Commctrl.h)
description: TB_SETHOTITEM2 message - Sets the hot item in a toolbar.
ms.assetid: 43666b1d-1197-452f-aa79-eb0a1a23e5b7
keywords:
- TB_SETHOTITEM2 message Windows Controls
topic_type:
- apiref
api_name:
- TB_SETHOTITEM2
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_SETHOTITEM2 message

Sets the hot item in a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the item that will be made hot. If this value is -1, none of the items will be hot.

</dd> <dt>

*lParam* 
</dt> <dd>A combination of HICF\_xxx flags. See <a href="/windows/win32/api/commctrl/ns-commctrl-nmtbhotitem">**NMTBHOTITEM**</a>.</dd> </dl>

## Return value

Returns the index of the previous hot item, or -1 if there was no hot item.

## Remarks

The behavior of this message is not defined for toolbars that do not have the [**TBSTYLE\_FLAT**](toolbar-control-and-button-styles.md) style.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





