---
title: TB_BUTTONSTRUCTSIZE message (Commctrl.h)
description: Specifies the size of the TBBUTTON structure.
ms.assetid: 4e63a075-4191-44c1-8df6-38fce51d4be5
keywords:
- TB_BUTTONSTRUCTSIZE message Windows Controls
topic_type:
- apiref
api_name:
- TB_BUTTONSTRUCTSIZE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_BUTTONSTRUCTSIZE message

Specifies the size of the [**TBBUTTON**](/windows/desktop/api/Commctrl/ns-commctrl-tbbutton) structure.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Size, in bytes, of the [**TBBUTTON**](/windows/desktop/api/Commctrl/ns-commctrl-tbbutton) structure.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

No return value.

## Remarks

The system uses the size to determine which version of the common control dynamic-link library (DLL) is being used.

If an application uses the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function to create the toolbar, the application must send this message to the toolbar before sending the [**TB\_ADDBITMAP**](tb-addbitmap.md) or [**TB\_ADDBUTTONS**](tb-addbuttons.md) message. The [**CreateToolbarEx**](/windows/desktop/api/Commctrl/nf-commctrl-createtoolbarex) function automatically sends **TB\_BUTTONSTRUCTSIZE**, and the size of the [**TBBUTTON**](/windows/desktop/api/Commctrl/ns-commctrl-tbbutton) structure is a parameter of the function.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

