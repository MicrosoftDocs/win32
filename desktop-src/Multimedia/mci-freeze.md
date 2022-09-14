---
title: MCI_FREEZE command (Mmsystem.h)
description: The MCI\_FREEZE command freezes motion on the display. Digital-video, video-overlay, and VCR devices recognize this command.
ms.assetid: 6f90984a-24dc-4046-8234-986b2125bab4
keywords:
- MCI_FREEZE command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_FREEZE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_FREEZE command

The MCI\_FREEZE command freezes motion on the display. Digital-video, video-overlay, and VCR devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_FREEZE, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_GENERIC_PARMS) lpFreeze
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

<span id="lpFreeze"></span><span id="lpfreeze"></span><span id="LPFREEZE"></span>*lpFreeze*
</dt> <dd>

Pointer to an [**MCI\_GENERIC\_PARMS**](mci-generic-parms.md) structure. (Devices with additional parameters might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional flags are used by the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_FREEZE_AT"></span><span id="mci_dgv_freeze_at"></span>MCI\_DGV\_FREEZE\_AT
</dt> <dd>

The **rc** member of the structure identified by *lpFreeze* contains a valid rectangle. The rectangle specifies a region within the frame buffer that will have the lock mask bit for each pixel turned on. The specified pixels will not be updated until their lock mask bit is turned off. If this flag is not specified, the rectangle defaults to the entire frame buffer. This flag is supported only if the [MCI\_GETDEVCAPS](mci-getdevcaps.md) command returns **TRUE** for the MCI\_DGV\_GETDEVCAPS\_CAN\_LOCK flag.

</dd> <dt>

<span id="MCI_DGV_FREEZE_OUTSIDE"></span><span id="mci_dgv_freeze_outside"></span>MCI\_DGV\_FREEZE\_OUTSIDE
</dt> <dd>

The area outside the region specified for the MCI\_DGV\_FREEZE\_AT flag is frozen.

</dd> </dl>

For digital-video devices, the *lpFreeze* parameter points to an [**MCI\_DGV\_FREEZE\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_rect_parms) structure.

The following additional flags are used by the **vcr** device type:

<dl> <dt>

<span id="MCI_VCR_FREEZE_FIELD"></span><span id="mci_vcr_freeze_field"></span>MCI\_VCR\_FREEZE\_FIELD
</dt> <dd>

Freeze only one member of the current frame.

</dd> <dt>

<span id="MCI_VCR_FREEZE_FRAME"></span><span id="mci_vcr_freeze_frame"></span>MCI\_VCR\_FREEZE\_FRAME
</dt> <dd>

Freeze both fields of the current frame.

</dd> <dt>

<span id="MCI_VCR_FREEZE_INPUT"></span><span id="mci_vcr_freeze_input"></span>MCI\_VCR\_FREEZE\_INPUT
</dt> <dd>

Freeze the current frame on the screen (used for recording).

</dd> <dt>

<span id="MCI_VCR_FREEZE_OUTPUT"></span><span id="mci_vcr_freeze_output"></span>MCI\_VCR\_FREEZE\_OUTPUT
</dt> <dd>

Freeze the current frame from the VCR (used with frame capture).

</dd> </dl>

For VCR devices, the *lpFreeze* parameter points to an [**MCI\_GENERIC\_PARMS**](mci-generic-parms.md) structure.

The following additional flag is used by the **overlay** device type:

<dl> <dt>

<span id="MCI_OVLY_RECT"></span><span id="mci_ovly_rect"></span>MCI\_OVLY\_RECT
</dt> <dd>

The **rc** member of the structure identified by *lpFreeze* contains a valid rectangle. If this flag is not specified, the device driver will freeze the entire frame.

</dd> </dl>

For video-overlay devices, the *lpFreeze* parameter points to an [**MCI\_OVLY\_RECT\_PARMS**](mci-ovly-rect-parms.md) structure.

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

 

