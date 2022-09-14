---
title: MCI_SETTIMECODE command (Mmsystem.h)
description: The MCI\_SETTIMECODE command enables or disables timecode recording for a VCR. VCR devices recognize this command.
ms.assetid: b014fbe0-de97-4540-a5fe-b22d157361f7
keywords:
- MCI_SETTIMECODE command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_SETTIMECODE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_SETTIMECODE command

The MCI\_SETTIMECODE command enables or disables timecode recording for a VCR. VCR devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_SETTIMECODE, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_GENERIC_PARMS) lpSetTimeCode
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

MCI\_NOTIFY, MCI\_WAIT, or MCI\_TEST. For information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> <dt>

<span id="lpSetTimeCode"></span><span id="lpsettimecode"></span><span id="LPSETTIMECODE"></span>*lpSetTimeCode*
</dt> <dd>

Pointer to an [**MCI\_GENERIC\_PARMS**](mci-generic-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional flag applies to VCR devices:

<dl> <dt>

<span id="MCI_VCR_SETTIMECODE_RECORD"></span><span id="mci_vcr_settimecode_record"></span>MCI\_VCR\_SETTIMECODE\_RECORD
</dt> <dd>

Sets the timecode track recording to on or off. This flag is used in combination with one of the following additional flags:

</dd> <dt>

<span id="MCI_SET_ON"></span><span id="mci_set_on"></span>MCI\_SET\_ON
</dt> <dd>

Timecode recording on.

</dd> <dt>

<span id="MCI_SET_OFF"></span><span id="mci_set_off"></span>MCI\_SET\_OFF
</dt> <dd>

Timecode recording off.

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

 

