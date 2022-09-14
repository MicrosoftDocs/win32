---
title: MCI_GETDEVCAPS command (Mmsystem.h)
description: The MCI\_GETDEVCAPS command retrieves static information about a device.
ms.assetid: a839006f-ea57-4595-9208-cfc465c95298
keywords:
- MCI_GETDEVCAPS command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_GETDEVCAPS
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_GETDEVCAPS command

The MCI\_GETDEVCAPS command retrieves static information about a device. All devices recognize this command. The parameters and flags available for this command depend on the selected device. Information is returned in the **dwReturn** member of the structure identified by *lpCapsParms*.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_GETDEVCAPS, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_GETDEVCAPS_PARMS) lpCapsParms
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

<span id="lpCapsParms"></span><span id="lpcapsparms"></span><span id="LPCAPSPARMS"></span>*lpCapsParms*
</dt> <dd>

Pointer to an [**MCI\_GETDEVCAPS\_PARMS**](mci-getdevcaps-parms.md) structure.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional standard and command-specific flags apply to all devices supporting MCI\_GETDEVCAPS:

<dl> <dt>

<span id="MCI_GETDEVCAPS_COMPOUND_DEVICE"></span><span id="mci_getdevcaps_compound_device"></span>MCI\_GETDEVCAPS\_COMPOUND\_DEVICE
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device uses data storage that must be explicitly opened and closed; it is set to **FALSE** otherwise.

</dd> <dt>

<span id="MCI_GETDEVCAPS_DEVICE_TYPE"></span><span id="mci_getdevcaps_device_type"></span>MCI\_GETDEVCAPS\_DEVICE\_TYPE
</dt> <dd>

The **dwReturn** member is set to one of the values listed in [MCI Device Types](mci-device-types.md).

</dd> <dt>

<span id="MCI_GETDEVCAPS_HAS_AUDIO"></span><span id="mci_getdevcaps_has_audio"></span>MCI\_GETDEVCAPS\_HAS\_AUDIO
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device has audio output; it is set to **FALSE** otherwise.

</dd> <dt>

<span id="MCI_GETDEVCAPS_HAS_VIDEO"></span><span id="mci_getdevcaps_has_video"></span>MCI\_GETDEVCAPS\_HAS\_VIDEO
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device has video output; it is set to **FALSE** otherwise. For example, the member is set to **TRUE** for devices that support the videodisc command set.

</dd> <dt>

<span id="MCI_GETDEVCAPS_ITEM"></span><span id="mci_getdevcaps_item"></span>MCI\_GETDEVCAPS\_ITEM
</dt> <dd>

Specifies that the **dwItem** member of the [**MCI\_GETDEVCAPS\_PARMS**](mci-getdevcaps-parms.md) structure contains one of the following constants:

</dd> <dt>

<span id="MCI_GETDEVCAPS_CAN_EJECT"></span><span id="mci_getdevcaps_can_eject"></span>MCI\_GETDEVCAPS\_CAN\_EJECT
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device can eject the media; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_GETDEVCAPS_CAN_PLAY"></span><span id="mci_getdevcaps_can_play"></span>MCI\_GETDEVCAPS\_CAN\_PLAY
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device can play the media; otherwise, it is set to **FALSE**. If a device specifies **TRUE**, it implies the device supports the [MCI\_PAUSE](mci-pause.md) and [MCI\_STOP](mci-stop.md) commands as well as the [MCI\_PLAY](mci-play.md) command.

</dd> <dt>

<span id="MCI_GETDEVCAPS_CAN_RECORD"></span><span id="mci_getdevcaps_can_record"></span>MCI\_GETDEVCAPS\_CAN\_RECORD
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device supports recording; otherwise, it is set to **FALSE**. If a device specifies **TRUE**, it implies the device supports the MCI\_PAUSE and MCI\_STOP commands as well as the [MCI\_RECORD](mci-record.md) command.

</dd> <dt>

<span id="MCI_GETDEVCAPS_CAN_SAVE"></span><span id="mci_getdevcaps_can_save"></span>MCI\_GETDEVCAPS\_CAN\_SAVE
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device can save a file; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_GETDEVCAPS_USES_FILES"></span><span id="mci_getdevcaps_uses_files"></span>MCI\_GETDEVCAPS\_USES\_FILES
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device requires a filename; it is set to **FALSE** otherwise. Only compound devices use files.

</dd> </dl>

