---
title: status command
description: The status command requests status information from a device. All devices recognize this command.
ms.assetid: '39961bd7-866d-450d-9fbf-347a8f508481'
keywords:
- status command Windows Multimedia
topic_type:
- apiref
api_name:
- status
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---




# status command

> [!NOTE]
> Bias-free Communication
Microsoft supports a diverse and inclusionary environment.  Within this document, there are references to the word 'slave.' Microsoft's [Style Guide for Bias-Free Communications](https://github.com/MicrosoftDocs/microsoft-style-guide/blob/master/styleguide/bias-free-communication.md) recognizes this as an exclusionary word.  This wording is used as it is currently the wording used within the commands. For consistency, this document contains this word. When this word is altered in the commands, we will correct this document to be in alignment.

The status command requests status information from a device. All devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand,
  TEXT("status %s %s %s"),
  lpszDeviceID,
  lpszRequest,
  lpszFlags
);
      
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszRequest"></span><span id="lpszrequest"></span><span id="LPSZREQUEST"></span>*lpszRequest*
</dt> <dd>

Flag for requesting status information. The following table lists device types that recognize the **status** command and the flags used by each type.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Device Type</th>
<th>Request Flags</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>cdaudio</td>
<td><ul>
<li>cdaudio type track <em>number</em></li>
<li>current track</li>
<li>length</li>
<li>length track <em>number</em></li>
<li>media present</li>
<li>mode</li>
<li>number of tracks</li>
<li>position</li>
<li>position track <em>number</em></li>
<li>ready</li>
<li>start position</li>
<li>time format</li>
</ul></td>
</tr>
<tr class="even">
<td>digitalvideo</td>
<td><ul>
<li>audio</li>
<li>audio alignment</li>
<li>audio bitspersample</li>
<li>audio breaks</li>
<li>audio bytespersec</li>
<li>audio input</li>
<li>audio record</li>
<li>audio source</li>
<li>audio samplespersec</li>
<li>audio stream</li>
<li>bass</li>
<li>bitsperpel</li>
<li>brightness</li>
<li>color</li>
<li>contrast</li>
<li>current track</li>
<li>disk space <em>drive</em></li>
<li>file completion</li>
<li>file format</li>
<li>file mode</li>
<li>forward</li>
<li>frames skipped</li>
<li>gamma</li>
<li>input</li>
<li>left volume</li>
<li>length</li>
<li>length track <em>number</em></li>
<li>media present</li>
<li>mode</li>
<li>monitor</li>
<li>monitor method</li>
<li>nominal</li>
<li>nominal frame rate</li>
<li>nominal record frame rate</li>
<li>number of tracks</li>
<li>output</li>
<li>palette handle</li>
<li>pause mode</li>
<li>play speed</li>
<li>position</li>
<li>position track <em>number</em></li>
<li>ready</li>
<li>record frame rate</li>
<li>reference <em>frame</em></li>
<li>reserved size</li>
<li>right volume</li>
<li>seek exactly</li>
<li>sharpness</li>
<li>smpte</li>
<li>speed</li>
<li>start position</li>
<li>still file format</li>
<li>time format</li>
<li>tint</li>
<li>treble</li>
<li>unsaved</li>
<li>video</li>
<li>video key index</li>
<li>video key color</li>
<li>video record</li>
<li>video source</li>
<li>video source number</li>
<li>video stream</li>
<li>volume</li>
<li>window handle</li>
<li>window visible</li>
<li>window minimized</li>
<li>window maximized</li>
</ul></td>
</tr>
<tr class="odd">
<td>overlay</td>
<td><ul>
<li>media present</li>
<li>mode</li>
<li>number of tracks</li>
<li>ready</li>
<li>stretch</li>
<li>window handle</li>
</ul></td>
</tr>
<tr class="even">
<td>sequencer</td>
<td><ul>
<li>current track</li>
<li>division type</li>
<li>length</li>
<li>length track <em>number</em> master</li>
<li>media present</li>
<li>mode</li>
<li>number of tracks</li>
<li>offset</li>
<li>port</li>
<li>position</li>
<li>position track <em>number</em></li>
<li>ready</li>
<li>slave</li>
<li>start position</li>
<li>tempo</li>
<li>time format</li>
</ul></td>
</tr>
<tr class="odd">
<td>vcr</td>
<td><ul>
<li>assemble record</li>
<li>audio monitor</li>
<li>audio monitor number</li>
<li>audio record</li>
<li>audio record track <em>number</em></li>
<li>audio source</li>
<li>audio source number</li>
<li>channel</li>
<li>channel tuner <em>number</em></li>
<li>clock</li>
<li>clock id</li>
<li>counter</li>
<li>counter format</li>
<li>counter resolution</li>
<li>current track</li>
<li>frame rate</li>
<li>index</li>
<li>index on</li>
<li>length</li>
<li>length track <em>number</em></li>
<li>media present</li>
<li>media type</li>
<li>mode</li>
<li>number of audio tracks</li>
<li>number of tracks</li>
<li>number of video tracks</li>
<li>pause <em>timeout</em></li>
<li>play format</li>
<li>position</li>
<li>position start</li>
<li>position track <em>number</em></li>
<li>postroll <em>duration</em></li>
<li>power on</li>
<li>preroll <em>duration</em></li>
<li>ready</li>
<li>record format</li>
<li>speed</li>
<li>time format</li>
<li>time mode</li>
<li>time type</li>
<li>timecode present</li>
<li>timecode record</li>
<li>timecode type</li>
<li>tuner number</li>
<li>video monitor</li>
<li>video monitor number</li>
<li>video record</li>
<li>video record track <em>number</em></li>
<li>video source</li>
<li>video source number</li>
<li>write protected</li>
</ul></td>
</tr>
<tr class="even">
<td>videodisc</td>
<td><ul>
<li>current track</li>
<li>disc size</li>
<li>forward</li>
<li>length</li>
<li>length track <em>number</em></li>
<li>media present</li>
<li>media type</li>
<li>mode</li>
<li>number of tracks</li>
<li>position</li>
<li>position track <em>number</em></li>
<li>ready</li>
<li>side</li>
<li>speed</li>
<li>start position</li>
<li>time format</li>
</ul></td>
</tr>
<tr class="odd">
<td>waveaudio</td>
<td><ul>
<li>alignment</li>
<li>bitspersample</li>
<li>bytespersec</li>
<li>channels</li>
<li>current track</li>
<li>format tag</li>
<li>input</li>
<li>length</li>
<li>length track <em>number</em></li>
<li>level</li>
<li>media present</li>
<li>mode</li>
<li>number of tracks</li>
<li>output</li>
<li>position</li>
<li>position track <em>number</em></li>
<li>ready</li>
<li>samplespersec</li>
<li>start position</li>
<li>time format</li>
</ul></td>
</tr>
</tbody>
</table>



 

