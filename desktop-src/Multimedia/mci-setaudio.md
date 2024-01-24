---
title: MCI_SETAUDIO command (Mmsystem.h)
description: The MCI\_SETAUDIO command sets values associated with audio playback and capture. Digital-video and VCR devices recognize this command.
ms.assetid: 78624596-e465-4ef1-8988-edcfe9a46f89
keywords:
- MCI_SETAUDIO command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_SETAUDIO
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_SETAUDIO command

The MCI\_SETAUDIO command sets values associated with audio playback and capture. Digital-video and VCR devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_SETAUDIO, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_GENERIC_PARMS) lpSetAudio
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

<span id="lpSetAudio"></span><span id="lpsetaudio"></span><span id="LPSETAUDIO"></span>*lpSetAudio*
</dt> <dd>

Pointer to an [**MCI\_GENERIC\_PARMS**](mci-generic-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following flags apply to the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_SETAUDIO_ALG"></span><span id="mci_dgv_setaudio_alg"></span>MCI\_DGV\_SETAUDIO\_ALG
</dt> <dd>

The **lpstrAlgorithm** member of the structure identified by *lpSetAudio* contains an address of a buffer containing the name of an audio compression algorithm. The compression algorithm is used by subsequent [MCI\_RESERVE](mci-reserve.md) or [MCI\_RECORD](mci-record.md) commands. The available algorithms are device dependent. If the algorithm is incompatible with the current file format, the file format is changed to the default format for the algorithm.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_CLOCKTIME"></span><span id="mci_dgv_setaudio_clocktime"></span>MCI\_DGV\_SETAUDIO\_CLOCKTIME
</dt> <dd>

The time specified is in milliseconds and is absolute time when used with MCI\_DGV\_SETAUDIO\_OVER. (This time is not in step with the playing of the workspace.)

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_INPUT"></span><span id="mci_dgv_setaudio_input"></span>MCI\_DGV\_SETAUDIO\_INPUT
</dt> <dd>

Modifies the bass, treble, or volume flag so that it affects the input signal and modifies what is recorded. If possible, this is the default when monitoring the input.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_ITEM"></span><span id="mci_dgv_setaudio_item"></span>MCI\_DGV\_SETAUDIO\_ITEM
</dt> <dd>

An audio constant is specified in the **dwItem** member of the structure identified by *lpSetAudio*. The constant identifies the value that is being set. The following constants are defined:

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_AVGBYTESPERSEC"></span><span id="mci_dgv_setaudio_avgbytespersec"></span>MCI\_DGV\_SETAUDIO\_AVGBYTESPERSEC
</dt> <dd>

The average number of bytes is specified in the **dwValue** member of the structure identified by *lpSetAudio*. This value sets the average number of bytes per second for playing or recording in the PCM (Pulse Code Modulation) and ADPCM (Adaptive Differential Pulse Code Modulation) formats. The file is saved in this format.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_BASS"></span><span id="mci_dgv_setaudio_bass"></span>MCI\_DGV\_SETAUDIO\_BASS
</dt> <dd>

The audio low frequency level is specified as a factor in the **dwValue** member of the structure identified by *lpSetAudio*.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_BITSPERSAMPLE"></span><span id="mci_dgv_setaudio_bitspersample"></span>MCI\_DGV\_SETAUDIO\_BITSPERSAMPLE
</dt> <dd>

The number of bits per sample is specified in the **dwValue** member of the structure identified by *lpSetAudio*. This value sets the number of bits per sample played or recorded in the PCM format. The file is saved in this format.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_BLOCKALIGN"></span><span id="mci_dgv_setaudio_blockalign"></span>MCI\_DGV\_SETAUDIO\_BLOCKALIGN
</dt> <dd>

The data block alignment is specified in the **dwValue** member of the structure identified by *lpSetAudio*. This value sets the alignment of data blocks relative to the start of input waveform data.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_SAMPLESPERSEC"></span><span id="mci_dgv_setaudio_samplespersec"></span>MCI\_DGV\_SETAUDIO\_SAMPLESPERSEC
</dt> <dd>

The sample rate is specified in the **dwValue** member of the structure identified by *lpSetAudio*. This value sets the sample rate for playing and recording with the PCM and ADPCM algorithms. The file is saved in this format.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_SOURCE"></span><span id="mci_dgv_setaudio_source"></span>MCI\_DGV\_SETAUDIO\_SOURCE
</dt> <dd>

A constant specifying the source of audio input is included in the **dwValue** member of the structure identified by *lpSetAudio*. The following constants are defined for the audio input sources:

MCI\_DGV\_SETAUDIO\_SOURCE\_AVERAGE

The average of the left and right audio channels.

MCI\_DGV\_SETAUDIO\_SOURCE\_LEFT

Left audio channel.

MCI\_DGV\_SETAUDIO\_SOURCE\_RIGHT

Right audio channel.

MCI\_DGV\_SETAUDIO\_SOURCE\_STEREO

Stereo.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_STREAM"></span><span id="mci_dgv_setaudio_stream"></span>MCI\_DGV\_SETAUDIO\_STREAM
</dt> <dd>

An audio-stream is specified in the **dwValue** member of the structure identified by *lpSetAudio*. The integer value specifies the audio stream played back from the workspace. If the stream is not specified, the first physically interleaved audio stream is played.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_TREBLE"></span><span id="mci_dgv_setaudio_treble"></span>MCI\_DGV\_SETAUDIO\_TREBLE
</dt> <dd>

The audio high-frequency level is specified as a factor in the **dwValue** member of the structure identified by *lpSetAudio*.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_VOLUME"></span><span id="mci_dgv_setaudio_volume"></span>MCI\_DGV\_SETAUDIO\_VOLUME
</dt> <dd>

The audio level for one or both audio channels is specified as a factor in the **dwValue** member of the structure identified by *lpSetAudio*. If the left and right volumes have been set to different values, then the ratio of left to right volume is approximately unchanged.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_LEFT"></span><span id="mci_dgv_setaudio_left"></span>MCI\_DGV\_SETAUDIO\_LEFT
</dt> <dd>

Enables the left audio channel when used with MCI\_SET\_ON. Disables the left audio channel when used with MCI\_SET\_OFF. When this flag is used with the combination of MCI\_DGV\_SETAUDIO\_VALUE and MCI\_DGV\_SETAUDIO\_VOLUME, it sets the volume of the left audio channel. When this flag is used with MCI\_DGV\_SETAUDIO\_SOURCE, it specifies the left audio channel as the source for the audio input digitizer.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_OVER"></span><span id="mci_dgv_setaudio_over"></span>MCI\_DGV\_SETAUDIO\_OVER
</dt> <dd>

A transition length parameter is included in the **dwOver** member of the structure identified by *lpSetAudio*. The length value specifies how long (in units of the current time format) it should take to make a change that uses a factor. If this flag is not used, changes occur immediately.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_QUALITY"></span><span id="mci_dgv_setaudio_quality"></span>MCI\_DGV\_SETAUDIO\_QUALITY
</dt> <dd>

The **lpstrQuality** member of the structure identified by *lpSetAudio* contains an address of a buffer defining the audio quality. A text-string within the buffer specifies the characteristics of the audio compression algorithm.

The MCI\_DGV\_SETAUDIO\_ALG flag can be used to select a quality descriptor for the specified algorithm. If this flag is omitted, then the current algorithm is used.

The algorithms and descriptor names available depend on the device. Each device supplies documentation for the available algorithms and a description of the applicable descriptor names. The [MCI\_QUALITY](mci-quality.md) command can define additional descriptor names.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_RECORD"></span><span id="mci_dgv_setaudio_record"></span>MCI\_DGV\_SETAUDIO\_RECORD
</dt> <dd>

Specifies whether recording includes or excludes audio data. When combined with MCI\_SET\_ON, audio data is recorded. When combined with MCI\_SET\_OFF, audio data is excluded. The default includes audio data.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_RIGHT"></span><span id="mci_dgv_setaudio_right"></span>MCI\_DGV\_SETAUDIO\_RIGHT
</dt> <dd>

Enables the right audio channel when used with MCI\_SET\_ON. Disables the right audio channel when used with MCI\_SET\_OFF. When this flag is used with the combination of MCI\_DGV\_SETAUDIO\_VALUE and MCI\_DGV\_SETAUDIO\_VOLUME, it sets the volume of the right audio channel.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_VALUE"></span><span id="mci_dgv_setaudio_value"></span>MCI\_DGV\_SETAUDIO\_VALUE
</dt> <dd>

A value is specified in the **dwValue** member of the structure identified by *lpSetAudio*. The meaning of the value is specified by the constant defined for the MCI\_DGV\_SETAUDIO\_ITEM flag.

</dd> <dt>

<span id="MCI_SET_OFF"></span><span id="mci_set_off"></span>MCI\_SET\_OFF
</dt> <dd>

Disables the specified audio channel.

</dd> <dt>

<span id="MCI_SET_ON"></span><span id="mci_set_on"></span>MCI\_SET\_ON
</dt> <dd>

Enables the specified audio channel.

</dd> <dt>

<span id="MCI_SETAUDIO_OUTPUT"></span><span id="mci_setaudio_output"></span>MCI\_SETAUDIO\_OUTPUT
</dt> <dd>

Modifies the bass, treble, or volume flag so that it modifies only the played signal and not what is recorded. If possible, this is the default when monitoring the input.

</dd> </dl>

For digital-video devices, the *lpSetAudio* parameter points to an [**MCI\_DGV\_SETAUDIO\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_setaudio_parmsa) structure.

The following additional flags are used with the **vcr** device type:

<dl> <dt>

<span id="MCI_VCR_SETAUDIO_RECORD"></span><span id="mci_vcr_setaudio_record"></span>MCI\_VCR\_SETAUDIO\_RECORD
</dt> <dd>

Sets the audio recording to on or off, which is used in conjunction with one of following flags:

MCI\_SET\_ON

Audio recording on.

MCI\_SET\_OFF

Audio recording off. It might be necessary to first turn off the assemble recording (using the [MCI\_SET](mci-set.md) command with the MCI\_VCR\_SET\_ASSEMBLE\_RECORD flag set to off) before the audio recording can be turned off.

MCI\_TRACK

The **dwTrack** member of the structure identified by *lpSetAudio* specifies which track is affected by the command.

MCI\_VCR\_SETAUDIO\_SOURCE

Sets the audio source. This flag must be used with the MCI\_VCR\_SETAUDIO\_TO flag.

MCI\_VCR\_SETAUDIO\_MONITOR

Sets the audio source monitor. This flag must be used with the MCI\_VCR\_SETAUDIO\_TO flag.

MCI\_VCR\_SETAUDIO\_TO

The **dwTo** member of the structure identified by *lpSetAudio* contains a constant describing the type of input or monitored input. It must be one of the following:

<dl> <dd>

MCI\_VCR\_SRC\_TYPE\_TUNER

Type is tuner.

</dd> <dd>

MCI\_VCR\_SRC\_TYPE\_LINE

Type is line.

</dd> <dd>

MCI\_VCR\_SRC\_TYPE\_AUX

Type is auxiliary.

</dd> <dd>

MCI\_VCR\_SRC\_TYPE\_GENERIC

Type is generic.

</dd> <dd>

MCI\_VCR\_SRC\_TYPE\_MUTE

Type is mute. This can be used only with the MCI\_VCR\_SETAUDIO\_SOURCE flag.

</dd> <dd>

MCI\_VCR\_SRC\_TYPE\_OUTPUT

Type is output.

</dd> <dd>

MCI\_VCR\_SETAUDIO\_NUMBER

The dwNumber member of the structure identified by lpSetAudio contains the audio input (of the type specified in the dwTo member) to use.

</dd> </dl> </dd> <dt>


</dt> <dd></dd> <dt>


</dt> <dd></dd> <dt>


</dt> <dd></dd> </dl>

For VCR devices, the *lpSetAudio* parameter points to an [**MCI\_VCR\_SETAUDIO\_PARMS**](mci-vcr-setaudio-parms.md) structure.

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

 

