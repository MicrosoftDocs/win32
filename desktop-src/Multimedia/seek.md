---
title: seek command
description: The seek command moves to the specified position and stops. CD audio, digital-video, MIDI sequencer, VCR, videodisc, and waveform-audio devices recognize this command.
ms.assetid: 'e9e8ca14-d181-4f29-b4d3-c7f5b0301164'
keywords:
- seek command Windows Multimedia
topic_type:
- apiref
api_name:
- seek
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# seek command

The seek command moves to the specified position and stops. CD audio, digital-video, MIDI sequencer, VCR, videodisc, and waveform-audio devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("seek %s %s %s"), 
  lpszDeviceID, 
  lpszSeekFlags, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszSeekFlags"></span><span id="lpszseekflags"></span><span id="LPSZSEEKFLAGS"></span>*lpszSeekFlags*
</dt> <dd>

Flag for moving to a specified position. The following table lists device types that recognize the **seek** command and the flags used by each type.



| Value        | Meaning                          | Meaning                      |
|--------------|----------------------------------|------------------------------|
| cdaudio      | to end to *position*             | to start                     |
| digitalvideo | to end to *position*             | to start                     |
| sequencer    | to end to *position*             | to start                     |
| vcr          | at *time*mark *mark\_num*reverse | to end to *position*to start |
| videodisc    | reverse to end                   | to *position*to start        |
| waveaudio    | to end to *position*             | to start                     |



 

The following table lists the flags that can be specified in the **lpszSeekFlags** parameter and their meanings.



| Value            | Meaning                                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| at *time*        | Indicates when the device should begin performing this command, or, if the device has been cued, when the cued command begins. For more information, see the [cue](cue.md) command.                             |
| mark *mark\_num* | Seeks to the relative mark indicated by *mark\_num*, which must be a positive integer value. Marks are signals written to the VCR tape using the [mark](mark.md) command and are used for high-speed searching. |
| reverse          | Indicates that the seek direction on VCRs and CAV videodiscs is backward. This flag is invalid if the "to" flag is specified. For VCRs, this flag must be used with the "mark" flag.                             |
| to end           | Seeks to the end of the content.                                                                                                                                                                                 |
| to *position*    | Specifies the position to stop the seek. For **cdaudio** devices, MCI returns an out-of-range error if the specified position is greater than the length of the disc.                                            |
| to start         | Seeks to the start of the content.                                                                                                                                                                               |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video and VCR devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

Before issuing any commands that use position values, you should set the desired time format by using the [set](set.md) command.

Digital-video devices support two seek modes, which you can change by using the [set](set.md) command. The "seek exactly on" mode causes the seek command to move to the specified frame. The "seek exactly off" mode causes the seek command to move to the closest key frame prior to the specified frame.

If a CD audio device is playing when the seek command is issued, playback is stopped. When the seek command is issued with a videodisc device, the device searches using fast forward or fast reverse with video and audio off.

When the seek command is issued with a waveform-audio device, the behavior depends on the sample size. If the sample size is 16 bits or greater, seek moves to the beginning of the nearest sample when a specified position does not coincide with the start of a sample.

## Examples

The following command seeks to the start of the media file associated with the "mysound" device.

``` syntax
seek mysound to start
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

[mark](mark.md)
</dt> <dt>

[set](set.md)
</dt> </dl>

 

