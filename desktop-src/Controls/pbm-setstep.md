---
title: PBM_SETSTEP message (Commctrl.h)
description: Specifies the step increment for a progress bar. The step increment is the amount by which the progress bar increases its current position whenever it receives a PBM\_STEPIT message. By default, the step increment is set to 10.
ms.assetid: 75c1085b-6c7a-4c44-9a12-f9bf21f7d945
keywords:
- PBM_SETSTEP message Windows Controls
topic_type:
- apiref
api_name:
- PBM_SETSTEP
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PBM\_SETSTEP message

Specifies the step increment for a progress bar. The step increment is the amount by which the progress bar increases its current position whenever it receives a [**PBM\_STEPIT**](pbm-stepit.md) message. By default, the step increment is set to 10.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

New step increment.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the previous step increment.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





