---
title: reserve command
description: The reserve command allocates contiguous disk space for the device instance's workspace. Digital-video devices recognize this command.
ms.assetid: 'ac4fc75e-82d0-4817-a5cf-a77996bc69e2'
keywords:
- reserve command Windows Multimedia
topic_type:
- apiref
api_name:
- reserve
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# reserve command

The reserve command allocates contiguous disk space for the device instance's workspace. Digital-video devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("reserve %s %s %s"), 
  lpszDeviceID, 
  lpszReserve, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszReserve"></span><span id="lpszreserve"></span><span id="LPSZRESERVE"></span>*lpszReserve*
</dt> <dd>

One or more of the following flags.



| Value           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| in *path*       | Specifies the drive and directory path (but not the name) of a temporary file used to hold recorded data. The name of this file is specified by the device. The temporary file is deleted when the device is closed. If this flag is omitted, the device specifies the location of the disk space.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| size *duration* | Specifies the approximate amount of disk space to reserve in the workspace. The *duration* value is specified in the current time format. The device bases its estimate of the required disk space on the following parameters: the requested time, the file format, the video and audio compression algorithm, and the compression quality values in effect. If [setvideo](setvideo.md) "record" is "off", then space is reserved only for audio. If [setaudio](setaudio.md) "record" is "off", then space is reserved only for video. If both are "off", or if *duration* is zero, then no space is reserved and any existing reserved space is deallocated. If this flag is omitted, the device will use a device-defined default. |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", "test", or a combination of these. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

If needed, subsequent [record](record.md) or [save](save.md) commands use the space reserved by this command. If the workspace contains unsaved data, the data is lost. Some devices do not require reserve and ignore it. If disk space is not reserved prior to recording, the record command performs an implied reserve with device-specific default flags. Use an explicit reserve command if you want better control of when the delay for disk allocation occurs, control of how much space is allocated, and control of where the disk space is allocated. Your application can change the amount and location of previously reserved disk space with subsequent reserve commands. Any allocated and still unused disk space is not deallocated until any recorded data is saved, or until the device instance is closed.

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

[record](record.md)
</dt> <dt>

[save](save.md)
</dt> <dt>

[setaudio](setaudio.md)
</dt> <dt>

[setvideo](setvideo.md)
</dt> </dl>

 

