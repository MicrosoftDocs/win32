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




| Value | Type | Type | 
|-------|------|------|
| cdaudio | <ul><li>can eject</li><li>can play</li><li>can record</li><li>can save</li><li>compound device</li></ul> | <ul><li>device type</li><li>has audio</li><li>has video</li><li>uses files</li></ul> | 
| digitalvideo | <ul><li>can eject</li><li>can freeze</li><li>can lock</li><li>can play</li><li>can record</li><li>can reverse</li><li>can save</li><li>can stretch</li><li>can stretch input</li><li>can test</li></ul> | <ul><li>compound device</li><li>device type</li><li>has audio</li><li>has still</li><li>has video</li><li>maximum play rate</li><li>minimum play rate</li><li>uses files</li><li>uses palettes</li><li>windows</li></ul> | 
| overlay | <ul><li>can eject</li><li>can freeze</li><li>can play</li><li>can record</li><li>can save</li><li>can stretch</li></ul> | <ul><li>compound device</li><li>device type</li><li>has audio</li><li>has video</li><li>uses files</li><li>windows</li></ul> | 
| sequencer | <ul><li>can eject</li><li>can play</li><li>can record</li><li>can save</li><li>compound device</li></ul> | <ul><li>device type</li><li>has audio</li><li>has video</li><li>uses files</li></ul> | 
| vcr | <ul><li>can detect length</li><li>can eject</li><li>can freeze</li><li>can monitor sources</li><li>can play</li><li>can preroll</li><li>can preview</li><li>can record</li><li>can reverse</li><li>can save</li><li>can test</li></ul> | <ul><li>clock increment rate</li><li>compound device</li><li>device type</li><li>has audio</li><li>has clock</li><li>has timecode</li><li>has video</li><li>number of marks</li><li>seek accuracy</li><li>uses files</li></ul> | 
| videodisc | <ul><li>can eject</li><li>can play</li><li>can record</li><li>can reverse</li><li>can save</li><li>CAV</li><li>CLV</li><li>compound device</li></ul> | <ul><li>device type</li><li>fast play rate</li><li>has audio</li><li>has video</li><li>normal play rate</li><li>slow play rate</li><li>uses files</li></ul> | 
| waveaudio | <ul><li>can eject</li><li>can play</li><li>can record</li><li>can save</li><li>compound device</li><li>device type</li></ul> | <ul><li>has audio</li><li>has video</li><li>inputs</li><li>outputs</li><li>uses files</li></ul> | 




 

The following table lists the flags that can be specified in the *lpszRequest* parameter and their meanings:




| Flags | Meaning | 
|-------|---------|
| can detect length | Returns <strong>TRUE</strong> if the device can detect the length of the media. | 
| can eject | Returns <strong>TRUE</strong> if the device can eject the media. | 
| can freeze | Returns <strong>TRUE</strong> if the device can freeze data in the frame buffer. | 
| can lock | Returns <strong>TRUE</strong> if the device can lock data. | 
| can monitor sources | Returns <strong>TRUE</strong> if the device can pass an input (source) to the monitored output, independent of the current input selection. | 
| can play | Returns <strong>TRUE</strong> if the device can play. | 
| can preroll | Returns <strong>TRUE</strong> if the device supports the "preroll" flag with the <a href="cue.md">cue</a> command. | 
| can preview | Returns <strong>TRUE</strong> if the device supports previews. | 
| can record | Returns <strong>TRUE</strong> if the device supports recording. | 
| can reverse | Returns <strong>TRUE</strong> if the device can play in reverse. | 
| can save | Returns <strong>TRUE</strong> if the device can save data. | 
| can stretch | Returns <strong>TRUE</strong> if the device can stretch frames to fill a given display rectangle. | 
| can stretch input | Returns <strong>TRUE</strong> if the device can resize an image in the process of digitizing it into the frame buffer. | 
| can test | Returns <strong>TRUE</strong> if the device recognizes the test keyword. | 
| cav | When combined with other items, this flag specifies that the return information applies to CAV format videodiscs. This is the default if no videodisc is inserted. | 
| clock increment rate | Returns the number of subdivisions the external clock supports per second. If the external clock is a millisecond clock, the return value is 1000. If the return value is 0, no clock is supported. | 
| clv | When combined with other items, this flag specifies that the return information applies to CLV format videodiscs. | 
| compound device | Returns <strong>TRUE</strong> if the device supports an element name (filename). | 
| device type | Returns a device type name, which can be one of the following:<ul><li>cdaudio</li><li>dat</li><li>digitalvideo</li><li>other</li><li>overlay</li><li>scanner</li><li>sequencer</li><li>vcr</li><li>videodisc</li><li>waveaudio</li></ul> | 
| fast play rate | Returns the fast play rate in frames per second, or zero if the device cannot play fast. | 
| has audio | Returns <strong>TRUE</strong> if the device supports audio playback. | 
| has clock | Returns <strong>TRUE</strong> if the device has a clock. | 
| has still | Returns <strong>TRUE</strong> if the device treats files with a single image more efficiently than motion video files. | 
| has timecode | Returns <strong>TRUE</strong> if the device is capable of supporting timecode, or if it is unknown. | 
| has video | Returns <strong>TRUE</strong> if the device supports video. | 
| inputs | Returns the total number of input devices. | 
| maximum play rate | Returns the maximum play rate, in frames per second, for the device. | 
| minimum play rate | Returns the minimum play rate, in frames per second, for the device. | 
| normal play rate | Returns the normal play rate, in frames per second, for the device. | 
| number of marks | Returns the maximum number of marks that can be used; zero indicates that marks are unsupported. | 
| outputs | Returns the total number of output devices. | 
| seek accuracy | Returns the expected accuracy of a search in frames; 0 indicates that the device is frame accurate, 1 indicates that the device expects to be within one frame of the indicated seek position, and so on. | 
| slow play rate | Returns the slow play rate in frames per second, or zero if the device cannot play slowly. | 
| uses files | Returns <strong>TRUE</strong> if the data storage used by a compound device is a file. | 
| uses palettes | Returns <strong>TRUE</strong> if the device uses palettes. | 
| windows | Returns the number of simultaneous display windows the device can support. | 




 

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

 

