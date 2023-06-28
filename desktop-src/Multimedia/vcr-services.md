---
title: VCR Services
description: VCR Services
ms.assetid: 140220f7-df7b-46e2-8374-e1200d873f3b
keywords:
- Video System Control Architecture (VISCA)
- VISCA (Video System Control Architecture)
- MCI VISCA driver
- VISCA driver
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VCR Services

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows provides VCR services through a device driver that is based on the MCI command set for VCRs. This section describes the MCI Video System Control Architecture (VISCA) driver and explains how to use it to control a VCR.

The *vcr* device type controls VCRs. For a list of the MCI commands recognized by VCR devices, see [VCR Command Set](vcr-command-set.md).

## The MCI VISCA Driver

The MCI VISCA driver controls Sony VISCA-compatible VCRs, such as the CVD-1000 VDeck. The VISCA driver controls the tape transport, channel tuners, and VCR input and output channels.

## Searching and Positioning with a VCR

The VISCA driver uses two methods to track videotape movement within the VCR tape transport: *timecode information* and *tape counters*. Timecode information is timing information that has been recorded on the videotape. Most VCRs allow timecodes to be recorded without destroying audio and video tracks. Tape counters estimate the amount of videotape that travels past the videotape head to obtain a position.

Both timecode information and tape counters increase as the videotape moves from beginning to end. Because of its accuracy, using timecode information to position a videotape is almost always preferable to using tape counters.

The MCI command flags for specifying positioning information are expressed as time dependencies: "time format", "duration", "from", "to", and "seek". (Also, the [**status**](status.md) "position" command returns its time value in the current time format.)

The VISCA driver uses the [**set**](set.md) "time mode" command to select the type of positioning to use with a videotape. When the time mode is set to "timecode", the **status** "position" and **set** "time format" commands use the timecode on the videotape. When the time mode is set to "counter", the **status** "position" and **set** "time format" commands use counters.

An application can set the time mode to "detect" if it doesn't matter that there might be two sources of position information. When in detect mode, the VISCA driver uses timecode information for positioning when any of the following conditions occur:

-   The timecode information is present when the driver is opened.
-   You change a videotape with the **set** "door open" command and timecode information is present on the videotape.
-   The [**set**](set.md) "time mode" command is reissued.

If timecode information cannot be found, the driver uses the tape counters.

To determine the current positioning method, issue the [**status**](status.md) "time type" command, which returns either "timecode" or "counter". You can also identify the current positioning mode by using the **status** "time mode" command, which returns "timecode", "counter", or "detect".

The **status** "counter" command retrieves the current tape counter value, regardless of the current positioning method; however, you can use this counter reading only with the [**set**](set.md) "counter" command.

The VISCA driver can retrieve the native timecode format recorded on a videotape by using the **status** "timecode type" and **status** "frame rate" commands together. For example, if timecode type is "smpte" and frame rate is 25, the native timecode format recorded on the videotape is SMPTE 25.

The VISCA driver can also retrieve the counter resolution by using the **status** "counter resolution" command, which returns "seconds" or "frames". The counter format might still be set to SMPTE 30, but the return value returns only a frame of 0. If the current time type is counter, then this resolution applies also to the value returned by **status** "position".

## Capturing Frames

Frame-capturing commands provide still images for a *frame-capture device*. A frame-capture device is a separate piece of hardware capable of reading and storing the video image. The VISCA driver supports the [**freeze**](freeze.md) ([**MCI\_FREEZE**](mci-freeze.md)) command to stabilize a still image for capturing. Also, the [**unfreeze**](unfreeze.md) ([**MCI\_UNFREEZE**](mci-unfreeze.md)) command can be used to restart the tape transport following a **freeze** command.

The **freeze** command provides a high-quality, stabilized, time-base – corrected image for a frame-capture device. This command exists because a device might not always deliver its maximum-quality output image during playback or while paused; such a video image is not suitable for capturing.

The **unfreeze** command unlocks the tape transport and resumes the transport mode in effect before the **freeze** command.

When your application needs to record a video image on the VCR, use the **freeze** "input" command or the [**cue**](cue.md) ([**MCI\_CUE**](mci-cue.md)) command to record the image.

## Selecting Inputs

The VISCA driver supports three input types: video, audio, and timecode. The video inputs include two standard channels (lines 1 and 2), an SVideo channel, an auxiliary channel, and a channel from an internal tuner. The audio inputs include two standard channels (lines 1 and 2) and a channel from an internal tuner. The timecode input is internal to the VCR.

The normal outputs carry the currently selected inputs when the VCR is recording or when the tape transport is stopped, and they carry the contents of the videotape when the tape transport is playing or paused. The monitored outputs carry the same information as the normal outputs plus current timecode and channel information.

Assuming the appropriate external inputs are connected to your VCR and you have decided what you want to record, you can select the inputs to be recorded. For example, to record or view from the "svideo" video and the "line 1" audio inputs, you would use the [**setvideo**](setvideo.md) ([**MCI\_SETVIDEO**](mci-setvideo.md)) and [**setaudio**](setaudio.md) ([**MCI\_SETAUDIO**](mci-setaudio.md)) commands to select these input sources. You can verify these selections by using the [**status**](status.md) ([**MCI\_STATUS**](mci-status.md)) command.

