---
title: sysinfo command
description: The sysinfo command retrieves MCI system information. The sysinfo command is an MCI system command; it is interpreted directly by MCI.
ms.assetid: '494e8976-aac3-4d9f-b14b-3d3fd1917b45'
keywords:
- sysinfo command Windows Multimedia
topic_type:
- apiref
api_name:
- sysinfo
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# sysinfo command

The sysinfo command retrieves MCI system information. The sysinfo command is an MCI system command; it is interpreted directly by MCI.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("sysinfo %s %s %s"), 
  lpszDeviceID, 
  lpszRequest, 
  lpszFlags
);
```

## Parameters

<dl> <dt>

*lpszDeviceID* 
</dt> <dd>

Identifier of an MCI device or device type. If a device type is specified, it must be a standard MCI device-type name, as listed in the reference material for the [**capability**](capability.md) command. You can specify "all" when the flag specified in *lpszRequest* allows that possibility.

</dd> <dt>

*lpszRequest* 
</dt> <dd>

One of the following flags.



| Value                                                                                                                                                                | Meaning                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="installname"></span><span id="INSTALLNAME"></span><dl> <dt>**installname**</dt> </dl>               | Returns the name listed in the registry or the SYSTEM.INI file used to install the open device with the specified device identifier.<br/>                                                                                                                                                                                                            |
| <span id="quantity"></span><span id="QUANTITY"></span><dl> <dt>**quantity**</dt> </dl>                        | Returns the number of MCI devices listed in the registry or the SYSTEM.INI file of the type specified in the *lpszDeviceID* parameter. This device identifier must be a standard MCI device-type name. Any digits after the device type are ignored. Specifying "all" for *lpszDeviceID* returns the total number of MCI devices in the system.<br/> |
| <span id="quantity_open"></span><span id="QUANTITY_OPEN"></span><dl> <dt>**quantity open**</dt> </dl>         | Returns the number of open MCI devices of the type specified in *lpszDeviceID*. This device identifier must be a standard MCI device-type name. Specifying "all" for *lpszDeviceID* returns the total number of open MCI devices in the system.<br/>                                                                                                 |
| <span id="name_index"></span><span id="NAME_INDEX"></span><dl> <dt>**name *index***</dt> </dl>                | Returns the name of an MCI device. The device identifier must be a standard MCI device-type name. The *index* ranges from 1 to the number of devices of that type. If "all" is specified for *lpszDeviceID*, *index* ranges from 1 to the total number of devices in the system.<br/>                                                                |
| <span id="name_index_open"></span><span id="NAME_INDEX_OPEN"></span><dl> <dt>**name *index* open**</dt> </dl> | Returns the name of an open MCI device. The device identifier must be a standard MCI device-type name. The *index* ranges from 1 to the number of open devices of that device type. If "all" is specified for *lpszDeviceID*, *index* ranges from 1 to the total number of open devices in the system.<br/>                                          |



 

</dd> <dt>

*lpszFlags* 
</dt> <dd>

Can be "wait", "notify", or both. For digital-video and VCR devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Examples

The following command returns the number of open waveform-audio devices.

``` syntax
sysinfo waveaudio quantity open
```

The following command returns the name (device alias) of the first open waveform-audio device.

``` syntax
sysinfo waveaudio name 1 open
```

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

[**capability**](capability.md)
</dt> </dl>

 

