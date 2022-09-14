---
title: Windows Animation Error Codes (Winerror.h)
description: If an error occurs, Windows Animation returns a code as an HRESULT value. This section provides a list of error codes specific to Windows Animation. For a list of general COM error codes, see COM Error Codes.
ms.assetid: 38f15d61-d415-4c7d-b454-5144fc7c9b1e
topic_type:
- apiref
api_name:
- UI_E_CREATE_FAILED
- UI_E_SHUTDOWN_CALLED
- UI_E_ILLEGAL_REENTRANCY
- UI_E_OBJECT_SEALED
- UI_E_VALUE_NOT_SET
- UI_E_VALUE_NOT_DETERMINED
- UI_E_INVALID_OUTPUT
- UI_E_BOOLEAN_EXPECTED
- UI_E_DIFFERENT_OWNER
- UI_E_AMBIGUOUS_MATCH
- UI_E_FP_OVERFLOW
- UI_E_WRONG_THREAD
- UI_E_STORYBOARD_ACTIVE
- UI_E_STORYBOARD_NOT_PLAYING
- UI_E_START_KEYFRAME_AFTER_END
- UI_E_END_KEYFRAME_NOT_DETERMINED
- UI_E_LOOPS_OVERLAP
- UI_E_TRANSITION_ALREADY_USED
- UI_E_TRANSITION_NOT_IN_STORYBOARD
- UI_E_TRANSITION_ECLIPSED
- UI_E_TIME_BEFORE_LAST_UPDATE
- UI_E_TIMER_CLIENT_ALREADY_CONNECTED
api_location:
- winerror.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Animation Error Codes

If an error occurs, Windows Animation returns a code as an **HRESULT** value. This section provides a list of error codes specific to Windows Animation. For a list of general COM error codes, see [COM Error Codes](/windows/desktop/com/com-error-codes).

<dl> <dt>

<span id="UI_E_CREATE_FAILED"></span><span id="ui_e_create_failed"></span>**UI\_E\_CREATE\_FAILED**
</dt> <dd> <dl> <dt>

0x802A0001
</dt> <dt>



The object could not be created.


</dt> </dl> </dd> <dt>

<span id="UI_E_SHUTDOWN_CALLED"></span><span id="ui_e_shutdown_called"></span>**UI\_E\_SHUTDOWN\_CALLED**
</dt> <dd> <dl> <dt>

0x802A0002
</dt> <dt>



The [**Shutdown**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationmanager-shutdown) method has been called on the animation manager, causing the animation manager to shut down and all the animation variables and storyboards it created to be released.

> [!Note]  
> No methods can be called on any animation object after [**Shutdown**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationmanager-shutdown).

 


</dt> </dl> </dd> <dt>

<span id="UI_E_ILLEGAL_REENTRANCY"></span><span id="ui_e_illegal_reentrancy"></span>**UI\_E\_ILLEGAL\_REENTRANCY**
</dt> <dd> <dl> <dt>

0x802A0003
</dt> <dt>



This method cannot be called during this type of callback.


</dt> </dl> </dd> <dt>

<span id="UI_E_OBJECT_SEALED"></span><span id="ui_e_object_sealed"></span>**UI\_E\_OBJECT\_SEALED**
</dt> <dd> <dl> <dt>

0x802A0004
</dt> <dt>



This object has been sealed, so this change is no longer allowed.


</dt> </dl> </dd> <dt>

<span id="UI_E_VALUE_NOT_SET"></span><span id="ui_e_value_not_set"></span>**UI\_E\_VALUE\_NOT\_SET**
</dt> <dd> <dl> <dt>

0x802A0005
</dt> <dt>



The requested value has never been set, and therefore cannot be retrieved.


</dt> </dl> </dd> <dt>

<span id="UI_E_VALUE_NOT_DETERMINED"></span><span id="ui_e_value_not_determined"></span>**UI\_E\_VALUE\_NOT\_DETERMINED**
</dt> <dd> <dl> <dt>

0x802A0006
</dt> <dt>



The requested value cannot be determined.


</dt> </dl> </dd> <dt>

<span id="UI_E_INVALID_OUTPUT"></span><span id="ui_e_invalid_output"></span>**UI\_E\_INVALID\_OUTPUT**
</dt> <dd> <dl> <dt>

0x802A0007
</dt> <dt>



A callback returned an invalid output parameter.


</dt> </dl> </dd> <dt>

<span id="UI_E_BOOLEAN_EXPECTED"></span><span id="ui_e_boolean_expected"></span>**UI\_E\_BOOLEAN\_EXPECTED**
</dt> <dd> <dl> <dt>

0x802A0008
</dt> <dt>



A callback returned a success code other than S\_OK or S\_FALSE.


</dt> </dl> </dd> <dt>

<span id="UI_E_DIFFERENT_OWNER"></span><span id="ui_e_different_owner"></span>**UI\_E\_DIFFERENT\_OWNER**
</dt> <dd> <dl> <dt>

0x802A0009
</dt> <dt>