By default, the monitor shows exactly what appears as the output. Sometimes, however, you might want to view one source while recording from another. This is a common practice using the tuner. For example, you might want to watch channel 4 while you record channel 7. In this case, you have two logical tuner inputs. You could set up the VCR by using the following commands:

## To review one source while recording from another

1.  Use the [**settuner**](settuner.md) ([**MCI\_SETTUNER**](mci-settuner.md)) command to select the channels to watch and record.
2.  Use the **setvideo** command to select the video-recording source.
3.  Use the [**setaudio**](setaudio.md) command to select the audio-recording source.
4.  Use the [**setvideo**](setvideo.md) command to route the channel 4 video input to the monitored output to display it on-screen.
5.  Use the [**setaudio**](setaudio.md) command to route the channel 4 audio input to the monitored output to play the audio.
6.  Verify your selections by using the [**status**](status.md) command.

The VISCA driver also supports a special input type for audio and video called *mute*. Mute allows the selection of "no input," which is useful when recording a blank signal.

## Selecting Recording Tracks

Three types of recording tracks exist on a videotape: video, audio, and timecode. You have only one video or timecode track, but you can use more than one audio track. When you do so, make track 1 the main audio track.

The VISCA driver supports two operating modes: assemble and insert. In *assemble mode*, all tracks are selected to be recorded. In *insert mode*, tracks can be independently selected for recording. Most VCRs are in assemble mode by default. Use the [**set**](set.md) ([**MCI\_SET**](mci-set.md)) command to change these modes.

## Recording and Editing

The [**record**](record.md) ([**MCI\_RECORD**](mci-record.md)) command provides simple recording and is accurate to approximately 1 second of the starting position. To record more accurately, or if you expect to edit the video content while simultaneously operating multiple decks, you should use the [**cue**](cue.md) ([**MCI\_CUE**](mci-cue.md)) command.

The **cue** command prepares the device for recording or playing. Use the **cue** "input" command to prepare the device for recording. The **cue** command is required because an application must know when the device is ready to perform the command (and because it can take several minutes to prepare for a [**play**](play.md) ([**MCI\_PLAY**](mci-play.md)) or **record** command).

The VCR prepares itself for recording or playing by seeking to the *in-point*, which is the current position or the position specified by using the **cue** "from" command. If the "preroll" flag is specified with the **cue** command, however, the VCR positions itself the preroll distance from the in-point. The "preroll" flag also indicates that the VCR uses any applicable editing mode, so it's important that you use "preroll", especially when you want the most accurate recording. (Use the [**capability**](capability.md) ([**MCI\_GETDEVCAPS**](mci-getdevcaps.md)) command with the "can preroll" flag to check whether the preroll mode is supported.)

> [!Note]  
> When you record using "from" and "to" positions, the "from" position is included in the edit, and the "to" position is not.

 

For more information about recording, see [Recording](recording.md).

## Using the Clock While Editing

When editing, you might want to record segments from one VCR to another. You can begin recording at a specific time and position on one VCR while another begins playing at the same time and position by specifying an action (play or record), a position, and a time for each VCR.

Both VCRs must use the same clock for this type of editing; the clock helps synchronize both devices. You can determine if two VCRs share the same clock by using the [**status**](status.md) ([**MCI\_STATUS**](mci-status.md)) command with the "clock id" flag to query each VCR. If the identification numbers returned by the **status** command are the same, the devices use the same clock. As a shared resource, the clock can be connected to multiple VCRs. The VISCA driver supports only one shared clock.

You can also determine clock resolution by using the **status** "clock increment rate" command. This command returns the number of increments the clock supports per second. For example, if the clock is updated every millisecond, the command returns 1000 as the clock increment rate. The advantage of using the increment rate is that the rate is expressed as an integer; otherwise, the increment would be a (single- or double-precision) floating-point value. As an integer, manipulating the increment rate is a simple operation and is not susceptible to rounding errors. You can reset the clock by using the [**set**](set.md) ([**MCI\_SET**](mci-set.md)) command with the "clock 0" (zero) flag.

When issuing a [**play**](play.md) ([**MCI\_PLAY**](mci-play.md)), [**record**](record.md) ([**MCI\_RECORD**](mci-record.md)), or [**seek**](seek.md) ([**MCI\_SEEK**](mci-seek.md)) command, you can specify when the command is to be executed. The characteristics of the VCRs being used determine when to start each VCR. The timing must account for the amount of preroll each device requires and the amount of time needed to complete the MCI commands used to set up the edit session. To do this, retrieve the clock time and add a waiting interval of 5 to 10 seconds. (The waiting interval must be long enough to let the preroll and any outstanding MCI commands finish executing.)

To ensure that the waiting period is long enough, place the **record** command last in your application and check the time immediately before it. If the interval is too short, restart the **play** command. Alternatively, you could check the time immediately after the last command of the script to verify that there is enough time to send and complete all the commands.

 

 




