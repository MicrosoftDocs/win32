---
title: TB\_SETROWS message
description: Sets the number of rows of buttons in a toolbar.
ms.assetid: 'd8ea7b80-d23e-4593-8eb1-d23808173fc9'
keywords: ["TB_SETROWS message Windows Controls"]
topic_type:
- apiref
api_name:
- TB_SETROWS
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# TB\_SETROWS message

Sets the number of rows of buttons in a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) specifies the number of rows requested. The minimum number of rows is one, and the maximum number of rows is equal to the number of buttons in the toolbar.

The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) is a **BOOL** that indicates whether to create more rows than requested when the system cannot create the number of rows specified by *wParam*. If **TRUE**, the system creates more rows. If **FALSE**, the system creates fewer rows.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897) structure that receives the bounding rectangle of the toolbar after the rows are set.

</dd> </dl>

## Return value

No return value.

## Remarks

Because the system does not break up button groups when setting the number of rows, the resulting number of rows might differ from the number requested.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





