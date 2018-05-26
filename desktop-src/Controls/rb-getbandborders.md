---
title: RB\_GETBANDBORDERS message
description: Retrieves the borders of a band. The result of this message can be used to calculate the usable area in a band.
ms.assetid: 45f2ae7e-636e-474b-a0d0-5235c6401e6a
keywords:
- RB_GETBANDBORDERS message Windows Controls
topic_type:
- apiref
api_name:
- RB_GETBANDBORDERS
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

# RB\_GETBANDBORDERS message

Retrieves the borders of a band. The result of this message can be used to calculate the usable area in a band.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the band for which the borders will be retrieved.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897) structure that will receive the band borders. If the rebar control has the [**RBS\_BANDBORDERS**](rebar-control-styles.md#rbs-bandborders) style, each member of this structure will receive the number of pixels, on the corresponding side of the band, that constitute the border. If the rebar control does not have the **RBS\_BANDBORDERS** style, only the **left** member of this structure receives valid information.

</dd> </dl>

## Return value

The return value is not used.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





