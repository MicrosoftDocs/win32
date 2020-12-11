---
title: record command
description: The record command starts recording data. VCR and waveform-audio devices recognize this command. Although digital-video devices and MIDI sequencers also recognize this command, the MCIAVI and MCISEQ drivers do not implement it.
ms.assetid: 'a0838153-5ac2-437f-ae1e-0c4f950fcac5'
keywords:
- record command Windows Multimedia
topic_type:
- apiref
api_name:
- record
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# record command

The record command starts recording data. VCR and waveform-audio devices recognize this command. Although digital-video devices and MIDI sequencers also recognize this command, the MCIAVI and MCISEQ drivers do not implement it.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("record %s %s %s"), 
  lpszDeviceID, 
  lpszRecordFlags, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszRecordFlags"></span><span id="lpszrecordflags"></span><span id="LPSZRECORDFLAGS"></span>*lpszRecordFlags*
</dt> <dd>

Flag for recording data. The following table lists device types that recognize the **record** command and the flags used by each type.



| Value        | Meaning                                                | Meaning                                             |
|--------------|--------------------------------------------------------|-----------------------------------------------------|
| digitalvideo | at *rectangle*audio stream *stream*from *position*hold | insert overwrite to *position*video stream *stream* |
| sequencer    | from *position*insert                                  | overwrite to *position*                             |
| vcr          | at *time*from *position*initialize                     | insert overwrite to *position*                      |
| waveaudio    | from *position*insert                                  | overwrite to *position*                             |



 

The following table lists the flags that can be specified in the **lpszRecordFlags** parameter and their meanings.



| Value                 | Meaning                                                                                                                                                                                                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| at *rectangle*        | Specifies a rectangular region of the external input used as the source for the pixels compressed and saved. If not specified, the rectangle defaults to the rectangle specified for [put](put.md) "video". When it is set differently from the "video" rectangle, the displayed image is not what is recorded. |
| at *time*             | Indicates when the device should begin performing this command, or, if the device has been cued, when the cued command begins. For more information, see the [cue](cue.md) command.                                                                                                                             |
| audio stream *stream* | Specifies the audio stream used for recording. If this flag is not specified and the file format does not define a default, it is recorded into the stream that is physically first.                                                                                                                             |
| from *position*       | Specifies a starting position for the recording. If the "from" flag is not specified, the device starts recording at the current position.                                                                                                                                                                       |
| hold                  | Freezes the image when recording has finished instead of showing live video. When recording stops, an automatic [monitor](monitor.md) "file" command is performed. To return to live video, issue the **monitor** "input" command.                                                                              |
| initialize            | Initialize the tape (media), which involves recording timecode (if possible) for blank video and audio. This command might take several hours if the entire tape must be initialized.                                                                                                                            |
| insert                | Specifies that new data is added to the file at the current position.                                                                                                                                                                                                                                            |
| overwrite             | Specifies that new data will replace data in the file.                                                                                                                                                                                                                                                           |
| to *position*         | Specifies an ending position for the recording. If the "to" flag is not specified, the device records until it receives a [stop](stop.md) or [pause](pause.md) command.                                                                                                                                        |
| video stream *stream* | Specifies the video stream used for recording. If this is not specified and the file format does not define a default, then it is recorded into the stream that is physically first.                                                                                                                             |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video and VCR devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The recording stops when a [stop](stop.md) or [pause](pause.md) command is issued. For the MCIWAVE driver, all data recorded after a file is opened is discarded if the file is closed without saving it.

Before issuing any commands that use position values, you should set the desired time format by using the [set](set.md) command. The tracks to be recorded are specified by the [settimecode](settimecode.md) "record", set "assemble record", [setvideo](setvideo.md) "record", and [setaudio](setaudio.md) "record" commands.

## Examples

The following command starts recording at the current position.

``` syntax
record mysound
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

[monitor](monitor.md)
</dt> <dt>

[pause](pause.md)
</dt> <dt>

[put](put.md)
</dt> <dt>

[set](set.md)
</dt> <dt>

[setaudio](setaudio.md)
</dt> <dt>

[settimecode](settimecode.md)
</dt> <dt>

[setvideo](setvideo.md)
</dt> <dt>

[stop](stop.md)
</dt> </dl>

 

