---
title: PBM_STEPIT message (Commctrl.h)
description: Advances the current position for a progress bar by the step increment and redraws the bar to reflect the new position. An application sets the step increment by sending the PBM\_SETSTEP message.
ms.assetid: fd9947f6-7a48-4207-b691-b7db78eb8a85
keywords:
- PBM_STEPIT message Windows Controls
topic_type:
- apiref
api_name:
- PBM_STEPIT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PBM\_STEPIT message

Advances the current position for a progress bar by the step increment and redraws the bar to reflect the new position. An application sets the step increment by sending the [**PBM\_SETSTEP**](pbm-setstep.md) message.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the previous position.

## Remarks

When the position exceeds the maximum range value, this message resets the current position so that the progress indicator starts over again from the beginning.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





