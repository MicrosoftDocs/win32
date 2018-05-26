---
title: MCM\_GETCALENDARGRIDINFO message
description: Gets information about a calendar grid.
ms.assetid: 6b385362-f963-4041-bc9f-d2b7a890c9b4
keywords:
- MCM_GETCALENDARGRIDINFO message Windows Controls
topic_type:
- apiref
api_name:
- MCM_GETCALENDARGRIDINFO
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

# MCM\_GETCALENDARGRIDINFO message

Gets information about a calendar grid.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**MCGRIDINFO**](/windows/win32/Commctrl/ns-commctrl-tagmcgridinfo?branch=master) structure that contains information about the calendar grid.

</dd> </dl>

## Return value

**TRUE** if successful, otherwise **FALSE**.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





