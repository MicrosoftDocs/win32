---
title: MCI_RECORD command (Mmsystem.h)
description: The MCI\_RECORD command starts recording from the current position or from one specified location to another specified location.
ms.assetid: d3c4e8a3-7d81-428e-91d8-d8d63fc0aa02
keywords:
- MCI_RECORD command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_RECORD
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_RECORD command

The [**MCI\_RECORD**](mci-record-parms.md) command starts recording from the current position or from one specified location to another specified location. VCR and waveform-audio devices recognize this command. Although digital-video devices and MIDI sequencers also recognize this command, the MCIAVI and MCISEQ drivers do not implement it.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_RECORD, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_RECORD_PARMS) lpRecord
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

MCI\_NOTIFY, MCI\_WAIT, or, for digital-video and VCR devices, MCI\_TEST. For information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> <dt>

<span id="lpRecord"></span><span id="lprecord"></span><span id="LPRECORD"></span>*lpRecord*
</dt> <dd>

Pointer to an [**MCI\_RECORD\_PARMS**](mci-record-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

This command is supported by devices that return **TRUE** when you call the [MCI\_GETDEVCAPS](mci-getdevcaps.md) command with the MCI\_GETDEVCAPS\_CAN\_RECORD flag. For the MCIWAVE driver, all data recorded after a file is opened is discarded if the file is closed without saving it.

The following additional flags apply to all devices supporting MCI\_RECORD:

<dl> <dt>

<span id="MCI_FROM"></span><span id="mci_from"></span>MCI\_FROM
</dt> <dd>

A starting location is included in the **dwFrom** member of the structure identified by *lpRecord*. The units assigned to the position values are specified with the MCI\_SET\_TIME\_FORMAT flag of the [MCI\_SET](mci-set.md) command. If MCI\_FROM is not specified, the starting location defaults to the current position.

</dd> <dt>

<span id="MCI_RECORD_INSERT"></span><span id="mci_record_insert"></span>MCI\_RECORD\_INSERT
</dt> <dd>

Newly recorded information should be inserted or pasted into the existing data. Some devices might not support this. If supported, this is the default.

</dd> <dt>

<span id="MCI_RECORD_OVERWRITE"></span><span id="mci_record_overwrite"></span>MCI\_RECORD\_OVERWRITE
</dt> <dd>

Data should overwrite existing data. The MCIWAVE.DRV device returns MCIERR\_UNSUPPORTED\_FUNCTION in response to this flag.

</dd> <dt>

<span id="MCI_TO"></span><span id="mci_to"></span>MCI\_TO
</dt> <dd>

An ending location is included in the **dwTo** member of the structure identified by *lpRecord*. The units assigned to the position values are specified with the MCI\_SET\_TIME\_FORMAT flag of the [MCI\_SET](mci-set.md) command. If MCI\_TO is not specified, the ending location defaults to the end of the content.

</dd> </dl>

The following additional flags are used with the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_RECORD_AUDIO_STREAM"></span><span id="mci_dgv_record_audio_stream"></span>MCI\_DGV\_RECORD\_AUDIO\_STREAM
</dt> <dd>

An audio-stream number is included in the **dwAudioStream** member of the structure identified by *lpRecord*. If you omit this flag, audio data is recorded into the first physical stream.

</dd> <dt>

<span id="MCI_DGV_RECORD_HOLD"></span><span id="mci_dgv_record_hold"></span>MCI\_DGV\_RECORD\_HOLD
</dt> <dd>

When recording stops, the screen will hold the last image and will not resume showing the video until an [MCI\_MONITOR](mci-monitor.md) command is issued.

</dd> <dt>

<span id="MCI_DGV_RECORD_VIDEO_STREAM"></span><span id="mci_dgv_record_video_stream"></span>MCI\_DGV\_RECORD\_VIDEO\_STREAM
</dt> <dd>

A video-stream number is included in the **dwVideoStream** member of the structure identified by *lpRecord*. If you omit this flag, video data is recorded into the first physical stream.

</dd> <dt>

<span id="MCI_DGV_RECT"></span><span id="mci_dgv_rect"></span>MCI\_DGV\_RECT
</dt> <dd>

A rectangle is specified in the **rc** member of the structure identified by *lpRecord*. The rectangle specifies the region of the external input used as the source for the pixels compressed and saved. This rectangle defaults to the rectangle specified (or defaulted) by the MCI\_DGV\_PUT\_VIDEO flag for the [MCI\_PUT](mci-put.md) command. When it is set differently than the video rectangle, what is displayed is not what is recorded

</dd> </dl>

For digital-video devices, *lpRecord* points to an [**MCI\_DGV\_RECORD\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_record_parms) structure.

The following additional flags are used with the **vcr** device type:

<dl> <dt>

<span id="MCI_VCR_RECORD_AT"></span><span id="mci_vcr_record_at"></span>MCI\_VCR\_RECORD\_AT
</dt> <dd>

The **dwAt** member of the structure identified by *lpRecord* contains a time when the entire command begins, or if the device is cued, when the device reaches the from position given by the cue command.

</dd> <dt>

<span id="MCI_VCR_RECORD_INITIALIZE"></span><span id="mci_vcr_record_initialize"></span>MCI\_VCR\_RECORD\_INITIALIZE
</dt> <dd>

Seek the device to the start of the media, begin recording blank video and audio, and record timecode, if possible.

</dd> </dl>

For VCR devices, *lpRecord* points to an [**MCI\_VCR\_RECORD\_PARMS**](mci-vcr-record-parms.md) structure.

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

 

