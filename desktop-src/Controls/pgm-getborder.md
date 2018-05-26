---
title: PGM\_GETBORDER message
description: Retrieves the current border size for the pager control. You can send this message explicitly or use the Pager\_GetBorder macro.
ms.assetid: 5d2f49ad-d940-4a0b-b5a0-05d742151b1c
keywords:
- PGM_GETBORDER message Windows Controls
topic_type:
- apiref
api_name:
- PGM_GETBORDER
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

# PGM\_GETBORDER message

Retrieves the current border size for the pager control. You can send this message explicitly or use the [**Pager\_GetBorder**](/windows/win32/Commctrl/nf-commctrl-pager_getborder?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns an INT value that contains the current border size, in pixels.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**PGM\_SETBORDER**](pgm-setborder.md)
</dt> </dl>

 

 