The following table lists the flags that can be specified in the **lpszRequest** parameter and their meanings.



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
<td>alignment</td>
<td>Returns the block alignment of data, in bytes.</td>
</tr>
<tr class="even">
<td>assemble record</td>
<td>Returns <strong>TRUE</strong> if the device is set to assemble mode recording.</td>
</tr>
<tr class="odd">
<td>audio</td>
<td>Returns &quot;on&quot; or &quot;off&quot; depending on the most recent <a href="setaudio.md">setaudio</a> &quot;on&quot; or &quot;off&quot; command. It returns &quot;on&quot; if either or both speakers are enabled, and &quot;off&quot; otherwise.</td>
</tr>
<tr class="even">
<td>audio alignment</td>
<td>Returns the alignment of data blocks relative to the start of input waveform-audio data.</td>
</tr>
<tr class="odd">
<td>audio bitspersample</td>
<td>Returns the number of bits per sample the device uses for recording. This flag applies only to devices supporting the &quot;pcm&quot; algorithm.</td>
</tr>
<tr class="even">
<td>audio breaks</td>
<td>Returns the number of times the audio portion of the last AVI sequence broke up. The system counts an audio break whenever it attempts to write audio data to the device driver and discovers that the driver has already played all of the available data. This flag is recognized only by the MCIAVI digital-video driver. It is meant for performance evaluation only; the return value is difficult to interpret.</td>
</tr>
<tr class="odd">
<td>audio bytespersec</td>
<td>Returns the average number of bytes per second used for recording.</td>
</tr>
<tr class="even">
<td>audio input</td>
<td>Returns the approximate instantaneous audio level of the analog input audio signal. A value greater than 1000 implies clipping distortion. Some devices can return this value only while recording audio. The value has no associated <a href="set.md">set</a> or <a href="setaudio.md">setaudio</a> command.</td>
</tr>
<tr class="odd">
<td>audio monitor</td>
<td>Returns &quot;output&quot;, or one of the valid source-input types. For more information, see the <strong>setaudio</strong> &quot;monitor&quot; command.</td>
</tr>
<tr class="even">
<td>audio monitor number</td>
<td>Returns the monitored-video number of the type specified by <strong>status</strong> &quot;audio monitor&quot;. For more information, see the <a href="setaudio.md">setaudio</a> command.</td>
</tr>
<tr class="odd">
<td>audio record</td>
<td>Returns &quot;on&quot; or &quot;off&quot;, reflecting the state set by <strong>setaudio</strong> &quot;record&quot;.</td>
</tr>
<tr class="even">
<td>audio record track <em>number</em></td>
<td>Returns <strong>TRUE</strong> if the VCR is set to record audio. If no track number is given, the default value of 1 is assumed.</td>
</tr>
<tr class="odd">
<td>audio samplespersec</td>
<td>Returns the number of samples per second recorded.</td>
</tr>
<tr class="even">
<td>audio source</td>
<td>Returns the current audio digitizer source: &quot;left&quot;, &quot;right&quot;, &quot;average&quot;, or &quot;stereo&quot;.</td>
</tr>
<tr class="odd">
<td>audio source number</td>
<td>Returns the audio-source number of the type returned by <strong>status</strong> &quot;audio source&quot;. For more information, see the <a href="setaudio.md">setaudio</a> command.</td>
</tr>
<tr class="even">
<td>audio stream</td>
<td>Returns the current audio-stream number.</td>
</tr>
<tr class="odd">
<td>bass</td>
<td>Returns the current audio-bass level.</td>
</tr>
<tr class="even">
<td>bitsperpel</td>
<td>Returns the number of bits per pixel for saving captured or recorded data.</td>
</tr>
<tr class="odd">
<td>bitspersample</td>
<td>Returns the bits per sample.</td>
</tr>
<tr class="even">
<td>brightness</td>
<td>Returns the current video-brightness level.</td>
</tr>
<tr class="odd">
<td>bytespersec</td>
<td>Returns the average number of bytes per second played or recorded.</td>
</tr>
<tr class="even">
<td>cdaudio type track <em>number</em></td>
<td>Returns the type of the specified track number. This can be &quot;audio&quot; or &quot;other.&quot;</td>
</tr>
<tr class="odd">
<td>channel</td>
<td>Returns the integer value of the channel set on the tuner.</td>
</tr>
<tr class="even">
<td>channel tuner <em>number</em></td>
<td>If &quot;tuner&quot; <em>number</em> is given, then the currently selected channel on the logical tuner <em>number</em> will be returned. Note that there can be several logical tuners.</td>
</tr>
<tr class="odd">
<td>channels</td>
<td>Returns the number of channels set (1 for mono, 2 for stereo).</td>
</tr>
<tr class="even">
<td>clock</td>
<td>Returns the external time. The time must be an unsigned long integer expressing total increments. For more information, see the <a href="capability.md">capability</a> &quot;clock increment rate&quot; command.</td>
</tr>
<tr class="odd">
<td>clock id</td>
<td>Returns a unique integer identifying the clock.</td>
</tr>
<tr class="even">
<td>color</td>
<td>Returns the current color level.</td>
</tr>
<tr class="odd">
<td>contrast</td>
<td>Returns the current contrast level.</td>
</tr>
<tr class="even">
<td>counter</td>
<td>Returns the counter position, in the current counter format.</td>
</tr>
<tr class="odd">
<td>counter format</td>
<td>Returns the current counter format. For more information, see the <a href="set.md">set</a> &quot;counter format&quot; command.</td>
</tr>
<tr class="even">
<td>counter resolution</td>
<td>Returns &quot;frames&quot; or &quot;seconds&quot;, indicating the counter's resolution. This is not the same as accuracy.</td>
</tr>
<tr class="odd">
<td>current track</td>
<td>Returns the current track. The MCISEQ sequencer returns 1.</td>
</tr>
<tr class="even">
<td>disc size</td>
<td>Returns either 8 or 12, indicating the size of the loaded disc in inches.</td>
</tr>
<tr class="odd">
<td>disk space <em>drive</em></td>
<td>Returns the approximate disk space, in the current time format, that can be obtained by a <a href="reserve.md">reserve</a> command for the specified disk <em>drive.</em> The <em>drive</em> is usually specified as a single letter or a single letter followed by a colon (:). Some devices, however, might use a path.</td>
</tr>
<tr class="even">
<td>division type</td>
<td>Returns one of the following file division types:
<ul>
<li>PPQN</li>
<li>SMPTE 24 frame</li>
<li>SMPTE 25 frame</li>
<li>SMPTE 30 drop frame</li>
<li>SMPTE 30 frame</li>
</ul>
<br/> Use this information to determine the format of the MIDI file and the meaning of tempo and position information.<br/></td>
</tr>
<tr class="odd">
<td>file completion</td>
<td>Returns the estimated percentage a <a href="load.md">load</a>, <a href="save.md">save</a>, <a href="capture.md">capture</a>, <a href="cut.md">cut</a>, <a href="copy.md">copy</a>, <a href="delete.md">delete</a>, <a href="paste.md">paste</a>, or <a href="undo.md">undo</a> operation has progressed. (Applications can use this to provide a visual indicator of progress.)</td>
</tr>
<tr class="even">
<td>file format</td>
<td>Returns the current file format for <a href="record.md">record</a> or <strong>save</strong> commands.</td>
</tr>
<tr class="odd">
<td>file mode</td>
<td>Returns &quot;loading&quot;, &quot;saving&quot;, &quot;editing&quot;, or &quot;idle&quot;. During a <a href="load.md"><strong>load</strong></a> operation, it returns &quot;loading&quot;. During <a href="https://www.bing.com/search?q=<strong>save</strong>"><strong>save</strong></a> and <a href="capture.md"><strong>capture</strong></a> operations, it returns &quot;saving&quot;. During <a href="cut.md"><strong>cut</strong></a>, <a href="copy.md"><strong>copy</strong></a>, <a href="delete.md"><strong>delete</strong></a>, <a href="paste.md"><strong>paste</strong></a>, or <a href="undo.md"><strong>undo</strong></a> operations, it returns &quot;editing&quot;.</td>
</tr>
<tr class="even">
<td>format tag</td>
<td>Returns the format tag.</td>
</tr>
<tr class="odd">
<td>forward</td>
<td>Returns <strong>TRUE</strong> if the play direction is forward or if the device is not playing.</td>
</tr>
<tr class="even">
<td>frame rate</td>
<td>Returns the number of frames per second that the device will use by default. NTSC devices return 30, PAL 25, and so on.</td>
</tr>
<tr class="odd">
<td>frames skipped</td>
<td>Returns the number of frames that were not drawn when the last AVI sequence was played. This flag is recognized only by the MCIAVI digital-video driver. It is meant for performance evaluation only; the return value is difficult to interpret.</td>
</tr>
<tr class="even">
<td>gamma</td>
<td>Returns the value set with <a href="setvideo.md"><strong>setvideo</strong></a> &quot;gamma to&quot; <em>value</em>.</td>
</tr>
<tr class="odd">
<td>index</td>
<td>Returns the current index display. For more information, see the <a href="set.md"><strong>set</strong></a> &quot;index&quot; command.</td>
</tr>
<tr class="even">
<td>index on</td>
<td>Returns <strong>TRUE</strong> if the index is on.</td>
</tr>
<tr class="odd">
<td>input</td>
<td>Returns the input set. If one is not set, the error returned indicates that any device can be used. For digital-video devices, modifies the &quot;bass&quot;, &quot;treble&quot;, &quot;volume&quot;, &quot;brightness&quot;, &quot;color&quot;, &quot;contrast&quot;, &quot;gamma&quot;, &quot;sharpness&quot;, or &quot;tint&quot; flag so that it applies only to the input. This is the default when monitoring the input.</td>
</tr>
<tr class="even">
<td>left volume</td>
<td>Returns the volume set for the left audio channel.</td>
</tr>
<tr class="odd">
<td>length</td>
<td>Returns the total length of the media, in the current time format. For PPQN files, the length is returned in song pointer units. For SMPTE files, it is returned as <em>hh:mm:ss:ff</em>, where <em>hh</em> is hours, <em>mm</em> is minutes, <em>ss</em> is seconds, and <em>ff</em> is frames. For VCR devices, the length is 2 hours (unless the length has been explicitly changed using the <a href="https://www.bing.com/search?q=<strong>set</strong>"><strong>set</strong></a> command).</td>
</tr>
<tr class="even">
<td>length track <em>number</em></td>
<td>Returns the length of the track, in time or frames, specified by <em>number</em>.For PPQN files, the length is returned in song pointer units. For SMPTE files, it is returned as <em>hh:mm:ss:ff</em>, where <em>hh</em> is hours, <em>mm</em> is minutes, <em>ss</em> is seconds, and <em>ff</em> is frames.<br/></td>
</tr>
<tr class="odd">
<td>level</td>
<td>Returns the current PCM audio sample value.</td>
</tr>
<tr class="even">
<td>master</td>
<td>Returns &quot;midi&quot;, &quot;none&quot;, or &quot;smpte&quot; depending on the type of synchronization set.</td>
</tr>
<tr class="odd">
<td>media present</td>
<td>Returns <strong>TRUE</strong> if the media is inserted in the device or <strong>FALSE</strong> otherwise. Sequencer, video-overlay, digital-video, and waveform-audio devices return <strong>TRUE</strong>.</td>
</tr>
<tr class="even">
<td>media type</td>
<td>Returns the type of the media. For VCRS, this is &quot;8mm&quot;, &quot;vhs&quot;, &quot;svhs&quot;, &quot;beta&quot;, &quot;Hi8&quot;, &quot;edbeta&quot;, or &quot;other&quot;. For videodiscs, this is &quot;CAV&quot;, &quot;CLV&quot;, or &quot;other&quot;, depending on the type of videodisc.</td>
</tr>
<tr class="odd">
<td>mode</td>
<td>Returns the current mode of the device. All devices can return the &quot;not ready&quot;, &quot;paused&quot;, &quot;playing&quot;, and &quot;stopped&quot; values. Some devices can return the additional &quot;open&quot;, &quot;parked&quot;, &quot;recording&quot;, and &quot;seeking&quot; values.</td>
</tr>
<tr class="even">
<td>monitor</td>
<td>Returns &quot;file&quot; or &quot;input&quot;. The returned value indicates the current presentation source.</td>
</tr>
<tr class="odd">
<td>monitor method</td>
<td>Returns &quot;pre&quot;, &quot;post&quot;, or &quot;direct&quot;. The returned value indicates the method used for input monitoring.</td>
</tr>
<tr class="even">
<td>nominal</td>
<td>The item modifies the &quot;bass&quot;, &quot;brightness&quot;, &quot;color&quot;, &quot;contrast&quot;, &quot;gamma&quot;, &quot;sharpness&quot;, &quot;tint&quot;, &quot;treble,&quot; and &quot;volume&quot; flags to return the nominal value instead of the current setting.</td>
</tr>
<tr class="odd">
<td>nominal frame rate</td>
<td>Returns the nominal frame rate associated with the file. The units are in frames per second multiplied by 1000.</td>
</tr>
<tr class="even">
<td>nominal record frame rate</td>
<td>Returns the nominal frame rate associated with the input video signal. The units are in frames per second multiplied by 1000.</td>
</tr>
<tr class="odd">
<td>number of audio tracks</td>
<td>Returns the number of audio tracks on the media.</td>
</tr>
<tr class="even">
<td>number of tracks</td>
<td>Returns the number of tracks on the media. The MCISEQ and MCIWAVE devices return 1, as do most VCR devices. The MCIPIONR device does not support this flag.</td>
</tr>
<tr class="odd">
<td>number of video tracks</td>
<td>Returns the number of video tracks on the media.</td>
</tr>
<tr class="even">
<td>offset</td>
<td>Returns the offset of a SMPTE-based file. The offset is the start time of a SMPTE-based sequence. The time is returned as <em>hh:mm:ss:ff</em>, where <em>hh</em> is hours, <em>mm</em> is minutes, <em>ss</em> is seconds, and <em>ff</em> is frames.</td>
</tr>
<tr class="odd">
<td>output</td>
<td>Returns the currently set output. If no output is set, the error returned indicates that any device can be used. For digital-video devices, modifies the &quot;bass&quot;, &quot;treble&quot;, &quot;volume&quot;, &quot;brightness&quot;, &quot;color&quot;, &quot;contrast&quot;, &quot;gamma&quot;, &quot;sharpness&quot;, or &quot;tint&quot; flag so that it applies only to the output. This is the default when monitoring a file.</td>
</tr>
<tr class="even">
<td>pause mode</td>
<td>Returns &quot;recording&quot; if the device is paused while recording. It returns &quot;playing&quot; if the device is paused while playing. It returns the error &quot;Action not applicable in current mode&quot; if the device is not paused.</td>
</tr>
<tr class="odd">
<td>pause timeout</td>
<td>Returns the maximum duration, in milliseconds, of a <a href="pause.md"><strong>pause</strong></a> command.</td>
</tr>
<tr class="even">
<td>play format</td>
<td>Returns a code indicating the format that the videotape will be played back in, if detectable: &quot;lp&quot;, &quot;ep&quot;, &quot;sp&quot;, or &quot;other&quot;. For more information, see the &quot;record format&quot; flag.</td>
</tr>
<tr class="odd">
<td>play speed</td>
<td>Returns a value representing how closely the actual playing time of the last AVI sequence matched the target playing time. The value 1000 indicates that the target time and the actual time were the same. A value of 2000, for example, would indicate that the AVI sequence took twice as long to play as it should have. This flag is recognized only by the MCIAVI digital-video driver. It is meant for performance evaluation only; the return value is difficult to interpret.</td>
</tr>
<tr class="even">
<td>port</td>
<td>Returns the MIDI port number assigned to the sequence.</td>
</tr>
<tr class="odd">
<td>position</td>
<td>Returns the current position.For PPQN files, the position is returned in song pointer units. For SMPTE files, it is returned as <em>hh:mm:ss:ff</em>, where <em>hh</em> is hours, <em>mm</em> is minutes, ss is seconds, and <em>ff</em> is frames.<br/></td>
</tr>
<tr class="even">
<td>position start</td>
<td>Returns the position of the start of the usable media.</td>
</tr>
<tr class="odd">
<td>position track <em>number</em></td>
<td>Returns the position of the start of the track specified by <em>number</em>. For PPQN files, the time format is returned in song pointer units. For SMPTE files, it is returned as <em>hh:mm:ss:ff</em>, where <em>hh</em> is hours, <em>mm</em> is minutes, <em>ss</em> is seconds, and <em>ff</em> is frames. The MCISEQ sequencer returns zero. The MCIPIONR device does not support this flag. The MCIWAVE device returns zero.</td>
</tr>
<tr class="even">
<td>postroll duration</td>
<td>Returns the length of videotape, in the current time format, needed to brake the VCR transport when a <a href="stop.md"><strong>stop</strong></a> or <a href="pause.md"><strong>pause</strong></a> command is issued.</td>
</tr>
<tr class="odd">
<td>power on</td>
<td>Returns <strong>TRUE</strong> if the VCR's power is on.</td>
</tr>
<tr class="even">
<td>preroll duration</td>
<td>Returns the length of videotape, in the current time format, needed to stabilize the VCR output.</td>
</tr>
<tr class="odd">
<td>ready</td>
<td>Returns <strong>TRUE</strong> if the device is ready to accept another command.</td>
</tr>
<tr class="even">
<td>record format</td>
<td>Returns a code indicating the format that the videotape will be recorded in. The current return types are &quot;lp&quot;, &quot;ep&quot;, &quot;sp&quot;, or &quot;other&quot;. These formats are not VHS specific and can be applied to any VCR that has multiple selectable recording formats. The &quot;sp&quot; type is the fastest, highest quality recording format and is used as default on single format VCRs.</td>
</tr>
<tr class="odd">
<td>record frame rate</td>
<td>Returns the frame rate, in frames per second multiplied by 1000, used for compression.</td>
</tr>
<tr class="even">
<td>reference <em>frame</em></td>
<td>Returns the frame number for the nearest key frame image that precedes the specified <em>frame</em>.</td>
</tr>
<tr class="odd">
<td>reserved size</td>
<td>Returns the size, in the current time format, of the reserved workspace. The size corresponds to the approximate time it would take to play the compressed data from a full workspace. It returns zero if there is no reserved disk space. This flag returns the approximate size because the precise disk space for compressed data cannot, in general, be predicted until after the data has been compressed.</td>
</tr>
<tr class="even">
<td>right volume</td>
<td>Returns the volume set for the right audio channel.</td>
</tr>
<tr class="odd">
<td>samplespersec</td>
<td>Returns the number of samples per second played or recorded.</td>
</tr>
<tr class="even">
<td>seek exactly</td>
<td>Returns &quot;on&quot; or &quot;off&quot;, indicating whether or not the &quot;seek exactly&quot; flag is set.</td>
</tr>
<tr class="odd">
<td>sharpness</td>
<td>Returns the current sharpness level of the device.</td>
</tr>
<tr class="even">
<td>side</td>
<td>Returns 1 or 2 to indicate which side of the videodisc is loaded.</td>
</tr>
<tr class="odd">
<td>slave</td>
<td>Returns &quot;file&quot; , &quot;midi&quot;, &quot;none&quot;, or &quot;smpte&quot; depending on the type of synchronization set.</td>
</tr>
<tr class="even">
<td>smpte</td>
<td>Returns the SMPTE timecode associated with the current position in the workspace. This is a string with the form <em>dd:dd:dd:dd</em>, where each <em>d</em> denotes a digit from 0 to 9. If the workspace data does not include timecode data, then this flag returns 00:00:00:00.</td>
</tr>
<tr class="odd">
<td>speed</td>
<td>Returns the current speed of the device in frames per second (or in the same format used by the <a href="https://www.bing.com/search?q=<strong>set</strong>"><strong>set</strong></a> &quot;speed&quot; command). The MCIPIONR videodisc player does not support this flag.</td>
</tr>
<tr class="even">
<td>start position</td>
<td>Returns the starting position of the media.</td>
</tr>
<tr class="odd">
<td>still file format</td>
<td>Returns the current file format for the <a href="capture.md"><strong>capture</strong></a> command.</td>
</tr>
<tr class="even">
<td>stretch</td>
<td>Returns <strong>TRUE</strong> if stretching is enabled.</td>
</tr>
<tr class="odd">
<td>tempo</td>
<td>Returns the current tempo of a MIDI sequence in the current time format. For files with PPQN format, the tempo is in beats per minute. For files with SMPTE format, the tempo is in frames per second.</td>
</tr>
<tr class="even">
<td>time format</td>
<td>Returns the current time format. For more information, see the time formats in the <a href="set.md"><strong>set</strong></a> command.</td>
</tr>
<tr class="odd">
<td>time mode</td>
<td>Returns the current position time mode. It can be &quot;detect&quot;, &quot;timecode&quot;, or &quot;counter&quot;.</td>
</tr>
<tr class="even">
<td>time type</td>
<td>Returns the current position time in use: &quot;timecode&quot; or &quot;counter&quot;.</td>
</tr>
<tr class="odd">
<td>timecode present</td>
<td>Returns <strong>TRUE</strong> if timecode has been recorded at the current position on the tape. The timecode must advance from the current position. A VCR might need to be played to check this condition.</td>
</tr>
<tr class="even">
<td>timecode record</td>
<td>Returns <strong>TRUE</strong> if the VCR is set to record timecode.</td>
</tr>
<tr class="odd">
<td>timecode type</td>
<td>Returns &quot;smpte&quot;, &quot;smpte drop&quot;, &quot;other&quot;, or &quot;none&quot;. Note the frames per second can be obtained from the status &quot;frame rate&quot; command, and the accuracy of the device can be returned by the <a href="capability.md"><strong>capability</strong></a> &quot;seek accuracy&quot; command.</td>
</tr>
<tr class="even">
<td>tint</td>
<td>Returns the current video-tint level.</td>
</tr>
<tr class="odd">
<td>treble</td>
<td>Returns the current audio-treble level.</td>
</tr>
<tr class="even">
<td>tuner number</td>
<td>Returns the current logical-tuner number.</td>
</tr>
<tr class="odd">
<td>unsaved</td>
<td>Returns <strong>TRUE</strong> if there is recorded data in the workspace that might be lost as a result of a <a href="close.md"><strong>close</strong></a>, <a href="load.md"><strong>load</strong></a>, <a href="record.md"><strong>record</strong></a>, <a href="reserve.md"><strong>reserve</strong></a>, <a href="cut.md"><strong>cut</strong></a>, <a href="delete.md"><strong>delete</strong></a>, or <a href="paste.md"><strong>paste</strong></a> command. Returns <strong>FALSE</strong> otherwise.</td>
</tr>
<tr class="even">
<td>video</td>
<td>Returns &quot;on&quot; or &quot;off&quot;, reflecting the state set by the <a href="setvideo.md"><strong>setvideo</strong></a> command.</td>
</tr>
<tr class="odd">
<td>video key color</td>
<td>Returns the value for the key color.</td>
</tr>
<tr class="even">
<td>video key index</td>
<td>Returns the value for the key index.</td>
</tr>
<tr class="odd">
<td>video monitor</td>
<td>Returns &quot;output&quot; or one of the valid source-input types. For more information, see the <a href="setvideo.md"><strong>setvideo</strong></a> &quot;monitor&quot; command.</td>
</tr>
<tr class="even">
<td>video monitor number</td>
<td>Returns the monitored-video number of the type returned by status &quot;video monitor&quot;. For more information, see the <a href="setvideo.md">setvideo</a> command.</td>
</tr>
<tr class="odd">
<td>video record</td>
<td>Returns &quot;on&quot; or &quot;off&quot;, reflecting the current state set by <a href="setvideo.md"><strong>setvideo</strong></a> &quot;record&quot;.</td>
</tr>
<tr class="even">
<td>video record track <em>number</em></td>
<td>Return <strong>TRUE</strong> if the VCR is set to record video. If no track number is given, the default value of 1 is assumed.</td>
</tr>
<tr class="odd">
<td>video source</td>
<td>Returns the video-source type. For more information, see the <a href="setvideo.md"><strong>setvideo</strong></a> command.</td>
</tr>
<tr class="even">
<td>video source number</td>
<td>Returns a number corresponding to the video source of the type in use. For example, it returns 2 if the second NTSC video source input is being used.</td>
</tr>
<tr class="odd">
<td>video stream</td>
<td>Returns the current video-stream number.</td>
</tr>
<tr class="even">
<td>volume</td>
<td>Returns the average volume to the left and right speaker. This returns an error if the device has not been played or volume has not been set.</td>
</tr>
<tr class="odd">
<td>window handle</td>
<td>Returns the ASCII decimal value for the window handle in the low-order word of the return value.</td>
</tr>
<tr class="even">
<td>window maximized</td>
<td>Returns <strong>TRUE</strong> if the window is maximized.</td>
</tr>
<tr class="odd">
<td>window minimized</td>
<td>Returns <strong>TRUE</strong> if the window is minimized.</td>
</tr>
<tr class="even">
<td>window visible</td>
<td>Returns <strong>TRUE</strong> if the window is not hidden.</td>
</tr>
<tr class="odd">
<td>write protected</td>
<td>Returns <strong>TRUE</strong> if the device detects that it cannot record (that is, if the write protect is on). If it can record, or if it is unable to determine whether or not it can record (without actually writing), the driver returns <strong>FALSE</strong>.</td>
</tr>
</tbody>
</table>



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video and VCR devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns information in the *lpszReturnString* parameter of [**mciSendString**](/previous-versions//dd757161(v=vs.85)). The information is dependent on the request type.

## Remarks

Before issuing any commands that use position values, you should set the desired time format by using the [set](set.md) command.

## Examples

The following command returns the current mode of the "mysound" device.

``` syntax
status mysound mode
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

[capability](capability.md)
</dt> <dt>

[capture](capture.md)
</dt> <dt>

[close](close.md)
</dt> <dt>

[cut](cut.md)
</dt> <dt>

[delete](delete.md)
</dt> <dt>

[load](load.md)
</dt> <dt>

[pause](pause.md)
</dt> <dt>

[paste](paste.md)
</dt> <dt>

[record](record.md)
</dt> <dt>

[reserve](reserve.md)
</dt> <dt>

[save](save.md)
</dt> <dt>

[set](set.md)
</dt> <dt>

[setaudio](setaudio.md)
</dt> <dt>

[setvideo](setvideo.md)
</dt> <dt>

[stop](stop.md)
</dt> <dt>

[undo](undo.md)
</dt> </dl>

 

