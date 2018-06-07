---
title: RB\_HITTEST message
description: Determines which portion of a rebar band is at a given point on the screen, if a rebar band exists at that point.
ms.assetid: 8f27db21-50d8-438f-a44c-2e65dd93fa2a
keywords:
- RB_HITTEST message Windows Controls
topic_type:
- apiref
api_name:
- RB_HITTEST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RB\_HITTEST message

Determines which portion of a rebar band is at a given point on the screen, if a rebar band exists at that point.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**RBHITTESTINFO**](/windows/desktop/api/Commctrl/ns-commctrl-_rb_hittestinfo) structure. Before sending the message, the **pt** member of this structure must be initialized to the point that will be hit tested, in client coordinates.

</dd> </dl>

## Return value

Returns the zero-based index of the band at the given point, or -1 if no rebar band was at the point.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





