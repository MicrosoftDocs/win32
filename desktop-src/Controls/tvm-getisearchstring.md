---
title: TVM_GETISEARCHSTRING message (Commctrl.h)
description: Retrieves the incremental search string for a tree-view control.
ms.assetid: 71f9a9b6-e124-4655-80fc-dd23f441496d
keywords:
- TVM_GETISEARCHSTRING message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETISEARCHSTRING
- TVM_GETISEARCHSTRINGA
- TVM_GETISEARCHSTRINGW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_GETISEARCHSTRING message

Retrieves the incremental search string for a tree-view control. The tree-view control uses the incremental search string to select an item based on characters typed by the user. You can send this message explicitly or by using the [**TreeView\_GetISearchString**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getisearchstring) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to the buffer that receives the incremental search string.

</dd> </dl>

## Return value

Returns the number of characters in the incremental search string.

## Remarks

**Security Warning:** Using this message incorrectly might compromise the security of your program. You must allocate a large enough buffer to hold the string. First call the message passing **NULL** in *lParam*. This returns the number of characters, excluding **NULL**, that are required. Then call the message a second time to retrieve the string. You should review [Security Considerations: Microsoft Windows Controls](sec-comctls.md) before continuing.

If the tree-view control is not in incremental search mode, the return value is zero.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVM\_GETISEARCHSTRINGW** (Unicode) and **TVM\_GETISEARCHSTRINGA** (ANSI)<br/> |



 

 





