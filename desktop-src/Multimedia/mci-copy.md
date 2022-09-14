---
title: MCI_COPY command (Mmsystem.h)
description: The MCI\_COPY command copies data to the clipboard. Digital-video devices recognize this command.
ms.assetid: 41807920-3312-4cdb-82e6-6ab4b9b35162
keywords:
- MCI_COPY command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_COPY
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_COPY command

The MCI\_COPY command copies data to the clipboard. Digital-video devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_COPY, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_DGV_COPY_PARMS) lpCopy
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

<span id="lpCopy"></span><span id="lpcopy"></span><span id="LPCOPY"></span>*lpCopy*
</dt> <dd>

Pointer to an [**MCI\_DGV\_COPY\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_copy_parms) structure.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional flags apply to digital-video devices:

<dl> <dt>

<span id="MCI_DGV_COPY_AT"></span><span id="mci_dgv_copy_at"></span>MCI\_DGV\_COPY\_AT
</dt> <dd>

A rectangle is included in the **rc** member of the structure identified by *lpCopy*. The rectangle specifies the portion of each frame to copy. If the flag is omitted, MCI\_COPY copies the entire frame.

</dd> <dt>

<span id="MCI_DGV_COPY_AUDIO_STREAM"></span><span id="mci_dgv_copy_audio_stream"></span>MCI\_DGV\_COPY\_AUDIO\_STREAM
</dt> <dd>

An audio-stream number is included in the **dwAudioStream** member of the structure identified by *lpCopy*. If you use this flag and also want to copy video, you must also use the MCI\_DGV\_COPY\_VIDEO\_STREAM flag. (If neither flag is specified, data from all audio and video streams is copied.)

</dd> <dt>

<span id="MCI_DGV_COPY_VIDEO_STREAM"></span><span id="mci_dgv_copy_video_stream"></span>MCI\_DGV\_COPY\_VIDEO\_STREAM
</dt> <dd>

A video-stream number is included in the **dwVideoStream** member of the structure identified by *lpCopy*. If you use this flag and also want to copy audio, you must also use the MCI\_DGV\_COPY\_AUDIO\_STREAM flag. (If neither flag is specified, data from all audio and video streams is copied.)

</dd> <dt>

<span id="MCI_FROM"></span><span id="mci_from"></span>MCI\_FROM
</dt> <dd>

A starting location is included in the **dwFrom** member of the structure identified by *lpCopy*. The units assigned to the position values are specified with the MCI\_SET\_TIME\_FORMAT flag of the [MCI\_SET](mci-set.md) command.

</dd> <dt>

<span id="MCI_TO"></span><span id="mci_to"></span>MCI\_TO
</dt> <dd>

An ending location is included in the **dwTo** member of the structure identified by *lpCopy*. The units assigned to the position values are specified with the MCI\_SET\_TIME\_FORMAT flag of the MCI\_SET command.

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

 

