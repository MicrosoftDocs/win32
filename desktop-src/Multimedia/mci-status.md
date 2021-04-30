---
title: MCI_STATUS command (Mmsystem.h)
description: The MCI\_STATUS command retrieves information about an MCI device. All devices recognize this command. Information is returned in the dwReturn member of the structure identified by the lpStatus parameter.
ms.assetid: d1c3dff9-c66f-4525-aac1-4a15b43083e7
keywords:
- MCI_STATUS command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_STATUS
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---



# MCI\_STATUS command

> [!NOTE]
> Bias-free Communication
Microsoft supports a diverse and inclusionary environment.  Within this document, there are references to the word 'slave.' Microsoft's [Style Guide for Bias-Free Communications](https://github.com/MicrosoftDocs/microsoft-style-guide/blob/master/styleguide/bias-free-communication.md) recognizes this as an exclusionary word.  This wording is used as it is currently the wording used within the commands. For consistency, this document contains this word. When this word is altered in the commands, we will correct this document to be in alignment.

The MCI\_STATUS command retrieves information about an MCI device. All devices recognize this command. Information is returned in the **dwReturn** member of the structure identified by the *lpStatus* parameter.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_STATUS, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_STATUS_PARMS) lpStatus
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

<span id="lpStatus"></span><span id="lpstatus"></span><span id="LPSTATUS"></span>*lpStatus*
</dt> <dd>

