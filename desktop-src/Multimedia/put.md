---
title: put command
description: The put command defines the area of the source image and destination window used for display. Digital-video and video-overlay devices recognize this command.
ms.assetid: '55fb7192-2083-45e7-a0bf-0d72a6320f91'
keywords:
- put command Windows Multimedia
topic_type:
- apiref
api_name:
- put
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# put command

The put command defines the area of the source image and destination window used for display. Digital-video and video-overlay devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("put %s %s %s"), 
  lpszDeviceID, 
  lpszRegions, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszRegions"></span><span id="lpszregions"></span><span id="LPSZREGIONS"></span>*lpszRegions*
</dt> <dd>

Flag for defining the area. The following table lists device types that recognize the put command and the flags used by each type.



| Value        | Meaning                                                                                      | Meaning                                                                                          |
|--------------|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| digitalvideo | destination destination at *rectangle*frame frame at *rectangle*source source at *rectangle* | video video at *rectangle*window window at *rectangle*window client window client at *rectangle* |
| overlay      | destination destination at *rectangle*frame frame at *rectangle*                             | source source at *rectangle*video video at *rectangle*                                           |



 

The following table lists the flags that can be specified in the **lpszRegions** parameter and their meanings.



| Value                        | Meaning                                                                                                                                                                                                                                                                                                                                               |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| destination                  | Selects the entire client area of the destination window to display the data.                                                                                                                                                                                                                                                                         |
| destination at *rectangle*   | Selects a portion of the client area of the destination window used to display the image. When an area of the display window is specified and the device supports stretching, the source image is stretched to the destination offset and extent.                                                                                                     |
| frame                        | Selects the entire frame buffer to receive the incoming video images.                                                                                                                                                                                                                                                                                 |
| frame at *rectangle*         | Selects a portion of the frame buffer to receive the incoming video images.                                                                                                                                                                                                                                                                           |
| source                       | Selects the entire image for display in the destination window.                                                                                                                                                                                                                                                                                       |
| source at *rectangle*        | Selects a portion of the image to display in the destination window. When an area of the source image is specified, and the device supports stretching, the source image is stretched to the destination offset and extent.                                                                                                                           |
| video                        | Selects the entire incoming video image to capture in the frame buffer.                                                                                                                                                                                                                                                                               |
| video at *rectangle*         | Selects a portion of the incoming video image to capture in the frame buffer.                                                                                                                                                                                                                                                                         |
| window                       | Restores the initial window size on the display. This command also displays the window.                                                                                                                                                                                                                                                               |
| window at *rectangle*        | Changes the size and location of the display window. The specified rectangle is relative to the parent window of the display window (usually the desktop) if the "style child" flag has been used for the [open](open.md) command. To change the location of the window without changing its height or width, specify zero for the height and width. |
| window client                | Restores the client area of the window.                                                                                                                                                                                                                                                                                                               |
| window client at *rectangle* | Changes the size and location of the client area of the window. The specified rectangle is relative to the parent window of the client window. To change the location of the window without changing its height or width, specify zero for the height and width.                                                                                      |



 

When a flag includes a rectangle, the rectangle coordinates are relative to the window origin or the image origin, as appropriate, and are specified as **X1 Y1 X2 Y2**. The coordinates **X1Y1** specify the upper left corner, and the coordinates **X2Y2** specify the width and height of the rectangle.

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The put command defines one or more of the following rectangles when working with video-overlay devices:

-   The video rectangle defines the region of the incoming video image to capture.
-   The frame rectangle defines the region of the frame buffer that receives the incoming video image.
-   The source rectangle defines which region of the frame buffer is copied to the destination rectangle.
-   The destination rectangle defines the region of the display window client area that receives the video image.

The video rectangle is related to the frame rectangle in the same way the source rectangle is related to the destination rectangle. Stretching can occur from the video rectangle to the frame rectangle and from the source rectangle to the destination rectangle. Not all devices support stretching, and stretching must be enabled (by using the [set](set.md) command).

The following command defines three regions for the video, frame, and source.

``` syntax
put vboard video 120 120 200 200 frame 0 0 200 200 source 0 0 200 200
```

The regions in this example are defined as follows:

-   A 200- by 200-pixel region of the incoming video data, starting at an origin 120 pixels from the upper left corner, will be captured to the frame buffer.
-   The video data will be placed in a 200- by 200-pixel region at the upper left corner of the frame buffer.
-   Transfers are made from the 200- by 200-pixel region at the upper left corner of the frame buffer to the destination window.

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

[open](open.md)
</dt> <dt>

[set](set.md)
</dt> </dl>

 

