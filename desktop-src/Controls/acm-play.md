---
title: ACM_PLAY message (Commctrl.h)
description: Plays an AVI clip in an animation control. The control plays the clip in the background while the thread continues executing. You can send this message explicitly or by using the Animate\_Play macro.
ms.assetid: 738b7305-bb77-441d-a198-17daf3b76039
keywords:
- ACM_PLAY message Windows Controls
topic_type:
- apiref
api_name:
- ACM_PLAY
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ACM\_PLAY message

Plays an AVI clip in an animation control. The control plays the clip in the background while the thread continues executing. You can send this message explicitly or by using the [**Animate\_Play**](/windows/desktop/api/Commctrl/nf-commctrl-animate_play) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A **UINT** that specifies the number of times to replay the AVI clip. A value of -1 means replay the clip indefinitely.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is the zero-based index of the frame where playing begins. The value must be less than 65,536. A value of zero means begin with the first frame in the AVI clip.

The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) is the zero-based index of the frame where playing ends. The value must be less than 65,536. A value of -1 means end with the last frame in the AVI clip.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Remarks

You can use [**Animate\_Seek**](/windows/desktop/api/Commctrl/nf-commctrl-animate_seek) to direct the animation control to display a particular frame of the AVI clip.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

