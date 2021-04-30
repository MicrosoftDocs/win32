---
title: capability command
description: The capability command requests information about a particular capability of a device. All MCI devices recognize this command.
ms.assetid: 1b470473-0de6-41ba-9f6e-41f0b13ceaeb
keywords:
- capability command Windows Multimedia
topic_type:
- apiref
api_name:
- capability
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# capability command

The capability command requests information about a particular capability of a device. All MCI devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("capability %s %s %s"), 
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

Flag that identifies a device capability. The following table lists device types that recognize the **capability** command and the flags used by each type:



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Type</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>cdaudio</td>
<td><ul>
<li>can eject</li>
<li>can play</li>
<li>can record</li>
<li>can save</li>
<li>compound device</li>
</ul></td>
<td><ul>
<li>device type</li>
<li>has audio</li>
<li>has video</li>
<li>uses files</li>
</ul></td>
</tr>
<tr class="even">
<td>digitalvideo</td>
<td><ul>
<li>can eject</li>
<li>can freeze</li>
<li>can lock</li>
<li>can play</li>
<li>can record</li>
<li>can reverse</li>
<li>can save</li>
<li>can stretch</li>
<li>can stretch input</li>
<li>can test</li>
</ul></td>
<td><ul>
<li>compound device</li>
<li>device type</li>
<li>has audio</li>
<li>has still</li>
<li>has video</li>
<li>maximum play rate</li>
<li>minimum play rate</li>
<li>uses files</li>
<li>uses palettes</li>
<li>windows</li>
</ul></td>
</tr>
<tr class="odd">
<td>overlay</td>
<td><ul>
<li>can eject</li>
<li>can freeze</li>
<li>can play</li>
<li>can record</li>
<li>can save</li>
<li>can stretch</li>
</ul></td>
<td><ul>
<li>compound device</li>
<li>device type</li>
<li>has audio</li>
<li>has video</li>
<li>uses files</li>
<li>windows</li>
</ul></td>
</tr>
<tr class="even">
<td>sequencer</td>
<td><ul>
<li>can eject</li>
<li>can play</li>
<li>can record</li>
<li>can save</li>
<li>compound device</li>
</ul></td>
<td><ul>
<li>device type</li>
<li>has audio</li>
<li>has video</li>
<li>uses files</li>
</ul></td>
</tr>
<tr class="odd">
<td>vcr</td>
<td><ul>
<li>can detect length</li>
<li>can eject</li>
<li>can freeze</li>
<li>can monitor sources</li>
<li>can play</li>
<li>can preroll</li>
<li>can preview</li>
<li>can record</li>
<li>can reverse</li>
<li>can save</li>
<li>can test</li>
</ul></td>
<td><ul>
<li>clock increment rate</li>
<li>compound device</li>
<li>device type</li>
<li>has audio</li>
<li>has clock</li>
<li>has timecode</li>
<li>has video</li>
<li>number of marks</li>
<li>seek accuracy</li>
<li>uses files</li>
</ul></td>
</tr>
<tr class="even">
<td>videodisc</td>
<td><ul>
<li>can eject</li>
<li>can play</li>
<li>can record</li>
<li>can reverse</li>
<li>can save</li>
<li>CAV</li>
<li>CLV</li>
<li>compound device</li>
</ul></td>
<td><ul>
<li>device type</li>
<li>fast play rate</li>
<li>has audio</li>
<li>has video</li>
<li>normal play rate</li>
<li>slow play rate</li>
<li>uses files</li>
</ul></td>
</tr>
<tr class="odd">
<td>waveaudio</td>
<td><ul>
<li>can eject</li>
<li>can play</li>
<li>can record</li>
<li>can save</li>
<li>compound device</li>
<li>device type</li>
</ul></td>
<td><ul>
<li>has audio</li>
<li>has video</li>
<li>inputs</li>
<li>outputs</li>
<li>uses files</li>
</ul></td>
</tr>
</tbody>
</table>



 

