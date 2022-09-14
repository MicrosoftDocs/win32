---
title: where command
description: The where command retrieves the rectangle specifying the source or destination area. This rectangle was specified using the put command. Digital-video, and video-overlay devices recognize this command.
ms.assetid: '85c68ded-bd3e-4a48-9af7-58478615a7f0'
keywords:
- where command Windows Multimedia
topic_type:
- apiref
api_name:
- where
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# where command

The where command retrieves the rectangle specifying the source or destination area. This rectangle was specified using the [put](put.md) command. Digital-video, and video-overlay devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("where %s %s %s"), 
  lpszDeviceID, 
  lpszRequestRect, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszRequestRect"></span><span id="lpszrequestrect"></span><span id="LPSZREQUESTRECT"></span>*lpszRequestRect*
</dt> <dd>

Flag that identifies the rectangle whose dimensions are retrieved. The following table lists device types that recognize the **where** command and the flags used by each type.



| Value        | Meaning                                                       | Meaning                                  |
|--------------|---------------------------------------------------------------|------------------------------------------|
| digitalvideo | destinationdestination [**max**](max.md)frameframe maxsource | source maxvideovideo maxwindowwindow max |
| overlay      | destinationframe                                              | sourcevideo                              |



 

The following table lists the flags that can be specified in the **lpszRequestRect** parameter and their meanings.



| Value                          | Meaning                                                                                                                                                                                                                                                                                              |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| destination                    | Retrieves the destination offset and extent. For video-overlay devices, the destination rectangle defines the area of the display window client area that displays the image data from the frame buffer.                                                                                             |
| destination [**max**](max.md) | Retrieves the current size of the client rectangle.                                                                                                                                                                                                                                                  |
| frame                          | Retrieves the offset and extent of the frame buffer rectangle. The frame buffer rectangle defines the area of the frame buffer that receives incoming video data. Images from the "video" rectangle are scaled into this region.                                                                     |
| frame [**max**](max.md)       | Returns the maximum size of the frame buffer.                                                                                                                                                                                                                                                        |
| source                         | Retrieves the source offset and extent. For video-overlay devices, the source rectangle defines the region of the frame buffer that is displayed in the destination window. The device uses this rectangle to crop the image before it is stretched to fit the destination rectangle on the display. |
| source [**max**](max.md)      | Retrieves the maximum size of the frame buffer.                                                                                                                                                                                                                                                      |
| video                          | Retrieves the offset and extent of the video rectangle. The video rectangle defines the region of the incoming video data that is transferred to the frame buffer.                                                                                                                                   |
| video [**max**](max.md)       | Returns the maximum size of the input.                                                                                                                                                                                                                                                               |
| window                         | Retrieves the current size and position of the display-window frame.                                                                                                                                                                                                                                 |
| window [**max**](max.md)      | Retrieves the size of the entire display.                                                                                                                                                                                                                                                            |



 

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns a rectangle in the *lpszReturnString* parameter of the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function. The rectangle describes the area specified in the *lpszRequestRect* parameter of this command. The rectangle is specified as *X1 Y1 X2 Y2*. The coordinates *X1 Y1* specify the upper left corner of the rectangle, and the coordinates *X2 Y2* specify the width and height.

## Examples

The following command returns the display rectangle of the "movie" device.

``` syntax
where movie destination
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

[put](put.md)
</dt> </dl>

 

