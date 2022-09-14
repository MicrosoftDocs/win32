---
title: MCI_PLAY command (Mmsystem.h)
description: The MCI\_PLAY command signals the device to begin transmitting output data. CD audio, digital-video, MIDI sequencer, videodisc, VCR, and waveform-audio devices recognize this command.
ms.assetid: d912ab49-63f0-40a9-aa4c-f9463782b54c
keywords:
- MCI_PLAY command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_PLAY
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_PLAY command

The MCI\_PLAY command signals the device to begin transmitting output data. CD audio, digital-video, MIDI sequencer, videodisc, VCR, and waveform-audio devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_PLAY, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_PLAY_PARMS ) lpPlay
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

<span id="lpPlay"></span><span id="lpplay"></span><span id="LPPLAY"></span>*lpPlay*
</dt> <dd>

Pointer to an [**MCI\_PLAY\_PARMS**](mci-play-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional flags apply to all devices supporting MCI\_PLAY:

<dl> <dt>

<span id="MCI_FROM"></span><span id="mci_from"></span>MCI\_FROM
</dt> <dd>

A starting location is included in the **dwFrom** member of the structure identified by *lpPlay*. The units assigned to the position values are specified with the MCI\_SET\_TIME\_FORMAT flag of the [MCI\_SET](mci-set.md) command. If MCI\_FROM is not specified, the starting location defaults to the current position.

</dd> <dt>

<span id="MCI_TO"></span><span id="mci_to"></span>MCI\_TO
</dt> <dd>

An ending location is included in the **dwTo** member of the structure identified by *lpPlay*. The units assigned to the position values are specified with the MCI\_SET\_TIME\_FORMAT flag of MCI\_SET. If MCI\_TO is not specified, the ending location defaults to the end of the media.

</dd> </dl>

The following additional flags are used with the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_PLAY_REPEAT"></span><span id="mci_dgv_play_repeat"></span>MCI\_DGV\_PLAY\_REPEAT
</dt> <dd>

Playback should start again at the beginning when the end of the content is reached.

</dd> <dt>

<span id="MCI_DGV_PLAY_REVERSE"></span><span id="mci_dgv_play_reverse"></span>MCI\_DGV\_PLAY\_REVERSE
</dt> <dd>

Playback should occur in reverse.

</dd> <dt>

<span id="MCI_MCIAVI_PLAY_WINDOW"></span><span id="mci_mciavi_play_window"></span>MCI\_MCIAVI\_PLAY\_WINDOW
</dt> <dd>

Playback should occur in the window associated with a device instance (the default). (This flag is specific to MCIAVI.DRV.)

</dd> <dt>

<span id="MCI_MCIAVI_PLAY_FULLSCREEN"></span><span id="mci_mciavi_play_fullscreen"></span>MCI\_MCIAVI\_PLAY\_FULLSCREEN
</dt> <dd>

Playback should use a full-screen display. Use this flag only when playing compressed or 8-bit files.

</dd> </dl>

For digital-video devices, *lpPlay* points to an [**MCI\_DGV\_PLAY\_PARMS**](/previous-versions//dd743396(v=vs.85)) structure.

The following additional flags are used with the **vcr** device type:

<dl> <dt>

<span id="MCI_VCR_PLAY_AT"></span><span id="mci_vcr_play_at"></span>MCI\_VCR\_PLAY\_AT
</dt> <dd>

The **dwAt** member of the structure identified by *lpPlay* contains a time when the entire command begins, or if the device is cued, when the device reaches the from position given by the [MCI\_CUE](mci-cue.md) command.

</dd> <dt>

<span id="MCI_VCR_PLAY_REVERSE"></span><span id="mci_vcr_play_reverse"></span>MCI\_VCR\_PLAY\_REVERSE
</dt> <dd>

Playback should occur in reverse.

</dd> <dt>

<span id="MCI_VCR_PLAY_SCAN"></span><span id="mci_vcr_play_scan"></span>MCI\_VCR\_PLAY\_SCAN
</dt> <dd>

Playback should be as fast as possible while maintaining video output.

</dd> </dl>

For VCR devices, *lpPlay* points to an [**MCI\_VCR\_PLAY\_PARMS**](mci-vcr-play-parms.md) structure.

The following additional flags are used with the **videodisc** device type:

<dl> <dt>

<span id="MCI_VD_PLAY_FAST"></span><span id="mci_vd_play_fast"></span>MCI\_VD\_PLAY\_FAST
</dt> <dd>

Play fast.

</dd> <dt>

<span id="MCI_VD_PLAY_REVERSE"></span><span id="mci_vd_play_reverse"></span>MCI\_VD\_PLAY\_REVERSE
</dt> <dd>

Play in reverse.

</dd> <dt>

<span id="MCI_VD_PLAY_SCAN"></span><span id="mci_vd_play_scan"></span>MCI\_VD\_PLAY\_SCAN
</dt> <dd>

Scan quickly.

</dd> <dt>

<span id="MCI_VD_PLAY_SLOW"></span><span id="mci_vd_play_slow"></span>MCI\_VD\_PLAY\_SLOW
</dt> <dd>

Play slowly.

</dd> <dt>

<span id="MCI_VD_PLAY_SPEED"></span><span id="mci_vd_play_speed"></span>MCI\_VD\_PLAY\_SPEED
</dt> <dd>

The play speed is included in the **dwSpeed** member in the structure identified by *lpPlay*.

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

 

