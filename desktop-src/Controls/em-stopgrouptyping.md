---
title: EM_STOPGROUPTYPING message (Richedit.h)
description: Stops a rich edit control from collecting additional typing actions into the current undo action. The control stores the next typing action, if any, into a new action in the undo queue.
ms.assetid: 3059826f-84d1-4b7b-b4a8-da17d5f41013
keywords:
- EM_STOPGROUPTYPING message Windows Controls
topic_type:
- apiref
api_name:
- EM_STOPGROUPTYPING
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_STOPGROUPTYPING message

Stops a rich edit control from collecting additional typing actions into the current undo action. The control stores the next typing action, if any, into a new action in the undo queue.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

The return value is zero. This message cannot fail.

## Remarks

A rich edit control groups consecutive typing actions, including characters deleted by using the **BackSpace** key, into a single undo action until one of the following events occurs:

-   The control receives an **EM\_STOPGROUPTYPING** message.
-   The control loses focus.
-   The user moves the current selection, either by using the arrow keys or by clicking the mouse.
-   The user presses the **Delete** key.
-   The user performs any other action, such as a paste operation that does **not** involve typing.

You can send the **EM\_STOPGROUPTYPING** message to break consecutive typing actions into smaller undo groups. For example, you could send **EM\_STOPGROUPTYPING** after each character or at each word break.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_UNDO**](em-undo.md)
</dt> </dl>

 

 