The following table lists the flags that can be specified in the *lpszRequest* parameter and their meanings:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Flags</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>can detect length</td>
<td>Returns <strong>TRUE</strong> if the device can detect the length of the media.</td>
</tr>
<tr class="even">
<td>can eject</td>
<td>Returns <strong>TRUE</strong> if the device can eject the media.</td>
</tr>
<tr class="odd">
<td>can freeze</td>
<td>Returns <strong>TRUE</strong> if the device can freeze data in the frame buffer.</td>
</tr>
<tr class="even">
<td>can lock</td>
<td>Returns <strong>TRUE</strong> if the device can lock data.</td>
</tr>
<tr class="odd">
<td>can monitor sources</td>
<td>Returns <strong>TRUE</strong> if the device can pass an input (source) to the monitored output, independent of the current input selection.</td>
</tr>
<tr class="even">
<td>can play</td>
<td>Returns <strong>TRUE</strong> if the device can play.</td>
</tr>
<tr class="odd">
<td>can preroll</td>
<td>Returns <strong>TRUE</strong> if the device supports the &quot;preroll&quot; flag with the <a href="cue.md">cue</a> command.</td>
</tr>
<tr class="even">
<td>can preview</td>
<td>Returns <strong>TRUE</strong> if the device supports previews.</td>
</tr>
<tr class="odd">
<td>can record</td>
<td>Returns <strong>TRUE</strong> if the device supports recording.</td>
</tr>
<tr class="even">
<td>can reverse</td>
<td>Returns <strong>TRUE</strong> if the device can play in reverse.</td>
</tr>
<tr class="odd">
<td>can save</td>
<td>Returns <strong>TRUE</strong> if the device can save data.</td>
</tr>
<tr class="even">
<td>can stretch</td>
<td>Returns <strong>TRUE</strong> if the device can stretch frames to fill a given display rectangle.</td>
</tr>
<tr class="odd">
<td>can stretch input</td>
<td>Returns <strong>TRUE</strong> if the device can resize an image in the process of digitizing it into the frame buffer.</td>
</tr>
<tr class="even">
<td>can test</td>
<td>Returns <strong>TRUE</strong> if the device recognizes the test keyword.</td>
</tr>
<tr class="odd">
<td>cav</td>
<td>When combined with other items, this flag specifies that the return information applies to CAV format videodiscs. This is the default if no videodisc is inserted.</td>
</tr>
<tr class="even">
<td>clock increment rate</td>
<td>Returns the number of subdivisions the external clock supports per second. If the external clock is a millisecond clock, the return value is 1000. If the return value is 0, no clock is supported.</td>
</tr>
<tr class="odd">
<td>clv</td>
<td>When combined with other items, this flag specifies that the return information applies to CLV format videodiscs.</td>
</tr>
<tr class="even">
<td>compound device</td>
<td>Returns <strong>TRUE</strong> if the device supports an element name (filename).</td>
</tr>
<tr class="odd">
<td>device type</td>
<td>Returns a device type name, which can be one of the following:
<ul>
<li>cdaudio</li>
<li>dat</li>
<li>digitalvideo</li>
<li>other</li>
<li>overlay</li>
<li>scanner</li>
<li>sequencer</li>
<li>vcr</li>
<li>videodisc</li>
<li>waveaudio</li>
</ul></td>
</tr>
<tr class="even">
<td>fast play rate</td>
<td>Returns the fast play rate in frames per second, or zero if the device cannot play fast.</td>
</tr>
<tr class="odd">
<td>has audio</td>
<td>Returns <strong>TRUE</strong> if the device supports audio playback.</td>
</tr>
<tr class="even">
<td>has clock</td>
<td>Returns <strong>TRUE</strong> if the device has a clock.</td>
</tr>
<tr class="odd">
<td>has still</td>
<td>Returns <strong>TRUE</strong> if the device treats files with a single image more efficiently than motion video files.</td>
</tr>
<tr class="even">
<td>has timecode</td>
<td>Returns <strong>TRUE</strong> if the device is capable of supporting timecode, or if it is unknown.</td>
</tr>
<tr class="odd">
<td>has video</td>
<td>Returns <strong>TRUE</strong> if the device supports video.</td>
</tr>
<tr class="even">
<td>inputs</td>
<td>Returns the total number of input devices.</td>
</tr>
<tr class="odd">
<td>maximum play rate</td>
<td>Returns the maximum play rate, in frames per second, for the device.</td>
</tr>
<tr class="even">
<td>minimum play rate</td>
<td>Returns the minimum play rate, in frames per second, for the device.</td>
</tr>
<tr class="odd">
<td>normal play rate</td>
<td>Returns the normal play rate, in frames per second, for the device.</td>
</tr>
<tr class="even">
<td>number of marks</td>
<td>Returns the maximum number of marks that can be used; zero indicates that marks are unsupported.</td>
</tr>
<tr class="odd">
<td>outputs</td>
<td>Returns the total number of output devices.</td>
</tr>
<tr class="even">
<td>seek accuracy</td>
<td>Returns the expected accuracy of a search in frames; 0 indicates that the device is frame accurate, 1 indicates that the device expects to be within one frame of the indicated seek position, and so on.</td>
</tr>
<tr class="odd">
<td>slow play rate</td>
<td>Returns the slow play rate in frames per second, or zero if the device cannot play slowly.</td>
</tr>
<tr class="even">
<td>uses files</td>
<td>Returns <strong>TRUE</strong> if the data storage used by a compound device is a file.</td>
</tr>
<tr class="odd">
<td>uses palettes</td>
<td>Returns <strong>TRUE</strong> if the device uses palettes.</td>
</tr>
<tr class="even">
<td>windows</td>
<td>Returns the number of simultaneous display windows the device can support.</td>
</tr>
</tbody>
</table>



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video and VCR devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns information in the *lpszReturnString* parameter of the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function. The information is dependent on the request type.

## Examples

The following command returns the device type of the "mysound" device.

``` syntax
capability mysound device type
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

[cue](cue.md)
</dt> </dl>

 

