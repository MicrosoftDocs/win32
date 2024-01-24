---
title: TB_SETBUTTONINFO message (Commctrl.h)
description: Sets the information for an existing button in a toolbar.
ms.assetid: ac9b88b9-d0d0-4669-a342-708924d97c8b
keywords:
- TB_SETBUTTONINFO message Windows Controls
topic_type:
- apiref
api_name:
- TB_SETBUTTONINFO
- TB_SETBUTTONINFOA
- TB_SETBUTTONINFOW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_SETBUTTONINFO message

Sets the information for an existing button in a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Button identifier.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TBBUTTONINFO**](/windows/desktop/api/Commctrl/ns-commctrl-tbbuttoninfoa) structure that contains the new button information. The **cbSize** and **dwMask** members of this structure must be filled in prior to sending this message.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Remarks

Text is commonly assigned to buttons when they are added to a toolbar by specifying the index of a string in the toolbar's string pool. If you use a **TB\_SETBUTTONINFO** to assign new text to a button, it will permanently override the text from the string pool. You can change the text by calling **TB\_SETBUTTONINFO** again, but you cannot reassign the string from the string pool.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TB\_SETBUTTONINFOW** (Unicode) and **TB\_SETBUTTONINFOA** (ANSI)<br/>         |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TB\_ADDBUTTONS**](tb-addbuttons.md)
</dt> <dt>

[**TB\_GETBUTTONINFO**](tb-getbuttoninfo.md)
</dt> <dt>

[**TB\_GETBUTTONTEXT**](tb-getbuttontext.md)
</dt> <dt>

[**TB\_GETSTRING**](tb-getstring.md)
</dt> <dt>

[**TB\_INSERTBUTTON**](tb-insertbutton.md)
</dt> </dl>

 

 





