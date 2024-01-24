---
title: Recording
description: Recording
ms.assetid: '0026eb1d-5be1-4090-801b-f1c65c179f42'
keywords:
- MCI_RECORD command
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Recording

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The general MCI specification supports recording with digital-video, MIDI sequencer, video-cassette recorder (VCR), and waveform-audio devices; however, only waveform-audio and VCR devices currently implement recording capabilities. You can insert or overwrite recorded information into an existing file or record into a new file. To record to an existing file, open a waveform-audio device and file as you would normally. To record into a new file, when you open the device specify "new" as the device name if you are using the command-string interface. If you are using the command-message interface, specify a zero-length filename.

When MCI creates a new file for recording, the data format is set to a default format specified by the device driver. To use a format other than the default format, you can use the [**set**](set.md) ([**MCI\_SET**](mci-set.md)) command.

To begin recording, use the [**record**](record.md) command (or [**MCI\_RECORD**](mci-record.md) and the [**MCI\_RECORD\_PARMS**](mci-record-parms.md) structure).

If you record in insert mode to an existing file, you can use the "from" (MCI\_FROM) and "to" (MCI\_TO) flags of the **record** command to specify starting and ending positions for recording. For example, if you record to a file that is 20 seconds long, and you begin recording at 5 seconds and end recording at 10 seconds, the resulting file will be 25 seconds long. The file will have a 5-second segment inserted 5 seconds into the original recording.

If you record with overwrite mode to an existing file, you can use the "from" and "to" flags to specify starting and ending locations of the section that is overwritten. For example, if you record to a file that is 20 seconds long, and you begin recording at 5 seconds and end recording at 10 seconds, you still have a recording 20 seconds long, but the section beginning at 5 seconds and ending at 10 seconds will have been replaced.

If you do not specify an ending location, recording continues until you send a [**stop**](stop.md) ([**MCI\_STOP**](mci-stop.md)) command, or until the driver runs out of free disk space. If you record to a new file, you can omit the "from" flag or set it to zero to start recording at the beginning of a new file. You can specify an ending location to terminate recording when recording to a new file.

The [**record**](record.md) command is sometimes accurate to within only 1 second of the starting location, such as with VCR devices. To record more accurately, you should use the [**cue**](cue.md) ([**MCI\_CUE**](mci-cue.md)) command. This command is recognized by digital-video, VCR, and waveform-audio devices. For more information about recording with VCR devices, see [VCR Services](vcr-services.md).

## Saving a Recorded File

When recording is complete, use the [**save**](save.md) command (or [**MCI\_SAVE**](mci-save.md) and the [**MCI\_SAVE\_PARMS**](mci-save-parms.md) structure) to save the recording before closing the device.

> [!Note]  
> If you close the device without saving, the recorded data is lost.

 

## Checking Input Levels (PCM Only)

To get the level of the input signal before recording on a PCM (Pulse Code Modulation) waveform-audio input device, use the [**status**](status.md) ([**MCI\_STATUS**](mci-status.md)) command. Specify the "level" flag (or the MCI\_STATUS\_ITEM flag and set the **dwItem** member of the [**MCI\_STATUS\_PARMS**](mci-status-parms.md) structure to MCI\_WAVE\_STATUS\_LEVEL). The average input signal level is returned. The left-channel value is in the high-order word and the right- or mono-channel value is in the low-order word.

The input level is represented as an unsigned value. For 8-bit samples, this value is in the range 0 through 127 (0x7F). For 16-bit samples, it is in the range 0 through 32,767 (0x7FFF).

 

 




