---
title: EM\_EXGETSEL message
description: Retrieves the starting and ending character positions of the selection in a rich edit control.
ms.assetid: 60fcf13e-6c45-4f4e-9b54-70f0985122fb
keywords:
- EM_EXGETSEL message Windows Controls
topic_type:
- apiref
api_name:
- EM_EXGETSEL
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EM\_EXGETSEL message

Retrieves the starting and ending character positions of the selection in a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A [**CHARRANGE**](/windows/win32/Richedit/ns-richedit-_charrange?branch=master) structure that receives the selection range.

</dd> </dl>

## Return value

This message does not return a value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**CHARRANGE**](/windows/win32/Richedit/ns-richedit-_charrange?branch=master)
</dt> </dl>

 

 





