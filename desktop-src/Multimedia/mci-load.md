---
title: MCI_LOAD command (Mmsystem.h)
description: The MCI\_LOAD command loads a file. Digital-video and video-overlay devices recognize this command.
ms.assetid: 0f48afa0-e845-4de5-8433-15bbf4eae683
keywords:
- MCI_LOAD command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_LOAD
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_LOAD command

The MCI\_LOAD command loads a file. Digital-video and video-overlay devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_LOAD, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_LOAD_PARMS) lpLoad
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

MCI\_NOTIFY, MCI\_WAIT, or, for digital-video devices, MCI\_TEST. For information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> <dt>

<span id="lpLoad"></span><span id="lpload"></span><span id="LPLOAD"></span>*lpLoad*
</dt> <dd>

Pointer to an [**MCI\_LOAD\_PARMS**](mci-load-parms.md) structure. (Devices with additional parameters might replace this structure with a device-specific structure. For digital-video devices, the **lpLoad** parameter points to an [**MCI\_DGV\_LOAD\_PARMS**](/previous-versions//dd743391(v=vs.85)) structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional flag applies to all devices supporting MCI\_LOAD:

<dl> <dt>

<span id="MCI_LOAD_FILE"></span><span id="mci_load_file"></span>MCI\_LOAD\_FILE
</dt> <dd>

The **lpfilename** member of the structure identified by *lpLoad* contains an address of a buffer containing the filename.

</dd> </dl>

The following additional flag is used with the **overlay** device type:

<dl> <dt>

<span id="MCI_OVLY_RECT"></span><span id="mci_ovly_rect"></span>MCI\_OVLY\_RECT
</dt> <dd>

The **rc** member of the structure identified by *lpLoad* contains a valid display rectangle that identifies the area of the video buffer to update.

</dd> </dl>

For video-overlay devices, the *lpLoad* parameter points to an [**MCI\_OVLY\_LOAD\_PARMS**](mci-ovly-load-parms.md) structure.

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

 

