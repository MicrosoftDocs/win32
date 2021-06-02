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



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Device Type</th>
<th>Command Flags</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>cdaudio</td>
<td><ul>
<li>audio all off</li>
<li>audio all on</li>
<li>audio left off</li>
<li>audio left on</li>
<li>audio right off</li>
<li>audio right on</li>
<li>door closed</li>
<li>door open</li>
<li>time format milliseconds</li>
<li>time format msf</li>
<li>time format tmsf</li>
</ul></td>
</tr>
<tr class="even">
<td>digitalvideo</td>
<td><ul>
<li>audio all off</li>
<li>audio all on</li>
<li>audio left off</li>
<li>audio left on</li>
<li>audio right off</li>
<li>audio right on</li>
<li>door closed</li>
<li>door open</li>
<li>file format <em>format</em></li>
<li>seek exactly on</li>
<li>seek exactly off</li>
<li>speed <em>factor</em></li>
<li>still file format <em>format</em></li>
<li>time format frames</li>
<li>time format milliseconds</li>
<li>video off</li>
<li>video on</li>
</ul></td>
</tr>
<tr class="odd">
<td>overlay</td>
<td><ul>
<li>audio all off</li>
<li>audio all on</li>
<li>audio left off</li>
<li>audio left on</li>
<li>audio right off</li>
<li>audio right on</li>
<li>door closed</li>
<li>door open</li>
<li>video off</li>
<li>video on</li>
</ul></td>
</tr>
<tr class="even">
<td>sequencer</td>
<td><ul>
<li>audio all off</li>
<li>audio all on</li>
<li>audio left off</li>
<li>audio left on</li>
<li>audio right off</li>
<li>audio right on</li>
<li>door closed</li>
<li>door open</li>
<li>master MIDI</li>
<li>master none</li>
<li>master SMPTE</li>
<li>offset <em>time</em></li>
<li>port mapper</li>
<li>port none</li>
<li>port <em>port_number</em></li>
<li>slave file</li>
<li>slave MIDI</li>
<li>slave none</li>
<li>slave SMPTE</li>
<li>tempo <em>tempo_value</em></li>
<li>time format milliseconds</li>
<li>time format SMPTE <em>fps</em></li>
<li>time format SMPTE 30 drop</li>
<li>time format song pointer</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>vcr</strong></td>
<td><ul>
<li>assemble record on</li>
<li>assemble record off</li>
<li>audio all off</li>
<li>audio all on</li>
<li>audio left off</li>
<li>audio left on</li>
<li>audio right off</li>
<li>audio right on</li>
<li>clock <em>time</em></li>
<li>counter format</li>
<li>counter <em>value</em></li>
<li>door closed</li>
<li>door open</li>
<li>index counter</li>
<li>index date</li>
<li>index time</li>
<li>index time</li>
<li>codelength <em>duration</em></li>
<li>pause <em>timeout</em></li>
<li>postroll duration -</li>
<li><em>duration</em></li>
<li>power on</li>
<li>power off</li>
<li>preroll duration <em>duration</em></li>
<li>record format SP</li>
<li>record format LP</li>
<li>record format EP</li>
<li>speed <em>factor</em></li>
<li>time format frames</li>
<li>time format hms</li>
<li>time format milliseconds</li>
<li>time format msf</li>
<li>time format SMPTE <em>fps</em></li>
<li>time format SMPTE 30 drop</li>
<li>time format tmsf</li>
<li>time mode counter</li>
<li>time mode detect</li>
<li>time mode timecode</li>
<li>tracking plus</li>
<li>tracking minus</li>
<li>tracking reset</li>
</ul></td>
</tr>
<tr class="even">
<td>videodisc</td>
<td><ul>
<li>audio all off</li>
<li>audio all on</li>
<li>audio left off</li>
<li>audio left on</li>
<li>audio right off</li>
<li>audio right on</li>
<li>door closed</li>
<li>door open</li>
<li>time format frames</li>
<li>time format hms</li>
<li>time format milliseconds</li>
<li>time format track</li>
<li>video off</li>
<li>video on</li>
</ul></td>
</tr>
<tr class="odd">
<td>waveaudio</td>
<td><ul>
<li>alignment <em>integer</em></li>
<li>any input</li>
<li>any output</li>
<li>audio all off</li>
<li>audio all on</li>
<li>audio left off</li>
<li>audio left on</li>
<li>audio right off</li>
<li>audio right on</li>
<li>bitspersample <em>bit_count</em></li>
<li>bytespersec <em>byte_rate</em></li>
<li>channels <em>channel_count</em></li>
<li>door closed</li>
<li>door open</li>
<li>format tag pcm</li>
<li>format tag <em>tag</em></li>
<li>input <em>integer</em></li>
<li>output <em>integer</em></li>
<li>samplespersec <em>integer</em></li>
<li>time format bytes</li>
<li>time format milliseconds</li>
<li>time format samples</li>
</ul></td>
</tr>
</tbody>
</table>



 

