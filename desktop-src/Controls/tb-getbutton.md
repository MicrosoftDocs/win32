---
title: TB\_GETBUTTON message
description: Retrieves information about the specified button in a toolbar.
ms.assetid: 'd90d053c-0daf-4a5a-b7ca-b9b4472c65a3'
keywords: ["TB_GETBUTTON message Windows Controls"]
topic_type:
- apiref
api_name:
- TB_GETBUTTON
api_location:
- Commctrl.h
api_type:
- HeaderDef
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

Pointer to the [**TBBUTTON**](tbbutton.md) structure that receives the button information.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