The following flags can be specified in the **dwItem** member of [**MCI\_GETDEVCAPS\_PARMS**](mci-getdevcaps-parms.md) for the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_GETDEVCAPS_CAN_FREEZE"></span><span id="mci_dgv_getdevcaps_can_freeze"></span>MCI\_DGV\_GETDEVCAPS\_CAN\_FREEZE
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device can freeze frames; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_DGV_GETDEVCAPS_CAN_LOCK"></span><span id="mci_dgv_getdevcaps_can_lock"></span>MCI\_DGV\_GETDEVCAPS\_CAN\_LOCK
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device can lock; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_DGV_GETDEVCAPS_CAN_REVERSE"></span><span id="mci_dgv_getdevcaps_can_reverse"></span>MCI\_DGV\_GETDEVCAPS\_CAN\_REVERSE
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device can play in reverse; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_DGV_GETDEVCAPS_CAN_STR_IN"></span><span id="mci_dgv_getdevcaps_can_str_in"></span>MCI\_DGV\_GETDEVCAPS\_CAN\_STR\_IN
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device can stretch input; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_DGV_GETDEVCAPS_CAN_STRETCH"></span><span id="mci_dgv_getdevcaps_can_stretch"></span>MCI\_DGV\_GETDEVCAPS\_CAN\_STRETCH
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device can stretch an image; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_DGV_GETDEVCAPS_CAN_TEST"></span><span id="mci_dgv_getdevcaps_can_test"></span>MCI\_DGV\_GETDEVCAPS\_CAN\_TEST
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device can perform tests; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_DGV_GETDEVCAPS_HAS_STILL"></span><span id="mci_dgv_getdevcaps_has_still"></span>MCI\_DGV\_GETDEVCAPS\_HAS\_STILL
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device can display still images; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_DGV_GETDEVCAPS_MAX_WINDOWS"></span><span id="mci_dgv_getdevcaps_max_windows"></span>MCI\_DGV\_GETDEVCAPS\_MAX\_WINDOWS
</dt> <dd>

The **dwReturn** member is set to the maximum number of windows that the device can handle simultaneously.

</dd> <dt>

<span id="MCI_DGV_GETDEVCAPS_MAXIMUM_RATE"></span><span id="mci_dgv_getdevcaps_maximum_rate"></span>MCI\_DGV\_GETDEVCAPS\_MAXIMUM\_RATE
</dt> <dd>

The **dwReturn** member is set to the maximum play rate for the device, in frames per second.

</dd> <dt>

<span id="MCI_DGV_GETDEVCAPS_MINIMUM_RATE"></span><span id="mci_dgv_getdevcaps_minimum_rate"></span>MCI\_DGV\_GETDEVCAPS\_MINIMUM\_RATE
</dt> <dd>

The **dwReturn** member is set to the minimum play rate for the device, in frames per second.

</dd> <dt>

<span id="MCI_DGV_GETDEVCAPS_PALETTES"></span><span id="mci_dgv_getdevcaps_palettes"></span>MCI\_DGV\_GETDEVCAPS\_PALETTES
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device can return a palette handle; otherwise, it is set to **FALSE**.

</dd> </dl>

The following flags can be specified in the **dwItem** member of [**MCI\_GETDEVCAPS\_PARMS**](mci-getdevcaps-parms.md) for the **vcr** device type:

<dl> <dt>

<span id="MCI_GETDEVCAPS_CLOCK_INCREMENT_RATE"></span><span id="mci_getdevcaps_clock_increment_rate"></span>MCI\_GETDEVCAPS\_CLOCK\_INCREMENT\_RATE
</dt> <dd>

The **dwReturn** member is set to the number of increments per second.

</dd> <dt>

<span id="MCI_VCR_GETDEVCAPS_CAN_DETECT_LENGTH"></span><span id="mci_vcr_getdevcaps_can_detect_length"></span>MCI\_VCR\_GETDEVCAPS\_CAN\_DETECT\_LENGTH
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device is capable of detecting the length of the media; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_VCR_GETDEVCAPS_CAN_FREEZE"></span><span id="mci_vcr_getdevcaps_can_freeze"></span>MCI\_VCR\_GETDEVCAPS\_CAN\_FREEZE
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device is capable of freezing the output image; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_VCR_GETDEVCAPS_CAN_MONITOR_SOURCES"></span><span id="mci_vcr_getdevcaps_can_monitor_sources"></span>MCI\_VCR\_GETDEVCAPS\_CAN\_MONITOR\_SOURCES
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device is capable of monitoring sources; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_VCR_GETDEVCAPS_CAN_PREROLL"></span><span id="mci_vcr_getdevcaps_can_preroll"></span>MCI\_VCR\_GETDEVCAPS\_CAN\_PREROLL
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device is capable of preroll; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_VCR_GETDEVCAPS_CAN_PREVIEW"></span><span id="mci_vcr_getdevcaps_can_preview"></span>MCI\_VCR\_GETDEVCAPS\_CAN\_PREVIEW
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device is capable of previews; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_VCR_GETDEVCAPS_CAN_REVERSE"></span><span id="mci_vcr_getdevcaps_can_reverse"></span>MCI\_VCR\_GETDEVCAPS\_CAN\_REVERSE
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device is capable of playing in reverse; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_VCR_GETDEVCAPS_CAN_TEST"></span><span id="mci_vcr_getdevcaps_can_test"></span>MCI\_VCR\_GETDEVCAPS\_CAN\_TEST
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device is capable of testing; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_VCR_GETDEVCAPS_HAS_CLOCK"></span><span id="mci_vcr_getdevcaps_has_clock"></span>MCI\_VCR\_GETDEVCAPS\_HAS\_CLOCK
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device supports an external clock; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_VCR_GETDEVCAPS_HAS_TIMECODE"></span><span id="mci_vcr_getdevcaps_has_timecode"></span>MCI\_VCR\_GETDEVCAPS\_HAS\_TIMECODE
</dt> <dd>

