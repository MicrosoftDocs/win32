---
title: setvideo command
description: The setvideo command sets values associated with video playback and capture. Digital-video and VCR devices recognize this command.
ms.assetid: 'a6851b9b-e09a-4251-bd1c-19b1e4b6f871'
keywords:
- setvideo command Windows Multimedia
topic_type:
- apiref
api_name:
- setvideo
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# setvideo command

The setvideo command sets values associated with video playback and capture. Digital-video and VCR devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("setvideo %s %s %s"), 
  lpszDeviceID, 
  lpszVideo, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszVideo"></span><span id="lpszvideo"></span><span id="LPSZVIDEO"></span>*lpszVideo*
</dt> <dd>

Flag for video playback and capture. The following table lists device types that recognize the **setvideo** command and the flags used by each type.



| Value        | Meaning                                                                                                                                                                                        | Meaning                                                                                                                                                                                                                                                                                                |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| digitalvideo | algorithm *algorithm*bitsperpel to *count*brightness to *factor*clocktimecolor to *factor*contrast to *factor*gamma to *value*halftoneinputkey color to *r:g:b*key index to *index*offonoutput | over *duration*palette color *color* over *index*to *newrgb* palette handle to *handle*quality *descriptor*record frame rate to *rate*record onrecord offsharpness to *factor*source to *source* number *value*still algorithm *algorithm*still quality *descriptor*stream to *number*tint to *factor* |
| vcr          | offonmonitor to *type* number *number*record offrecord track *track\_number* off                                                                                                               | record onrecord track *track\_number* onsource to *type* number *number* track *track\_number* offtrack *track\_number* on                                                                                                                                                                             |



 

The following table lists the flags that can be specified in the **lpszVideo** parameter and their meanings.



