---
title: MCI_SIGNAL command (Mmsystem.h)
description: The MCI\_SIGNAL command sets a specified position in the workspace. Digital-video devices recognize this command. MCIAVI supports only one active signal at a time.
ms.assetid: 32ca21a0-e2df-47f1-8e13-67c9d8f149db
keywords:
- MCI_SIGNAL command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_SIGNAL
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_SIGNAL command

The MCI\_SIGNAL command sets a specified position in the workspace. Digital-video devices recognize this command. MCIAVI supports only one active signal at a time.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_SIGNAL, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_DGV_SIGNAL_PARMS) lpSignal
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

<span id="lpSignal"></span><span id="lpsignal"></span><span id="LPSIGNAL"></span>*lpSignal*
</dt> <dd>

Pointer to an [**MCI\_DGV\_SIGNAL\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_signal_parms) structure.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The window whose handle you specify in the **dwCallback** member of the [**MCI\_DGV\_SIGNAL\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_signal_parms) structure receives the MM\_MCISIGNAL message.

The following flags apply to digital-video devices:

<dl> <dt>

<span id="MCI_DGV_SIGNAL_AT"></span><span id="mci_dgv_signal_at"></span>MCI\_DGV\_SIGNAL\_AT
</dt> <dd>

A signal position is included in the **dwPosition** member of the structure identified by *lpSignal*.

</dd> <dt>

<span id="MCI_DGV_SIGNAL_CANCEL"></span><span id="mci_dgv_signal_cancel"></span>MCI\_DGV\_SIGNAL\_CANCEL
</dt> <dd>

Removes the signal position specified by the value associated with MCI\_DGV\_SIGNAL\_USERVAL.

</dd> <dt>

<span id="MCI_DGV_SIGNAL_EVERY"></span><span id="mci_dgv_signal_every"></span>MCI\_DGV\_SIGNAL\_EVERY
</dt> <dd>

A signal-period value is included in the **dwPeriod** member of the structure identified by *lpSignal*.

</dd> <dt>

<span id="MCI_DGV_SIGNAL_POSITION"></span><span id="mci_dgv_signal_position"></span>MCI\_DGV\_SIGNAL\_POSITION
</dt> <dd>

The device will send the position value with the Windows message instead of the user-specified value.

</dd> <dt>

<span id="MCI_DGV_SIGNAL_USERVAL"></span><span id="mci_dgv_signal_userval"></span>MCI\_DGV\_SIGNAL\_USERVAL
</dt> <dd>

A data value is included in the **dwUserParm** member of the structure identified by *lpSignal*. The data value associated with this request is reported back with the Windows message.

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

 