The **dwReturn** member is set to **TRUE** if device has timecode capability or if this capability is unknown; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_VCR_GETDEVCAPS_NUMBER_OF_MARKS"></span><span id="mci_vcr_getdevcaps_number_of_marks"></span>MCI\_VCR\_GETDEVCAPS\_NUMBER\_OF\_MARKS
</dt> <dd>

The **dwReturn** member is set to the number of marks (99).

</dd> <dt>

<span id="MCI_VCR_GETDEVCAPS_SEEK_ACCURACY"></span><span id="mci_vcr_getdevcaps_seek_accuracy"></span>MCI\_VCR\_GETDEVCAPS\_SEEK\_ACCURACY
</dt> <dd>

The **dwReturn** member is set to the seek accuracy of the device.

</dd> </dl>

The following flags can be specified in the **dwItem** member of [**MCI\_GETDEVCAPS\_PARMS**](mci-getdevcaps-parms.md) for the **overlay** device type:

<dl> <dt>

<span id="MCI_OVLY_GETDEVCAPS_CAN_FREEZE"></span><span id="mci_ovly_getdevcaps_can_freeze"></span>MCI\_OVLY\_GETDEVCAPS\_CAN\_FREEZE
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device can freeze the image; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_OVLY_GETDEVCAPS_CAN_STRETCH"></span><span id="mci_ovly_getdevcaps_can_stretch"></span>MCI\_OVLY\_GETDEVCAPS\_CAN\_STRETCH
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the device can stretch the image to fill the frame; otherwise, it is set to **FALSE**.

</dd> <dt>

<span id="MCI_OVLY_GETDEVCAPS_MAX_WINDOWS"></span><span id="mci_ovly_getdevcaps_max_windows"></span>MCI\_OVLY\_GETDEVCAPS\_MAX\_WINDOWS
</dt> <dd>

The **dwReturn** member is set to the maximum number of windows that the device can handle simultaneously.

</dd> </dl>

The following flags can be specified in the **dwItem** member of [**MCI\_GETDEVCAPS\_PARMS**](mci-getdevcaps-parms.md) for the **videodisc** device type:

<dl> <dt>

<span id="MCI_VD_GETDEVCAPS_CAN_REVERSE"></span><span id="mci_vd_getdevcaps_can_reverse"></span>MCI\_VD\_GETDEVCAPS\_CAN\_REVERSE
</dt> <dd>

The **dwReturn** member is set to **TRUE** if the videodisc player can play in reverse; otherwise, it is set to **FALSE**. Some players can play CLV discs in reverse as well as CAV discs.

</dd> <dt>

<span id="MCI_VD_GETDEVCAPS_CAV"></span><span id="mci_vd_getdevcaps_cav"></span>MCI\_VD\_GETDEVCAPS\_CAV
</dt> <dd>

When combined with other items, specifies that the return information applies to CAV format videodiscs. This is the default if no videodisc is inserted.

</dd> <dt>

<span id="MCI_VD_GETDEVCAPS_CLV"></span><span id="mci_vd_getdevcaps_clv"></span>MCI\_VD\_GETDEVCAPS\_CLV
</dt> <dd>

When combined with other items, specifies that the return information applies to CLV format videodiscs.

</dd> <dt>

<span id="MCI_VD_GETDEVCAPS_FAST_RATE"></span><span id="mci_vd_getdevcaps_fast_rate"></span>MCI\_VD\_GETDEVCAPS\_FAST\_RATE
</dt> <dd>

The **dwReturn** member is set to the standard fast play rate in frames per second.

</dd> <dt>

<span id="MCI_VD_GETDEVCAPS_NORMAL_RATE"></span><span id="mci_vd_getdevcaps_normal_rate"></span>MCI\_VD\_GETDEVCAPS\_NORMAL\_RATE
</dt> <dd>

The **dwReturn** member is set to the normal play rate in frames per second.

</dd> <dt>

<span id="MCI_VD_GETDEVCAPS_SLOW_RATE"></span><span id="mci_vd_getdevcaps_slow_rate"></span>MCI\_VD\_GETDEVCAPS\_SLOW\_RATE
</dt> <dd>

The **dwReturn** member is set to the standard slow play rate in frames per second.

</dd> </dl>

The following flags can be specified in the **dwItem** member of [**MCI\_GETDEVCAPS\_PARMS**](mci-getdevcaps-parms.md) for the **waveaudio** device type:

<dl> <dt>

<span id="MCI_WAVE_GETDEVCAPS_INPUT"></span><span id="mci_wave_getdevcaps_input"></span>MCI\_WAVE\_GETDEVCAPS\_INPUT
</dt> <dd>

The **dwReturn** member is set to the total number of waveform input (recording) devices.

</dd> <dt>

<span id="MCI_WAVE_GETDEVCAPS_OUTPUT"></span><span id="mci_wave_getdevcaps_output"></span>MCI\_WAVE\_GETDEVCAPS\_OUTPUT
</dt> <dd>

The **dwReturn** member is set to the total number of waveform output (playback) devices.

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

 

