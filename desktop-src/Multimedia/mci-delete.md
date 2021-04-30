---
title: MCI_DELETE command (Mmsystem.h)
description: The MCI\_DELETE command removes data from the file. Digital-video and waveform-audio devices recognize this command.
ms.assetid: cf7fae86-e81e-4006-9755-fd01f81aeb62
keywords:
- MCI_DELETE command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_DELETE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_DELETE command

The MCI\_DELETE command removes data from the file. Digital-video and waveform-audio devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_DELETE, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_GENERIC_PARMS) lpDelete
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

MCI\_NOTIFY, MCI\_WAIT, or, for digital-video devices, MCI\_TEST. For information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> <dt>

<span id="lpDelete"></span><span id="lpdelete"></span><span id="LPDELETE"></span>*lpDelete*
</dt> <dd>

Pointer to an [**MCI\_GENERIC\_PARMS**](mci-generic-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following flags apply to the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_DELETE_AT"></span><span id="mci_dgv_delete_at"></span>MCI\_DGV\_DELETE\_AT
</dt> <dd>

A rectangle is included in the **rc** member of the structure identified by *lpDelete*. The rectangle specifies the portion of each frame to delete. When this flag is used, the frame is retained in the workspace and the area specified by the rectangle becomes black. If the flag is omitted, MCI\_DELETE defaults to the entire frame and removes the frame from the workspace.

</dd> <dt>

<span id="MCI_DGV_DELETE_AUDIO_STREAM"></span><span id="mci_dgv_delete_audio_stream"></span>MCI\_DGV\_DELETE\_AUDIO\_STREAM
</dt> <dd>

An audio-stream number is included in the **dwAudioStream** member of the structure identified by *lpDelete*. If you use this flag and also want to delete video, you must also use the MCI\_DGV\_DELETE\_VIDEO\_STREAM flag. (If neither flag is specified, data from all audio and video streams is deleted.)

</dd> <dt>

<span id="MCI_DGV_DELETE_VIDEO_STREAM"></span><span id="mci_dgv_delete_video_stream"></span>MCI\_DGV\_DELETE\_VIDEO\_STREAM
</dt> <dd>

A video-stream number is included in the **dwVideoStream** member of the structure identified by *lpDelete*. If you use this flag and also want to delete audio, you must also use the MCI\_DGV\_DELETE\_AUDIO\_STREAM flag. (If neither flag is specified, data from all audio and video streams is deleted.)

</dd> <dt>

<span id="MCI_FROM"></span><span id="mci_from"></span>MCI\_FROM
</dt> <dd>

A starting location is included in the **dwFrom** member of the structure identified by *lpDelete*. The units assigned to the position values are specified with the MCI\_SET\_TIME\_FORMAT flag of the [MCI\_SET](mci-set.md) command.

</dd> <dt>

<span id="MCI_TO"></span><span id="mci_to"></span>MCI\_TO
</dt> <dd>

An ending location is included in the **dwTo** member of the structure identified by *lpDelete*. The units assigned to the position values are specified with the MCI\_SET\_TIME\_FORMAT flag of MCI\_SET.

</dd> </dl>

For digital-video devices, the *lpDelete* parameter points to an [**MCI\_DGV\_DELETE\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_delete_parms) structure.

The following flags apply to the **waveaudio** device type:

<dl> <dt>

<span id="MCI_FROM"></span><span id="mci_from"></span>MCI\_FROM
</dt> <dd>

A starting location is included in the **dwFrom** member of the structure identified by *lpDelete*. The units assigned to the position values are specified with the MCI\_SET\_TIME\_FORMAT flag of [MCI\_SET](mci-set.md).

</dd> <dt>

<span id="MCI_TO"></span><span id="mci_to"></span>MCI\_TO
</dt> <dd>

An ending location is included in the **dwTo** member of the structure identified by *lpDelete*. The units assigned to the position values are specified with the MCI\_SET\_TIME\_FORMAT flag of MCI\_SET.

</dd> </dl>

For waveform-audio devices, the *lpDelete* parameter points to an [**MCI\_WAVE\_DELETE\_PARMS**](mci-wave-delete-parms.md) structure.

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

 

