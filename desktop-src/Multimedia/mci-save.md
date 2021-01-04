---
title: MCI_SAVE command (Mmsystem.h)
description: The MCI\_SAVE command saves the current file.
ms.assetid: 286e6f31-cb93-443b-8191-8c363b366eae
keywords:
- MCI_SAVE command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_SAVE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_SAVE command

The MCI\_SAVE command saves the current file. Devices that modify files should not destroy the original copy until they receive the save message. Video-overlay and waveform-audio devices recognize this command. Although digital-video devices and MIDI sequencers also recognize this command, the MCIAVI and MCISEQ drivers do not implement it.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_SAVE, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_SAVE_PARMS ) lpSave
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

<span id="lpSave"></span><span id="lpsave"></span><span id="LPSAVE"></span>*lpSave*
</dt> <dd>

Pointer to an [**MCI\_SAVE\_PARMS**](mci-save-parms.md) structure. (Devices with additional parameters might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

This command is supported by devices that return **TRUE** when you call the [MCI\_GETDEVCAPS](mci-getdevcaps.md) command with the MCI\_GETDEVCAPS\_CAN\_SAVE flag.

The following additional flag applies to all devices supporting [MCI\_SAVE](/windows):

<dl> <dt>

<span id="MCI_SAVE_FILE"></span><span id="mci_save_file"></span>MCI\_SAVE\_FILE
</dt> <dd>

The **lpfilename** member of the structure identified by *lpSave* contains an address of a buffer containing the destination filename.

</dd> </dl>

The following additional flags are used with the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_RECT"></span><span id="mci_dgv_rect"></span>MCI\_DGV\_RECT
</dt> <dd>

The **rc** member of the structure identified by *lpSave* contains a valid rectangle. The rectangle specifies a region of the frame buffer that will be saved to the specified file. The first pair of coordinates specifies the upper left corner of the rectangle; the second pair specifies the width and height. Digital-video devices must use the [MCI\_CAPTURE](mci-capture.md) command to capture the contents of the frame buffer. (Video-overlay devices should also use MCI\_CAPTURE.) This flag is for compatibility with the existing MCI video-overlay command set.

</dd> <dt>

<span id="MCI_DGV_SAVE_ABORT"></span><span id="mci_dgv_save_abort"></span>MCI\_DGV\_SAVE\_ABORT
</dt> <dd>

Stops a save operation in progress. This must be the only flag present.

</dd> <dt>

<span id="MCI_DGV_SAVE_KEEPRESERVE"></span><span id="mci_dgv_save_keepreserve"></span>MCI\_DGV\_SAVE\_KEEPRESERVE
</dt> <dd>

Unused disk space left over from the original [MCI\_RESERVE](mci-reserve.md) command is not deallocated.

</dd> </dl>

For digital-video devices, the *lpSave* parameter points to an [**MCI\_DGV\_SAVE\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_save_parmsa) structure.

The following additional flag is used with the **overlay** device type:

<dl> <dt>

<span id="MCI_OVLY_RECT"></span><span id="mci_ovly_rect"></span>MCI\_OVLY\_RECT
</dt> <dd>

The **rc** member of the structure identified by *lpSave* contains a valid display rectangle indicating the area of the video buffer to save.

</dd> </dl>

For video-overlay devices, the *lpSave* parameter points to an [**MCI\_OVLY\_SAVE\_PARMS**](/previous-versions//dd743447(v=vs.85)) structure.

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

 