The following table lists the flags that can be specified in the **lpszSetting** parameter and their meanings.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>alignment <em>integer</em></td>
<td>Sets the alignment of data blocks relative to the start of data passed to the waveform-audio device. The file is saved in this format.</td>
</tr>
<tr class="even">
<td>any input</td>
<td>Use any input that supports the current format when recording. This is the default setting.</td>
</tr>
<tr class="odd">
<td>any output</td>
<td>Use any output that supports the current format when playing. This is the default.</td>
</tr>
<tr class="even">
<td>assemble record on <br/> assemble record off <br/></td>
<td>In assemble mode, all tracks are recorded as defined by the device. Most VCRs are in assemble mode by default.</td>
</tr>
<tr class="odd">
<td>audio all off <br/> audio all on <br/></td>
<td>Disables or enables audio output. Video-overlay devices, the MCISEQ sequencer, and the MCIWAVE waveform-audio device do not support this flag.</td>
</tr>
<tr class="even">
<td>audio left off <br/> audio left on <br/> audio right off <br/> audio right on <br/></td>
<td>Disables or enables output to either the left or the right audio channel. Video-overlay devices, the MCISEQ sequencer, and the MCIWAVE waveform-audio device do not support this flag.</td>
</tr>
<tr class="odd">
<td>bitspersample <em>bit_count</em></td>
<td>Sets the number of bits per PCM (Pulse Code Modulation) sample played or recorded. The file is saved in this format.</td>
</tr>
<tr class="even">
<td>bytespersec <em>byte_rate</em></td>
<td>Sets the average number of bytes per second played or recorded. The file is saved in this format.</td>
</tr>
<tr class="odd">
<td>channels <em>channel_count</em></td>
<td>Sets the channels for playing and recording. The file is saved in this format.</td>
</tr>
<tr class="even">
<td>clock <em>time</em></td>
<td>Sets time on the external clock to <em>time.</em> The format is specified as a long unsigned integer.</td>
</tr>
<tr class="odd">
<td>counter format</td>
<td>Set the time format for the counter, as returned by <a href="status.md">status</a> &quot;counter&quot;. For information about applicable types, see the <strong>set</strong> &quot;time format&quot; command.</td>
</tr>
<tr class="even">
<td>counter <em>value</em></td>
<td>Sets the VCR counter to the specified value. The value must be specified in the current counter format. For more information, see the <strong>set</strong> &quot;counter format&quot; command.</td>
</tr>
<tr class="odd">
<td>door closed</td>
<td>Retracts the tray and closes the door, if possible. For VCRs, loads the tape automatically.</td>
</tr>
<tr class="even">
<td>door open</td>
<td>Opens the door and ejects the tray or tape, if possible.</td>
</tr>
<tr class="odd">
<td>file format <em>format</em></td>
<td>Specifies a file format that is used for <a href="save.md">save</a> or <a href="capture.md">capture</a> commands. If omitted, this might default to a device driver defined format. If the specified file format conflicts with the currently selected algorithm and quality, then they are changed to the defaults for the file format. The following file formats are defined:
<ul>
<li>avi: Specifies AVI format.</li>
<li>avss: Specifies AVSS format.</li>
<li>dib: Specifies DIB format.</li>
<li>jfif: Specifies JFIF format.</li>
<li>jpeg: Specifies JPEG format.</li>
<li>mpeg: Specifies MPEG format.</li>
<li>rdib: Specifies RLE DIB format.</li>
<li>rjpeg: Specifies RJPEG format.</li>
</ul></td>
</tr>
<tr class="even">
<td>format tag pcm</td>
<td>Sets the format type to PCM for playing and recording. The file is saved in this format.</td>
</tr>
<tr class="odd">
<td>format tag <em>tag</em></td>
<td>Sets the format type for playing and recording. The file is saved in this format.</td>
</tr>
<tr class="even">
<td>index timecode <br/> index counter <br/> index date <br/> index time <br/></td>
<td>Sets the current display screen on the VCR.</td>
</tr>
<tr class="odd">
<td>input <em>integer</em></td>
<td>Sets the audio channel used as the input.</td>
</tr>
<tr class="even">
<td>length <em>duration</em></td>
<td>Sets the user-specified length of the tape in the VCR. This length is returned by the <a href="status.md">status</a> &quot;length&quot; command and is provided for compatibility with applications that require this command to return a valid length.</td>
</tr>
<tr class="odd">
<td>master midi</td>
<td>Sets the MIDI sequencer as the synchronization source. Synchronization data is sent in MIDI format. The MCISEQ sequencer does not support this flag.</td>
</tr>
<tr class="even">
<td>master none</td>
<td>Inhibits the MIDI sequencer from sending synchronization data. The MCISEQ sequencer does not support this flag.</td>
</tr>
<tr class="odd">
<td>master smpte</td>
<td>Sets the MIDI sequencer as the synchronization source. Synchronization data is sent in SMPTE (Society of Motion Picture and Television Engineers) format. The MCISEQ sequencer does not support this flag.</td>
</tr>
<tr class="even">
<td>offset <em>time</em></td>
<td>Sets the SMPTE offset <em>time</em>. The offset is the beginning time of a SMPTE based sequence. The <em>time</em> is expressed as <em>hh</em>: <em>mm</em>: <em>ss</em>: <em>ff</em>, where <em>hh</em> is hours, <em>mm</em> is minutes, <em>ss</em> is seconds, and <em>ff</em> is frames.</td>
</tr>
<tr class="odd">
<td>output <em>integer</em></td>
<td>Sets the audio channel used as the output.</td>
</tr>
<tr class="even">
<td>pause <em>timeout</em></td>
<td>Sets the maximum duration, in milliseconds, of a <a href="pause.md">pause</a> command. A <em>timeout</em> value of zero indicates that no time-out will occur.</td>
</tr>
<tr class="odd">
<td>postroll duration <em>duration</em></td>
<td>Sets the length, in the current time format, needed to brake the VCR transport when a <a href="stop.md">stop</a> or <strong>pause</strong> command is issued.</td>
</tr>
<tr class="even">
<td>port mapper</td>
<td>Sets the MIDI mapper as the port receiving the MIDI messages. This command fails if the MIDI mapper or a port it needs is being used by another application.</td>
</tr>
<tr class="odd">
<td>port none</td>
<td>Disables the sending of MIDI messages. This command also closes a MIDI port.</td>
</tr>
<tr class="even">
<td>port <em>port_number</em></td>
<td>Sets the MIDI port receiving the MIDI messages. This command fails if the port you are trying to open is being used by another application.</td>
</tr>
<tr class="odd">
<td>power on <br/> power off <br/></td>
<td>Sets the device power to on or off.</td>
</tr>
<tr class="even">
<td>preroll duration <em>duration</em></td>
<td>Sets the length, in the current time format, needed to stabilize the VCR output.</td>
</tr>
<tr class="odd">
<td>record format SP <br/> record format LP <br/> record format EP <br/></td>
<td>Sets the recording mode for the VCR to SP for standard play, EP for extended play, or LP for long play. These values are not intended to be VHS specific. They map to any three appropriate modes with other tape formats. For example, SP maps to the fastest, highest quality recording.</td>
</tr>
<tr class="even">
<td>samplespersec <em>integer</em></td>
<td>Sets the sample rate for playing and recording. The file is saved in this format.</td>
</tr>
<tr class="odd">
<td>seek exactly on<br/> seek exactly off <br/></td>
<td>Selects one of two seek modes. With &quot;seek exactly on&quot;, seek will always move to the frame specified. With &quot;seek exactly off&quot;, seek will move to the closest key frame prior to the frame specified.</td>
</tr>
<tr class="even">
<td>slave file</td>
<td>Sets the MIDI sequencer to use file data as the synchronization source. This is the default setting.</td>
</tr>
<tr class="odd">
<td>slave midi</td>
<td>Sets the MIDI sequencer to use incoming MIDI data for the synchronization source. The sequencer recognizes synchronization data with the MIDI format. The MCISEQ sequencer does not support this flag.</td>
</tr>
<tr class="even">
<td>slave none</td>
<td>Sets the MIDI sequencer to ignore synchronization</td>
</tr>
<tr class="odd">
<td>slave smpte</td>
<td>Sets the MIDI sequencer to use incoming MIDI data for the synchronization source. The sequencer recognizes synchronization data with the SMPTE format. The MCISEQ sequencer does not support this flag.</td>
</tr>
<tr class="even">
<td>speed factor</td>
<td>Sets the relative speed of video and audio playback from the workspace. Factor is the ratio between the nominal frame rate and the desired frame rate, where the nominal frame rate is designated as 1000. (A rate of 500 is half normal speed, 2000 is twice normal speed, and so on.) Setting the speed to zero plays the video as fast as possible without dropping frames and without audio.</td>
</tr>
<tr class="odd">
<td>still file format <em>format</em></td>
<td>Specifies the file format used for capture commands.</td>
</tr>
<tr class="even">
<td>tempo tempo_value</td>
<td>Sets the tempo of the sequence according to the current time format. For a PPQN-based file, the tempo_value is interpreted as beats per minute. For a SMPTE-based file, the tempo_value is interpreted as frames per second.</td>
</tr>
<tr class="odd">
<td>time format bytes</td>
<td>In a PCM file format, sets the time format to bytes. All position information is specified as bytes following this command.</td>
</tr>
<tr class="even">
<td>time format frames</td>
<td>Sets the time format to frames. All commands that use position values will assume frames. When the device is opened, frames is the default mode. Supported by videodiscs using CAV format.</td>
</tr>
<tr class="odd">
<td>time format hms</td>
<td>Sets the time format to hours, minutes, and seconds. All commands that use position values will assume HMS. HMS is the default format for CLV videodiscs. Specify an HMS value as hh:mm:ss, where hh is hours, mm is minutes, and ss is seconds. You can omit a field if it and all following fields are zero. For example, 3, 3:0, and 3:0:0 are all valid ways to express 3 hours. <br/></td>
</tr>
<tr class="even">
<td>time format milliseconds</td>
<td>Sets the time format to milliseconds. All commands that use position values will assume milliseconds. You can abbreviate milliseconds as &quot;ms&quot;. For sequencer devices, the sequence file sets the default format to PPQN or SMPTE. Video-overlay devices do not support this flag.<br/></td>
</tr>
<tr class="odd">
<td>time format msf</td>
<td>Sets the time format to minutes, seconds, and frames. All commands that use position values will assume MSF (the default format for CD audio). Specify an MSF value as mm:ss:ff, where mm is minutes, ss is seconds, and ff is frames. You can omit a field if it and all following fields are zero. For example, 3, 3:0, and 3:0:0 are valid ways to express 3 minutes.<br/> The MSF fields have the following maximum values:<br/>
<ul>
<li>Minutes 99</li>
<li>Seconds 59</li>
<li>Frames 74</li>
</ul></td>
</tr>
<tr class="even">
<td>time format samples</td>
<td>Sets the time format to samples. All position information is specified as samples following this command.</td>
</tr>
<tr class="odd">
<td>time format smpte 24<br/> time format smpte 25<br/> time format smpte 30<br/></td>
<td>Sets the time format to an SMPTE frame rate. For VCRs, sets the time format to hh:mm:ss:ff, where the legal values are 00:00:00:00 through 23:59:59:xx, and xx is one less than the frames per second as specified by the number 24, 25, or 30 as specified in the flag. On input, colons (:) are required to separate the components. The least significant units can be omitted if they are 00; for example, 02:00 is the same as 02:00:00:00. All commands that use position values will assume SMPTE format.<br/> The sequence file sets the default format to PPQN or SMPTE.<br/></td>
</tr>
<tr class="even">
<td>time format smpte 30 drop</td>
<td>Sets the time format to SMPTE 30 drop frame rate. For VCRs, same as SMPTE 30, except that certain timecode positions are dropped from the format to have the recorded timecode positions for each frame (at the NTSC frame rate of 29.97 fps) correspond to real time (at 30 fps). Timecode positions that are dropped are as follows: two every minute, on the minute, for the first nine of every ten minutes of recorded content. For example, at 01:04:59:29, the next timecode position would be 01:05:00:02, not 01:05:00:00. All commands that use position values will assume SMPTE format.<br/> The sequence file sets the default format to PPQN or SMPTE.<br/></td>
</tr>
<tr class="odd">
<td>time format song pointer</td>
<td>Sets the time format to song pointer (sixteenth notes). All commands that use position values will assume song pointer units. This flag is valid only for a sequence of division type PPQN.</td>
</tr>
<tr class="even">
<td>time format tmsf</td>
<td>Sets the time format to tracks, minutes, seconds, and frames. All commands that use position values will assume TMSF. Specify a TMSF value as tt:mm:ss:ff, where tt is tracks, mm is minutes, ss is seconds, and ff is frames. You can omit a field if it and all following fields are zero. For example, 3, 3:0, 3:0:0, and 3:0:0:0 are all valid ways to express track 3. <br/> The TMSF fields have the following maximum values:<br/>
<ul>
<li>Tracks 99</li>
<li>Minutes 90</li>
<li>Seconds 59</li>
<li>Frames 74</li>
</ul></td>
</tr>
<tr class="odd">
<td>time format track</td>
<td>Sets the position format to tracks. All commands that use position values will assume tracks.</td>
</tr>
<tr class="even">
<td>time mode counter</td>
<td>Sets the position-information mode to use the VCR counters.</td>
</tr>
<tr class="odd">
<td>time mode detect</td>
<td>Sets the position information mode based on detection of timecode information on the tape. If timecode information is detected, the time type is set to &quot;timecode&quot;; otherwise, the time type is set to &quot;counter&quot;. &quot;Detect&quot; is a special mode. Whenever the driver is opened, a new tape is inserted, or the &quot;time mode&quot; command is issued, the driver checks the current time mode available on the tape and sets &quot;time type&quot; to either &quot;timecode&quot; or &quot;counter&quot;. Once &quot;time type&quot; is set, the driver doesn't change it until one of the above conditions occurs again.<br/></td>
</tr>
<tr class="even">
<td>time mode timecode</td>
<td>Sets the position information mode to use &quot;timecode&quot; information on the tape.</td>
</tr>
<tr class="odd">
<td>tracking plus <br/> tracking minus <br/> tracking reset <br/></td>
<td>Adjusts the speed of the videotape transport in fine increments. Use the &quot;tracking&quot; flags when a noisy picture is obtained from a VCR. &quot;Tracking plus&quot; increases the transport speed. &quot;Tracking minus&quot; decreases the transport speed. &quot;Tracking reset&quot; returns the tracking adjustment to zero.</td>
</tr>
<tr class="even">
<td>video off</td>
<td>Disables video output.</td>
</tr>
<tr class="odd">
<td>video on</td>
<td>Enables video output.</td>
</tr>
</tbody>
</table>



 

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

 

