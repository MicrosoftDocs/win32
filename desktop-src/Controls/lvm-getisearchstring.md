---
title: LVM_GETISEARCHSTRING message (Commctrl.h)
description: Retrieves the incremental search string of a list-view control. You can send this message explicitly or by using the ListView\_GetISearchString macro.
ms.assetid: e953c4a0-0556-4987-8abf-3276e787fe49
keywords:
- LVM_GETISEARCHSTRING message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETISEARCHSTRING
- LVM_GETISEARCHSTRINGA
- LVM_GETISEARCHSTRINGW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETISEARCHSTRING message

Retrieves the incremental search string of a list-view control. You can send this message explicitly or by using the [**ListView\_GetISearchString**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getisearchstring) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a buffer that receives the incremental search string. To just retrieve the length of the string, set *lParam* to **NULL**.

</dd> </dl>

## Return value

Returns the number of characters in the incremental search string, not including the terminating NULL character, or zero if the list-view control is not in incremental search mode.

## Remarks

**Security Warning:** Using this message incorrectly might compromise the security of your program. This message does not provide a way for you to know the size of the buffer. If you use this message, first call the message passing **NULL** in the *lParam*, this returns the number of characters, excluding **NULL** that are required. Then call the message a second time to retrieve the string. You should review the [Security Considerations: Microsoft Windows Controls](sec-comctls.md) before continuing.

The *incremental search string* is the character sequence that the user types while the list view has the input focus. Each time the user types a character, the system appends the character to the search string and then searches for a matching item. If the system finds a match, it selects the item and, if necessary, scrolls it into view.

A time-out period is associated with each character that the user types. If the time-out period elapses before the user types another character, the incremental search string is reset.

Make sure that the buffer is large enough to hold the string and the terminating NULL character. If it is too small, an immediate invalid page fault will result.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVM\_GETISEARCHSTRINGW** (Unicode) and **LVM\_GETISEARCHSTRINGA** (ANSI)<br/> |



 

 





