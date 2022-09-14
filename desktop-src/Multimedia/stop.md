---
title: stop command
description: The stop command stops playback or recording. CD audio, digital-video, MIDI sequencer, videodisc, VCR, and waveform-audio devices recognize this command.
ms.assetid: '82b2da63-f1ac-48f3-a206-6c5cfe00f5be'
keywords:
- stop command Windows Multimedia
topic_type:
- apiref
api_name:
- stop
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# stop command

The stop command stops playback or recording. CD audio, digital-video, MIDI sequencer, videodisc, VCR, and waveform-audio devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("stop %s %s %s"), 
  lpszDeviceID, 
  lpszStopFlags, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszStopFlags"></span><span id="lpszstopflags"></span><span id="LPSZSTOPFLAGS"></span>*lpszStopFlags*
</dt> <dd>

For digital-video devices, it can be the following flag.



| Value | Meaning                                                                                                                                                                                      |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| hold  | Prevents the release of resources required to redraw a still image on the screen. The frame buffer remains available for use in updating the display when, for example, the window is moved. |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video and VCR devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

For CD audio devices, the stop command stops playback and resets the current track position to zero.

## Examples

The following command stops playback or recording on the "mysound" device.

``` syntax
stop mysound
```

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[MCI](mci.md)
</dt> <dt>

[MCI Command Strings](mci-command-strings.md)
</dt> </dl>

 

