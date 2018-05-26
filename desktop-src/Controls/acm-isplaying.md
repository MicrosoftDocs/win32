---
title: ACM\_ISPLAYING message
description: Checks whether an Audio-Video Interleaved (AVI) clip is playing. You can send this message explicitly or use the Animate\_IsPlaying macro.
ms.assetid: ebb0c92a-99d2-49c1-9de1-8bdbd032be3a
keywords:
- ACM_ISPLAYING message Windows Controls
topic_type:
- apiref
api_name:
- ACM_ISPLAYING
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

# ACM\_ISPLAYING message

Checks whether an Audio-Video Interleaved (AVI) clip is playing. You can send this message explicitly or use the [**Animate\_IsPlaying**](/windows/win32/Commctrl/nf-commctrl-animate_isplaying?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





