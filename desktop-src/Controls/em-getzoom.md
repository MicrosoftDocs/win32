---
title: EM\_GETZOOM message
description: Gets the current zoom ratio of a rich edit control. The zoom ration is always between 1/64 and 64.
ms.assetid: d4a1daee-4af7-44d1-80d6-0fcaaf3672a8
keywords:
- EM_GETZOOM message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETZOOM
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EM\_GETZOOM message

Gets the current zoom ratio of a rich edit control. The zoom ration is always between 1/64 and 64.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Receives the numerator of the zoom ratio.

</dd> <dt>

*lParam* 
</dt> <dd>

Receives the denominator of the zoom ratio.

</dd> </dl>

## Return value

The message returns **TRUE** if message is processed, which it will be if both *wParam* and *lParam* are not **NULL**.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | Rich Edit 3.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_SETZOOM**](em-setzoom.md)
</dt> </dl>

 

 





