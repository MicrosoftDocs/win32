---
title: TB_GETINSERTMARK message (Commctrl.h)
description: Retrieves the current insertion mark for the toolbar.
ms.assetid: b22770a4-e859-451d-a726-279bbc49b984
keywords:
- TB_GETINSERTMARK message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETINSERTMARK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETINSERTMARK message

Retrieves the current insertion mark for the toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TBINSERTMARK**](/windows/desktop/api/Commctrl/ns-commctrl-tbinsertmark) structure that receives the insertion mark.

</dd> </dl>

## Return value

Always returns **TRUE**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TB\_SETINSERTMARK**](tb-setinsertmark.md)
</dt> </dl>

 

 





