---
title: MCI_SET command (Mmsystem.h)
description: The MCI\_SET command sets device information. CD audio, digital-video, MIDI sequencer, VCR, videodisc, video-overlay, and waveform-audio devices recognize this command.
ms.assetid: c527f9d6-2119-4274-98b7-dc892e9b70f9
keywords:
- MCI_SET command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_SET
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---



# MCI\_SET command

> [!NOTE]
> Bias-free Communication
Microsoft supports a diverse and inclusionary environment.  Within this document, there are references to the word 'slave.' Microsoft's [Style Guide for Bias-Free Communications](https://github.com/MicrosoftDocs/microsoft-style-guide/blob/master/styleguide/bias-free-communication.md) recognizes this as an exclusionary word.  This wording is used as it is currently the wording used within the commands. For consistency, this document contains this word. When this word is altered in the commands, we will correct this document to be in alignment.

The MCI\_SET command sets device information. CD audio, digital-video, MIDI sequencer, VCR, videodisc, video-overlay, and waveform-audio devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_SET, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_SET_PARMS) lpSet
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

<span id="lpSet"></span><span id="lpset"></span><span id="LPSET"></span>*lpSet*
</dt> <dd>

Pointer to an [**MCI\_SET\_PARMS**](mci-set-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional flags apply to all devices supporting MCI\_SET:

<dl> <dt>

<span id="MCI_SET_AUDIO"></span><span id="mci_set_audio"></span>MCI\_SET\_AUDIO
</dt> <dd>

An audio channel number is included in the dwAudio member of the structure identified by *lpSet*. This flag must be used with MCI\_SET\_ON or MCI\_SET\_OFF. Use one of the following constants to indicate the channel number:

</dd> <dt>

<span id="MCI_SET_AUDIO_ALL"></span><span id="mci_set_audio_all"></span>MCI\_SET\_AUDIO\_ALL
</dt> <dd>

All audio channels.

</dd> <dt>

<span id="MCI_SET_AUDIO_LEFT"></span><span id="mci_set_audio_left"></span>MCI\_SET\_AUDIO\_LEFT
</dt> <dd>

Left channel.

</dd> <dt>

<span id="MCI_SET_AUDIO_RIGHT"></span><span id="mci_set_audio_right"></span>MCI\_SET\_AUDIO\_RIGHT
</dt> <dd>

Right channel.

</dd> <dt>

<span id="MCI_SET_DOOR_CLOSED"></span><span id="mci_set_door_closed"></span>MCI\_SET\_DOOR\_CLOSED
</dt> <dd>

Closes the media cover (if any).

</dd> <dt>

<span id="MCI_SET_DOOR_OPEN"></span><span id="mci_set_door_open"></span>MCI\_SET\_DOOR\_OPEN
</dt> <dd>

Opens the media cover (if any).

</dd> <dt>

<span id="MCI_SET_OFF"></span><span id="mci_set_off"></span>MCI\_SET\_OFF
</dt> <dd>

Disables the specified video or audio channel.

</dd> <dt>

<span id="MCI_SET_ON"></span><span id="mci_set_on"></span>MCI\_SET\_ON
</dt> <dd>

Enables the specified video or audio channel.

</dd> <dt>

<span id="MCI_SET_TIME_FORMAT"></span><span id="mci_set_time_format"></span>MCI\_SET\_TIME\_FORMAT
</dt> <dd>

A time format parameter is included in the **dwTimeFormat** member of the structure identified by *lpSet*. The following flags are used with this flag:

</dd> <dt>

<span id="MCI_FORMAT_BYTES"></span><span id="mci_format_bytes"></span>MCI\_FORMAT\_BYTES
</dt> <dd>

Within a PCM (Pulse Code Modulation) data format, changes the time member description to bytes for input or output. Recognized by the **waveaudio** device type.

</dd> <dt>

<span id="MCI_FORMAT_FRAMES"></span><span id="mci_format_frames"></span>MCI\_FORMAT\_FRAMES
</dt> <dd>

Subsequent commands will use frames. Recognized by the **digitalvideo**, **vcr**, and **videodisc** device types.

</dd> <dt>

<span id="MCI_FORMAT_HMS"></span><span id="mci_format_hms"></span>MCI\_FORMAT\_HMS
</dt> <dd>

Changes the time format to hours, minutes, and seconds. Recognized by the **vcr** and **videodisc** device types.

</dd> <dt>

<span id="MCI_FORMAT_MILLISECONDS"></span><span id="mci_format_milliseconds"></span>MCI\_FORMAT\_MILLISECONDS
</dt> <dd>

Changes the time format to milliseconds. Recognized by all device types.

</dd> <dt>

<span id="MCI_FORMAT_MSF"></span><span id="mci_format_msf"></span>MCI\_FORMAT\_MSF
</dt> <dd>

Changes the time format to minutes, seconds, and frames. Recognized by the **cdaudio** and **vcr** device types.

</dd> <dt>

<span id="MCI_FORMAT_SAMPLES"></span><span id="mci_format_samples"></span>MCI\_FORMAT\_SAMPLES
</dt> <dd>

Changes the time format to samples for input or output. Recognized by the **waveaudio** device type.

</dd> <dt>

<span id="MCI_FORMAT_SMPTE_24__MCI_FORMAT_SMPTE_25__and_MCI_FORMAT_SMPTE_30"></span><span id="mci_format_smpte_24__mci_format_smpte_25__and_mci_format_smpte_30"></span><span id="MCI_FORMAT_SMPTE_24__MCI_FORMAT_SMPTE_25__AND_MCI_FORMAT_SMPTE_30"></span>MCI\_FORMAT\_SMPTE\_24, MCI\_FORMAT\_SMPTE\_25, and MCI\_FORMAT\_SMPTE\_30
</dt> <dd>

Sets the time format to 24, 25, and 30 frame SMPTE (Society of Motion Picture and Television Engineers), respectively. Recognized by the **sequencer** and **vcr** device types.

</dd> <dt>

<span id="MCI_FORMAT_SMPTE_30DROP"></span><span id="mci_format_smpte_30drop"></span>MCI\_FORMAT\_SMPTE\_30DROP
</dt> <dd>

Sets the time format to 30 drop-frame SMPTE. Recognized by the **sequencer** and **vcr** device types.

</dd> <dt>

<span id="MCI_FORMAT_TMSF"></span><span id="mci_format_tmsf"></span>MCI\_FORMAT\_TMSF
</dt> <dd>

Changes the time format to tracks, minutes, seconds, and frames. (MCI uses continuous track numbers.) Recognized by the **cdaudio** and **vcr** device types.

</dd> <dt>

<span id="MCI_SET_VIDEO"></span><span id="mci_set_video"></span>MCI\_SET\_VIDEO
</dt> <dd>

Sets the video signal on or off. This flag must be used with either MCI\_SET\_ON or MCI\_SET\_OFF. Devices that do not have video return MCIERR\_UNSUPPORTED\_FUNCTION.

</dd> <dt>


</dt> <dd></dd> <dt>


</dt> <dd></dd> </dl>

The following additional flags are used with the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_SET_FILEFORMAT"></span><span id="mci_dgv_set_fileformat"></span>MCI\_DGV\_SET\_FILEFORMAT
</dt> <dd>

A file format parameter is included in the **dwFileFormat** member of the structure identified by *lpSet*. For digital-video devices, the file format is used for save or capture commands. If omitted, this might default to a device driver defined format. If the specified file format conflicts with the currently selected algorithm and quality, then they are changed to the defaults for the file format. The following file format constants are defined:

</dd> <dt>

<span id="MCI_DGV_FF_AVI"></span><span id="mci_dgv_ff_avi"></span>MCI\_DGV\_FF\_AVI
</dt> <dd>

AVI format.

</dd> <dt>

<span id="MCI_DGV_FF_AVSS"></span><span id="mci_dgv_ff_avss"></span>MCI\_DGV\_FF\_AVSS
</dt> <dd>

AVSS format.

</dd> <dt>

<span id="MCI_DGV_FF_DIB"></span><span id="mci_dgv_ff_dib"></span>MCI\_DGV\_FF\_DIB
</dt> <dd>

DIB format.

</dd> <dt>

<span id="MCI_DGV_FF_JFIF"></span><span id="mci_dgv_ff_jfif"></span>MCI\_DGV\_FF\_JFIF
</dt> <dd>

JFIF format.

</dd> <dt>

<span id="MCI_DGV_FF_JPEG"></span><span id="mci_dgv_ff_jpeg"></span>MCI\_DGV\_FF\_JPEG
</dt> <dd>

JPEG format.

</dd> <dt>

<span id="MCI_DGV_FF_MPEG"></span><span id="mci_dgv_ff_mpeg"></span>MCI\_DGV\_FF\_MPEG
</dt> <dd>

MPEG format.

</dd> <dt>

<span id="MCI_DGV_FF_RDIB"></span><span id="mci_dgv_ff_rdib"></span>MCI\_DGV\_FF\_RDIB
</dt> <dd>

RLE DIB format.

</dd> <dt>

<span id="MCI_DGV_FF_RJPEG"></span><span id="mci_dgv_ff_rjpeg"></span>MCI\_DGV\_FF\_RJPEG
</dt> <dd>

RJPEG format.

</dd> <dt>

<span id="MCI_DGV_SET_SEEK_EXACTLY"></span><span id="mci_dgv_set_seek_exactly"></span>MCI\_DGV\_SET\_SEEK\_EXACTLY
</dt> <dd>

Sets the format used for positioning. This flag must be used with MCI\_SET\_ON or MCI\_SET\_OFF. If MCI\_SET\_ON is specified, playing or recording precisely accesses the frame specified with the MCI\_FROM flag. This might add some extra delay if the requested frame is not a key frame. If MCI\_SET\_OFF is specified, the device will seek to a key-frame image that precedes the requested frame. For some files and devices, this might be the first frame of the file. The default for this flag is device dependent.

</dd> <dt>

<span id="MCI_DGV_SET_SPEED"></span><span id="mci_dgv_set_speed"></span>MCI\_DGV\_SET\_SPEED
</dt> <dd>

A speed parameter is included in the **dwSpeed** member of the structure identified by *lpSet*. Speed is specified as a ratio between the nominal frame rate and the desired frame rate where the nominal frame rate is designated as 1000. Half speed is 500 and double speed is 2000. The allowable speed range is dependent on the device and possibly the file, too.

</dd> <dt>

<span id="MCI_DGV_SET_STILL"></span><span id="mci_dgv_set_still"></span>MCI\_DGV\_SET\_STILL
</dt> <dd>

When used with MCI\_DGV\_SET\_FILEFORMAT, MCI\_SET sets the file format used for capture commands.

</dd> <dt>


</dt> <dd></dd> <dt>


</dt> <dd></dd> </dl>

For digital-video devices, the *lpSet* parameter points to an [**MCI\_DGV\_SET\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_set_parms) structure.

The following additional flags are used with the **sequencer** device type:

<dl> <dt>

<span id="MCI_SEQ_FORMAT_SONGPTR"></span><span id="mci_seq_format_songptr"></span>MCI\_SEQ\_FORMAT\_SONGPTR
</dt> <dd>

Sets the time format to song pointer units.

</dd> <dt>

<span id="MCI_SEQ_SET_MASTER"></span><span id="mci_seq_set_master"></span>MCI\_SEQ\_SET\_MASTER
</dt> <dd>

Sets the sequencer as a source of synchronization data and indicates that the type of synchronization is specified in the **dwMaster** member of the structure identified by *lpSet*. MCISEQ returns MCIERR\_UNSUPPORTED\_FUNCTION. The following constants are defined for the synchronization type:

</dd> <dt>

<span id="MCI_SEQ_MIDI"></span><span id="mci_seq_midi"></span>MCI\_SEQ\_MIDI
</dt> <dd>

The sequencer will send MIDI format synchronization data.

</dd> <dt>

<span id="MCI_SEQ_SMPTE"></span><span id="mci_seq_smpte"></span>MCI\_SEQ\_SMPTE
</dt> <dd>

The sequencer will send SMPTE format synchronization data.

</dd> <dt>

<span id="MCI_SEQ_NONE"></span><span id="mci_seq_none"></span>MCI\_SEQ\_NONE
</dt> <dd>

The sequencer will not send synchronization data.

</dd> <dt>

<span id="MCI_SEQ_SET_OFFSET"></span><span id="mci_seq_set_offset"></span>MCI\_SEQ\_SET\_OFFSET
</dt> <dd>

Changes the SMPTE offset of a sequence to that specified by the **dwOffset** member of the structure identified by *lpSet*. This affects only sequences with a SMPTE division type.

</dd> <dt>

<span id="MCI_SEQ_SET_PORT"></span><span id="mci_seq_set_port"></span>MCI\_SEQ\_SET\_PORT
</dt> <dd>

Sets the output MIDI port of a sequence to that specified by the MIDI device identifier in the **dwPort** member of the structure identified by *lpSet*. The device closes the previous port (if any), and attempts to open and use the new port. If it fails, it returns an error and reopens the previously used port (if any). The following constants are defined for the ports:

</dd> <dt>

<span id="MCI_SEQ_NONE"></span><span id="mci_seq_none"></span>MCI\_SEQ\_NONE
</dt> <dd>

Closes the previously used port (if any). The sequencer behaves exactly the same as if a port were open, except no MIDI message is sent.

</dd> <dt>

<span id="MIDI_MAPPER"></span><span id="midi_mapper"></span>MIDI\_MAPPER
</dt> <dd>

Sets the port opened to the MIDI mapper.

</dd> <dt>

<span id="MCI_SEQ_SET_SLAVE"></span><span id="mci_seq_set_slave"></span>MCI\_SEQ\_SET\_SLAVE
</dt> <dd>

Sets the sequencer to receive synchronization data and indicates that the type of synchronization is specified in the **dwSlave** member of the structure identified by *lpSet*. MCISEQ returns MCIERR\_UNSUPPORTED\_FUNCTION. The following constants are defined for the synchronization type:

</dd> <dt>

<span id="MCI_SEQ_FILE"></span><span id="mci_seq_file"></span>MCI\_SEQ\_FILE
</dt> <dd>

Sets the sequencer to receive synchronization data contained in the MIDI file.

</dd> <dt>

<span id="MCI_SEQ_MIDI"></span><span id="mci_seq_midi"></span>MCI\_SEQ\_MIDI
</dt> <dd>

Sets the sequencer to receive MIDI synchronization data.

</dd> <dt>

<span id="MCI_SEQ_NONE"></span><span id="mci_seq_none"></span>MCI\_SEQ\_NONE
</dt> <dd>

Sets the sequencer to ignore synchronization data in a MIDI stream.

</dd> <dt>

<span id="MCI_SEQ_SMPTE"></span><span id="mci_seq_smpte"></span>MCI\_SEQ\_SMPTE
</dt> <dd>

Sets the sequencer to receive SMPTE synchronization data.

</dd> <dt>

<span id="MCI_SEQ_SET_TEMPO"></span><span id="mci_seq_set_tempo"></span>MCI\_SEQ\_SET\_TEMPO
</dt> <dd>

Changes the tempo of the MIDI sequence to that specified by the **dwTempo** member of the structure pointed to by *lpSet*. For sequences with division type PPQN, tempo is specified in beats per minute; for sequences with division type SMPTE, tempo is specified in frames per second.

</dd> </dl>

For sequencer devices, the *lpSet* parameter points to an [**MCI\_SEQ\_SET\_PARMS**](mci-seq-set-parms.md) structure.

The following additional flags are used with the **vcr** device type:

<dl> <dt>

<span id="MCI_VCR_SET_ASSEMBLE_RECORD"></span><span id="mci_vcr_set_assemble_record"></span>MCI\_VCR\_SET\_ASSEMBLE\_RECORD
</dt> <dd>

Sets the device to record in assemble or insert modes (when assemble is off, insert is on, and vice-versa). Use with one of the following flag:

</dd> <dt>

<span id="MCI_SET_ON"></span><span id="mci_set_on"></span>MCI\_SET\_ON
</dt> <dd>

Sets assemble record on, and turns insert record off. Records all video, audio and timecode tracks.

</dd> <dt>

<span id="MCI_SET_OFF"></span><span id="mci_set_off"></span>MCI\_SET\_OFF
</dt> <dd>

Sets assemble record off, and turns insert record on. When assemble record is off, individual tracks of video, audio, and timecode can be selected for recording.

</dd> <dt>

<span id="MCI_VCR_SET_CLOCK"></span><span id="mci_vcr_set_clock"></span>MCI\_VCR\_SET\_CLOCK
</dt> <dd>

The **dwClock** member of the structure identified by *lpSet* contains the new clock time.

</dd> <dt>

<span id="MCI_VCR_SET_COUNTER_FORMA"></span><span id="mci_vcr_set_counter_forma"></span>MCI\_VCR\_SET\_COUNTER\_FORMA
</dt> <dd>

The **dwCounterFormat** member of the structure identified by *lpSet* contains a constant specifying the new counter-time format to be used by the status counter. For a list of valid constants, see MCI\_SET\_TIME\_FORMAT in the list of additional flags for this command.

</dd> <dt>

<span id="MCI_VCR_SET_COUNTER_VALUE"></span><span id="mci_vcr_set_counter_value"></span>MCI\_VCR\_SET\_COUNTER\_VALUE
</dt> <dd>

The **dwCounterValue** member of the structure identified by *lpSet* contains the new counter value.

</dd> <dt>

<span id="MCI_VCR_SET_INDEX"></span><span id="mci_vcr_set_index"></span>MCI\_VCR\_SET\_INDEX
</dt> <dd>

The **dwIndex** member of the structure identified by *lpSet* contains a constant indicating the contents of the on-screen display and must be one of the following:

</dd> <dt>

<span id="MCI_VCR_INDEX_COUNTER"></span><span id="mci_vcr_index_counter"></span>MCI\_VCR\_INDEX\_COUNTER
</dt> <dd>

Displays counter.

</dd> <dt>

<span id="MCI_VCR_INDEX_DATE"></span><span id="mci_vcr_index_date"></span>MCI\_VCR\_INDEX\_DATE
</dt> <dd>

Displays date.

</dd> <dt>

<span id="MCI_VCR_INDEX_TIME"></span><span id="mci_vcr_index_time"></span>MCI\_VCR\_INDEX\_TIME
</dt> <dd>

Displays time.

</dd> <dt>

<span id="MCI_VCR_INDEX_TIMECODE"></span><span id="mci_vcr_index_timecode"></span>MCI\_VCR\_INDEX\_TIMECODE
</dt> <dd>

Displays timecode.

For more information, see the [MCI\_INDEX](mci-index.md) command.

</dd> <dt>

<span id="MCI_VCR_SET_PAUSE_TIMEOUT"></span><span id="mci_vcr_set_pause_timeout"></span>MCI\_VCR\_SET\_PAUSE\_TIMEOUT
</dt> <dd>

The **dwPauseTimeout** member of the structure identified by *lpSet* contains the maximum duration, in milliseconds, of a pause command.

</dd> <dt>

<span id="MCI_VCR_SET_POSTROLL_DURATION"></span><span id="mci_vcr_set_postroll_duration"></span>MCI\_VCR\_SET\_POSTROLL\_DURATION
</dt> <dd>

The **dwPostrollDuration** member of the structure identified by *lpSet* contains the videotape length, in the current time format, needed to brake the VCR transport when a stop or pause command is issued.

</dd> <dt>

<span id="MCI_VCR_SET_POWER"></span><span id="mci_vcr_set_power"></span>MCI\_VCR\_SET\_POWER
</dt> <dd>

Sets the power on or off. Must be used with one of the following flags:

</dd> <dt>

<span id="MCI_SET_OFF"></span><span id="mci_set_off"></span>MCI\_SET\_OFF
</dt> <dd>

Turns power off.

</dd> <dt>

<span id="MCI_SET_ON"></span><span id="mci_set_on"></span>MCI\_SET\_ON
</dt> <dd>

Turns power on.

</dd> <dt>

<span id="MCI_VCR_SET_PREROLL_DURATION"></span><span id="mci_vcr_set_preroll_duration"></span>MCI\_VCR\_SET\_PREROLL\_DURATION
</dt> <dd>

The **dwPrerollDuration** member of the structure identified by *lpSet* contains the videotape length, in the current time format, needed to stabilize the VCR output.

</dd> <dt>

<span id="MCI_VCR_SET_RECORD_FORMAT"></span><span id="mci_vcr_set_record_format"></span>MCI\_VCR\_SET\_RECORD\_FORMAT
</dt> <dd>

The **dwRecordFormat** member of the structure identified by *lpSet* contains a constant describing the record speed, which must be one of the following:

</dd> <dt>

<span id="MCI_VCR_FORMAT_EP"></span><span id="mci_vcr_format_ep"></span>MCI\_VCR\_FORMAT\_EP
</dt> <dd>

Records at slow speed.

</dd> <dt>

<span id="MCI_VCR_FORMAT_LP"></span><span id="mci_vcr_format_lp"></span>MCI\_VCR\_FORMAT\_LP
</dt> <dd>

Records at medium-slow speed.

</dd> <dt>

<span id="MCI_VCR_FORMAT_SP"></span><span id="mci_vcr_format_sp"></span>MCI\_VCR\_FORMAT\_SP
</dt> <dd>

Records at standard speed.

</dd> <dt>

<span id="MCI_VCR_SET_SPEED"></span><span id="mci_vcr_set_speed"></span>MCI\_VCR\_SET\_SPEED
</dt> <dd>

The **dwSpeed** member of the structure identified by *lpSet* contains the new speed setting, where 1000 is normal speed, 2000 is double speed, and 500 is half speed, and so on.

</dd> <dt>

<span id="MCI_VCR_SET_TAPE_LENGTH"></span><span id="mci_vcr_set_tape_length"></span>MCI\_VCR\_SET\_TAPE\_LENGTH
</dt> <dd>

The **dwTapeLength** member of the structure identified by *lpSet* contains the new length of the tape, provided that the length of the tape is undetectable.

</dd> <dt>

<span id="MCI_VCR_SET_TIME_MODE"></span><span id="mci_vcr_set_time_mode"></span>MCI\_VCR\_SET\_TIME\_MODE
</dt> <dd>

The **dwTimeMode** member of the structure identified by *lpSet* contains a constant indicating the new positional time mode. The following constants are valid:

</dd> <dt>

<span id="MCI_VCR_TIME_COUNTER"></span><span id="mci_vcr_time_counter"></span>MCI\_VCR\_TIME\_COUNTER
</dt> <dd>

Forces the device to use counter exclusively.

</dd> <dt>

<span id="MCI_VCR_TIME_DETECT"></span><span id="mci_vcr_time_detect"></span>MCI\_VCR\_TIME\_DETECT
</dt> <dd>

Each time a new videotape is inserted into the device, or the mode changes from not ready to ready, the device should attempt to determine if there is timecode available on the videotape. If timecode is available, use timecode in all subsequent commands that specify positions. Otherwise, use the counter.

</dd> <dt>

<span id="MCI_VCR_TIME_TIMECODE"></span><span id="mci_vcr_time_timecode"></span>MCI\_VCR\_TIME\_TIMECODE
</dt> <dd>

Forces the device to use timecode exclusively.

</dd> <dt>

<span id="MCI_VCR_SET_TRACKING"></span><span id="mci_vcr_set_tracking"></span>MCI\_VCR\_SET\_TRACKING
</dt> <dd>

Tunes the speed of the VCR tape transport with a fine adjustment, and must be used with one of the following flags:

</dd> <dt>

<span id="MCI_VCR_PLUS"></span><span id="mci_vcr_plus"></span>MCI\_VCR\_PLUS
</dt> <dd>

Increases the tape transport speed.

</dd> <dt>

<span id="MCI_VCR_MINUS"></span><span id="mci_vcr_minus"></span>MCI\_VCR\_MINUS
</dt> <dd>

Decreases the tape transport speed.

</dd> <dt>

<span id="MCI_VCR_RESET"></span><span id="mci_vcr_reset"></span>MCI\_VCR\_RESET
</dt> <dd>

Returns the tracking adjustment to zero.

</dd> </dl>

For VCR devices, the *lpSet* parameter points to an [**MCI\_VCR\_SET\_PARMS**](mci-vcr-set-parms.md) structure.

The following additional flag is used with the **videodisc** device type:

<dl> <dt>

<span id="MCI_VD_FORMAT_TRACK"></span><span id="mci_vd_format_track"></span>MCI\_VD\_FORMAT\_TRACK
</dt> <dd>

Changes the time format to tracks. MCI uses continuous track numbers.

</dd> </dl>

The following additional flags are used with the **waveaudio** device type:

<dl> <dt>

<span id="MCI_WAVE_INPUT"></span><span id="mci_wave_input"></span>MCI\_WAVE\_INPUT
</dt> <dd>

Sets the input used for recording to the **wInput** member of the structure identified by *lpSet*.

</dd> <dt>

<span id="MCI_WAVE_OUTPUT"></span><span id="mci_wave_output"></span>MCI\_WAVE\_OUTPUT
</dt> <dd>

Sets the output used for playing to the **wOutput** member of the structure identified by *lpSet*.

</dd> <dt>

<span id="MCI_WAVE_SET_ANYINPUT"></span><span id="mci_wave_set_anyinput"></span>MCI\_WAVE\_SET\_ANYINPUT
</dt> <dd>

Any wave input compatible with the current format can be used for recording.

</dd> <dt>

<span id="MCI_WAVE_SET_ANYOUTPUT"></span><span id="mci_wave_set_anyoutput"></span>MCI\_WAVE\_SET\_ANYOUTPUT
</dt> <dd>

Any wave output compatible with the current format can be used for playing.

</dd> <dt>

<span id="MCI_WAVE_SET_AVGBYTESPERSEC"></span><span id="mci_wave_set_avgbytespersec"></span>MCI\_WAVE\_SET\_AVGBYTESPERSEC
</dt> <dd>

Sets the bytes per second used for playing, recording, and saving to the **nAvgBytesPerSec** member of the structure identified by *lpSet*.

</dd> <dt>

<span id="MCI_WAVE_SET_BITSPERSAMPLE"></span><span id="mci_wave_set_bitspersample"></span>MCI\_WAVE\_SET\_BITSPERSAMPLE
</dt> <dd>

Sets the bits per sample used for playing, recording, and saving to the **nBitsPerSample** member of the PCM data format identified by *lpSet*.

</dd> <dt>

<span id="MCI_WAVE_SET_BLOCKALIGN"></span><span id="mci_wave_set_blockalign"></span>MCI\_WAVE\_SET\_BLOCKALIGN
</dt> <dd>

Sets the block alignment used for playing, recording, and saving to the **nBlockAlign** member of the structure identified by *lpSet*.

</dd> <dt>

<span id="MCI_WAVE_SET_CHANNELS"></span><span id="mci_wave_set_channels"></span>MCI\_WAVE\_SET\_CHANNELS
</dt> <dd>

The number of channels is indicated in the **nChannels** member of the structure identified by *lpSet*.

</dd> <dt>

<span id="MCI_WAVE_SET_FORMATTAG"></span><span id="mci_wave_set_formattag"></span>MCI\_WAVE\_SET\_FORMATTAG
</dt> <dd>

Sets the format type used for playing, recording, and saving to the **wFormatTag** member of the structure identified by *lpSet*. Specifying WAVE\_FORMAT\_PCM changes the format to PCM.

</dd> <dt>

<span id="MCI_WAVE_SET_SAMPLESPERSEC"></span><span id="mci_wave_set_samplespersec"></span>MCI\_WAVE\_SET\_SAMPLESPERSEC
</dt> <dd>

Sets the samples per second used for playing, recording, and saving to the **nSamplesPerSec** member of the structure identified by *lpSet*.

</dd> </dl>

For waveform-audio devices, the *lpSet* parameter points to an [**MCI\_WAVE\_SET\_PARMS**](mci-wave-set-parms.md) structure.

Several properties of waveform-audio data are defined when the file to store the data is created. These properties describe how the data is structured within the file and cannot be changed once recording begins. The following list of flags identifies these properties:

-   MCI\_WAVE\_SET\_AVGBYTESPERSEC
-   MCI\_WAVE\_SET\_BITSPERSAMPLE
-   MCI\_WAVE\_SET\_BLOCKALIGN
-   MCI\_WAVE\_SET\_CHANNELS
-   MCI\_WAVE\_SET\_FORMATTAG
-   MCI\_WAVE\_SET\_SAMPLESPERSEC

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

 

