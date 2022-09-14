---
title: MCI_RESERVE command (Mmsystem.h)
description: The MCI\_RESERVE command allocates contiguous disk space for the workspace of the device driver instance for use with subsequent recording. Digital-video devices recognize this command.
ms.assetid: 01f0a377-0179-4b05-a642-af152a7a12ae
keywords:
- MCI_RESERVE command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_RESERVE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_RESERVE command

The MCI\_RESERVE command allocates contiguous disk space for the workspace of the device driver instance for use with subsequent recording. Digital-video devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_RESERVE, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_DGV_RESERVE_PARMS) lpReserve
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

<span id="lpReserve"></span><span id="lpreserve"></span><span id="LPRESERVE"></span>*lpReserve*
</dt> <dd>

Pointer to an [**MCI\_DGV\_RESERVE\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_reserve_parmsa) structure.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

If the workspace contains unsaved data, this data is lost. If disk space is not reserved prior to recording, the [MCI\_RECORD](mci-record.md) command performs an implied reserve with device-specific default parameters. On some implementations, reserve is not required and might be ignored by the device driver. Explicitly reserving space gives you better control over when the delay for disk allocation occurs, how much space is allocated, and where the disk space is allocated. The amount and location of disk space already reserved for this device instance can be changed by issuing MCI\_RESERVE again. Any allocated and still unused disk space is not deallocated until any recorded data is saved or until the device driver instance is closed.

If video is turned off with the MCI\_OFF flag of the [MCI\_SETVIDEO](mci-setvideo.md) command, the space reserved does not include any video. If audio is turned off with the MCI\_OFF flag of the [MCI\_SETAUDIO](mci-setaudio.md) command, the space reserved does not include any audio. If both audio and video are turned off or if the requested size is zero, no space is reserved and any existing reserved space is deallocated.

The following additional flags apply to digital-video devices:

<dl> <dt>

<span id="MCI_DGV_RESERVE_IN"></span><span id="mci_dgv_reserve_in"></span>MCI\_DGV\_RESERVE\_IN
</dt> <dd>

The **lpstrPath** member of the structure identified by *lpReserve* contains an address of a buffer containing the location of a temporary file. The buffer contains only the drive and directory path of the file used to hold recorded data; the filename is specified by the device driver. This temporary file is deleted when the device instance is closed unless it is explicitly saved. If this flag is omitted, the device driver specifies where disk space is allocated.

</dd> <dt>

<span id="MCI_DGV_RESERVE_SIZE"></span><span id="mci_dgv_reserve_size"></span>MCI\_DGV\_RESERVE\_SIZE
</dt> <dd>

The **dwSize** member of the structure identified by *lpReserve* specifies the approximate amount of disk space to reserve in the workspace for recording. The value is specified in the current time format. The amount of disk space is estimated from the requested time and from which file format and video and audio algorithm and quality values are in effect. If this flag is omitted, the device driver might use a default value it defines.

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

 

