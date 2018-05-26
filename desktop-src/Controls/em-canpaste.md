---
title: EM\_CANPASTE message
description: Determines whether a rich edit control can paste a specified clipboard format.
ms.assetid: 1b858ad8-1312-407b-b12a-c63668ba9f72
keywords:
- EM_CANPASTE message Windows Controls
topic_type:
- apiref
api_name:
- EM_CANPASTE
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

# EM\_CANPASTE message

Determines whether a rich edit control can paste a specified clipboard format.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the [Clipboard Formats](https://msdn.microsoft.com/library/windows/desktop/ms649013) to try. To try any format currently on the clipboard, set this parameter to zero.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> </dl>

## Return value

If the clipboard format can be pasted, the return value is a nonzero value.

If the clipboard format cannot be pasted, the return value is zero.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**SendMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644950)
</dt> </dl>

 

 





