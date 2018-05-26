---
title: PGM\_GETBUTTONSIZE message
description: Retrieves the current button size for the pager control. You can send this message explicitly or use the Pager\_GetButtonSize macro.
ms.assetid: fa8b4814-4587-4149-83a7-84faad2a4641
keywords:
- PGM_GETBUTTONSIZE message Windows Controls
topic_type:
- apiref
api_name:
- PGM_GETBUTTONSIZE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PGM\_GETBUTTONSIZE message

Retrieves the current button size for the pager control. You can send this message explicitly or use the [**Pager\_GetButtonSize**](/windows/win32/Commctrl/nf-commctrl-pager_getbuttonsize?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns an INT value that contains the current button size, in pixels.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**PGM\_SETBUTTONSIZE**](pgm-setbuttonsize.md)
</dt> </dl>

 

 





