---
title: MCI_SPIN command (Mmsystem.h)
description: The MCI\_SPIN command starts the device spinning up or down. Videodisc devices recognize this command.
ms.assetid: 9e491455-d06d-44c6-8aca-6360384ec266
keywords:
- MCI_SPIN command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_SPIN
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_SPIN command

The MCI\_SPIN command starts the device spinning up or down. Videodisc devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_SPIN, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_GENERIC_PARMS) lpSpin
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

MCI\_NOTIFY or MCI\_WAIT. For information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> <dt>

<span id="lpSpin"></span><span id="lpspin"></span><span id="LPSPIN"></span>*lpSpin*
</dt> <dd>

Pointer to an [**MCI\_GENERIC\_PARMS**](mci-generic-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional flags apply to videodisc devices:

<dl> <dt>

<span id="MCI_VD_SPIN_DOWN"></span><span id="mci_vd_spin_down"></span>MCI\_VD\_SPIN\_DOWN
</dt> <dd>

Stops the disc spinning.

</dd> <dt>

<span id="MCI_VD_SPIN_UP"></span><span id="mci_vd_spin_up"></span>MCI\_VD\_SPIN\_UP
</dt> <dd>

Starts the disc spinning.

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

 

