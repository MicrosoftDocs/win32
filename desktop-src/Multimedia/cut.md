---
title: cut command
description: The cut command removes data from the workspace and copies it to the clipboard. Digital-video devices recognize this command.
ms.assetid: f42c7364-49cb-41be-b601-bda6e97d1e76
keywords:
- cut command Windows Multimedia
topic_type:
- apiref
api_name:
- cut
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# cut command

The cut command removes data from the workspace and copies it to the clipboard. Digital-video devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("cut %s %s %s"), 
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

One of the following flags identifying the item to cut.



| Value                 | Meaning                                                                                                                                                                                                                               |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| at *rectangle*        | Specifies the portion of each frame cut. If omitted, it defaults to the entire frame. When this item is specified, frames are not deleted. Instead the area inside the rectangle becomes black.                                       |
| audio stream *stream* | Specifies the audio stream in the workspace affected by the command. If you use this flag and also want to cut video, you must also use the "video stream" flag. (If neither flag is specified, all audio and video streams are cut.) |
| from *position*       | Specifies the start of the range cut. If omitted, it defaults to the current position.                                                                                                                                                |
| to *position*         | Specifies the end of the range cut. The audio and video data cut are exclusive of this position. If omitted it defaults to the end of the workspace.                                                                                  |
| video stream *stream* | Specifies the video stream in the workspace affected by the command. If you use this flag and also want to cut audio, you must also use the "audio stream" flag. (If neither flag is specified, all audio and video streams are cut.) |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", "test", or a combination of these. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The change becomes permanent only when the data is explicitly saved; however, playback acts as if the data has been removed.

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

 

