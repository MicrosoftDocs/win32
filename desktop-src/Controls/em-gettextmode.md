---
title: EM_GETTEXTMODE message
description: Gets the current text mode and undo level of a rich edit control.
ms.assetid: 5c976a82-9c51-4700-9db4-a6b0ed7bb852
keywords:
- EM_GETTEXTMODE message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETTEXTMODE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EM\_GETTEXTMODE message

Gets the current text mode and undo level of a rich edit control.

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

The return value is one or more values from the [**TEXTMODE**](/windows/desktop/api/Richedit/ne-richedit-tagtextmode) enumeration type. The values indicate the current text mode and undo level of the control.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_SETTEXTMODE**](em-settextmode.md)
</dt> <dt>

[**TEXTMODE**](/windows/desktop/api/Richedit/ne-richedit-tagtextmode)
</dt> </dl>

 

 





