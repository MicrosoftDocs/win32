---
title: EM_SELECTIONTYPE message (Richedit.h)
description: Determines the selection type for a rich edit control.
ms.assetid: a4200e32-1056-47bd-be47-5fabaf99c058
keywords:
- EM_SELECTIONTYPE message Windows Controls
topic_type:
- apiref
api_name:
- EM_SELECTIONTYPE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SELECTIONTYPE message

Determines the selection type for a rich edit control.

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

If the selection is empty, the return value is SEL\_EMPTY.

If the selection is not empty, the return value is a set of flags containing one or more of the following values.



| Return code                                                                                     | Description                                 |
|-------------------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>**SEL\_TEXT**</dt> </dl>        | Text.<br/>                            |
| <dl> <dt>**SEL\_OBJECT**</dt> </dl>      | At least one COM object.<br/>         |
| <dl> <dt>**SEL\_MULTICHAR**</dt> </dl>   | More than one character of text.<br/> |
| <dl> <dt>**SEL\_MULTIOBJECT**</dt> </dl> | More than one COM object.<br/>        |



 

## Remarks

This message is useful during [**WM\_SIZE**](/windows/desktop/winmsg/wm-size) processing for the parent of a bottomless rich edit control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**WM\_SIZE**](/windows/desktop/winmsg/wm-size)
</dt> </dl>

 

