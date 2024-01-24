---
title: play command
description: The play command starts playing a device. CD audio, digital-video, MIDI sequencer, videodisc, VCR, and waveform-audio devices recognize this command.
ms.assetid: '3ee707d6-6af4-494d-a887-d91ea5666ac4'
keywords:
- play command Windows Multimedia
topic_type:
- apiref
api_name:
- play
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# play command

The play command starts playing a device. CD audio, digital-video, MIDI sequencer, videodisc, VCR, and waveform-audio devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("play %s %s %s"), 
  lpszDeviceID, 
  lpszPlayFlags, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszPlayFlags"></span><span id="lpszplayflags"></span><span id="LPSZPLAYFLAGS"></span>*lpszPlayFlags*
</dt> <dd>

Flag for playing a device. The following table lists device types that recognize the **play** command and the flags used by each type.



| Value        | Meaning                          | Meaning                           |
|--------------|----------------------------------|-----------------------------------|
| cdaudio      | from *position*                  | to *position*                     |
| digitalvideo | from *position*fullscreen repeat | reverse to *position*window       |
| sequencer    | from *position*                  | to *position*                     |
| vcr          | at *time*from *position*reverse  | scan to *position*                |
| videodisc    | fast from *position*reverse scan | slow speed *integer*to *position* |
| waveaudio    | from *position*                  | to *position*                     |



 

The following table lists the flags that can be specified in the **lpszPlayFlags** parameter and their meanings.



| Value           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| at *time*       | Indicates when the device should begin performing this command, or, if the device has been cued, when the cued command begins. For more information, see the [cue](cue.md) command.                                                                                                                                                                                                                                                                 |
| fast            | Indicates that the device should play faster than normal. To determine the exact speed on a videodisc player, use the "speed" flag of the [status](status.md) command. To specify the speed more precisely, use the "speed" flag of this command.                                                                                                                                                                                                   |
| from *position* | Specifies a starting position for the playback. If the "from" flag is not specified, playback begins at the current position. For **cdaudio** devices, if the "from" position is greater than the end position of the disc, or if the "from" position is greater than the "to" position, the driver returns an error. For **videodisc** devices, the default positions are in frames for CAV discs and in hours, minutes, and seconds for CLV discs. |
| fullscreen      | Specifies that a full-screen display should be used. Use this flag only when playing compressed files. (Uncompressed files won't play full-screen.)                                                                                                                                                                                                                                                                                                  |
| repeat          | Specifies that playback should restart when the end of the content is reached.                                                                                                                                                                                                                                                                                                                                                                       |
| reverse         | Specifies that the play direction is backward. You cannot specify an ending location with the "reverse" flag. For videodiscs, "scan" applies only to CAV format.                                                                                                                                                                                                                                                                                     |
| scan            | Plays as fast as possible without disabling video (although audio might be disabled). For videodiscs, "scan" applies only to CAV format.                                                                                                                                                                                                                                                                                                             |
| slow            | Plays slowly. To determine the exact speed on a videodisc player, use the "speed" flag of the [status](status.md) command. To specify the speed more precisely, use the "speed" flag of this command. For videodiscs, "slow" applies only to CAV format.                                                                                                                                                                                            |
| speed *integer* | Plays a videodisc at the specified speed, in frames per second. This flag applies only to CAV discs.                                                                                                                                                                                                                                                                                                                                                 |
| to *position*   | Specifies an ending position for the playback. If the "to" flag is not specified, playback stops at the end of the content. For **cdaudio** devices, if the "to" position is greater than the end position of the disc, the driver returns an error. For **videodisc** devices, the default positions are in frames for CAV discs and in hours, minutes, and seconds for CLV discs.                                                                  |
| window          | Specifies that playing should use the window associated with the device instance. This is the default setting.                                                                                                                                                                                                                                                                                                                                       |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video and VCR devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

Before issuing commands that use position values, you should set the desired time format by using the [set](set.md) command. This command begins playing at the current speed, as set with the set "speed" command. The direction is reverse if the "reverse" flag is specified, or if the "to" flag is specified as a value less than the "from" flag. If the "from" flag is not specified, playback begins at the current position. The "to" and "reverse" flags cannot be used together.

## Examples

The following command plays the "mysound" device from position 1000 through position 2000, sending a notification message when the playback completes.

``` syntax
play mysound from 1000 to 2000 notify
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
</dt> <dt>

[cue](cue.md)
</dt> <dt>

[set](set.md)
</dt> </dl>

 

