---
title: MCI_CUE command (Mmsystem.h)
description: The MCI\_CUE command cues a device so that playback or recording begins with minimum delay. Digital-video, VCR, and waveform-audio devices recognize this command.
ms.assetid: 22da4a84-a7af-42df-b950-8d1184fff9ba
keywords:
- MCI_CUE command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_CUE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_CUE command

The MCI\_CUE command cues a device so that playback or recording begins with minimum delay. Digital-video, VCR, and waveform-audio devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_CUE, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_GENERIC_PARMS) lpCue
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

<span id="lpCue"></span><span id="lpcue"></span><span id="LPCUE"></span>*lpCue*
</dt> <dd>

Pointer to an [**MCI\_GENERIC\_PARMS**](mci-generic-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional flags are used with the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_CUE_INPUT"></span><span id="mci_dgv_cue_input"></span>MCI\_DGV\_CUE\_INPUT
</dt> <dd>

A digital-video instance should prepare for recording. If the application has not reserved disk space, the device reserves the disk space using its default parameters. The application can omit this flag if the current presentation source is already the external input. (This flag has no effect on selecting the presentation source.)

</dd> <dt>

<span id="MCI_DGV_CUE_NOSHOW"></span><span id="mci_dgv_cue_noshow"></span>MCI\_DGV\_CUE\_NOSHOW
</dt> <dd>

A digital-video instance should prepare for playing the frame specified with the command without displaying it. When this flag is specified, the display continues to show the image in the frame buffer even though its corresponding frame is not the current position. For example, if the frame buffer contains the image from frame 7, the device continues to show frame 7 when this flag is used to cue the device to any other position. A subsequent cue command without this flag and without the MCI\_TO flag displays the current frame.

</dd> <dt>

<span id="MCI_DGV_CUE_OUTPUT"></span><span id="mci_dgv_cue_output"></span>MCI\_DGV\_CUE\_OUTPUT
</dt> <dd>

A digital-video instance should prepare for playing. If the workspace is paused, no positioning occurs. If the workspace is stopped, the position might change to a previous key-frame image. The application can omit this flag if the current presentation source is already the workspace.

</dd> <dt>

<span id="MCI_TO"></span><span id="mci_to"></span>MCI\_TO
</dt> <dd>

A workspace position is included in the **dwTo** member of the structure identified by *lpCue*. The units assigned to position values are specified using the MCI\_SET\_TIME\_FORMAT flag of the [MCI\_SET](mci-set.md) command. This is equivalent to seeking to a position, except the device is paused after the command.

</dd> </dl>

For **digitalvideo** devices, the *lpCue* parameter points to an [**MCI\_DGV\_CUE\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_cue_parms) structure.

The following additional flags are used with the **vcr** device type:

<dl> <dt>

<span id="MCI_FROM"></span><span id="mci_from"></span>MCI\_FROM
</dt> <dd>

The **dwFrom** member of the structure pointed to by *lpCue* contains the starting location specified in the current time format.

</dd> <dt>

<span id="MCI_TO"></span><span id="mci_to"></span>MCI\_TO
</dt> <dd>

The **dwTo** member of the structure pointed to by *lpCue* contains the ending (pausing) location specified in the current time format.

</dd> <dt>

<span id="MCI_VCR_CUE_INPUT"></span><span id="mci_vcr_cue_input"></span>MCI\_VCR\_CUE\_INPUT
</dt> <dd>

Prepare for recording.

</dd> <dt>

<span id="MCI_VCR_CUE_OUTPUT"></span><span id="mci_vcr_cue_output"></span>MCI\_VCR\_CUE\_OUTPUT
</dt> <dd>

Prepare for playing. If neither MCI\_VCR\_CUE\_INPUT nor MCI\_VCR\_CUE\_OUTPUT is specified, MCI\_VCR\_CUE\_OUTPUT is assumed.

</dd> <dt>

<span id="MCI_VCR_CUE_PREROLL"></span><span id="mci_vcr_cue_preroll"></span>MCI\_VCR\_CUE\_PREROLL
</dt> <dd>

Cue the device to the current position, or the **dwFrom** position, minus the preroll duration. This will allow the device to prepare itself before entering record or playback mode.

</dd> <dt>

<span id="MCI_VCR_CUE_REVERSE"></span><span id="mci_vcr_cue_reverse"></span>MCI\_VCR\_CUE\_REVERSE
</dt> <dd>

The direction of the next play or record command is reverse.

</dd> </dl>

When cueing for playback by using the MCI\_CUE command with the MCI\_VCR\_CUE\_OUTPUT flag, you can cancel MCI\_CUE by issuing the [MCI\_PLAY](mci-play.md) command with MCI\_FROM, MCI\_TO, or MCI\_VCR\_PLAY\_REVERSE.

When cueing for recording by using MCI\_CUE with the MCI\_VCR\_CUE\_INPUT flag, you can cancel MCI\_CUE by issuing the [MCI\_RECORD](mci-record.md) command with MCI\_FROM, MCI\_TO, or MCI\_VCR\_RECORD\_INITIALIZE.

For **vcr** devices, the *lpCue* parameter points to an [**MCI\_VCR\_CUE\_PARMS**](mci-vcr-cue-parms.md) structure.

The following additional flags are used with the **waveaudio** device type:

<dl> <dt>

<span id="MCI_WAVE_INPUT"></span><span id="mci_wave_input"></span>MCI\_WAVE\_INPUT
</dt> <dd>

A waveform-audio input device should be cued.

</dd> <dt>

<span id="MCI_WAVE_OUTPUT"></span><span id="mci_wave_output"></span>MCI\_WAVE\_OUTPUT
</dt> <dd>

A waveform-audio output device should be cued. This is the default flag if a flag is not specified.

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

 

