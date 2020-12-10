---
title: MCI_SYSINFO command (Mmsystem.h)
description: The MCI\_SYSINFO command retrieves information about MCI devices.
ms.assetid: 605efd25-8849-42aa-99fd-b36b6fd2c7b7
keywords:
- MCI_SYSINFO command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_SYSINFO
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_SYSINFO command

The MCI\_SYSINFO command retrieves information about MCI devices. MCI supports this command directly rather than passing it to the device. Any MCI application can use this command. String information is returned in the application-supplied buffer pointed to by the **lpstrReturn** member of the structure identified by *lpSysInfo*. Numeric information is returned as a **DWORD** value placed in the application-supplied buffer. The **dwRetSize** member specifies the buffer length.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_SYSINFO, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_SYSINFO_PARMS) lpSysInfo
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

One or more of the following standard and command-specific flags:

</dd> <dt>

<span id="MCI_SYSINFO_INSTALLNAME"></span><span id="mci_sysinfo_installname"></span>MCI\_SYSINFO\_INSTALLNAME
</dt> <dd>

Obtains the name (listed in the registry or the SYSTEM.INI file) used to install the device.

</dd> <dt>

<span id="MCI_SYSINFO_NAME"></span><span id="mci_sysinfo_name"></span>MCI\_SYSINFO\_NAME
</dt> <dd>

Obtains a device name corresponding to the device number specified in the **dwNumber** member of the structure identified by**lpSysInfo**. If the MCI\_SYSINFO\_OPEN flag is set, MCI returns the names of open devices.

</dd> <dt>

<span id="MCI_SYSINFO_OPEN"></span><span id="mci_sysinfo_open"></span>MCI\_SYSINFO\_OPEN
</dt> <dd>

Obtains the quantity or name of open devices.

</dd> <dt>

<span id="MCI_SYSINFO_QUANTITY"></span><span id="mci_sysinfo_quantity"></span>MCI\_SYSINFO\_QUANTITY
</dt> <dd>

Obtains the number of devices of the specified type that are listed in the registry or the \[mci\] section of the SYSTEM.INI file. If the MCI\_SYSINFO\_OPEN flag is set, the number of open devices is returned.

</dd> <dt>

<span id="lpSysInfo"></span><span id="lpsysinfo"></span><span id="LPSYSINFO"></span>*lpSysInfo*
</dt> <dd>

Pointer to an [**MCI\_SYSINFO\_PARMS**](mci-sysinfo-parms.md) structure.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The **wDeviceType** member of the structure identified by *lpSysInfo* is used to indicate the device type of the query. If the *wDeviceID* parameter is set to MCI\_ALL\_DEVICE\_ID, it overrides the value of **wDeviceType**. For a list of device types, see [MCI Device Types](mci-device-types.md).

Integer return values are **DWORD** values returned in the buffer pointed to by the **lpstrReturn** member of the structure identified by *lpSysInfo*.

String return values are null-terminated strings returned in the buffer pointed to by the **lpstrReturn** member of the structure identified by *lpSysInfo*.

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

 