| Value                                          | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| algorithm *algorithm*                          | Specifies a video compression algorithm for use by a subsequent [reserve](reserve.md) or [record](record.md) command. Algorithms supported by a device are device specific. MCI defines the constants "mpeg" and "h261" for *algorithm*.If the specified algorithm conflicts with the current file format, the file format is changed to the default format for the algorithm.<br/>                                                                                                                                     |
| bitsperpel to *count*                          | Sets the number of bits per pixel for saving data with the [capture](capture.md) or [record](record.md) command.                                                                                                                                                                                                                                                                                                                                                                                                              |
| brightness to *factor*                         | Sets the video brightness level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| clocktime                                      | Indicates that the time specified in the "over" flag is in milliseconds. The time is absolute and not in step with the playing of the workspace.                                                                                                                                                                                                                                                                                                                                                                                |
| color to *factor*                              | Sets the color-saturation level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| contrast to *factor*                           | Sets the video-contrast level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| gamma to *value*                               | Specifies the gamma correction exponent multiplied by 1000. For example, to specify an exponent of 2.2, use 2200 for *value*. A gamma value of 1.0 (1000) indicates no gamma correction is applied. Gamma correction adjusts the mapping between the intensity encoded in the presentation source and the displayed brightness.                                                                                                                                                                                                 |
| halftone                                       | Causes the halftone palette to be used instead of the default palette. This flag is recognized only by the MCIAVI digital-video driver.                                                                                                                                                                                                                                                                                                                                                                                         |
| input                                          | Modifies the "brightness", "color", "contrast", "gamma", "sharpness", or "tint" flag so that it affects the input signal and modifies what is recorded. If possible, this is the default when monitoring the input.                                                                                                                                                                                                                                                                                                             |
| key color to *r:g:b*                           | Sets the key color. The *r:g:b* variable is an RGB value. Colons (:) separate the individual red, green, and blue values.                                                                                                                                                                                                                                                                                                                                                                                                       |
| key index to *index*                           | Sets the key index. The *index* variable is a physical palette index.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| monitor to *type* number *number*              | Controls which source input will be passed to the VCR output, without changing the recording source input selection. Type can be "output", or one of the valid input sources. If "number" is not specified, then the first input of that type is chosen.                                                                                                                                                                                                                                                                        |
| offon                                          | Enables or disables display of video. Disabling video sets the pixels in the [put](put.md) "destination" rectangle (or its default, the client region of the current window) to a solid color. It has no effect on the frame buffer.The video source, whether the workspace or an external input, might continue to store new images in the frame buffer. They are not displayed until video is enabled. You can use the [window](window.md) "state" command to hide the window. The default is **setvideo** "on".<br/> |
| output                                         | Modifies the "brightness", "color", "contrast", "gamma", "sharpness", or "tint" flag so that it modifies only the displayed signal and not what is recorded. If possible, this is the default when monitoring a file.                                                                                                                                                                                                                                                                                                           |
| over *duration*                                | Specifies how long it should take to make a change that uses a *factor* variable. The units for *duration* are in the current time format. Changes occur in step with the playing of the workspace. When playing is suspended, the change is also suspended until the play continues. If "over" is not used or not supported, the change occurs immediately.                                                                                                                                                                    |
| palette color *color* over *index* to *newrgb* | Sets a new palette color. The color and palette index to be changed are specified by the *color* and *index* parameters; the new color is specified by *newrgb*. This flag is recognized only by the MCIAVI digital-video driver.                                                                                                                                                                                                                                                                                               |
| palette handle to *handle*                     | Specifies the handle to a palette the device must use for rendering. This item is supported only by devices that use palettes. If *handle* is zero, the default palette is used.Digital-video devices should not free the palette passed with this command. Applications should free it after they close the device.<br/>                                                                                                                                                                                                 |
| quality *descriptor*                           | Specifies the characteristics of the video compression performed when video is recorded to a file. All devices support the three descriptors: "low", "medium", and "high". The default is device specific. The significance of these names depends on the algorithm and the device. Devices might define additional descriptor names. The [quality](quality.md) command can be used to define additional descriptor names.If the "algorithm" flag is not used, the *descriptor* applies to the current algorithm.<br/>   |
| record frame rate to *rate*                    | Sets the recording for motion video. The recording *rate* is specified in units of frames per second multiplied by 1000. For example, the NTSC frame rate of 29.97 frames per second is represented as 29970.                                                                                                                                                                                                                                                                                                                   |
| record onrecord off                            | Enables or disables recording of video data. Recording video data is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| record track *track\_number* off               | Clears the video-source selection so that no video will be recorded with the next [record](record.md) command. "Track" allows independent track selection. If "track" is not specified, a default value of 1 is assumed. It might be necessary to first issue a [set](set.md) "assemble record off" command before the video recording can be turned off.                                                                                                                                                                     |
| record track *track\_number* on                | Selects the video source to be recorded with the next **record** command. "Track" allows independent track selection. Track 2 corresponds to the PCM track in Hi8. If "track" is not specified, a default of 1 is assumed.                                                                                                                                                                                                                                                                                                      |
| sharpness to *factor*                          | Sets the video sharpness level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| source to *source* number *value*              | Sets the source of the video input. This usually corresponds to external connectors. The constants defined for *source* include "rgb", "pal", "ntsc", "svideo", and "secam". If more than one input of the specified type exists, the optional "number" *value* indicates the desired input. For example, **setvideo** "source to ntsc number 2" specifies the second NTSC input.If "to" *source* is omitted, then the absolute source is used as defined by the [list](list.md) "video source" command.<br/>            |
| source to *type* number *number*               | Selects the video source to be recorded on the tape. *Type* must be "tuner", "line", "svideo", "aux", "generic", "mute", or "rgb".                                                                                                                                                                                                                                                                                                                                                                                              |
| still algorithm *algorithm*                    | Specifies the still image compression algorithm used by the [capture](capture.md) command. Every device must support an *algorithm* of "none", which means no compression. This is the default. In this case, digital-video devices save still images as RGB device-independent bitmaps. Devices might also support a device-specific list of additional algorithms.                                                                                                                                                           |
| still quality *descriptor*                     | Specifies the characteristics of the still-image compression performed while capturing a still image. All devices support the descriptors "low", "medium", and "high". The default is device specific.If the "algorithm" flag is not used, the *descriptor* applies to the current algorithm.<br/> The [quality](quality.md) command can be used to define other descriptor names.<br/>                                                                                                                            |
| stream to *number*                             | Specifies the video stream played back from the workspace. If the stream is not specified and a default stream is not defined by the file format, then the physically first interleaved video stream is played.                                                                                                                                                                                                                                                                                                                 |
| tint to *factor*                               | Sets the image tint. Typically, this adjustment is modeled after the tint control of many color television sets, with 250 meaning green, 750 meaning red, and 0 (or                                                                                                                                                                                                                                                                                                                                                             |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", "test", or a combination of these. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

For VCR devices, using setvideo with a flag that turns off an individual track ("track *track\_number* off") might cause your application to receive a status message indicating that the command could not be carried out. Some VCRs can turn off only combinations of tracks, not individual tracks; for example, the first audio track and a video track of a video cassette. In this case, simply use [setaudio](setaudio.md) and setvideo to continue to turn off the other tracks that make up the combination. The driver will turn off the tracks when it receives the command to turn off the last track in the combination.

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

[list](list.md)
</dt> <dt>

[put](put.md)
</dt> <dt>

[record](record.md)
</dt> <dt>

[reserve](reserve.md)
</dt> <dt>

[set](set.md)
</dt> <dt>

[setaudio](setaudio.md)
</dt> <dt>

[window](window.md)
</dt> </dl>

 

