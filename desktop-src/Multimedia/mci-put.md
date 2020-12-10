---
title: MCI_PUT command (Mmsystem.h)
description: The MCI\_PUT command sets the source, destination, and frame rectangles. Digital-video and video-overlay devices recognize this command.
ms.assetid: 9d81682b-6546-4e6d-a6df-e2de8c013b66
keywords:
- MCI_PUT command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_PUT
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_PUT command

The MCI\_PUT command sets the source, destination, and frame rectangles. Digital-video and video-overlay devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_PUT, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_GENERIC_PARMS) lpDest
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

<span id="lpDest"></span><span id="lpdest"></span><span id="LPDEST"></span>*lpDest*
</dt> <dd>

Pointer to an [**MCI\_GENERIC\_PARMS**](mci-generic-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional flags are used with the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_PUT_CLIENT"></span><span id="mci_dgv_put_client"></span>MCI\_DGV\_PUT\_CLIENT
</dt> <dd>

The rectangle defined for MCI\_DGV\_RECT applies to the position of the client window. The rectangle specified is relative to the parent window of the display window. MCI\_DGV\_PUT\_WINDOW must be set concurrently with this flag.

</dd> <dt>

<span id="MCI_DGV_PUT_DESTINATION"></span><span id="mci_dgv_put_destination"></span>MCI\_DGV\_PUT\_DESTINATION
</dt> <dd>

The rectangle defined for MCI\_DGV\_RECT specifies a destination rectangle. The destination rectangle specifies the portion of the client window associated with this device driver instance that shows the image or video.

</dd> <dt>

<span id="MCI_DGV_PUT_FRAME"></span><span id="mci_dgv_put_frame"></span>MCI\_DGV\_PUT\_FRAME
</dt> <dd>

The rectangle defined for MCI\_DGV\_RECT applies to the frame rectangle. The frame rectangle specifies the portion of the frame buffer used as the destination of the video images obtained from the video rectangle. The video should be scaled to fit within the frame buffer rectangle.

The rectangle is specified in frame buffer coordinates. The default rectangle is the full frame buffer. Specifying this rectangle lets the device scale the image as it digitizes the data. Devices that cannot scale the image reject this command with MCIERR\_UNSUPPORTED\_FUNCTION. You can use the MCI\_GETDEVCAPS\_CAN\_STRETCH flag with the [MCI\_GETDEVCAPS](mci-getdevcaps.md) command to determine if a device scales the image. A device returns **FALSE** if it cannot scale the image.

</dd> <dt>

<span id="MCI_DGV_PUT_SOURCE"></span><span id="mci_dgv_put_source"></span>MCI\_DGV\_PUT\_SOURCE
</dt> <dd>

The rectangle defined for MCI\_DGV\_RECT specifies a source rectangle. The source rectangle specifies which portion of the frame buffer is to be scaled to fit into the destination rectangle.

</dd> <dt>

<span id="MCI_DGV_PUT_VIDEO"></span><span id="mci_dgv_put_video"></span>MCI\_DGV\_PUT\_VIDEO
</dt> <dd>

The rectangle defined for MCI\_DGV\_RECT applies to the video rectangle. The video rectangle specifies which portion of the current presentation source is stored in the frame buffer. The rectangle is specified using the natural coordinates of the presentation source. It allows the specification of cropping that occurs prior to storing images and video in the frame buffer. The default rectangle is the full active scan area or the full decompressed images and video.

</dd> <dt>

<span id="MCI_DGV_PUT_WINDOW"></span><span id="mci_dgv_put_window"></span>MCI\_DGV\_PUT\_WINDOW
</dt> <dd>

The rectangle defined for MCI\_DGV\_RECT applies to the display window. This rectangle is relative to the parent window of the display window (usually the desktop). If the window is not specified, it defaults to the initial window size and position.

</dd> <dt>

<span id="MCI_DGV_RECT"></span><span id="mci_dgv_rect"></span>MCI\_DGV\_RECT
</dt> <dd>

The **rc** member of the structure identified by *lpDest* contains a valid rectangle.

</dd> </dl>

For digital-video devices, *lpDest* points to an [**MCI\_DGV\_PUT\_PARMS**](/previous-versions//dd743397(v=vs.85)) structure.

The following additional flags are used with the **overlay** device type:

<dl> <dt>

<span id="MCI_OVLY_PUT_DESTINATION"></span><span id="mci_ovly_put_destination"></span>MCI\_OVLY\_PUT\_DESTINATION
</dt> <dd>

The rectangle defined for MCI\_OVLY\_RECT specifies the area of the client window used to display an image. The rectangle contains the offset and visible extent of the image relative to the window origin. If the frame is being stretched, the source is stretched to the destination rectangle.

</dd> <dt>

<span id="MCI_OVLY_PUT_FRAME"></span><span id="mci_ovly_put_frame"></span>MCI\_OVLY\_PUT\_FRAME
</dt> <dd>

The rectangle defined for MCI\_OVLY\_RECT specifies the area of the video buffer used to receive the video image. The rectangle contains the offset and extent of the buffer area relative to the video buffer origin.

</dd> <dt>

<span id="MCI_OVLY_PUT_SOURCE"></span><span id="mci_ovly_put_source"></span>MCI\_OVLY\_PUT\_SOURCE
</dt> <dd>

The rectangle defined for MCI\_OVLY\_RECT specifies the area of the video buffer used as the source of the digital image. The rectangle contains the offset and extent of the clipping rectangle for the video buffer relative to its origin.

</dd> <dt>

<span id="MCI_OVLY_PUT_VIDEO"></span><span id="mci_ovly_put_video"></span>MCI\_OVLY\_PUT\_VIDEO
</dt> <dd>

The rectangle defined for MCI\_OVLY\_RECT specifies the area of the video source capture by the video buffer. The rectangle contains the offset and extent of the clipping rectangle for the video source relative to its origin.

</dd> <dt>

<span id="MCI_OVLY_RECT"></span><span id="mci_ovly_rect"></span>MCI\_OVLY\_RECT
</dt> <dd>

The **rc** member of the structure identified by *lpDest* contains a valid display rectangle. If this flag is not specified, the default rectangle matches the coordinates of the video buffer or window being clipped.

</dd> </dl>

For video-overlay devices, *lpDest* points to an [**MCI\_OVLY\_RECT\_PARMS**](mci-ovly-rect-parms.md) structure.

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

 

