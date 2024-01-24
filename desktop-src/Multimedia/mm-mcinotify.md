---
title: MM_MCINOTIFY message (Mmsystem.h)
description: The MM\_MCINOTIFY message notifies an application that an MCI device has completed an operation. MCI devices send this message only when the MCI\_NOTIFY flag is used.
ms.assetid: a0840130-2969-4ce5-b098-3e45401eebb1
keywords:
- MM_MCINOTIFY message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_MCINOTIFY
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_MCINOTIFY message

The **MM\_MCINOTIFY** message notifies an application that an MCI device has completed an operation. MCI devices send this message only when the MCI\_NOTIFY flag is used.


```C++
MM_MCINOTIFY 
wParam = (WPARAM) wFlags 
lParam = (LONG) lDevID
```



## Parameters

<dl> <dt>

<span id="wFlags"></span><span id="wflags"></span><span id="WFLAGS"></span>*wFlags*
</dt> <dd>

Reason for the notification. The following values are defined:



| Requirement | Value |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MCI\_NOTIFY\_ABORTED    | The device received a command that prevented the current conditions for initiating the callback function from being met. If a new command interrupts the current command and it also requests notification, the device sends this message only and not MCI\_NOTIFY\_SUPERSEDED |
| MCI\_NOTIFY\_FAILURE    | A device error occurred while the device was executing the command.                                                                                                                                                                                                            |
| MCI\_NOTIFY\_SUCCESSFUL | The conditions initiating the callback function have been met.                                                                                                                                                                                                                 |
| MCI\_NOTIFY\_SUPERSEDED | The device received another command with the "notify" flag set and the current conditions for initiating the callback function have been superseded.                                                                                                                           |



 

</dd> <dt>

<span id="lDevID"></span><span id="ldevid"></span><span id="LDEVID"></span>*lDevID*
</dt> <dd>

Identifier of the device initiating the callback function.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

For more information about the MCI\_NOTIFY flag, see [The Notify Flag](the-notify-flag.md).

A device returns the MCI\_NOTIFY\_SUCCESSFUL flag with **MM\_MCINOTIFY** when the action for a command finishes. For example, a CD audio device uses this flag for notification for the [**play**](play.md) ( [**MCI\_PLAY**](mci-play.md)) command when the device finishes playing. The **play** command is successful only when it reaches the specified end position or reaches the end of the media. Similarly, the [**seek**](seek.md) ( [**MCI\_SEEK**](mci-seek.md)) and [**record**](record.md) ( [**MCI\_RECORD**](mci-record.md)) commands do not return MCI\_NOTIFY\_SUCCESSFUL until they reach the specified end position or reach the end of the media.

A device returns the MCI\_NOTIFY\_ABORTED flag with **MM\_MCINOTIFY** only when it receives a command that prevents it from meeting the notification conditions. For example, the [**play**](play.md) command would not abort notification for a previous **play** command provided that the new command does not change the play direction or change the ending position. The [**seek**](seek.md) and [**record**](record.md) commands behave similarly. MCI also does not send MCI\_NOTIFY\_ABORTED when playback or recording is paused with the [**pause**](pause.md) ( [**MCI\_PAUSE**](mci-pause.md)) command. Sending the [**resume**](resume.md) ( [**MCI\_RESUME**](mci-resume.md)) command allows them to continue to meet the callback conditions.

When your application requests notification for a command, check the error return of the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) or [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) functions. If these functions encounter an error and return a nonzero value, MCI will not set notification for the command.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[MCI](mci.md)
</dt> <dt>

[MCI Messages](mci-messages.md)
</dt> <dt>

[**pause**](pause.md)
</dt> <dt>

[**play**](play.md)
</dt> <dt>

[**record**](record.md)
</dt> <dt>

[**resume**](resume.md)
</dt> <dt>

[**seek**](seek.md)
</dt> </dl>

 

