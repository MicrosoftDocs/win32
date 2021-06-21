---
title: LM_GETIDEALHEIGHT message (Commctrl.h)
description: LM_GETIDEALHEIGHT message - Retrieves the preferred height of a link for the control's current width.
ms.assetid: bf6ef3c1-89bc-4c56-9384-085fd00234e1
keywords:
- LM_GETIDEALHEIGHT message Windows Controls
topic_type:
- apiref
api_name:
- LM_GETIDEALHEIGHT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LM\_GETIDEALHEIGHT message

Retrieves the preferred height of a link for the control's current width.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Integer representing the preferred height of the link text, in pixels.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





