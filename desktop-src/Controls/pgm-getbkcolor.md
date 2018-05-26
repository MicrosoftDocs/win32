---
title: PGM\_GETBKCOLOR message
description: Retrieves the current background color for the pager control. You can send this message explicitly or use the Pager\_GetBkColor macro.
ms.assetid: c39ad721-fe39-44e9-8305-67444acc5d65
keywords:
- PGM_GETBKCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- PGM_GETBKCOLOR
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

# PGM\_GETBKCOLOR message

Retrieves the current background color for the pager control. You can send this message explicitly or use the [**Pager\_GetBkColor**](/windows/win32/Commctrl/nf-commctrl-pager_getbkcolor?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a **COLORREF** value that contains the current background color.

## Remarks

By default, the pager control will use the system button face color as the background color. This is the same color that can be retrieved by calling [**GetSysColorBrush**](https://msdn.microsoft.com/library/windows/desktop/dd144927) with COLOR\_BTNFACE.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