Pointer to an [**MCI\_STATUS\_PARMS**](mci-status-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional standard and command-specific flags apply to all devices supporting MCI\_STATUS:

<dl> <dt>

<span id="MCI_STATUS_ITEM"></span><span id="mci_status_item"></span>MCI\_STATUS\_ITEM
</dt> <dd>

Specifies that the **dwItem** member of the structure identified by *lpStatus* contains a constant specifying which status item to obtain. The following constants define which status item to return in the **dwReturn** member of the structure:

MCI\_STATUS\_CURRENT\_TRACK

The **dwReturn** member is set to the current track number. MCI uses continuous track numbers.

MCI\_STATUS\_LENGTH

The **dwReturn** member is set to the total media length.

</dd> <dt>

<span id="MCI_STATUS_MODE"></span><span id="mci_status_mode"></span>MCI\_STATUS\_MODE
</dt> <dd>

The **dwReturn** member is set to the current mode of the device. The modes include the following:

-   MCI\_MODE\_NOT\_READY
-   MCI\_MODE\_PAUSE
-   MCI\_MODE\_PLAY
-   MCI\_MODE\_STOP
-   MCI\_MODE\_OPEN
-   MCI\_MODE\_RECORD
-   MCI\_MODE\_SEEK

</dd> <dt>

<span id="MCI_STATUS_NUMBER_OF_TRACKS"></span><span id="mci_status_number_of_tracks"></span>MCI\_STATUS\_NUMBER\_OF\_TRACKS
</dt> <dd>

The **dwReturn** member is set to the total number of playable tracks.

</dd> <dt>

<span id="MCI_STATUS_POSITION"></span><span id="mci_status_position"></span>MCI\_STATUS\_POSITION
</dt> <dd>

The **dwReturn** member is set to the current position.

</dd> <dt>

<span id="MCI_STATUS_READY"></span><span id="mci_status_ready"></span>MCI\_STATUS\_READY
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device is ready; it is set to **FALSE** otherwise.

</dd> <dt>

<span id="MCI_STATUS_TIME_FORMAT"></span><span id="mci_status_time_format"></span>MCI\_STATUS\_TIME\_FORMAT
</dt> <dd>

The **dwReturn** member is set to the current time format of the device. The time formats include:

-   MCI\_FORMAT\_BYTES
-   MCI\_FORMAT\_FRAMES
-   MCI\_FORMAT\_HMS
-   MCI\_FORMAT\_MILLISECONDS
-   MCI\_FORMAT\_MSF
-   MCI\_FORMAT\_SAMPLES
-   MCI\_FORMAT\_TMSF

</dd> <dt>

<span id="MCI_STATUS_START"></span><span id="mci_status_start"></span>MCI\_STATUS\_START
</dt> <dd>

Obtains the starting position of the media. To get the starting position, combine this flag with MCI\_STATUS\_ITEM and set the **dwItem** member of the structure identified by *lpStatus* to MCI\_STATUS\_POSITION.

</dd> <dt>

<span id="MCI_TRACK"></span><span id="mci_track"></span>MCI\_TRACK
</dt> <dd>

Indicates a status track parameter is included in the **dwTrack** member of the structure identified by *lpStatus*. You must use this flag with the MCI\_STATUS\_POSITION or MCI\_STATUS\_LENGTH constants. When used with MCI\_STATUS\_POSITION, MCI\_TRACK obtains the starting position of the specified track. When used with MCI\_STATUS\_LENGTH, MCI\_TRACK obtains the length of the specified track. MCI uses continuous track numbers.

</dd> </dl>

The following additional flags are used with the **cdaudio** device type. These constants are used in the **dwItem** member of the structure pointed to by the *lpStatus* parameter when MCI\_STATUS\_ITEM is specified for the *dwFlags* parameter.

<dl> <dt>

<span id="MCI_CDA_STATUS_TYPE_TRACK"></span><span id="mci_cda_status_type_track"></span>MCI\_CDA\_STATUS\_TYPE\_TRACK
</dt> <dd>

The **dwReturn** member is set to one of the following values:

-   MCI\_CDA\_TRACK\_AUDIO
-   MCI\_CDA\_TRACK\_OTHER

To use this flag, the MCI\_TRACK flag must be set, and the **dwTrack** member of the structure identified by *lpStatus* must contain a valid track number.

</dd> <dt>

<span id="MCI_STATUS_MEDIA_PRESENT"></span><span id="mci_status_media_present"></span>MCI\_STATUS\_MEDIA\_PRESENT
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the media is inserted in the device; it is set to **FALSE** otherwise.

</dd> </dl>

The following additional flags are used with the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_STATUS_DISKSPACE"></span><span id="mci_dgv_status_diskspace"></span>MCI\_DGV\_STATUS\_DISKSPACE
</dt> <dd>

The **lpstrDrive** member of the structure identified by *lpStatus* specifies a disk drive or, in some implementations, a path. The MCI\_STATUS command returns the approximate amount of disk space that could be obtained by the [MCI\_RESERVE](mci-reserve.md) command in the **dwReturn** member of the structure identified by *lpStatus*. The disk space is measured in units of the current time format.

</dd> <dt>

<span id="MCI_DGV_STATUS_INPUT"></span><span id="mci_dgv_status_input"></span>MCI\_DGV\_STATUS\_INPUT
</dt> <dd>

The constant specified by the **dwItem** member of the structure identified by *lpStatus* applies to the input.

</dd> <dt>

<span id="MCI_DGV_STATUS_LEFT"></span><span id="mci_dgv_status_left"></span>MCI\_DGV\_STATUS\_LEFT
</dt> <dd>

The constant specified by the **dwItem** member of the structure identified by *lpStatus* applies to the left audio channel.

</dd> <dt>

<span id="MCI_DGV_STATUS_NOMINAL"></span><span id="mci_dgv_status_nominal"></span>MCI\_DGV\_STATUS\_NOMINAL
</dt> <dd>

The constant specified by the **dwItem** member of the structure identified by *lpStatus* requests the nominal value rather than the current value.

</dd> <dt>

<span id="MCI_DGV_STATUS_OUTPUT"></span><span id="mci_dgv_status_output"></span>MCI\_DGV\_STATUS\_OUTPUT
</dt> <dd>

The constant specified by the **dwItem** member of the structure identified by *lpStatus* applies to the output.

</dd> <dt>

<span id="MCI_DGV_STATUS_RECORD"></span><span id="mci_dgv_status_record"></span>MCI\_DGV\_STATUS\_RECORD
</dt> <dd>

The frame rate returned for the MCI\_DGV\_STATUS\_FRAME\_RATE flag is the rate used for compression.

</dd> <dt>

<span id="MCI_DGV_STATUS_REFERENCE"></span><span id="mci_dgv_status_reference"></span>MCI\_DGV\_STATUS\_REFERENCE
</dt> <dd>

The **dwReturn** member of the structure identified by *lpStatus* returns the nearest key-frame image that precedes the frame specified in the **dwReference** member.

</dd> <dt>

<span id="MCI_DGV_STATUS_RIGHT"></span><span id="mci_dgv_status_right"></span>MCI\_DGV\_STATUS\_RIGHT
</dt> <dd>

The constant specified by the **dwItem** member of the structure identified by *lpStatus* applies to the right audio channel.

</dd> </dl>

The following constants are used with the **digitalvideo** device type in the **dwItem** member of the structure pointed to by the *lpStatus* parameter when MCI\_STATUS\_ITEM is specified for the *dwFlags* parameter.

<dl> <dt>

<span id="MCI_AVI_STATUS_AUDIO_BREAKS"></span><span id="mci_avi_status_audio_breaks"></span>MCI\_AVI\_STATUS\_AUDIO\_BREAKS
</dt> <dd>

The **dwReturn** member returns the number of times the audio portion of the last AVI sequence broke up. The system counts an audio break whenever it attempts to write audio data to the device driver and discovers that the driver has already played all of the available data. This flag is recognized only by the MCIAVI digital-video driver.

</dd> <dt>

<span id="MCI_AVI_STATUS_FRAMES_SKIPPED"></span><span id="mci_avi_status_frames_skipped"></span>MCI\_AVI\_STATUS\_FRAMES\_SKIPPED
</dt> <dd>

The **dwReturn** member returns the number of frames that were not drawn when the last AVI sequence was played. This flag is recognized only by the MCIAVI digital-video driver.

</dd> <dt>

<span id="MCI_AVI_STATUS_LAST_PLAY_SPEED"></span><span id="mci_avi_status_last_play_speed"></span>MCI\_AVI\_STATUS\_LAST\_PLAY\_SPEED
</dt> <dd>

The **dwReturn** member returns a value representing how closely the actual playing time of the last AVI sequence matched the target playing time. The value 1000 indicates that the target time and the actual time were the same. A value of 2000, for example, would indicate that the AVI sequence took twice as long to play as it should have. This flag is recognized only by the MCIAVI digital-video driver.

</dd> <dt>

<span id="MCI_DGV_STATUS_AUDIO"></span><span id="mci_dgv_status_audio"></span>MCI\_DGV\_STATUS\_AUDIO
</dt> <dd>

The **dwReturn** member returns MCI\_ON or MCI\_OFF depending on the most recent MCI\_SET\_AUDIO option for the [MCI\_SET](mci-set.md) command. It returns MCI\_ON if either or both speakers are enabled, and MCI\_OFF otherwise.

</dd> <dt>

<span id="MCI_DGV_STATUS_AUDIO_INPUT"></span><span id="mci_dgv_status_audio_input"></span>MCI\_DGV\_STATUS\_AUDIO\_INPUT
</dt> <dd>

The **dwReturn** member returns the approximate instantaneous audio level of the analog audio signal. A value greater than 1000 implies there is clipping distortion. Some devices can determine this value only while recording audio. This status value has no associated **MCI\_SET** or [MCI\_SETAUDIO](mci-setaudio.md) command. This value is related to, but normalized differently from, the waveform-audio command MCI\_WAVE\_STATUS\_LEVEL.

</dd> <dt>

<span id="MCI_DGV_STATUS_AUDIO_RECORD"></span><span id="mci_dgv_status_audio_record"></span>MCI\_DGV\_STATUS\_AUDIO\_RECORD
</dt> <dd>

The **dwReturn** member returns MCI\_ON or MCI\_OFF reflecting the state set by the MCI\_DGV\_SETAUDIO\_RECORD flag of the **MCI\_SETAUDIO** command.

</dd> <dt>

<span id="MCI_DGV_STATUS_AUDIO_SOURCE"></span><span id="mci_dgv_status_audio_source"></span>MCI\_DGV\_STATUS\_AUDIO\_SOURCE
</dt> <dd>

The **dwReturn** member returns the current audio digitizer source:

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_AVERAGE"></span><span id="mci_dgv_setaudio_average"></span>MCI\_DGV\_SETAUDIO\_AVERAGE
</dt> <dd>

Specifies the average of the left and right audio channels.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_LEFT"></span><span id="mci_dgv_setaudio_left"></span>MCI\_DGV\_SETAUDIO\_LEFT
</dt> <dd>

Specifies the left audio channel.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_RIGHT"></span><span id="mci_dgv_setaudio_right"></span>MCI\_DGV\_SETAUDIO\_RIGHT
</dt> <dd>

Specifies the right audio channel.

</dd> <dt>

<span id="MCI_DGV_SETAUDIO_STEREO"></span><span id="mci_dgv_setaudio_stereo"></span>MCI\_DGV\_SETAUDIO\_STEREO
</dt> <dd>

Specifies stereo.

</dd> <dt>

<span id="MCI_DGV_STATUS_AUDIO_STREAM"></span><span id="mci_dgv_status_audio_stream"></span>MCI\_DGV\_STATUS\_AUDIO\_STREAM
</dt> <dd>

The **dwReturn** member returns the current audio-stream number.

</dd> <dt>

<span id="MCI_DGV_STATUS_AVGBYTESPERSEC"></span><span id="mci_dgv_status_avgbytespersec"></span>MCI\_DGV\_STATUS\_AVGBYTESPERSEC
</dt> <dd>

The **dwReturn** member returns the average number of bytes per second used for recording.

</dd> <dt>

<span id="MCI_DGV_STATUS_BASS"></span><span id="mci_dgv_status_bass"></span>MCI\_DGV\_STATUS\_BASS
</dt> <dd>

The **dwReturn** member returns the current audio bass level. Use MCI\_DGV\_STATUS\_NOMINAL with this flag to obtain the nominal level.

</dd> <dt>

<span id="MCI_DGV_STATUS_BITSPERPEL"></span><span id="mci_dgv_status_bitsperpel"></span>MCI\_DGV\_STATUS\_BITSPERPEL
</dt> <dd>

The **dwReturn** member returns the number of bits per pixel used for saving captured or recorded data.

</dd> <dt>

<span id="MCI_DGV_STATUS_BITSPERSAMPLE"></span><span id="mci_dgv_status_bitspersample"></span>MCI\_DGV\_STATUS\_BITSPERSAMPLE
</dt> <dd>

The **dwReturn** member returns the number of bits per sample the device uses for recording. This applies only to devices supporting the PCM format.

</dd> <dt>

<span id="MCI_DGV_STATUS_BLOCKALIGN"></span><span id="mci_dgv_status_blockalign"></span>MCI\_DGV\_STATUS\_BLOCKALIGN
</dt> <dd>

The **dwReturn** member returns the alignment of data blocks relative to the start of the input waveform.

</dd> <dt>

<span id="MCI_DGV_STATUS_BRIGHTNESS"></span><span id="mci_dgv_status_brightness"></span>MCI\_DGV\_STATUS\_BRIGHTNESS
</dt> <dd>

The **dwReturn** member returns the current video brightness level. Use MCI\_DGV\_STATUS\_NOMINAL with this flag to obtain the nominal level.

</dd> <dt>

<span id="MCI_DGV_STATUS_COLOR"></span><span id="mci_dgv_status_color"></span>MCI\_DGV\_STATUS\_COLOR
</dt> <dd>

The **dwReturn** member returns the current color level. Use MCI\_DGV\_STATUS\_NOMINAL with this flag to obtain the nominal level.

</dd> <dt>

<span id="MCI_DGV_STATUS_CONTRAST"></span><span id="mci_dgv_status_contrast"></span>MCI\_DGV\_STATUS\_CONTRAST
</dt> <dd>

The **dwReturn** member returns the current contrast level. Use MCI\_DGV\_STATUS\_NOMINAL with this flag to obtain the nominal level.

</dd> <dt>

<span id="MCI_DGV_STATUS_FILEFORMAT"></span><span id="mci_dgv_status_fileformat"></span>MCI\_DGV\_STATUS\_FILEFORMAT
</dt> <dd>

The **dwReturn** member returns the current file format for recording or saving.

</dd> <dt>

<span id="MCI_DGV_STATUS_FILE_MODE"></span><span id="mci_dgv_status_file_mode"></span>MCI\_DGV\_STATUS\_FILE\_MODE
</dt> <dd>

The **dwReturn** member returns the state of the file operation:

MCI\_DGV\_FILE\_MODE\_EDITING

Returned during cut, copy, delete, paste, and undo operations.

MCI\_DGV\_FILE\_MODE\_IDLE

Returned when the file is ready for the next operation.

MCI\_DGV\_FILE\_MODE\_LOADING

Returned while the file is being loaded.

MCI\_DGV\_FILE\_MODE\_SAVING

Returned while the file is being saved.

</dd> <dt>

<span id="MCI_DGV_STATUS_FILE_COMPLETION"></span><span id="mci_dgv_status_file_completion"></span>MCI\_DGV\_STATUS\_FILE\_COMPLETION
</dt> <dd>

The **dwReturn** member returns the estimated percentage a load, save, capture, cut, copy, delete, paste, or undo operation has progressed. (Applications can use this to provide a visual indicator of progress.) This flag is not supported by all digital-video devices.

</dd> <dt>

<span id="MCI_DGV_STATUS_FORWARD"></span><span id="mci_dgv_status_forward"></span>MCI\_DGV\_STATUS\_FORWARD
</dt> <dd>

The **dwReturn** member returns **TRUE** if the device direction is forward or the device is not playing.

</dd> <dt>

<span id="MCI_DGV_STATUS_FRAME_RATE"></span><span id="mci_dgv_status_frame_rate"></span>MCI\_DGV\_STATUS\_FRAME\_RATE
</dt> <dd>

The **dwReturn** member must be used with MCI\_DGV\_STATUS\_NOMINAL, MCI\_DGV\_STATUS\_RECORD, or both. When used with MCI\_DGV\_STATUS\_RECORD, the current frame rate used for recording is returned. When used with both MCI\_DGV\_STATUS\_RECORD and MCI\_DGV\_STATUS\_NOMINAL, the nominal frame rate associated with the input video signal is returned. When used with MCI\_DGV\_STATUS\_NOMINAL, the nominal frame rate associated with the file is returned. In all cases the units are in frames per second multiplied by 1000.

</dd> <dt>

<span id="MCI_DGV_STATUS_GAMMA"></span><span id="mci_dgv_status_gamma"></span>MCI\_DGV\_STATUS\_GAMMA
</dt> <dd>

The **dwReturn** member returns the current gamma value. Use MCI\_DGV\_STATUS\_NOMINAL with this flag to obtain the nominal level.

</dd> <dt>

<span id="MCI_DGV_STATUS_HPAL"></span><span id="mci_dgv_status_hpal"></span>MCI\_DGV\_STATUS\_HPAL
</dt> <dd>

The **dwReturn** member returns the ASCII decimal value for the current palette handle. The handle is contained in the low-order word of the returned value.

</dd> <dt>

<span id="MCI_DGV_STATUS_HWND"></span><span id="mci_dgv_status_hwnd"></span>MCI\_DGV\_STATUS\_HWND
</dt> <dd>

The **dwReturn** member returns the ASCII decimal value for the current explicit or default window handle associated with this device driver instance. The handle is contained in the low-order word of the returned value.

</dd> <dt>

<span id="MCI_DGV_STATUS_KEY_COLOR"></span><span id="mci_dgv_status_key_color"></span>MCI\_DGV\_STATUS\_KEY\_COLOR
</dt> <dd>

The **dwReturn** member returns the current key-color value.

</dd> <dt>

<span id="MCI_DGV_STATUS_KEY_INDEX"></span><span id="mci_dgv_status_key_index"></span>MCI\_DGV\_STATUS\_KEY\_INDEX
</dt> <dd>

The **dwReturn** member returns the current key-index value.

</dd> <dt>

<span id="MCI_DGV_STATUS_MONITOR"></span><span id="mci_dgv_status_monitor"></span>MCI\_DGV\_STATUS\_MONITOR
</dt> <dd>

The **dwReturn** member returns a constant indicating the source of the current presentation. The following constants are defined:

MCI\_DGV\_MONITOR\_FILE

A file is the source.

MCI\_DGV\_MONITOR\_INPUT

The input is the source.

</dd> <dt>

<span id="MCI_DGV_STATUS_MONITOR_METHOD"></span><span id="mci_dgv_status_monitor_method"></span>MCI\_DGV\_STATUS\_MONITOR\_METHOD
</dt> <dd>

The **dwReturn** member returns a constant indicating the method used for input monitoring. The following constants are defined:

MCI\_DGV\_METHOD\_DIRECT

Direct input monitoring.

MCI\_DGV\_METHOD\_POST

Post-input monitoring.

MCI\_DGV\_METHOD\_PRE

Pre-input monitoring.

</dd> <dt>

<span id="MCI_DGV_STATUS_PAUSE_MODE"></span><span id="mci_dgv_status_pause_mode"></span>MCI\_DGV\_STATUS\_PAUSE\_MODE
</dt> <dd>

The **dwReturn** member returns MCI\_MODE\_PLAY if the device was paused while playing and returns MCI\_MODE\_RECORD if the device was paused while recording. The command returns MCIERR\_NONAPPLICABLE\_FUNCTION as an error return if the device is not paused.

</dd> <dt>

<span id="MCI_DGV_STATUS_SAMPLESPERSECOND"></span><span id="mci_dgv_status_samplespersecond"></span>MCI\_DGV\_STATUS\_SAMPLESPERSECOND
</dt> <dd>

The **dwReturn** member returns the number of samples per second recorded.

</dd> <dt>

<span id="MCI_DGV_STATUS_SEEK_EXACTLY"></span><span id="mci_dgv_status_seek_exactly"></span>MCI\_DGV\_STATUS\_SEEK\_EXACTLY
</dt> <dd>

The **dwReturn** member returns **TRUE** or **FALSE** indicating whether or not the seek exactly format is set. (Applications can set this format by using the [MCI\_SET](mci-set.md) command with the MCI\_DGV\_SET\_SEEK\_EXACTLY flag.)

</dd> <dt>

<span id="MCI_DGV_STATUS_SHARPNESS"></span><span id="mci_dgv_status_sharpness"></span>MCI\_DGV\_STATUS\_SHARPNESS
</dt> <dd>

The **dwReturn** member returns the current sharpness level. Use MCI\_DGV\_STATUS\_NOMINAL with this flag to obtain the nominal level.

</dd> <dt>

<span id="MCI_DGV_STATUS_SIZE"></span><span id="mci_dgv_status_size"></span>MCI\_DGV\_STATUS\_SIZE
</dt> <dd>

The **dwReturn** member returns the approximate playback duration of compressed data that the reserved workspace will hold. The duration units are in the current time format. It returns zero if there is no reserved disk space. The size returned is approximate since the precise disk space for compressed data cannot, in general, be predicted until after the data has been compressed.

</dd> <dt>

<span id="MCI_DGV_STATUS_SMPTE"></span><span id="mci_dgv_status_smpte"></span>MCI\_DGV\_STATUS\_SMPTE
</dt> <dd>

The **dwReturn** member returns the SMPTE time code associated with the current position in the workspace.

</dd> <dt>

<span id="MCI_DGV_STATUS_SPEED"></span><span id="mci_dgv_status_speed"></span>MCI\_DGV\_STATUS\_SPEED
</dt> <dd>

The **dwReturn** member returns the current playback speed.

</dd> <dt>

<span id="MCI_DGV_STATUS_STILL_FILEFORMAT"></span><span id="mci_dgv_status_still_fileformat"></span>MCI\_DGV\_STATUS\_STILL\_FILEFORMAT
</dt> <dd>

The **dwReturn** member returns the current file format for the [MCI\_CAPTURE](mci-capture.md) command.

</dd> <dt>

<span id="MCI_DGV_STATUS_TINT"></span><span id="mci_dgv_status_tint"></span>MCI\_DGV\_STATUS\_TINT
</dt> <dd>

The **dwReturn** member returns the current video tint level. Use MCI\_DGV\_STATUS\_NOMINAL with this flag to obtain the nominal level.

</dd> <dt>

<span id="MCI_DGV_STATUS_TREBLE"></span><span id="mci_dgv_status_treble"></span>MCI\_DGV\_STATUS\_TREBLE
</dt> <dd>

The **dwReturn** member returns the current audio treble level. Use MCI\_DGV\_STATUS\_NOMINAL with this flag to obtain the nominal level.

</dd> <dt>

<span id="MCI_DGV_STATUS_UNSAVED"></span><span id="mci_dgv_status_unsaved"></span>MCI\_DGV\_STATUS\_UNSAVED
</dt> <dd>

The **dwReturn** member returns **TRUE** if there is recorded data in the workspace that might be lost as a result of a [MCI\_CLOSE](mci-close.md), [MCI\_LOAD](mci-load.md), [MCI\_RECORD](mci-record.md), [MCI\_RESERVE](mci-reserve.md), [MCI\_CUT](mci-cut.md), [MCI\_DELETE](mci-delete.md), or [MCI\_PASTE](mci-paste.md) command. The member returns **FALSE** otherwise.

</dd> <dt>

<span id="MCI_DGV_STATUS_VIDEO"></span><span id="mci_dgv_status_video"></span>MCI\_DGV\_STATUS\_VIDEO
</dt> <dd>

The **dwReturn** member returns MCI\_ON if video is enabled or MCI\_OFF if it is disabled.

</dd> <dt>

<span id="MCI_DGV_STATUS_VIDEO_RECORD"></span><span id="mci_dgv_status_video_record"></span>MCI\_DGV\_STATUS\_VIDEO\_RECORD
</dt> <dd>

The **dwReturn** member returns MCI\_ON or MCI\_OFF, reflecting the state set by the MCI\_DGV\_SETVIDEO\_RECORD flag of the [MCI\_SETVIDEO](mci-setvideo.md) command.

</dd> <dt>

<span id="MCI_DGV_STATUS_VIDEO_SOURCE"></span><span id="mci_dgv_status_video_source"></span>MCI\_DGV\_STATUS\_VIDEO\_SOURCE
</dt> <dd>

The **dwReturn** member returns a constant indicating the type of video source set by the MCI\_DGV\_SETVIDEO\_SOURCE flag of the **MCI\_SETVIDEO** command.

</dd> <dt>

<span id="MCI_DGV_STATUS_VIDEO_SRC_NUM"></span><span id="mci_dgv_status_video_src_num"></span>MCI\_DGV\_STATUS\_VIDEO\_SRC\_NUM
</dt> <dd>

The **dwReturn** member returns the number within its type of the video-input source currently active.

</dd> <dt>

<span id="MCI_DGV_STATUS_VIDEO_STREAM"></span><span id="mci_dgv_status_video_stream"></span>MCI\_DGV\_STATUS\_VIDEO\_STREAM
</dt> <dd>

The **dwReturn** member returns the current video-stream number.

</dd> <dt>

<span id="MCI_DGV_STATUS_VOLUME"></span><span id="mci_dgv_status_volume"></span>MCI\_DGV\_STATUS\_VOLUME
</dt> <dd>

The **dwReturn** member returns the average of the volume to the left and right speakers. Use MCI\_DGV\_STATUS\_NOMINAL with this flag to obtain the nominal level.

</dd> <dt>

<span id="MCI_DGV_STATUS_WINDOW_VISIBLE"></span><span id="mci_dgv_status_window_visible"></span>MCI\_DGV\_STATUS\_WINDOW\_VISIBLE
</dt> <dd>

The **dwReturn** member returns **TRUE** if the window is not hidden.

</dd> <dt>

<span id="MCI_DGV_STATUS_WINDOW_MINIMIZED"></span><span id="mci_dgv_status_window_minimized"></span>MCI\_DGV\_STATUS\_WINDOW\_MINIMIZED
</dt> <dd>

The **dwReturn** member returns **TRUE** if the window is minimized.

</dd> <dt>

<span id="MCI_DGV_STATUS_WINDOW_MAXIMIZED"></span><span id="mci_dgv_status_window_maximized"></span>MCI\_DGV\_STATUS\_WINDOW\_MAXIMIZED
</dt> <dd>

The **dwReturn** member returns **TRUE** if the window is maximized.

</dd> <dt>

<span id="MCI_STATUS_MEDIA_PRESENT"></span><span id="mci_status_media_present"></span>MCI\_STATUS\_MEDIA\_PRESENT
</dt> <dd>

The **dwReturn** member returns **TRUE**.

</dd> </dl>

For digital-video devices, the *lpStatus* parameter points to an [**MCI\_DGV\_STATUS\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_status_parmsa) structure.

The following additional flags are used with the **sequencer** device type. These constants are used in the **dwItem** member of the structure pointed to by the *lpStatus* parameter when MCI\_STATUS\_ITEM is specified for the *dwFlags* parameter.

<dl> <dt>

<span id="MCI_SEQ_STATUS_DIVTYPE"></span><span id="mci_seq_status_divtype"></span>MCI\_SEQ\_STATUS\_DIVTYPE
</dt> <dd>

The **dwReturn** member is set to one of the following values indicating the current division type of a sequence:

-   MCI\_SEQ\_DIV\_PPQN
-   MCI\_SEQ\_DIV\_SMPTE\_24
-   MCI\_SEQ\_DIV\_SMPTE\_25
-   MCI\_SEQ\_DIV\_SMPTE\_30
-   MCI\_SEQ\_DIV\_SMPTE\_30DROP

</dd> <dt>

<span id="MCI_SEQ_STATUS_MASTER"></span><span id="mci_seq_status_master"></span>MCI\_SEQ\_STATUS\_MASTER
</dt> <dd>

The **dwReturn** member is set to the synchronization type used for master operation.

</dd> <dt>

<span id="MCI_SEQ_STATUS_OFFSET"></span><span id="mci_seq_status_offset"></span>MCI\_SEQ\_STATUS\_OFFSET
</dt> <dd>

The **dwReturn** member is set to the current SMPTE offset of a sequence.

</dd> <dt>

<span id="MCI_SEQ_STATUS_PORT"></span><span id="mci_seq_status_port"></span>MCI\_SEQ\_STATUS\_PORT
</dt> <dd>

The **dwReturn** member is set to the MIDI device identifier for the current port used by the sequence.

</dd> <dt>

<span id="MCI_SEQ_STATUS_SLAVE"></span><span id="mci_seq_status_slave"></span>MCI\_SEQ\_STATUS\_SLAVE
</dt> <dd>

The **dwReturn** member is set to the synchronization type used for subordinate operation.

</dd> <dt>

<span id="MCI_SEQ_STATUS_TEMPO"></span><span id="mci_seq_status_tempo"></span>MCI\_SEQ\_STATUS\_TEMPO
</dt> <dd>

The **dwReturn** member is set to the current tempo of a MIDI sequence in beats per minute for PPQN files, or frames per second for SMPTE files.

</dd> <dt>

<span id="MCI_STATUS_MEDIA_PRESENT"></span><span id="mci_status_media_present"></span>MCI\_STATUS\_MEDIA\_PRESENT
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the media is inserted in the device; it is set to **FALSE** otherwise.

</dd> </dl>

The following additional flags are used with the **vcr** device type. These constants are used in the **dwItem** member of the structure pointed to by the *lpStatus* parameter when MCI\_STATUS\_ITEM is specified for the *dwFlags* parameter.

<dl> <dt>

<span id="MCI_STATUS_MEDIA_PRESENT"></span><span id="mci_status_media_present"></span>MCI\_STATUS\_MEDIA\_PRESENT
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the media is inserted in the device; it is set to **FALSE** otherwise.

</dd> <dt>

<span id="MCI_VCR_STATUS_ASSEMBLE_RECORD"></span><span id="mci_vcr_status_assemble_record"></span>MCI\_VCR\_STATUS\_ASSEMBLE\_RECORD
</dt> <dd>

The **dwReturn** member is set to **TRUE** if assemble mode is on; it is set to **FALSE** otherwise.

</dd> <dt>

<span id="MCI_VCR_STATUS_AUDIO_MONITOR"></span><span id="mci_vcr_status_audio_monitor"></span>MCI\_VCR\_STATUS\_AUDIO\_MONITOR
</dt> <dd>

The **dwReturn** member is set to a constant, indicating the currently selected audio-monitor type.

</dd> <dt>

<span id="MCI_VCR_STATUS_AUDIO_MONITOR_NUMBER"></span><span id="mci_vcr_status_audio_monitor_number"></span>MCI\_VCR\_STATUS\_AUDIO\_MONITOR\_NUMBER
</dt> <dd>

The **dwReturn** member is set to the number of the currently selected audio-monitor type.

</dd> <dt>

<span id="MCI_VCR_STATUS_AUDIO_RECORD"></span><span id="mci_vcr_status_audio_record"></span>MCI\_VCR\_STATUS\_AUDIO\_RECORD
</dt> <dd>

The **dwReturn** member is set to **TRUE** if audio will be recorded when the next record command is given; it is set to **FALSE** otherwise. If you specify MCI\_TRACK in the *dwFlags* parameter of this command, **dwTrack** contains the track this inquiry applies to.

</dd> <dt>

<span id="MCI_VCR_STATUS_AUDIO_SOURCE"></span><span id="mci_vcr_status_audio_source"></span>MCI\_VCR\_STATUS\_AUDIO\_SOURCE
</dt> <dd>

The **dwReturn** member is set to a constant, indicating the current audio-source type.

</dd> <dt>

<span id="MCI_VCR_STATUS_AUDIO_SOURCE_NUMBER"></span><span id="mci_vcr_status_audio_source_number"></span>MCI\_VCR\_STATUS\_AUDIO\_SOURCE\_NUMBER
</dt> <dd>

The **dwReturn** member is set to the number of the currently selected audio-source type.

</dd> <dt>

<span id="MCI_VCR_STATUS_CLOCK"></span><span id="mci_vcr_status_clock"></span>MCI\_VCR\_STATUS\_CLOCK
</dt> <dd>

The **dwReturn** member is set to the current clock value, in total clock increments.

</dd> <dt>

<span id="MCI_VCR_STATUS_CLOCK_ID"></span><span id="mci_vcr_status_clock_id"></span>MCI\_VCR\_STATUS\_CLOCK\_ID
</dt> <dd>

The **dwReturn** member is set to a number which uniquely describes the clock in use.

</dd> <dt>

<span id="MCI_VCR_STATUS_COUNTER_FORMAT"></span><span id="mci_vcr_status_counter_format"></span>MCI\_VCR\_STATUS\_COUNTER\_FORMAT
</dt> <dd>

The **dwReturn** member is set to a constant describing the current counter format. For more information, see the MCI\_SET\_TIME\_FORMAT flag of the [MCI\_SET](mci-set.md) command.

</dd> <dt>

<span id="MCI_VCR_STATUS_COUNTER_RESOLUTION"></span><span id="mci_vcr_status_counter_resolution"></span>MCI\_VCR\_STATUS\_COUNTER\_RESOLUTION
</dt> <dd>

The **dwReturn** member is set to a constant describing the resolution of the counter, and is one of the following values:

-   MCI\_VCR\_COUNTER\_RES\_FRAMES: Counter has resolution of frames.
-   MCI\_VCR\_COUNTER\_RES\_SECONDS: Counter has resolution of seconds.
-   MCI\_VCR\_STATUS\_COUNTER\_VALUE: The **dwReturn** member is set to the current counter reading, in the current counter-time format.

</dd> <dt>

<span id="MCI_VCR_STATUS_FRAME_RATE"></span><span id="mci_vcr_status_frame_rate"></span>MCI\_VCR\_STATUS\_FRAME\_RATE
</dt> <dd>

The **dwReturn** member is set to the current native frame rate of the device.

</dd> <dt>

<span id="MCI_VCR_STATUS_INDEX"></span><span id="mci_vcr_status_index"></span>MCI\_VCR\_STATUS\_INDEX
</dt> <dd>

The **dwReturn** member is set to a constant, describing the current contents of the on-screen display, and is one of the following:

-   MCI\_VCR\_INDEX\_COUNTER
-   MCI\_VCR\_INDEX\_DATE
-   MCI\_VCR\_INDEX\_TIME
-   MCI\_VCR\_INDEX\_TIMECODE

</dd> <dt>

<span id="MCI_VCR_STATUS_INDEX_ON"></span><span id="mci_vcr_status_index_on"></span>MCI\_VCR\_STATUS\_INDEX\_ON
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the on-screen display is on; it is set to **FALSE** otherwise.

</dd> <dt>

<span id="MCI_VCR_STATUS_MEDIA_TYPE"></span><span id="mci_vcr_status_media_type"></span>MCI\_VCR\_STATUS\_MEDIA\_TYPE
</dt> <dd>

The **dwReturn** member is set to one of the following:

-   MCI\_VCR\_MEDIA\_8MM
-   MCI\_VCR\_MEDIA\_HI8
-   MCI\_VCR\_MEDIA\_VHS
-   MCI\_VCR\_MEDIA\_SVHS
-   MCI\_VCR\_MEDIA\_BETA
-   MCI\_VCR\_MEDIA\_EDBETA
-   MCI\_VCR\_MEDIA\_OTHER

</dd> <dt>

<span id="MCI_VCR_STATUS_NUMBER"></span><span id="mci_vcr_status_number"></span>MCI\_VCR\_STATUS\_NUMBER
</dt> <dd>

The **dwNumber** member is set to the logical-tuner number when you use this flag with the MCI\_VCR\_STATUS\_TUNER\_CHANNEL flag.

</dd> <dt>

<span id="MCI_VCR_STATUS_NUMBER_OF_AUDIO_TRACKS"></span><span id="mci_vcr_status_number_of_audio_tracks"></span>MCI\_VCR\_STATUS\_NUMBER\_OF\_AUDIO\_TRACKS
</dt> <dd>

The **dwReturn** member is set to the number of audio tracks that are independently selectable.

</dd> <dt>

<span id="MCI_VCR_STATUS_NUMBER_OF_VIDEO_TRACKS"></span><span id="mci_vcr_status_number_of_video_tracks"></span>MCI\_VCR\_STATUS\_NUMBER\_OF\_VIDEO\_TRACKS
</dt> <dd>

The **dwReturn** member is set to the number of video tracks that are independently selectable.

</dd> <dt>

<span id="MCI_VCR_STATUS_PAUSE_TIMEOUT"></span><span id="mci_vcr_status_pause_timeout"></span>MCI\_VCR\_STATUS\_PAUSE\_TIMEOUT
</dt> <dd>

The **dwReturn** member is set to the maximum duration, in milliseconds, of a pause command. The return value of zero indicates that no time-out will occur.

</dd> <dt>

<span id="MCI_VCR_STATUS_PLAY_FORMAT"></span><span id="mci_vcr_status_play_format"></span>MCI\_VCR\_STATUS\_PLAY\_FORMAT
</dt> <dd>

The **dwReturn** member is set to one of the following:

-   MCI\_VCR\_FORMAT\_EP
-   MCI\_VCR\_FORMAT\_LP
-   MCI\_VCR\_FORMAT\_OTHER
-   MCI\_VCR\_FORMAT\_SP

</dd> <dt>

<span id="MCI_VCR_STATUS_POSTROLL_DURATION"></span><span id="mci_vcr_status_postroll_duration"></span>MCI\_VCR\_STATUS\_POSTROLL\_DURATION
</dt> <dd>

The **dwReturn** member is set to the length of the videotape that will play after the spot at which it was stopped, in the current time format. This is needed to brake the VCR tape transport from a stop or pause command.

</dd> <dt>

<span id="MCI_VCR_STATUS_POWER_ON"></span><span id="mci_vcr_status_power_on"></span>MCI\_VCR\_STATUS\_POWER\_ON
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the power is on; it is set to **FALSE** otherwise.

</dd> <dt>

<span id="MCI_VCR_STATUS_PREROLL_DURATION"></span><span id="mci_vcr_status_preroll_duration"></span>MCI\_VCR\_STATUS\_PREROLL\_DURATION
</dt> <dd>

The **dwReturn** member is set to the length of the videotape that will play before the spot at which it was started, in the current time format. This is needed to stabilize the VCR output.

</dd> <dt>

<span id="MCI_VCR_STATUS_RECORD_FORMAT"></span><span id="mci_vcr_status_record_format"></span>MCI\_VCR\_STATUS\_RECORD\_FORMAT
</dt> <dd>

The **dwReturn** member is set to one of the following:

-   MCI\_VCR\_FORMAT\_EP
-   MCI\_VCR\_FORMAT\_LP
-   MCI\_VCR\_FORMAT\_OTHER
-   MCI\_VCR\_FORMAT\_SP

</dd> <dt>

<span id="MCI_VCR_STATUS_SPEED"></span><span id="mci_vcr_status_speed"></span>MCI\_VCR\_STATUS\_SPEED
</dt> <dd>

The **dwReturn** member is set to the current speed. For more information, see the MCI\_VCR\_SET\_SPEED flag of the [MCI\_SET](mci-set.md) command.

</dd> <dt>

<span id="MCI_VCR_STATUS_TIME_MODE"></span><span id="mci_vcr_status_time_mode"></span>MCI\_VCR\_STATUS\_TIME\_MODE
</dt> <dd>

The **dwReturn** member is set to one of the following:

-   MCI\_VCR\_TIME\_COUNTER
-   MCI\_VCR\_TIME\_DETECT
-   MCI\_VCR\_TIME\_TIMECODE

For more information, see the MCI\_VCR\_SET\_TIME\_MODE flag of the [MCI\_SET](mci-set.md) command.

</dd> <dt>

<span id="MCI_VCR_STATUS_TIME_TYPE"></span><span id="mci_vcr_status_time_type"></span>MCI\_VCR\_STATUS\_TIME\_TYPE
</dt> <dd>

The **dwReturn** member is set to a constant describing the current time type in use (used by [play](play.md), [record](record.md), [seek](seek.md), and so on), and is one of the following:

</dd> <dt>

<span id="MCI_VCR_TIME_COUNTER"></span><span id="mci_vcr_time_counter"></span>MCI\_VCR\_TIME\_COUNTER
</dt> <dd>

Counter is in use.

</dd> <dt>

<span id="MCI_VCR_TIME_TIMECODE"></span><span id="mci_vcr_time_timecode"></span>MCI\_VCR\_TIME\_TIMECODE
</dt> <dd>

Timecode is in use.

</dd> <dt>

<span id="MCI_VCR_STATUS_TIMECODE_PRESENT"></span><span id="mci_vcr_status_timecode_present"></span>MCI\_VCR\_STATUS\_TIMECODE\_PRESENT
</dt> <dd>

The **dwReturn** member is set to **TRUE** if timecode is present at the current position in the content; it is set to **FALSE** otherwise.

</dd> <dt>

<span id="MCI_VCR_STATUS_TIMECODE_RECORD"></span><span id="mci_vcr_status_timecode_record"></span>MCI\_VCR\_STATUS\_TIMECODE\_RECORD
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the timecode will be recorded when the next record command is given; it is set to **FALSE** otherwise.

</dd> <dt>

<span id="MCI_VCR_STATUS_TIMECODE_TYPE"></span><span id="mci_vcr_status_timecode_type"></span>MCI\_VCR\_STATUS\_TIMECODE\_TYPE
</dt> <dd>

The **dwReturn** member is set to a constant, describing the type of timecode that is directly supported by the device, and is one of the following:

-   MCI\_VCR\_TIMECODE\_TYPE\_NONE: This device does not use a timecode.
-   MCI\_VCR\_TIMECODE\_TYPE\_OTHER: This device uses an unspecified timecode.
-   MCI\_VCR\_TIMECODE\_TYPE\_SMPTE: This device uses SMPTE timecode.
-   MCI\_VCR\_TIMECODE\_TYPE\_SMPTE\_DROP: This device uses SMPTE drop timecode.

</dd> <dt>

<span id="MCI_VCR_STATUS_TUNER_CHANNEL"></span><span id="mci_vcr_status_tuner_channel"></span>MCI\_VCR\_STATUS\_TUNER\_CHANNEL
</dt> <dd>

The **dwReturn** member is set to the current channel number. If you specify MCI\_VCR\_STATUS\_NUMBER in the *dwFlags* parameter of this command, **dwNumber** contains the logical-tuner number this command applies to.

</dd> <dt>

<span id="MCI_VCR_STATUS_VIDEO_MONITOR"></span><span id="mci_vcr_status_video_monitor"></span>MCI\_VCR\_STATUS\_VIDEO\_MONITOR
</dt> <dd>

The **dwReturn** member is set to a constant, indicating the currently selected video-monitor type.

</dd> <dt>

<span id="MCI_VCR_STATUS_VIDEO_MONITOR_NUMBER"></span><span id="mci_vcr_status_video_monitor_number"></span>MCI\_VCR\_STATUS\_VIDEO\_MONITOR\_NUMBER
</dt> <dd>

The **dwReturn** member is set to the number of the currently selected video-monitor type.

</dd> <dt>

<span id="MCI_VCR_STATUS_VIDEO_RECORD"></span><span id="mci_vcr_status_video_record"></span>MCI\_VCR\_STATUS\_VIDEO\_RECORD
</dt> <dd>

The **dwReturn** member is set to **TRUE** if video will be recorded when the next record command is given; it is set to **FALSE** otherwise. If you specify MCI\_TRACK in the *dwFlags* parameter of this command, **dwTrack** contains the track this inquiry applies to.

</dd> <dt>

<span id="MCI_VCR_STATUS_VIDEO_SOURCE"></span><span id="mci_vcr_status_video_source"></span>MCI\_VCR\_STATUS\_VIDEO\_SOURCE
</dt> <dd>

The **dwReturn** member is set to a constant indicating the currently selected video-source type.

</dd> <dt>

<span id="MCI_VCR_STATUS_VIDEO_SOURCE_NUMBER"></span><span id="mci_vcr_status_video_source_number"></span>MCI\_VCR\_STATUS\_VIDEO\_SOURCE\_NUMBER
</dt> <dd>

The **dwReturn** member is set to the number of the currently selected video-source type.

</dd> <dt>

<span id="MCI_VCR_STATUS_WRITE_PROTECTED"></span><span id="mci_vcr_status_write_protected"></span>MCI\_VCR\_STATUS\_WRITE\_PROTECTED
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the media is write-protected; it is set to **FALSE** otherwise.

</dd> </dl>

For VCR devices, the *lpStatus* parameter points to an [**MCI\_VCR\_STATUS\_PARMS**](mci-vcr-status-parms.md) structure.

Using the MCI\_STATUS\_LENGTH flag to determine the length of the media always returns 2 hours for VCR devices, unless the length has been explicitly changed using the [MCI\_SET](mci-set.md) command.

The following additional flags are used with the **overlay** device type. These constants are used in the **dwItem** member of the structure pointed to by the *lpStatus* parameter when MCI\_STATUS\_ITEM is specified for the *dwFlags* parameter.

<dl> <dt>

<span id="MCI_OVLY_STATUS_HWND"></span><span id="mci_ovly_status_hwnd"></span>MCI\_OVLY\_STATUS\_HWND
</dt> <dd>

The **dwReturn** member is set to the handle of the window associated with the video-overlay device.

</dd> <dt>

<span id="MCI_OVLY_STATUS_STRETCH"></span><span id="mci_ovly_status_stretch"></span>MCI\_OVLY\_STATUS\_STRETCH
</dt> <dd>

The **dwReturn** member is set to **TRUE** if stretching is enabled; it is set to **FALSE** otherwise.

</dd> <dt>

<span id="MCI_STATUS_MEDIA_PRESENT"></span><span id="mci_status_media_present"></span>MCI\_STATUS\_MEDIA\_PRESENT
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the media is inserted in the device; it is set to **FALSE** otherwise.

</dd> </dl>

The following additional flags are used with the **videodisc** device type. These constants are used in the **dwItem** member of the structure pointed to by the *lpStatus* parameter when MCI\_STATUS\_ITEM is specified for the *dwFlags* parameter.

<dl> <dt>

<span id="MCI_STATUS_MEDIA_PRESENT"></span><span id="mci_status_media_present"></span>MCI\_STATUS\_MEDIA\_PRESENT
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the media is inserted in the device; it is set to **FALSE** otherwise.

</dd> <dt>

<span id="MCI_STATUS_MODE"></span><span id="mci_status_mode"></span>MCI\_STATUS\_MODE
</dt> <dd>

The **dwReturn** member is set to the current mode of the device. Videodisc devices can return the MCI\_VD\_MODE\_PARK constant, in addition to the constants any device can return, as documented with the *dwFlags* parameter.

</dd> <dt>

<span id="MCI_VD_STATUS_DISC_SIZE"></span><span id="mci_vd_status_disc_size"></span>MCI\_VD\_STATUS\_DISC\_SIZE
</dt> <dd>

The **dwReturn** member is set to the size of the loaded disc in inches (8 or 12).

</dd> <dt>

<span id="MCI_VD_STATUS_FORWARD"></span><span id="mci_vd_status_forward"></span>MCI\_VD\_STATUS\_FORWARD
</dt> <dd>

The **dwReturn** member is set to **TRUE** if playing forward; it is set to **FALSE** otherwise.

The MCI videodisc device does not support this flag.

</dd> <dt>

<span id="MCI_VD_STATUS_MEDIA_TYPE"></span><span id="mci_vd_status_media_type"></span>MCI\_VD\_STATUS\_MEDIA\_TYPE
</dt> <dd>

The **dwReturn** member is set to the media type of the inserted media. The following media types can be returned:

MCI\_VD\_MEDIA\_CAV

MCI\_VD\_MEDIA\_CLV

MCI\_VD\_MEDIA\_OTHER

</dd> <dt>

<span id="MCI_VD_STATUS_SIDE"></span><span id="mci_vd_status_side"></span>MCI\_VD\_STATUS\_SIDE
</dt> <dd>

The **dwReturn** member is set to 1 or 2 to indicate which side of the disc is loaded. Not all videodisc devices support this flag.

</dd> <dt>

<span id="MCI_VD_STATUS_SPEED"></span><span id="mci_vd_status_speed"></span>MCI\_VD\_STATUS\_SPEED
</dt> <dd>

The **dwReturn** member is set to the play speed in frames per second. The MCIPIONR.DRV device driver returns MCIERR\_UNSUPPORTED\_FUNCTION.

</dd> </dl>

The following additional flags are used with the **waveaudio** device type. These constants are used in the **dwItem** member of the structure pointed to by the *lpStatus* parameter when MCI\_STATUS\_ITEM is specified for the *dwFlags* parameter.

<dl> <dt>

<span id="MCI_WAVE_FORMATTAG"></span><span id="mci_wave_formattag"></span>MCI\_WAVE\_FORMATTAG
</dt> <dd>

The **dwReturn** member is set to the current format tag used for playing, recording, and saving.

</dd> <dt>

<span id="MCI_WAVE_INPUT"></span><span id="mci_wave_input"></span>MCI\_WAVE\_INPUT
</dt> <dd>

The **dwReturn** member is set to the wave input device used for recording. If no device is in use and no device has been explicitly set, then the error return is MCIERR\_WAVE\_INPUTUNSPECIFIED.

</dd> <dt>

<span id="MCI_WAVE_OUTPUT"></span><span id="mci_wave_output"></span>MCI\_WAVE\_OUTPUT
</dt> <dd>

The **dwReturn** member is set to the wave output device used for playing. If no device is in use and no device has been explicitly set, then the error return is MCIERR\_WAVE\_OUTPUTUNSPECIFIED.

</dd> <dt>

<span id="MCI_WAVE_STATUS_AVGBYTESPERSEC"></span><span id="mci_wave_status_avgbytespersec"></span>MCI\_WAVE\_STATUS\_AVGBYTESPERSEC
</dt> <dd>

The **dwReturn** member is set to the current bytes per second used for playing, recording, and saving.

</dd> <dt>

<span id="MCI_WAVE_STATUS_BITSPERSAMPLE"></span><span id="mci_wave_status_bitspersample"></span>MCI\_WAVE\_STATUS\_BITSPERSAMPLE
</dt> <dd>

The **dwReturn** member is set to the current bits per sample used for playing, recording, and saving PCM formatted data.

</dd> <dt>

<span id="MCI_WAVE_STATUS_BLOCKALIGN"></span><span id="mci_wave_status_blockalign"></span>MCI\_WAVE\_STATUS\_BLOCKALIGN
</dt> <dd>

The **dwReturn** member is set to the current block alignment used for playing, recording, and saving.

</dd> <dt>

<span id="MCI_WAVE_STATUS_CHANNELS"></span><span id="mci_wave_status_channels"></span>MCI\_WAVE\_STATUS\_CHANNELS
</dt> <dd>

The **dwReturn** member is set to the current channel count used for playing, recording, and saving.

</dd> <dt>

<span id="MCI_WAVE_STATUS_LEVEL"></span><span id="mci_wave_status_level"></span>MCI\_WAVE\_STATUS\_LEVEL
</dt> <dd>

The **dwReturn** member is set to the current record or playback level of PCM formatted data. The value is returned as an 8- or 16-bit value, depending on the sample size used. The right or mono channel level is returned in the low-order word. The left channel level is returned in the high-order word.

</dd> <dt>

<span id="MCI_WAVE_STATUS_SAMPLESPERSEC"></span><span id="mci_wave_status_samplespersec"></span>MCI\_WAVE\_STATUS\_SAMPLESPERSEC
</dt> <dd>

The **dwReturn** member is set to the current samples per second used for playing, recording, and saving.

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
</dt> <dt>

[MCI\_CUT](mci-cut.md)
</dt> <dt>

[MCI\_DELETE](mci-delete.md)
</dt> <dt>

[MCI\_PASTE](mci-paste.md)
</dt> <dt>

[MCI\_RESERVE](mci-reserve.md)
</dt> <dt>

[MCI\_SET](mci-set.md)
</dt> <dt>

[play](play.md)
</dt> <dt>

[record](record.md)
</dt> <dt>

[seek](seek.md)
</dt> </dl>

 

