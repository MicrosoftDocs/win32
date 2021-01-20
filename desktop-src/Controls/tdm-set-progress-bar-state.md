---
title: TDM_SET_PROGRESS_BAR_STATE message (Commctrl.h)
description: Sets the state of the progress bar in a task dialog.
ms.assetid: 8b0f2ee9-e6ca-4a5b-8687-6e2682eda7d0
keywords:
- TDM_SET_PROGRESS_BAR_STATE message Windows Controls
topic_type:
- apiref
api_name:
- TDM_SET_PROGRESS_BAR_STATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDM\_SET\_PROGRESS\_BAR\_STATE message

Sets the state of the progress bar in a task dialog.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

An **int** that specifies the state of the progress bar. This parameter can be one of the following values.



| Value                                                                                                                                                   | Meaning                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <span id="PBST_NORMAL"></span><span id="pbst_normal"></span><dl> <dt>**PBST\_NORMAL**</dt> </dl> | Sets the progress bar to the normal state.<br/> |
| <span id="PBST_PAUSED"></span><span id="pbst_paused"></span><dl> <dt>**PBST\_PAUSED**</dt> </dl>    | Sets the progress bar to the paused state.<br/> |
| <span id="PBST_ERROR"></span><span id="pbst_error"></span><dl> <dt>**PBST\_ERROR**</dt> </dl>    | Set the progress bar to the error state.<br/>   |



 

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

If the function succeeds, the return value is non zero.

If the function fails, the return value is zero. To get extended error information call GetLastError.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





