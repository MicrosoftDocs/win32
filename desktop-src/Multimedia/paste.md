---
title: paste command
description: The paste command copies the contents of the clipboard into the workspace. Digital-video devices recognize this command.
ms.assetid: 'c09418e1-2535-40d1-8912-e5ece91ee673'
keywords:
- paste command Windows Multimedia
topic_type:
- apiref
api_name:
- paste
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# paste command

The paste command copies the contents of the clipboard into the workspace. Digital-video devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("paste %s %s %s"), 
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

One or more of the following flags.



| Value                 | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| at *rectangle*        | Specifies the location within the frame where the data is pasted. The upper left corner of the *rectangle* corresponds to the upper left corner of the added data. If the rectangle has a nonzero size in X or Y, the contents of the clipboard are scaled in those dimensions when they are pasted into the frame. If omitted, the *rectangle* defaults to the entire frame. If this flag is specified in "insert" mode (the default), any region outside the rectangle is painted a solid color.                       |
| audio stream *stream* | Specifies the audio stream in the workspace affected by the command. If only one audio stream exists on the clipboard, the audio data is pasted into the designated *stream*. If more than one audio stream exists on the clipboard, the *stream* indicates the starting number for the stream sequences. If you use this flag and also want to paste video, you must also use the "video stream" flag. (If neither flag is specified, all audio and video streams are pasted and retain their original stream numbers.) |
| insert                | Specifies that the data is inserted into the workspace. Any data after the insertion point is moved forward in the workspace to make room. This is the default value.                                                                                                                                                                                                                                                                                                                                                    |
| overwrite             | Specifies that the data is copied into the workspace by writing over any existing data after the insertion point. The "insert" and "overwrite" flags affect whether frames are destroyed or moved during the paste operation, not how the data is pasted within each frame.                                                                                                                                                                                                                                              |
| to *position*         | Specifies the position in the workspace at which the data is pasted. If omitted, it defaults to the current position.                                                                                                                                                                                                                                                                                                                                                                                                    |
| video stream *stream* | Specifies the video stream in the workspace affected by the command. If only one video stream exists on the clipboard, the video data is pasted into the designated *stream*. If more than one video stream exists on the clipboard, the *stream* indicates the starting number for the stream sequences. If you use this flag and also want to paste audio, you must also use the "audio stream" flag. (If neither flag is specified, all audio and video streams are pasted and retain their original stream numbers.) |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", "test", or a combination of these. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

No signals are present in the data copied from the clipboard. The change becomes permanent only when the data is explicitly saved; however, playback acts as if the data has been added.

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

 

