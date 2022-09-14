---
title: MCI_MONITOR command (Mmsystem.h)
description: The MCI\_MONITOR command specifies the presentation source. Digital-video devices recognize this command.
ms.assetid: b6c476ef-d1a4-477d-a104-dda10be60915
keywords:
- MCI_MONITOR command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_MONITOR
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_MONITOR command

The MCI\_MONITOR command specifies the presentation source. Digital-video devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_MONITOR, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_DGV_MONITOR_PARMS) lpMonitor
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

<span id="lpMonitor"></span><span id="lpmonitor"></span><span id="LPMONITOR"></span>*lpMonitor*
</dt> <dd>

Pointer to an [**MCI\_DGV\_MONITOR\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_monitor_parms) structure.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional flags apply to digital-video devices:

<dl> <dt>

<span id="MCI_DGV_MONITOR_METHOD"></span><span id="mci_dgv_monitor_method"></span>MCI\_DGV\_MONITOR\_METHOD
</dt> <dd>

A constant indicating the method of monitoring is included in the **dwMethod** member of the structure identified by *lpMonitor*.

When the MCI\_DGV\_MONITOR\_INPUT flag is used in the **dwSource** member, this selects the method of monitoring. Typically, different monitoring methods have different implications on how the hardware is used. The default monitoring method is selected by the device.

</dd> <dt>

<span id="MCI_DGV_MONITOR_SOURCE"></span><span id="mci_dgv_monitor_source"></span>MCI\_DGV\_MONITOR\_SOURCE
</dt> <dd>

A constant indicating the monitor source is included in the **dwSource** member of the structure identified by *lpMonitor*.

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

 

