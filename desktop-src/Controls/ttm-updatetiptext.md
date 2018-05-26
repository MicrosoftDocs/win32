---
title: TTM\_UPDATETIPTEXT message
description: Sets the tooltip text for a tool.
ms.assetid: 2a7432dd-76f9-42b4-b639-178dce1d89ef
keywords:
- TTM_UPDATETIPTEXT message Windows Controls
topic_type:
- apiref
api_name:
- TTM_UPDATETIPTEXT
- TTM_UPDATETIPTEXTA
- TTM_UPDATETIPTEXTW
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

# TTM\_UPDATETIPTEXT message

Sets the tooltip text for a tool.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TOOLINFO**](/windows/win32/Commctrl/ns-commctrl-tagtoolinfoa?branch=master) structure. The **hinst** and **lpszText** members must specify the instance handle and the address of the text. The **hwnd** and **uId** members identify the tool to update. The **cbSize** member of this structure must be filled in before sending this message.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TTM\_UPDATETIPTEXTW** (Unicode) and **TTM\_UPDATETIPTEXTA** (ANSI)<br/>       |



 

 





