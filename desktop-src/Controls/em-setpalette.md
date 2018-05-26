---
title: EM\_SETPALETTE message
description: Changes the palette that a rich edit control uses for its display window.
ms.assetid: c1dc0c24-eaf2-47a8-9bb1-59f37b206feb
keywords:
- EM_SETPALETTE message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETPALETTE
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

# EM\_SETPALETTE message

Changes the palette that a rich edit control uses for its display window.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Handle to the new palette used by the rich edit control.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

The rich edit control does not check whether the new palette is valid.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

 





