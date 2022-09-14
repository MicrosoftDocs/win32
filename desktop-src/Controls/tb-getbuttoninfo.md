---
title: TB_GETBUTTONINFO message (Commctrl.h)
description: Retrieves extended information for a button in a toolbar.
ms.assetid: 87430dd2-43d1-4e33-96ac-d33f89a654b6
keywords:
- TB_GETBUTTONINFO message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETBUTTONINFO
- TB_GETBUTTONINFOA
- TB_GETBUTTONINFOW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETBUTTONINFO message

Retrieves extended information for a button in a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Command identifier of the button.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TBBUTTONINFO**](/windows/desktop/api/Commctrl/ns-commctrl-tbbuttoninfoa) structure that receives the button information. The **cbSize** and **dwMask** members of this structure must be filled in prior to sending this message.

</dd> </dl>

## Return value

Returns the zero-based index of the button, or -1 if an error occurs.

## Remarks

When you use [**TB\_ADDBUTTONS**](tb-addbuttons.md) or [**TB\_INSERTBUTTON**](tb-insertbutton.md) to place buttons on the toolbar, the button text is commonly specified by its string pool index. **TB\_GETBUTTONINFO** will not retrieve this string. To use **TB\_GETBUTTONINFO** to retrieve button text, you must first set the text string with [**TB\_SETBUTTONINFO**](tb-setbuttoninfo.md). Once you have set the button text with **TB\_SETBUTTONINFO**, you can no longer use the string pool index.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TB\_GETBUTTONINFOW** (Unicode) and **TB\_GETBUTTONINFOA** (ANSI)<br/>         |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TB\_SETBUTTONINFO**](tb-setbuttoninfo.md)
</dt> <dt>

[**TB\_GETBUTTONTEXT**](tb-getbuttontext.md)
</dt> </dl>

 

 





