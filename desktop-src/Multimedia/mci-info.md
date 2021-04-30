---
title: MCI_INFO command (Mmsystem.h)
description: The MCI\_INFO command retrieves string information from a device.
ms.assetid: aed3fed3-87b9-4673-9171-4f57770d765c
keywords:
- MCI_INFO command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_INFO
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_INFO command

The MCI\_INFO command retrieves string information from a device. All devices recognize this command. Information is returned in the **lpstrReturn** member of the structure identified by *lpInfo*. The **dwRetSize** member specifies the buffer length for the returned data.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_INFO, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_INFO_PARMS) lpInfo
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

<span id="lpInfo"></span><span id="lpinfo"></span><span id="LPINFO"></span>*lpInfo*
</dt> <dd>

Pointer to an [**MCI\_INFO\_PARMS**](mci-info-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional standard and command-specific flag applies to all devices supporting MCI\_INFO:

<dl> <dt>

<span id="MCI_INFO_PRODUCT"></span><span id="mci_info_product"></span>MCI\_INFO\_PRODUCT
</dt> <dd>

Obtains a description of the hardware associated with a device. Devices should supply a description that identifies both the driver and the hardware used.

</dd> </dl>

The following additional flags apply to the **cdaudio** device type:

<dl> <dt>

<span id="MCI_INFO_MEDIA_IDENTITY"></span><span id="mci_info_media_identity"></span>MCI\_INFO\_MEDIA\_IDENTITY
</dt> <dd>

Produces a unique identifier for the audio CD currently loaded in the player being queried. This flag returns a string of 16 hexadecimal digits.

</dd> <dt>

<span id="MCI_INFO_MEDIA_UPC"></span><span id="mci_info_media_upc"></span>MCI\_INFO\_MEDIA\_UPC
</dt> <dd>

Produces the Universal Product Code (UPC) that is encoded on an audio CD. The UPC is a string of digits. It might not be available for all CDs.

</dd> </dl>

The following additional flags apply to the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_INFO_ITEM"></span><span id="mci_dgv_info_item"></span>MCI\_DGV\_INFO\_ITEM
</dt> <dd>

A constant indicating the information desired is included in the **dwItem** member of the structure identified by *lpInfo*. The following constants are defined for digital-video devices:

</dd> <dt>

<span id="MCI_DGV_INFO_AUDIO_ALG"></span><span id="mci_dgv_info_audio_alg"></span>MCI\_DGV\_INFO\_AUDIO\_ALG
</dt> <dd>

Returns the name for the current audio compression algorithm.

</dd> <dt>

<span id="MCI_DGV_INFO_AUDIO_QUALITY"></span><span id="mci_dgv_info_audio_quality"></span>MCI\_DGV\_INFO\_AUDIO\_QUALITY
</dt> <dd>

Returns the name for the current audio quality descriptor.

</dd> <dt>

<span id="MCI_DGV_INFO_STILL_ALG"></span><span id="mci_dgv_info_still_alg"></span>MCI\_DGV\_INFO\_STILL\_ALG
</dt> <dd>

Returns the name for the current still image compression algorithm.

</dd> <dt>

<span id="MCI_DGV_INFO_STILL_QUALITY"></span><span id="mci_dgv_info_still_quality"></span>MCI\_DGV\_INFO\_STILL\_QUALITY
</dt> <dd>

Returns the name for the current still image quality descriptor.

</dd> <dt>

<span id="MCI_DGV_INFO_USAGE"></span><span id="mci_dgv_info_usage"></span>MCI\_DGV\_INFO\_USAGE
</dt> <dd>

Returns a string describing usage restrictions that might be imposed by the owner of the visual or audible data in the workspace.

</dd> <dt>

<span id="MCI_DGV_INFO_VIDEO_ALG"></span><span id="mci_dgv_info_video_alg"></span>MCI\_DGV\_INFO\_VIDEO\_ALG
</dt> <dd>

Returns the name for the current video compression algorithm.

</dd> <dt>

<span id="MCI_DGV_INFO_VIDEO_QUALITY"></span><span id="mci_dgv_info_video_quality"></span>MCI\_DGV\_INFO\_VIDEO\_QUALITY
</dt> <dd>

Returns the name for the current video quality descriptor.

</dd> <dt>

<span id="MCI_INFO_VERSION"></span><span id="mci_info_version"></span>MCI\_INFO\_VERSION
</dt> <dd>

Returns the release level of the device driver and hardware. Device driver developers must document the syntax of the returned string.

</dd> <dt>

<span id="MCI_DGV_INFO_TEXT"></span><span id="mci_dgv_info_text"></span>MCI\_DGV\_INFO\_TEXT
</dt> <dd>

Obtains the window caption.

</dd> <dt>

<span id="MCI_INFO_FILE"></span><span id="mci_info_file"></span>MCI\_INFO\_FILE
</dt> <dd>

Obtains the path and filename of the last file specified with the [MCI\_OPEN](mci-open.md) or [MCI\_LOAD](mci-load.md) command. If a file has not been specified, the device returns a null-terminated string. This flag is supported only by devices that return **TRUE** to the MCI\_GETDEVCAPS\_USES\_FILES flag of the [MCI\_GETDEVCAPS](mci-getdevcaps.md) command.

</dd> </dl>

For digital-video devices, *lpInfo* points to an [**MCI\_DGV\_INFO\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_info_parmsa) structure.

The following additional flags apply to the **sequencer** device type:

<dl> <dt>

<span id="MCI_INFO_COPYRIGHT"></span><span id="mci_info_copyright"></span>MCI\_INFO\_COPYRIGHT
</dt> <dd>

Obtains the MIDI file copyright notice from the copyright meta event.

</dd> <dt>

<span id="MCI_INFO_FILE"></span><span id="mci_info_file"></span>MCI\_INFO\_FILE
</dt> <dd>

Obtains the filename of the current file. This flag is supported only by devices that return **TRUE** when you call the [MCI\_GETDEVCAPS](mci-getdevcaps.md) command with the MCI\_GETDEVCAPS\_USES\_FILES flag.

</dd> <dt>

<span id="MCI_INFO_NAME"></span><span id="mci_info_name"></span>MCI\_INFO\_NAME
</dt> <dd>

Obtains the sequence name from the sequence/track name meta event.

</dd> </dl>

The following additional flag applies to the **vcr** device type:

<dl> <dt>

<span id="MCI_VCR_INFO_VERSION"></span><span id="mci_vcr_info_version"></span>MCI\_VCR\_INFO\_VERSION
</dt> <dd>

Sets **lpstrReturn** member of the [**MCI\_INFO\_PARMS**](mci-info-parms.md) structure to point to the version number. Also sets the **dwRetSize** member equal to the length of the string pointed to.

</dd> </dl>

The following additional flags apply to the **overlay** device type:

<dl> <dt>

<span id="MCI_INFO_FILE"></span><span id="mci_info_file"></span>MCI\_INFO\_FILE
</dt> <dd>

Obtains the filename of the current file. This flag is supported only by devices that return **TRUE** to the MCI\_GETDEVCAPS\_USES\_FILES flag of the [MCI\_GETDEVCAPS](mci-getdevcaps.md) command.

</dd> <dt>

<span id="MCI_OVLY_INFO_TEXT"></span><span id="mci_ovly_info_text"></span>MCI\_OVLY\_INFO\_TEXT
</dt> <dd>

Obtains the caption of the window associated with the video-overlay device.

</dd> </dl>

The following additional flags apply to the **waveaudio** device type:

<dl> <dt>

<span id="MCI_INFO_FILE"></span><span id="mci_info_file"></span>MCI\_INFO\_FILE
</dt> <dd>

Obtains the filename of the current file. This flag is supported by devices that return **TRUE** when you call the [MCI\_GETDEVCAPS](mci-getdevcaps.md) command with the MCI\_GETDEVCAPS\_USES\_FILES flag.

</dd> <dt>

<span id="MCI_WAVE_INPUT"></span><span id="mci_wave_input"></span>MCI\_WAVE\_INPUT
</dt> <dd>

Obtains the product name of the current input.

</dd> <dt>

<span id="MCI_WAVE_OUTPUT"></span><span id="mci_wave_output"></span>MCI\_WAVE\_OUTPUT
</dt> <dd>

Obtains the product name of the current output and its value is device specific.

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
</dt> </dl>

 

