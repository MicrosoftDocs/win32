---
title: TB_GETBUTTON message (Commctrl.h)
description: Retrieves information about the specified button in a toolbar.
ms.assetid: d90d053c-0daf-4a5a-b7ca-b9b4472c65a3
keywords:
- TB_GETBUTTON message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETBUTTON
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETBUTTON message

Retrieves information about the specified button in a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the button for which to retrieve information.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to the [**TBBUTTON**](/windows/desktop/api/Commctrl/ns-commctrl-tbbutton) structure that receives the button information.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





