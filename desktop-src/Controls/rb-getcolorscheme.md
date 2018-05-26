---
title: RB\_GETCOLORSCHEME message
description: Retrieves the color scheme information from the rebar control.
ms.assetid: 01f81c4b-bbc9-43ae-a1f5-1e289c6fa278
keywords:
- RB_GETCOLORSCHEME message Windows Controls
topic_type:
- apiref
api_name:
- RB_GETCOLORSCHEME
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

# RB\_GETCOLORSCHEME message

Retrieves the color scheme information from the rebar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**COLORSCHEME**](/windows/win32/Commctrl/ns-commctrl-tagcolorscheme?branch=master) structure that will receive the color scheme information. You must set the **dwSize** member of this structure to **sizeof**(COLORSCHEME) before sending this message.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**RB\_SETCOLORSCHEME**](rb-setcolorscheme.md)
</dt> </dl>

 

 





