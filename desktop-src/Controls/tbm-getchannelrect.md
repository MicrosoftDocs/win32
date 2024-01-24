---
title: TBM_GETCHANNELRECT message (Commctrl.h)
description: Retrieves the size and position of the bounding rectangle for a trackbar's channel.
ms.assetid: 353edae3-1a26-4e85-8a32-ba8b5a976d24
keywords:
- TBM_GETCHANNELRECT message Windows Controls
topic_type:
- apiref
api_name:
- TBM_GETCHANNELRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_GETCHANNELRECT message

Retrieves the size and position of the bounding rectangle for a trackbar's channel. (The channel is the area over which the slider moves. It contains the highlight when a range is selected.)

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure. The message fills this structure with the channel's bounding rectangle, in client coordinates of the trackbar's window.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

