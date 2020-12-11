---
title: PBM_SETMARQUEE message (Commctrl.h)
description: Sets the progress bar to marquee mode. This causes the progress bar to move like a marquee.
ms.assetid: 6501bcb9-a711-470f-874f-f3484d3613b6
keywords:
- PBM_SETMARQUEE message Windows Controls
topic_type:
- apiref
api_name:
- PBM_SETMARQUEE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PBM\_SETMARQUEE message

Sets the progress bar to marquee mode. This causes the progress bar to move like a marquee.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Indicates whether to turn the marquee mode on or off.

</dd> <dt>

*lParam* 
</dt> <dd>Time, in milliseconds, between marquee animation updates. If this parameter is zero, the marquee animation is updated every 30 milliseconds.</dd> </dl>

## Return value

Always returns **TRUE**.

## Remarks

Use this message when you do not know the amount of progress toward completion but wish to indicate that progress is being made.

Send the **PBM\_SETMARQUEE** message to start or stop the animation.

> [!Note]  
> You must set the control style to [**PBS\_MARQUEE**](progress-bar-control-styles.md) before attempting to start the animation.

 

> [!Note]  
> This message requires ComCtl32.dll version 6.00 or later.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





