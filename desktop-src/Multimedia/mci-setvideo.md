---
title: MCI_SETVIDEO command (Mmsystem.h)
description: The MCI\_SETVIDEO command sets values associated with video playback. Digital-video and VCR devices recognize this command.
ms.assetid: b84956d8-01a0-49f6-a96c-2693a25e6f2a
keywords:
- MCI_SETVIDEO command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_SETVIDEO
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_SETVIDEO command

The MCI\_SETVIDEO command sets values associated with video playback. Digital-video and VCR devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_SETVIDEO, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_GENERIC_PARMS) lpSetVideo
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

**MCI\_NOTIFY**, **MCI\_WAIT**, or **MCI\_TEST**. For information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> <dt>

<span id="lpSetVideo"></span><span id="lpsetvideo"></span><span id="LPSETVIDEO"></span>*lpSetVideo*
</dt> <dd>

Pointer to an [**MCI\_GENERIC\_PARMS**](mci-generic-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional flags are used with the "digitalvideo" device type:

<dl> <dt>

<span id="MCI_DGV_SETVIDEO_ALG"></span><span id="mci_dgv_setvideo_alg"></span>MCI\_DGV\_SETVIDEO\_ALG
</dt> <dd>

The **lpstrAlgorithm** member of the structure identified by *lpSetVideo* contains an address of a buffer containing the name of a video compression algorithm. The compression algorithm is used by subsequent [MCI\_RESERVE](mci-reserve.md) or [MCI\_RECORD](mci-record.md) commands. The available algorithms are device dependent.

If the specified algorithm is incompatible with the current file format, the file format is changed to the default format for the algorithm.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_CLOCKTIME"></span><span id="mci_dgv_setvideo_clocktime"></span>MCI\_DGV\_SETVIDEO\_CLOCKTIME
</dt> <dd>

When used with **MCI\_DGV\_SETVIDEO\_OVER**, indicates time is specified in milliseconds and is absolute time. (This time is not in step with the playing of the workspace.)

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_INPUT"></span><span id="mci_dgv_setvideo_input"></span>MCI\_DGV\_SETVIDEO\_INPUT
</dt> <dd>

Modifies the **MCI\_DGV\_SETVIDEO\_BRIGHTNESS**, **MCI\_DGV\_SETVIDEO\_COLOR**, **MCI\_DGV\_SETVIDEO\_CONTRAST**, **MCI\_DGV\_SETVIDEO\_GAMMA**, **MCI\_DGV\_SETVIDEO\_SHARPNESS**, or **MCI\_DGV\_SETVIDEO\_TINT** so that it affects the input signal and modifies what is recorded. If possible, this is the default when monitoring the input.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_ITEM"></span><span id="mci_dgv_setvideo_item"></span>MCI\_DGV\_SETVIDEO\_ITEM
</dt> <dd>

A video constant is specified in the **dwItem** member of the structure identified by *lpSetVideo*. The constant identifies the value that is being set. You can specify the following constants with this flag:

</dd> <dt>

<span id="MCI_AVI_SETVIDEO_DRAW_PROCEDURE"></span><span id="mci_avi_setvideo_draw_procedure"></span>MCI\_AVI\_SETVIDEO\_DRAW\_PROCEDURE
</dt> <dd>

A new drawing procedure address is specified in the **dwValue** member of the structure identified by *lpSetVideo*. You can specify a new drawing procedure only when the device is idle. This flag is recognized only by the MCIAVI digital-video driver. There is no equivalent to this flag in the string command interface.

</dd> <dt>

<span id="MCI_AVI_SETVIDEO_PALETTE_COLOR"></span><span id="mci_avi_setvideo_palette_color"></span>MCI\_AVI\_SETVIDEO\_PALETTE\_COLOR
</dt> <dd>

A new palette color is specified in the **dwOver** and **dwValue** members of the structure identified by *lpSetVideo*. The **dwOver** member specifies the palette index of the color to be changed and the **dwValue** member specifies the new color, as an RGB value. You must also specify the **MCI\_DGV\_SETVIDEO\_OVER** and **MCI\_DGV\_SETVIDEO\_VALUE** flags with **MCI\_DGV\_SETVIDEO\_ITEM** when you use this constant. This flag is recognized only by the MCIAVI digital-video driver.

</dd> <dt>

<span id="MCI_AVI_SETVIDEO_PALETTE_HALFTONE"></span><span id="mci_avi_setvideo_palette_halftone"></span>MCI\_AVI\_SETVIDEO\_PALETTE\_HALFTONE
</dt> <dd>

Indicates that the halftone palette should be used, instead of the default palette. This flag is recognized only by the MCIAVI digital-video driver.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_BITSPERPEL"></span><span id="mci_dgv_setvideo_bitsperpel"></span>MCI\_DGV\_SETVIDEO\_BITSPERPEL
</dt> <dd>

The number of bits per pixel is specified in the **dwValue** member of the structure identified by *lpSetVideo*. The number of bits per pixel is used for saving captured or recorded data

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_BRIGHTNESS"></span><span id="mci_dgv_setvideo_brightness"></span>MCI\_DGV\_SETVIDEO\_BRIGHTNESS
</dt> <dd>

The video brightness level is specified as a factor in the **dwValue** member of the structure identified by *lpSetVideo*.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_COLOR"></span><span id="mci_dgv_setvideo_color"></span>MCI\_DGV\_SETVIDEO\_COLOR
</dt> <dd>

The video color saturation level is specified as a factor in the **dwValue** member of the structure identified by *lpSetVideo*.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_CONTRAST"></span><span id="mci_dgv_setvideo_contrast"></span>MCI\_DGV\_SETVIDEO\_CONTRAST
</dt> <dd>

The video contrast level is specified as a factor in the **dwValue** member of the structure identified by *lpSetVideo*.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_FRAME_RATE"></span><span id="mci_dgv_setvideo_frame_rate"></span>MCI\_DGV\_SETVIDEO\_FRAME\_RATE
</dt> <dd>

A frame rate is specified in the **dwValue** member of the structure identified by *lpSetVideo*. The rate is specified in units of frames per second times 1000. For example, 29.97 frames per second is specified as 29970.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_GAMMA"></span><span id="mci_dgv_setvideo_gamma"></span>MCI\_DGV\_SETVIDEO\_GAMMA
</dt> <dd>

A gamma correction exponent value is specified in the **dwValue** member of the structure identified by *lpSetVideo*. Gamma correction adjusts the mapping between the intensity encoded in the presentation source and the displayed brightness. The value is the exponent multiplied by 1000. For example, 2200 indicates an exponent of 2.2. A value of 1000 indicates an exponent of 1, which applies no gamma correction.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_KEY_COLOR"></span><span id="mci_dgv_setvideo_key_color"></span>MCI\_DGV\_SETVIDEO\_KEY\_COLOR
</dt> <dd>

A key color is specified in the **dwValue** member of the structure identified by *lpSetVideo*. The key color is an RGB value.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_KEY_INDEX"></span><span id="mci_dgv_setvideo_key_index"></span>MCI\_DGV\_SETVIDEO\_KEY\_INDEX
</dt> <dd>

A key index value is specified in the **dwValue** member of the structure identified by *lpSetVideo*. The index parameter is a physical palette index.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_PALHANDLE"></span><span id="mci_dgv_setvideo_palhandle"></span>MCI\_DGV\_SETVIDEO\_PALHANDLE
</dt> <dd>

A palette handle is specified in the **dwValue** member of the structure identified by *lpSetVideo*. The palette handle is contained in the low-order word. Digital-video devices should not free the palette passed with this command. Applications should free it after they close the device. This flag is supported only by devices that use palettes. If this specified palette handle is zero, then the default palette is used.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_SHARPNESS"></span><span id="mci_dgv_setvideo_sharpness"></span>MCI\_DGV\_SETVIDEO\_SHARPNESS
</dt> <dd>

A video sharpness value is specified as a factor in the **dwValue** member of the structure identified by *lpSetVideo*.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_SOURCE"></span><span id="mci_dgv_setvideo_source"></span>MCI\_DGV\_SETVIDEO\_SOURCE
</dt> <dd>

A constant specifying the source of the video input is specified in the **dwValue** member of the structure identified by *lpSetVideo*. The following constants are defined:

-   **MCI\_DGV\_SETVIDEO\_SRC\_NTSC**: NTSC television.
-   MCI\_DGV\_SETVIDEO\_SRC\_PAL: PAL television.
-   MCI\_DGV\_SETVIDEO\_SRC\_RGB: RGB video.
-   MCI\_DGV\_SETVIDEO\_SRC\_SECAM: SECAM television.
-   MCI\_DGV\_SETVIDEO\_SRC\_SVIDEO: S-Video.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_STREAM"></span><span id="mci_dgv_setvideo_stream"></span>MCI\_DGV\_SETVIDEO\_STREAM
</dt> <dd>

A video stream is specified in the **dwValue** member of the structure identified by *lpSetVideo*. The integer value specifies the video stream played back from the workspace. If the stream is not specified and the file format does not define a default stream, the first physically interleaved video stream is played.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_TINT"></span><span id="mci_dgv_setvideo_tint"></span>MCI\_DGV\_SETVIDEO\_TINT
</dt> <dd>

A video tint value is specified as a factor in the **dwValue** member of the structure identified by *lpSetVideo*. Typically, this adjustment is modeled after the tint control of many color television sets, with 250 defined as green, 750 defined as red, and 0 (or 1000) defined as blue. The nominal value is always 500.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_OUTPUT"></span><span id="mci_dgv_setvideo_output"></span>MCI\_DGV\_SETVIDEO\_OUTPUT
</dt> <dd>

The **MCI\_DGV\_SETVIDEO\_BRIGHTNESS**, **MCI\_DGV\_SETVIDEO\_COLOR**, **MCI\_DGV\_SETVIDEO\_CONTRAST**, **MCI\_DGV\_SETVIDEO\_GAMMA**, **MCI\_DGV\_SETVIDEO\_SHARPNESS**, or **MCI\_DGV\_SETVIDEO\_TINT** flag is modified so that it affects only the displayed signal and not what is recorded. If possible, this is the default when monitoring a file.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_OVER"></span><span id="mci_dgv_setvideo_over"></span>MCI\_DGV\_SETVIDEO\_OVER
</dt> <dd>

A transition length parameter is included in the **dwOver** member of the structure identified by *lpSetVideo*. The transition length specifies how long (in the current time format) it should take to make a change. If this flag is not used, the change occurs immediately.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_QUALITY"></span><span id="mci_dgv_setvideo_quality"></span>MCI\_DGV\_SETVIDEO\_QUALITY
</dt> <dd>

The **lpstrQuality** member of the structure identified by *lpSetVideo* contains an address of a buffer describing the video quality. A text-string in the buffer specifies the characteristics of the video compression algorithm.

The **MCI\_DGV\_SETVIDEO\_ALG** flag can be used to select a quality descriptor for the specified algorithm. If this flag is omitted, then the current algorithm is used.

The algorithms and descriptor names available depend on the device. Each device supplies documentation for the available algorithms and a description of the applicable descriptor names. The [MCI\_QUALITY](mci-quality.md) command can define additional descriptor names. All devices support the descriptors "low", "medium", and "high". The default is driver specific.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_RECORD"></span><span id="mci_dgv_setvideo_record"></span>MCI\_DGV\_SETVIDEO\_RECORD
</dt> <dd>

Specifies whether recording includes or excludes video data. When combined with **MCI\_SET\_ON**, video data is recorded. When combined with **MCI\_SET\_OFF**, video data is excluded. The default includes video data.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_SRC_NUMBER"></span><span id="mci_dgv_setvideo_src_number"></span>MCI\_DGV\_SETVIDEO\_SRC\_NUMBER
</dt> <dd>

A number for the video source is specified in the **dwSourceNumber** member of the structure identified by *lpSetVideo*. If there is more than one input of the type specified by **MCI\_DGV\_SETVIDEO\_VALUE**, the value selects the input. This flag must always be used with **MCI\_DGV\_SETVIDEO\_SOURCE**. If **MCI\_DGV\_SETVIDEO\_VALUE** is omitted, however, the specified source number indicates the absolute source to use as specified in the [MCI\_LIST](mci-list.md) command.

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_STILL"></span><span id="mci_dgv_setvideo_still"></span>MCI\_DGV\_SETVIDEO\_STILL
</dt> <dd>

The algorithm name or quality value specified applies to still images.

Every device driver must support an algorithm of "none", which means no compression. This is the default. In this case, digital-video devices save still images as RGB device-independent bitmaps (DIBs).

</dd> <dt>

<span id="MCI_DGV_SETVIDEO_VALUE"></span><span id="mci_dgv_setvideo_value"></span>MCI\_DGV\_SETVIDEO\_VALUE
</dt> <dd>

A value is included in the **dwValue** member of the structure identified by *lpSetVideo*. The meaning of the value is specified by the **MCI\_DGV\_SETVIDEO\_ITEM** flag.

</dd> <dt>

<span id="MCI_SET_OFF"></span><span id="mci_set_off"></span>MCI\_SET\_OFF
</dt> <dd>

Disables video output. For digital-video devices, disabling video sets the pixels in the destination rectangle defined by the [MCI\_PUT](mci-put.md) command (or its default, the client region of the current window) to a solid color, but it has no effect on the frame buffer. You can hide the window with the [MCI\_WINDOW](mci-window.md) command if desired. The source of video, whether it's the workspace or an external input, might continue to store new images in the frame buffer, but they are not displayed until the video is enabled. While applications should use the MCI\_SETVIDEO command to control this function, digital-video devices must still support this flag. The default value after an open is on.

</dd> <dt>

<span id="MCI_SET_ON"></span><span id="mci_set_on"></span>MCI\_SET\_ON
</dt> <dd>

Enables video output.

</dd> </dl>

For digital-video devices, the *lpSetVideo* parameter points to an [**MCI\_DGV\_SETVIDEO\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_setvideo_parmsa) structure.

The following additional flags are used with the "vcr" device type:

<dl> <dt>

<span id="MCI_VCR_SETVIDEO_RECORD"></span><span id="mci_vcr_setvideo_record"></span>MCI\_VCR\_SETVIDEO\_RECORD
</dt> <dd>

Sets the video recording to on or off. Used in conjunction with one of following flags:

-   **MCI\_SET\_ON**. Video recording on.
-   **MCI\_SET\_OFF**. Video recording off. It might be necessary to first turn off the assemble recording (using the [MCI\_SET](mci-set.md) command with the **MCI\_VCR\_SET\_ASSEMBLE\_RECORD** flag set to off) before the video recording can be turned off.

</dd> <dt>

<span id="MCI_TRACK"></span><span id="mci_track"></span>MCI\_TRACK
</dt> <dd>

The **dwTrack** member of the structure identified by *lpSetVideo* specifies which track is affected by the command.

</dd> <dt>

<span id="MCI_VCR_SETVIDEO_SOURCE"></span><span id="mci_vcr_setvideo_source"></span>MCI\_VCR\_SETVIDEO\_SOURCE
</dt> <dd>

Sets the video source, and must be used with the **MCI\_VCR\_SETVIDEO\_TO** flag.

</dd> <dt>

<span id="MCI_VCR_SETVIDEO_MONITOR"></span><span id="mci_vcr_setvideo_monitor"></span>MCI\_VCR\_SETVIDEO\_MONITOR
</dt> <dd>

Sets the video source monitor, and must be used with the MCI\_VCR\_SETVIDEO\_TO flag.

</dd> <dt>

<span id="MCI_VCR_SETVIDEO_TO"></span><span id="mci_vcr_setvideo_to"></span>MCI\_VCR\_SETVIDEO\_TO
</dt> <dd>

The **dwTo** member of the structure identified by *lpSetVideo* contains one of the following constants:

<dl> <dd>**MCI\_VCR\_SRC\_TYPE\_TUNER**</dd> <dd>**MCI\_VCR\_SRC\_TYPE\_LINE**</dd> <dd>**MCI\_VCR\_SRC\_TYPE\_AUX**</dd> <dd>**MCI\_VCR\_SRC\_TYPE\_GENERIC**</dd> <dd>**MCI\_VCR\_SRC\_TYPE\_MUTE**</dd> <dd>**MCI\_VCR\_SRC\_TYPE\_OUTPUT**</dd> <dd>**MCI\_VCR\_SRC\_TYPE\_RGB**</dd> <dd>**MCI\_VCR\_SETVIDEO\_NUMBER**</dd> </dl>

The **dwNumber** member of the structure identified by *lpSetVideo* contains the video input (of the type specified in the **dwTo** member) to use.

</dd> </dl>

For VCR devices, the *lpSetVideo* parameter points to an [**MCI\_VCR\_SETVIDEO\_PARMS**](mci-vcr-setvideo-parms.md) structure.

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

 

