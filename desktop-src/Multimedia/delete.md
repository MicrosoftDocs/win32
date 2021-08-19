---
title: delete command
description: The delete command deletes a data segment from a file. Digital-video and waveform-audio devices recognize this command.
ms.assetid: 9cf084f6-d64e-4487-9407-b68502b7cec9
keywords:
- delete command Windows Multimedia
topic_type:
- apiref
api_name:
- delete
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# delete command

The delete command deletes a data segment from a file. Digital-video and waveform-audio devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("delete %s %s %s"), 
  lpszDeviceID, 
  lpszPosition, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszPosition"></span><span id="lpszposition"></span><span id="LPSZPOSITION"></span>*lpszPosition*
</dt> <dd>

Flag that identifies a data segment to delete. The following table lists device types that recognize the **delete** command and the flags used by each type.




| Value | Meaning | Meaning | 
|-------|---------|---------|
| digitalvideo | <ul><li>at <em>rectangle</em></li><li>audio stream <em>stream</em></li><li>from <em>position</em></li></ul> | <ul><li>to <em>position</em></li><li>video stream <em>stream</em></li></ul> | 
| waveaudio | from <em>position</em> | to <em>position</em> | 




 

The following table lists the flags that can be specified in the *lpszPosition* parameter and their meanings.



| Value                 | Meaning                                                                                                                                                                                                                                      |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| at *rectangle*        | Specifies the portion of each frame deleted. If omitted, it defaults to the entire frame. When this item is specified, frames are not deleted. Instead the area inside the rectangle becomes black.                                          |
| audio stream *stream* | Specifies the audio stream in the workspace affected by the command. If you use this flag and also want to delete video, you must also use the "video stream" flag. (If neither flag is specified, all audio and video streams are deleted.) |
| from *position*       | Specifies the position at which deletion begins. If this flag is omitted, the deletion begins at the current position.                                                                                                                       |
| to *position*         | Specifies the position at which deletion ends. If this flag is omitted, the deletion continues to the end of the content or workspace.                                                                                                       |
| video stream *stream* | Specifies the video stream in the workspace affected by the command. If you use this flag and also want to delete audio, you must also use "audio stream" flag. (If neither flag is specified, all audio and video streams are deleted.)     |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video and VCR devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

Before issuing any commands that use position values, you should set the desired time format by using the [set](set.md) command.

## Examples

The following command deletes the waveform-audio data from 1 millisecond through 900 milliseconds (assuming the time format is set to milliseconds).

``` syntax
delete mysound from 1 to 900
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

[set](set.md)
</dt> </dl>

 

