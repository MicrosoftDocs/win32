---
title: MCI_PASTE command (Mmsystem.h)
description: The MCI\_PASTE command pastes data from the clipboard into a file. Digital-video devices recognize this command.
ms.assetid: cad5799a-08ef-4e34-803a-415b937d8fbd
keywords:
- MCI_PASTE command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_PASTE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_PASTE command

The MCI\_PASTE command pastes data from the clipboard into a file. Digital-video devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_PASTE, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_DGV_PASTE_PARMS) lpPaste
);
```



## Parameters

<dl> <dt>

<span id="wDeviceID"></span><span id="wdeviceid"></span><span id="WDEVICEID"></span>*wDeviceID*
</dt> <dd>

Device identifier of the MCI device that is to receive the command message.

</dd> <dt>

<span id="dwFlags"></span><span id="dwflags"></span><span id="DWFLAGS"></span>*dwFlags*
</dt> <dd>

MCI\_NOTIFY, MCI\_WAIT, or MCI\_TEST. For information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> <dt>

<span id="lpPaste"></span><span id="lppaste"></span><span id="LPPASTE"></span>*lpPaste*
</dt> <dd>

Pointer to an [**MCI\_ DGV\_ PASTE\_ PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_paste_parms) structure.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional flags apply to digital-video devices:

<dl> <dt>

<span id="MCI_DGV_PASTE_AT"></span><span id="mci_dgv_paste_at"></span>MCI\_DGV\_PASTE\_AT
</dt> <dd>

A rectangle is included in the **rc** member of the structure identified by *lpPaste*. The first two values of the rectangle specify the point within the frame to place the clipboard information. If the rectangle height and width are nonzero, the clipboard contents are scaled to those dimensions when they are pasted in the frame. If the flag is omitted, MCI\_PASTE defaults to the entire frame rectangle.

</dd> <dt>

<span id="MCI_DGV_PASTE_AUDIO_STREAM"></span><span id="mci_dgv_paste_audio_stream"></span>MCI\_DGV\_PASTE\_AUDIO\_STREAM
</dt> <dd>

An audio-stream number is included in the **dwAudioStream** member of the structure identified by *lpPaste*. If only one audio stream exists on the clipboard, the audio data is pasted into the designated stream. If more than one audio stream exists on the clipboard, the stream indicates the starting number for the stream sequences. If you use this flag and also want to paste video, you must also use the MCI\_DGV\_PASTE\_VIDEO\_STREAM flag. (If neither flag is specified, all audio and video streams are pasted starting with the first audio and video stream. Each pasted stream retains its original stream number.)

</dd> <dt>

<span id="MCI_DGV_PASTE_INSERT"></span><span id="mci_dgv_paste_insert"></span>MCI\_DGV\_PASTE\_INSERT
</dt> <dd>

Clipboard data should be inserted in the existing workspace at the position specified by the MCI\_TO flag. Any existing data after the insertion point is moved in the workspace to make room. This is the default.

</dd> <dt>

<span id="MCI_DGV_PASTE_OVERWRITE"></span><span id="mci_dgv_paste_overwrite"></span>MCI\_DGV\_PASTE\_OVERWRITE
</dt> <dd>

Clipboard data should replace data already present in the workspace. The workspace data replaced follows the insertion point.

</dd> <dt>

<span id="MCI_DGV_PASTE_VIDEO_STREAM"></span><span id="mci_dgv_paste_video_stream"></span>MCI\_DGV\_PASTE\_VIDEO\_STREAM
</dt> <dd>

A video-stream number is included in the **dwVideoStream** member of the structure identified by *lpPaste*. If only one video stream exists on the clipboard, the video data is pasted into the designated stream. If more than one video stream exists on the clipboard, the stream indicates the starting number for the stream sequences. If you use this flag and also want to paste audio, you must also use the MCI\_DGV\_PASTE\_AUDIO\_STREAM flag. (If neither flag is specified, all audio and video streams are pasted starting with the first audio and video stream. Each pasted stream retains its original stream number.)

</dd> <dt>

<span id="MCI_TO"></span><span id="mci_to"></span>MCI\_TO
</dt> <dd>

A position value is included in the **dwTo** member of the structure identified by *lpPaste*. The position value specifies the position to begin pasting data into the workspace. If this flag is omitted, the position defaults to the current position.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[MCI](mci.md)
</dt> <dt>

[MCI Commands](mci-commands.md)
</dt> </dl>

 

