---
title: MPDETECTION_STATE enumeration (MpClient.h)
description: The state of the currently detected threat.
ms.assetid: 293771FF-A210-41D0-88A5-3B52ACAA9295
keywords:
- MPDETECTION_STATE enumeration Legacy Windows Environment Features
- PMPDETECTION_STATE enumeration pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPDETECTION_STATE
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPDETECTION\_STATE enumeration

The state of the currently detected threat.

## Syntax


```C++
typedef enum tagMPDETECTION_STATE { 
  MPDETECTION_STATE_UNKNOWN             = 0,
  MPDETECTION_STATE_ACTIVE              = 1,
  MPDETECTION_STATE_FINISHED            = 2,
  MPDETECTION_STATE_ADDITIONAL_ACTIONS  = 3,
  MPDETECTION_STATE_FAILED              = 4,
  MPDETECTION_STATE_CRITICALLY_FAILED   = 5,
  MPDETECTION_STATE_CLEARED             = 6
} MPDETECTION_STATE, *PMPDETECTION_STATE;
```



## Constants

<dl> <dt>

<span id="MPDETECTION_STATE_UNKNOWN"></span><span id="mpdetection_state_unknown"></span>**MPDETECTION\_STATE\_UNKNOWN**
</dt> <dd>

In an error state.

</dd> <dt>

<span id="MPDETECTION_STATE_ACTIVE"></span><span id="mpdetection_state_active"></span>**MPDETECTION\_STATE\_ACTIVE**
</dt> <dd>

Active threat.

</dd> <dt>

<span id="MPDETECTION_STATE_FINISHED"></span><span id="mpdetection_state_finished"></span>**MPDETECTION\_STATE\_FINISHED**
</dt> <dd>

Pending 24 hours to a move to cleared.

</dd> <dt>

<span id="MPDETECTION_STATE_ADDITIONAL_ACTIONS"></span><span id="mpdetection_state_additional_actions"></span>**MPDETECTION\_STATE\_ADDITIONAL\_ACTIONS**
</dt> <dd>

Additional actions required.

</dd> <dt>

<span id="MPDETECTION_STATE_FAILED"></span><span id="mpdetection_state_failed"></span>**MPDETECTION\_STATE\_FAILED**
</dt> <dd>

Non-critical remediation failure.

</dd> <dt>

<span id="MPDETECTION_STATE_CRITICALLY_FAILED"></span><span id="mpdetection_state_critically_failed"></span>**MPDETECTION\_STATE\_CRITICALLY\_FAILED**
</dt> <dd>

Critical remediation failure.

</dd> <dt>

<span id="MPDETECTION_STATE_CLEARED"></span><span id="mpdetection_state_cleared"></span>**MPDETECTION\_STATE\_CLEARED**
</dt> <dd>

Threat does not show up in the state query, only in history.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





