---
title: set command
description: The set command establishes control settings for the device. CD audio, digital-video, MIDI sequencer, VCR, videodisc, video-overlay, and waveform-audio devices recognize this command.
ms.assetid: '1ec4d84e-372a-4b6d-b694-f5afb41f90b2'
keywords:
- set command Windows Multimedia
topic_type:
- apiref
api_name:
- set
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---



# set command

> [!NOTE]
> Bias-free Communication
Microsoft supports a diverse and inclusionary environment.  Within this document, there are references to the word 'slave.' Microsoft's [Style Guide for Bias-Free Communications](https://github.com/MicrosoftDocs/microsoft-style-guide/blob/master/styleguide/bias-free-communication.md) recognizes this as an exclusionary word.  This wording is used as it is currently the wording used within the commands. For consistency, this document contains this word. When this word is altered in the commands, we will correct this document to be in alignment.


The set command establishes control settings for the device. CD audio, digital-video, MIDI sequencer, VCR, videodisc, video-overlay, and waveform-audio devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand,
  TEXT("set %s %s %s"),
  lpszDeviceID,
  lpszSetting,
  lpszFlags
);
      
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszSetting"></span><span id="lpszsetting"></span><span id="LPSZSETTING"></span>*lpszSetting*
</dt> <dd>

Flag for establishing control settings. The following table lists device types that recognize the **set** command and the flags used by each type.




| Device Type | Command Flags | 
|-------------|---------------|
| cdaudio | <ul><li>audio all off</li><li>audio all on</li><li>audio left off</li><li>audio left on</li><li>audio right off</li><li>audio right on</li><li>door closed</li><li>door open</li><li>time format milliseconds</li><li>time format msf</li><li>time format tmsf</li></ul> | 
| digitalvideo | <ul><li>audio all off</li><li>audio all on</li><li>audio left off</li><li>audio left on</li><li>audio right off</li><li>audio right on</li><li>door closed</li><li>door open</li><li>file format <em>format</em></li><li>seek exactly on</li><li>seek exactly off</li><li>speed <em>factor</em></li><li>still file format <em>format</em></li><li>time format frames</li><li>time format milliseconds</li><li>video off</li><li>video on</li></ul> | 
| overlay | <ul><li>audio all off</li><li>audio all on</li><li>audio left off</li><li>audio left on</li><li>audio right off</li><li>audio right on</li><li>door closed</li><li>door open</li><li>video off</li><li>video on</li></ul> | 
| sequencer | <ul><li>audio all off</li><li>audio all on</li><li>audio left off</li><li>audio left on</li><li>audio right off</li><li>audio right on</li><li>door closed</li><li>door open</li><li>master MIDI</li><li>master none</li><li>master SMPTE</li><li>offset <em>time</em></li><li>port mapper</li><li>port none</li><li>port <em>port_number</em></li><li>slave file</li><li>slave MIDI</li><li>slave none</li><li>slave SMPTE</li><li>tempo <em>tempo_value</em></li><li>time format milliseconds</li><li>time format SMPTE <em>fps</em></li><li>time format SMPTE 30 drop</li><li>time format song pointer</li></ul> | 
| <strong>vcr</strong> | <ul><li>assemble record on</li><li>assemble record off</li><li>audio all off</li><li>audio all on</li><li>audio left off</li><li>audio left on</li><li>audio right off</li><li>audio right on</li><li>clock <em>time</em></li><li>counter format</li><li>counter <em>value</em></li><li>door closed</li><li>door open</li><li>index counter</li><li>index date</li><li>index time</li><li>index time</li><li>codelength <em>duration</em></li><li>pause <em>timeout</em></li><li>postroll duration -</li><li><em>duration</em></li><li>power on</li><li>power off</li><li>preroll duration <em>duration</em></li><li>record format SP</li><li>record format LP</li><li>record format EP</li><li>speed <em>factor</em></li><li>time format frames</li><li>time format hms</li><li>time format milliseconds</li><li>time format msf</li><li>time format SMPTE <em>fps</em></li><li>time format SMPTE 30 drop</li><li>time format tmsf</li><li>time mode counter</li><li>time mode detect</li><li>time mode timecode</li><li>tracking plus</li><li>tracking minus</li><li>tracking reset</li></ul> | 
| videodisc | <ul><li>audio all off</li><li>audio all on</li><li>audio left off</li><li>audio left on</li><li>audio right off</li><li>audio right on</li><li>door closed</li><li>door open</li><li>time format frames</li><li>time format hms</li><li>time format milliseconds</li><li>time format track</li><li>video off</li><li>video on</li></ul> | 
| waveaudio | <ul><li>alignment <em>integer</em></li><li>any input</li><li>any output</li><li>audio all off</li><li>audio all on</li><li>audio left off</li><li>audio left on</li><li>audio right off</li><li>audio right on</li><li>bitspersample <em>bit_count</em></li><li>bytespersec <em>byte_rate</em></li><li>channels <em>channel_count</em></li><li>door closed</li><li>door open</li><li>format tag pcm</li><li>format tag <em>tag</em></li><li>input <em>integer</em></li><li>output <em>integer</em></li><li>samplespersec <em>integer</em></li><li>time format bytes</li><li>time format milliseconds</li><li>time format samples</li></ul> | 




 

