---
title: EM\_HIDESELECTION message
description: The EM\_HIDESELECTION message hides or shows the selection in a rich edit control.
ms.assetid: '1245618f-c9e6-4876-9133-6009370cdb97'
keywords: ["EM_HIDESELECTION message Windows Controls"]
topic_type:
- apiref
api_name:
- EM_HIDESELECTION
api_location:
- Richedit.h
api_type:
- HeaderDef
---

# EM\_HIDESELECTION message

The **EM\_HIDESELECTION** message hides or shows the selection in a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Value specifying whether to hide or show the selection. If this parameter is zero, the selection is shown. Otherwise, the selection is hidden.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> </dl>

## Return value

This message does not return a value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

 





