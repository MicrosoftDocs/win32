---
title: TB\_COMMANDTOINDEX message
description: Retrieves the zero-based index for the button associated with the specified command identifier.
ms.assetid: '079d318e-56b2-4890-ac4a-c1798fc2f62a'
keywords: ["TB_COMMANDTOINDEX message Windows Controls"]
topic_type:
- apiref
api_name:
- TB_COMMANDTOINDEX
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# TB\_COMMANDTOINDEX message

Retrieves the zero-based index for the button associated with the specified command identifier.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Command identifier associated with the button.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the zero-based index for the button or -1 if the specified command identifier is invalid.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