A parameter that should be owned by this object is owned by a different object.


</dt> </dl> </dd> <dt>

<span id="UI_E_AMBIGUOUS_MATCH"></span><span id="ui_e_ambiguous_match"></span>**UI\_E\_AMBIGUOUS\_MATCH**
</dt> <dd> <dl> <dt>

0x802A000A
</dt> <dt>



More than one item matched the search criteria.


</dt> </dl> </dd> <dt>

<span id="UI_E_FP_OVERFLOW"></span><span id="ui_e_fp_overflow"></span>**UI\_E\_FP\_OVERFLOW**
</dt> <dd> <dl> <dt>

0x802A000B
</dt> <dt>



A floating-point overflow occurred.


</dt> </dl> </dd> <dt>

<span id="UI_E_WRONG_THREAD"></span><span id="ui_e_wrong_thread"></span>**UI\_E\_WRONG\_THREAD**
</dt> <dd> <dl> <dt>

0x802A000C
</dt> <dt>



This method can only be called from the thread that created the object.


</dt> </dl> </dd> <dt>

<span id="UI_E_STORYBOARD_ACTIVE"></span><span id="ui_e_storyboard_active"></span>**UI\_E\_STORYBOARD\_ACTIVE**
</dt> <dd> <dl> <dt>

0x802A0101
</dt> <dt>



The storyboard is currently in the schedule.


</dt> </dl> </dd> <dt>

<span id="UI_E_STORYBOARD_NOT_PLAYING"></span><span id="ui_e_storyboard_not_playing"></span>**UI\_E\_STORYBOARD\_NOT\_PLAYING**
</dt> <dd> <dl> <dt>

0x802A0102
</dt> <dt>



The storyboard is not playing.


</dt> </dl> </dd> <dt>

<span id="UI_E_START_KEYFRAME_AFTER_END"></span><span id="ui_e_start_keyframe_after_end"></span>**UI\_E\_START\_KEYFRAME\_AFTER\_END**
</dt> <dd> <dl> <dt>

0x802A0103
</dt> <dt>



The start keyframe might occur after the end keyframe.


</dt> </dl> </dd> <dt>

<span id="UI_E_END_KEYFRAME_NOT_DETERMINED"></span><span id="ui_e_end_keyframe_not_determined"></span>**UI\_E\_END\_KEYFRAME\_NOT\_DETERMINED**
</dt> <dd> <dl> <dt>

0x802A0104
</dt> <dt>



It might not be possible to determine the end keyframe time when the start keyframe is reached.


</dt> </dl> </dd> <dt>

<span id="UI_E_LOOPS_OVERLAP"></span><span id="ui_e_loops_overlap"></span>**UI\_E\_LOOPS\_OVERLAP**
</dt> <dd> <dl> <dt>

0x802A0105
</dt> <dt>



Two repeated portions of a storyboard might overlap.


</dt> </dl> </dd> <dt>

<span id="UI_E_TRANSITION_ALREADY_USED"></span><span id="ui_e_transition_already_used"></span>**UI\_E\_TRANSITION\_ALREADY\_USED**
</dt> <dd> <dl> <dt>

0x802A0106
</dt> <dt>



The transition has already been added to a different storyboard or has been added to a storyboard that has finished playing and been released.


</dt> </dl> </dd> <dt>

<span id="UI_E_TRANSITION_NOT_IN_STORYBOARD"></span><span id="ui_e_transition_not_in_storyboard"></span>**UI\_E\_TRANSITION\_NOT\_IN\_STORYBOARD**
</dt> <dd> <dl> <dt>

0x802A0107
</dt> <dt>



The transition has not been added to any storyboard.


</dt> </dl> </dd> <dt>

<span id="UI_E_TRANSITION_ECLIPSED"></span><span id="ui_e_transition_eclipsed"></span>**UI\_E\_TRANSITION\_ECLIPSED**
</dt> <dd> <dl> <dt>

0x802A0108
</dt> <dt>



The transition might eclipse the beginning of another transition in the storyboard.


</dt> </dl> </dd> <dt>

<span id="UI_E_TIME_BEFORE_LAST_UPDATE"></span><span id="ui_e_time_before_last_update"></span>**UI\_E\_TIME\_BEFORE\_LAST\_UPDATE**
</dt> <dd> <dl> <dt>

0x802A0109
</dt> <dt>



The specified time is earlier than the time passed to the last update.


</dt> </dl> </dd> <dt>

<span id="UI_E_TIMER_CLIENT_ALREADY_CONNECTED"></span><span id="ui_e_timer_client_already_connected"></span>**UI\_E\_TIMER\_CLIENT\_ALREADY\_CONNECTED**
</dt> <dd> <dl> <dt>

0x802A010A
</dt> <dt>



This client is already connected to a timer.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7, Windows Vista and Platform Update for Windows Vista \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                                                       |
| Header<br/>                   | <dl> <dt>Winerror.h</dt> </dl>           |



## See also

<dl> <dt>

[Windows Animation Reference](windows-animation-reference.md)
</dt> </dl>

 

