---
title: PBM_GETBKCOLOR message (Commctrl.h)
description: Gets the background color of the progress bar.
ms.assetid: 9526ed78-08d9-468f-831b-72bb7c8c92d1
keywords:
- PBM_GETBKCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- PBM_GETBKCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PBM\_GETBKCOLOR message

Gets the background color of the progress bar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the background color of the progress bar.

## Remarks

This is the color set by the [**PBM\_SETBKCOLOR**](pbm-setbkcolor.md) message. The default value is CLR\_DEFAULT, which is defined in commctrl.h.

This function only affects the classic mode, not any visual style.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





