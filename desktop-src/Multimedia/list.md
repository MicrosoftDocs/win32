---
title: list command
description: The list command determines the number and types of video and audio inputs. Digital-video and VCR devices recognize this command.
ms.assetid: b3fe3819-0b8a-4de5-9c79-03e1e089436f
keywords:
- list command Windows Multimedia
topic_type:
- apiref
api_name:
- list
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# list command

The list command determines the number and types of video and audio inputs. Digital-video and VCR devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("list %s %s %s"), 
  lpszDeviceID, 
  lpszList, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszList"></span><span id="lpszlist"></span><span id="LPSZLIST"></span>*lpszList*
</dt> <dd>

Flag that identifies the number and types of video and audio inputs. The following table lists device types that recognize the **list** command and the flags used by each type.



| Value        | Meaning                                                                           | Meaning                                                                                                                      |
|--------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| digitalvideo | audio algorithmaudio quality algorithm *algorithm*audio streamcountnumber *index* | still algorithmstill quality algorithm *algorithm*video algorithmvideo quality algorithm *algorithm*video sourcevideo stream |
| vcr          | audio source countaudio source number *index*                                     | video source countvideo source number *index*                                                                                |



 

The following table lists the flags that can be specified in the **lpszList** parameter and their meanings.



| Value                               | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| audio algorithm                     | Specifies the command should retrieve audio algorithm names.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| audio quality algorithm *algorithm* | Specifies the command should retrieve quality levels associated with the specified *algorithm*. If *algorithm* is "current", the quality level of the current algorithm is returned.                                                                                                                                                                                                                                                                                                   |
| audio source count                  | Returns the total number of audio inputs.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| audio source number *index*         | Returns the type of audio input of source *index*.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| audio stream                        | Specifies the command should retrieve the names of the audio streams associated with the workspace. These strings (such as "English" or "German") are embedded in the file and identify the stream.                                                                                                                                                                                                                                                                                    |
| count                               | Returns the number of options of the specified type.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| number *index*                      | Returns a string describing a specific option (as identified by *index*) of the specified option type. *Index* must be an integer between 1 and the value returned by "count".                                                                                                                                                                                                                                                                                                         |
| still algorithm                     | Specifies the command should retrieve still algorithm names.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| still quality algorithm *algorithm* | Specifies the command should retrieve quality levels associated with the specified still *algorithm*. If *algorithm* is "current", the quality level of the current algorithm is returned.                                                                                                                                                                                                                                                                                             |
| video algorithm                     | Specifies the command should retrieve video algorithm names.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| video quality algorithm *algorithm* | Specifies the command should retrieve quality levels associated with the specified video *algorithm*. If *algorithm* is "current", the quality level of the current algorithm is returned.                                                                                                                                                                                                                                                                                             |
| video source                        | Specifies the command should return information about the video sources. When used with the "count" flag, it returns the number of video sources. When used with the "number" flag, it returns the type of a video source. MCI defines the following constants for type: "ntsc", "rgb", "pal", "secam", "svideo", and "generic". There might be more than one source of each type returned. The "generic" source type is used when more than one signal is allowed for that connector. |
| video source count                  | Returns total number of video inputs.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| video source number *index*         | Returns the type of video input of source *index*.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| video stream                        | Specifies the command should retrieve the names of video streams associated with the workspace. These strings (such as "funny ending" or "sad ending") are embedded in the file and identify the stream.                                                                                                                                                                                                                                                                               |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or "test". For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

For VCR devices, either "video source" or "audio source" must be specified with either the "count" or "number" flags. If "count" is specified, the total number of inputs of video or audio is returned. If "number" is specified, the driver returns a type corresponding to the input. The type can be any one of the following: "tuner", "line", "svideo", "aux", or "generic". Typically, you should first query the VCR for the "count" and then use the count as the range for the "number" flag. The "source" numbers start from 1.

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

 

