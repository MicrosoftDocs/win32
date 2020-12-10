---
title: EM_FILELINEFROMCHAR message (CommCtrl.h)
description: Gets the index of the line that contains the specified character index in a multiline edit control, independently of how lines are displayed on the screen.
ms.assetid: e8e9217b-3f0c-478d-b44d-2a51868dbc5a
keywords:
- EM_FILELINEFROMCHAR message Windows Controls
topic_type:
- apiref
api_name:
- EM_FILELINEFROMCHAR
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_FILELINEFROMCHAR message

Gets the index of the line that contains the specified character index in a multiline edit control, independently of how lines are displayed on the screen. A character index is the zero-based index of the character from the beginning of the edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The character index of the character contained in the line whose number is to be retrieved. If this parameter is -1, **EM\_FILELINEFROMCHAR** retrieves either the line number of the current line (the line containing the caret) or, if there is a selection, the line number of the line containing the beginning of the selection.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is the zero-based line number of the line containing the character index specified by *wParam*, independently of how lines are displayed on the screen.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, 1809 \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2019 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>CommCtrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_FILELINEINDEX**](em-filelineindex.md)
</dt> </dl>

 

 