The following table lists the flags that can be specified in the **lpszSetting** parameter and their meanings.




| Value | Meaning | 
|-------|---------|
| alignment <em>integer</em> | Sets the alignment of data blocks relative to the start of data passed to the waveform-audio device. The file is saved in this format. | 
| any input | Use any input that supports the current format when recording. This is the default setting. | 
| any output | Use any output that supports the current format when playing. This is the default. | 
| assemble record on <br /> assemble record off <br /> | In assemble mode, all tracks are recorded as defined by the device. Most VCRs are in assemble mode by default. | 
| audio all off <br /> audio all on <br /> | Disables or enables audio output. Video-overlay devices, the MCISEQ sequencer, and the MCIWAVE waveform-audio device do not support this flag. | 
| audio left off <br /> audio left on <br /> audio right off <br /> audio right on <br /> | Disables or enables output to either the left or the right audio channel. Video-overlay devices, the MCISEQ sequencer, and the MCIWAVE waveform-audio device do not support this flag. | 
| bitspersample <em>bit_count</em> | Sets the number of bits per PCM (Pulse Code Modulation) sample played or recorded. The file is saved in this format. | 
| bytespersec <em>byte_rate</em> | Sets the average number of bytes per second played or recorded. The file is saved in this format. | 
| channels <em>channel_count</em> | Sets the channels for playing and recording. The file is saved in this format. | 
| clock <em>time</em> | Sets time on the external clock to <em>time.</em> The format is specified as a long unsigned integer. | 
| counter format | Set the time format for the counter, as returned by <a href="status.md">status</a> "counter". For information about applicable types, see the <strong>set</strong> "time format" command. | 
| counter <em>value</em> | Sets the VCR counter to the specified value. The value must be specified in the current counter format. For more information, see the <strong>set</strong> "counter format" command. | 
| door closed | Retracts the tray and closes the door, if possible. For VCRs, loads the tape automatically. | 
| door open | Opens the door and ejects the tray or tape, if possible. | 
| file format <em>format</em> | Specifies a file format that is used for <a href="save.md">save</a> or <a href="capture.md">capture</a> commands. If omitted, this might default to a device driver defined format. If the specified file format conflicts with the currently selected algorithm and quality, then they are changed to the defaults for the file format. The following file formats are defined:<ul><li>avi: Specifies AVI format.</li><li>avss: Specifies AVSS format.</li><li>dib: Specifies DIB format.</li><li>jfif: Specifies JFIF format.</li><li>jpeg: Specifies JPEG format.</li><li>mpeg: Specifies MPEG format.</li><li>rdib: Specifies RLE DIB format.</li><li>rjpeg: Specifies RJPEG format.</li></ul> | 
| format tag pcm | Sets the format type to PCM for playing and recording. The file is saved in this format. | 
| format tag <em>tag</em> | Sets the format type for playing and recording. The file is saved in this format. | 
| index timecode <br /> index counter <br /> index date <br /> index time <br /> | Sets the current display screen on the VCR. | 
| input <em>integer</em> | Sets the audio channel used as the input. | 
| length <em>duration</em> | Sets the user-specified length of the tape in the VCR. This length is returned by the <a href="status.md">status</a> "length" command and is provided for compatibility with applications that require this command to return a valid length. | 
| master midi | Sets the MIDI sequencer as the synchronization source. Synchronization data is sent in MIDI format. The MCISEQ sequencer does not support this flag. | 
| master none | Inhibits the MIDI sequencer from sending synchronization data. The MCISEQ sequencer does not support this flag. | 
| master smpte | Sets the MIDI sequencer as the synchronization source. Synchronization data is sent in SMPTE (Society of Motion Picture and Television Engineers) format. The MCISEQ sequencer does not support this flag. | 
| offset <em>time</em> | Sets the SMPTE offset <em>time</em>. The offset is the beginning time of a SMPTE based sequence. The <em>time</em> is expressed as <em>hh</em>: <em>mm</em>: <em>ss</em>: <em>ff</em>, where <em>hh</em> is hours, <em>mm</em> is minutes, <em>ss</em> is seconds, and <em>ff</em> is frames. | 
| output <em>integer</em> | Sets the audio channel used as the output. | 
| pause <em>timeout</em> | Sets the maximum duration, in milliseconds, of a <a href="pause.md">pause</a> command. A <em>timeout</em> value of zero indicates that no time-out will occur. | 
| postroll duration <em>duration</em> | Sets the length, in the current time format, needed to brake the VCR transport when a <a href="stop.md">stop</a> or <strong>pause</strong> command is issued. | 
| port mapper | Sets the MIDI mapper as the port receiving the MIDI messages. This command fails if the MIDI mapper or a port it needs is being used by another application. | 
| port none | Disables the sending of MIDI messages. This command also closes a MIDI port. | 
| port <em>port_number</em> | Sets the MIDI port receiving the MIDI messages. This command fails if the port you are trying to open is being used by another application. | 
| power on <br /> power off <br /> | Sets the device power to on or off. | 
| preroll duration <em>duration</em> | Sets the length, in the current time format, needed to stabilize the VCR output. | 
| record format SP <br /> record format LP <br /> record format EP <br /> | Sets the recording mode for the VCR to SP for standard play, EP for extended play, or LP for long play. These values are not intended to be VHS specific. They map to any three appropriate modes with other tape formats. For example, SP maps to the fastest, highest quality recording. | 
| samplespersec <em>integer</em> | Sets the sample rate for playing and recording. The file is saved in this format. | 
| seek exactly on<br /> seek exactly off <br /> | Selects one of two seek modes. With "seek exactly on", seek will always move to the frame specified. With "seek exactly off", seek will move to the closest key frame prior to the frame specified. | 
| slave file | Sets the MIDI sequencer to use file data as the synchronization source. This is the default setting. | 
| slave midi | Sets the MIDI sequencer to use incoming MIDI data for the synchronization source. The sequencer recognizes synchronization data with the MIDI format. The MCISEQ sequencer does not support this flag. | 
| slave none | Sets the MIDI sequencer to ignore synchronization | 
| slave smpte | Sets the MIDI sequencer to use incoming MIDI data for the synchronization source. The sequencer recognizes synchronization data with the SMPTE format. The MCISEQ sequencer does not support this flag. | 
| speed factor | Sets the relative speed of video and audio playback from the workspace. Factor is the ratio between the nominal frame rate and the desired frame rate, where the nominal frame rate is designated as 1000. (A rate of 500 is half normal speed, 2000 is twice normal speed, and so on.) Setting the speed to zero plays the video as fast as possible without dropping frames and without audio. | 
| still file format <em>format</em> | Specifies the file format used for capture commands. | 
| tempo tempo_value | Sets the tempo of the sequence according to the current time format. For a PPQN-based file, the tempo_value is interpreted as beats per minute. For a SMPTE-based file, the tempo_value is interpreted as frames per second. | 
| time format bytes | In a PCM file format, sets the time format to bytes. All position information is specified as bytes following this command. | 
| time format frames | Sets the time format to frames. All commands that use position values will assume frames. When the device is opened, frames is the default mode. Supported by videodiscs using CAV format. | 
| time format hms | Sets the time format to hours, minutes, and seconds. All commands that use position values will assume HMS. HMS is the default format for CLV videodiscs. Specify an HMS value as hh:mm:ss, where hh is hours, mm is minutes, and ss is seconds. You can omit a field if it and all following fields are zero. For example, 3, 3:0, and 3:0:0 are all valid ways to express 3 hours. <br /> | 
| time format milliseconds | Sets the time format to milliseconds. All commands that use position values will assume milliseconds. You can abbreviate milliseconds as "ms". For sequencer devices, the sequence file sets the default format to PPQN or SMPTE. Video-overlay devices do not support this flag.<br /> | 
| time format msf | Sets the time format to minutes, seconds, and frames. All commands that use position values will assume MSF (the default format for CD audio). Specify an MSF value as mm:ss:ff, where mm is minutes, ss is seconds, and ff is frames. You can omit a field if it and all following fields are zero. For example, 3, 3:0, and 3:0:0 are valid ways to express 3 minutes.<br /> The MSF fields have the following maximum values:<br /><ul><li>Minutes 99</li><li>Seconds 59</li><li>Frames 74</li></ul> | 
| time format samples | Sets the time format to samples. All position information is specified as samples following this command. | 
| time format smpte 24<br /> time format smpte 25<br /> time format smpte 30<br /> | Sets the time format to an SMPTE frame rate. For VCRs, sets the time format to hh:mm:ss:ff, where the legal values are 00:00:00:00 through 23:59:59:xx, and xx is one less than the frames per second as specified by the number 24, 25, or 30 as specified in the flag. On input, colons (:) are required to separate the components. The least significant units can be omitted if they are 00; for example, 02:00 is the same as 02:00:00:00. All commands that use position values will assume SMPTE format.<br /> The sequence file sets the default format to PPQN or SMPTE.<br /> | 
| time format smpte 30 drop | Sets the time format to SMPTE 30 drop frame rate. For VCRs, same as SMPTE 30, except that certain timecode positions are dropped from the format to have the recorded timecode positions for each frame (at the NTSC frame rate of 29.97 fps) correspond to real time (at 30 fps). Timecode positions that are dropped are as follows: two every minute, on the minute, for the first nine of every ten minutes of recorded content. For example, at 01:04:59:29, the next timecode position would be 01:05:00:02, not 01:05:00:00. All commands that use position values will assume SMPTE format.<br /> The sequence file sets the default format to PPQN or SMPTE.<br /> | 
| time format song pointer | Sets the time format to song pointer (sixteenth notes). All commands that use position values will assume song pointer units. This flag is valid only for a sequence of division type PPQN. | 
| time format tmsf | Sets the time format to tracks, minutes, seconds, and frames. All commands that use position values will assume TMSF. Specify a TMSF value as tt:mm:ss:ff, where tt is tracks, mm is minutes, ss is seconds, and ff is frames. You can omit a field if it and all following fields are zero. For example, 3, 3:0, 3:0:0, and 3:0:0:0 are all valid ways to express track 3. <br /> The TMSF fields have the following maximum values:<br /><ul><li>Tracks 99</li><li>Minutes 90</li><li>Seconds 59</li><li>Frames 74</li></ul> | 
| time format track | Sets the position format to tracks. All commands that use position values will assume tracks. | 
| time mode counter | Sets the position-information mode to use the VCR counters. | 
| time mode detect | Sets the position information mode based on detection of timecode information on the tape. If timecode information is detected, the time type is set to "timecode"; otherwise, the time type is set to "counter". "Detect" is a special mode. Whenever the driver is opened, a new tape is inserted, or the "time mode" command is issued, the driver checks the current time mode available on the tape and sets "time type" to either "timecode" or "counter". Once "time type" is set, the driver doesn't change it until one of the above conditions occurs again.<br /> | 
| time mode timecode | Sets the position information mode to use "timecode" information on the tape. | 
| tracking plus <br /> tracking minus <br /> tracking reset <br /> | Adjusts the speed of the videotape transport in fine increments. Use the "tracking" flags when a noisy picture is obtained from a VCR. "Tracking plus" increases the transport speed. "Tracking minus" decreases the transport speed. "Tracking reset" returns the tracking adjustment to zero. | 
| video off | Disables video output. | 
| video on | Enables video output. | 




 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video and VCR devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

Several properties of waveform-audio data are defined when the file to store the data is created. These properties describe how the data is structured within the file and cannot be changed once recording begins. The following list identifies these properties:

-   alignment
-   bitspersample
-   bytespersec
-   channels
-   format tag
-   samplespersec

## Examples

The following command sets the time format to milliseconds and sets the waveform-audio format to 8 bit, mono, 11 kHz.

``` syntax
set mysound time format ms bitspersample 8 channels 1 samplespersec 11025
```

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[MCI](mci.md)
</dt> <dt>

[MCI Command Strings](mci-command-strings.md)
</dt> <dt>

[capture](capture.md)
</dt> <dt>

[pause](pause.md)
</dt> <dt>

[save](save.md)
</dt> <dt>

[stop](stop.md)
</dt> </dl>

 

