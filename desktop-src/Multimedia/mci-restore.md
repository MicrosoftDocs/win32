---
title: MCI_RESTORE command (Mmsystem.h)
description: The MCI\_RESTORE command copies a bitmap from a file to the frame buffer. Digital-video devices recognize this command. This command performs the opposite action of the MCI\_CAPTURE command.
ms.assetid: ed309cc6-72a3-4abb-aef2-40a55381d8b6
keywords:
- MCI_RESTORE command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_RESTORE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_RESTORE command

The MCI\_RESTORE command copies a bitmap from a file to the frame buffer. Digital-video devices recognize this command. This command performs the opposite action of the [MCI\_CAPTURE](mci-capture.md) command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_RESTORE, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_DGV_RESTORE_PARMS) lpRestore
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

<span id="lpRestore"></span><span id="lprestore"></span><span id="LPRESTORE"></span>*lpRestore*
</dt> <dd>

Pointer to an [**MCI\_DGV\_RESTORE\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_restore_parmsa) structure.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The implementation can recognize a variety of image formats, but a Windows device-independent bitmap (DIB) is always accepted.

The following additional flags apply to digital-video devices:

<dl> <dt>

<span id="MCI_DGV_RESTORE_FROM"></span><span id="mci_dgv_restore_from"></span>MCI\_DGV\_RESTORE\_FROM
</dt> <dd>

The **lpstrFileName** member of the structure identified by *lpRestore* contains an address of a buffer containing the source filename. The filename is required.

</dd> <dt>

<span id="MCI_DGV_RESTORE_AT"></span><span id="mci_dgv_restore_at"></span>MCI\_DGV\_RESTORE\_AT
</dt> <dd>

The **rc** member of the structure identified by *lpRestore* contains a valid rectangle. The rectangle specifies a region of the frame buffer relative to its origin. The first pair of coordinates specifies the upper left corner of the rectangle; the second pair specifies the width and height. If this flag is not specified, the image is copied to the upper left corner of the frame buffer.

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

 

