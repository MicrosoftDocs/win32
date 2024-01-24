---
title: copy command
description: The copy command copies data to the clipboard. Digital-video devices recognize this command.
ms.assetid: '4f7b5be6-12c3-43a0-bac9-19eb49384330'
keywords:
- copy command Windows Multimedia
topic_type:
- apiref
api_name:
- copy
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# copy command

The copy command copies data to the clipboard. Digital-video devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("copy %s %s %s"), 
  lpszDeviceID, 
  lpszItem, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszItem"></span><span id="lpszitem"></span><span id="LPSZITEM"></span>*lpszItem*
</dt> <dd>

One of the following flags identifying the item to copy.



| Value                 | Meaning                                                                                                                                                                                                                                   |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| at *rectangle*        | Specifies the portion of each frame that will be copied. If omitted, the default setting is the entire frame.                                                                                                                             |
| audio stream *stream* | Specifies the audio stream in the workspace affected by the command. If you use this flag and also want to copy video, you must also use the "video stream" flag. (If neither flag is specified, all audio and video streams are copied.) |
| from *position*       | Specifies the start of the range copied. If omitted, the default setting is the current position.                                                                                                                                         |
| to *position*         | Specifies the end of the range copied. The audio and video data copied are exclusive of this position. If omitted, the default setting is the end of the workspace.                                                                       |
| video stream *stream* | Specifies the video stream in the workspace affected by the command. If you use this flag and also want to copy audio, you must also use the "audio stream" flag. (If neither flag is specified, all audio and video streams are copied.) |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", "test", or a combination of these. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

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

 

