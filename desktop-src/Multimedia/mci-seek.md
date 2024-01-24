---
title: MCI_SEEK command (Mmsystem.h)
description: The MCI\_SEEK command changes the current position in the content as quickly as possible.
ms.assetid: 5ffab964-a28d-4dc2-ac04-da501cd34d24
keywords:
- MCI_SEEK command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_SEEK
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_SEEK command

The MCI\_SEEK command changes the current position in the content as quickly as possible. Video and audio output are disabled during the seek. After the seek is complete, the device is stopped. CD audio, digital-video, MIDI sequencer, VCR, videodisc, and waveform-audio devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_SEEK, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_SEEK_PARMS) lpSeek
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

<span id="lpSeek"></span><span id="lpseek"></span><span id="LPSEEK"></span>*lpSeek*
</dt> <dd>

Pointer to an [**MCI\_SEEK\_PARMS**](mci-seek-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

If a data sample size for a device is larger than 1 byte (such as with waveform-audio stereo data), this command moves to the beginning of the nearest sample when a specified position does not coincide with the start of a sample.

The following additional flags apply to all devices supporting MCI\_SEEK:

<dl> <dt>

<span id="MCI_SEEK_TO_END"></span><span id="mci_seek_to_end"></span>MCI\_SEEK\_TO\_END
</dt> <dd>

Seek to the end of the content.

</dd> <dt>

<span id="MCI_SEEK_TO_START"></span><span id="mci_seek_to_start"></span>MCI\_SEEK\_TO\_START
</dt> <dd>

Seek to the beginning of the content.

</dd> <dt>

<span id="MCI_TO"></span><span id="mci_to"></span>MCI\_TO
</dt> <dd>

A position is included in the **dwTo** member of the structure identified by *lpSeek*. The units assigned to the position values are specified with the MCI\_SET\_TIME\_FORMAT flag of the [MCI\_SET](mci-set.md) command. Do not use this flag with MCI\_SEEK\_TO\_END or MCI\_SEEK\_TO\_START.

</dd> </dl>

The following additional flags are used with the **vcr** device type:

<dl> <dt>

<span id="MCI_VCR_SEEK_AT"></span><span id="mci_vcr_seek_at"></span>MCI\_VCR\_SEEK\_AT
</dt> <dd>

The **dwAt** member of the structure identified by *lpSeek* contains a time when the entire command begins.

</dd> <dt>

<span id="MCI_VCR_SEEK_MARK"></span><span id="mci_vcr_seek_mark"></span>MCI\_VCR\_SEEK\_MARK
</dt> <dd>

The **dwMark** member of the structure identified by *lpSeek* contains the numbered mark to search for.

</dd> <dt>

<span id="MCI_VCR_SEEK_REVERSE"></span><span id="mci_vcr_seek_reverse"></span>MCI\_VCR\_SEEK\_REVERSE
</dt> <dd>

Seek direction is reverse; this is used only with the MCI\_VCR\_SEEK\_MARK flag.

</dd> </dl>

For VCR devices, the *lpSeek* parameter points to an [**MCI\_VCR\_SEEK\_PARMS**](mci-vcr-seek-parms.md) structure.

The following additional flag is used with the **videodisc** device type:

<dl> <dt>

<span id="MCI_VD_SEEK_REVERSE"></span><span id="mci_vd_seek_reverse"></span>MCI\_VD\_SEEK\_REVERSE
</dt> <dd>

Seek direction is reverse.

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

 

