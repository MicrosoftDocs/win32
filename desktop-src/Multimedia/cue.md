---
title: cue command
description: The cue command prepares for playing or recording. Digital-video, VCR, and waveform-audio devices recognize this command.
ms.assetid: 94fa0d0c-d5c9-4ef1-bb7d-22dfb09a7689
keywords:
- cue command Windows Multimedia
topic_type:
- apiref
api_name:
- cue
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# cue command

The cue command prepares for playing or recording. Digital-video, VCR, and waveform-audio devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("cue %s %s %s"), 
  lpszDeviceID, 
  lpszInOutTo, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszInOutTo"></span><span id="lpszinoutto"></span><span id="LPSZINOUTTO"></span>*lpszInOutTo*
</dt> <dd>

Flag that prepares a device for playing or recording. The following table lists device types that recognize the **cue** command and the flags used by each type.




| Value | Cue | Cue | 
|-------|-----|-----|
| digitalvideo | <ul><li>input</li><li>noshow</li></ul> | <ul><li>output</li><li>to <em>position</em></li></ul> | 
| vcr | <ul><li>from <em>position</em></li><li>input</li><li>output</li></ul> | <ul><li>preroll</li><li>reverse</li><li>to <em>position</em></li></ul> | 
| waveaudio | input | output | 




 

The following table lists the flags that can be specified in the *lpszInOutTo* parameter and their meanings.



| Value           | Meaning                                                                                                                                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| from *position* | Indicates where to start.                                                                                                                                                                                                                                                                                      |
| input           | Prepares for recording. For digital-video devices, this flag can be omitted if the current presentation source is already the external input.                                                                                                                                                                  |
| noshow          | Prepares for playing a frame without displaying it. When this flag is specified, the display continues to show the image in the frame buffer even though its corresponding frame is not the current position. A subsequent cue command without this flag and without the "to" flag displays the current frame. |
| output          | Prepares for playing. If neither "input" nor "output" is specified, the default setting is "output".                                                                                                                                                                                                           |
| preroll         | Moves the preroll distance from the *in-point*. The in-point is the current position, or the position specified by the "from" flag.                                                                                                                                                                            |
| reverse         | Indicates play direction is in reverse (backward).                                                                                                                                                                                                                                                             |
| to *position*   | Moves the workspace to the specified position. For VCR devices, this flag indicates where to stop.                                                                                                                                                                                                             |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video and VCR devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

Although it is not necessary, issuing the cue command before playing or recording on some devices might reduce the delay before the device starts the action.

This command fails if playing or recording is in progress or if the device is paused.

When cueing for playback (using cue "output"), issuing the [play](play.md) command with the "from", "to", or "reverse" flag cancels the cue command.

When cueing for recording (using cue "input"), issuing the [record](record.md) command with the "from", "to", or "initialize" flag cancels the cue command.

## Examples

The following command prepares the "mysound" device for recording.

``` syntax
cue mysound input
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

[play](play.md)
</dt> <dt>

[record](record.md)
</dt> </dl>

 

