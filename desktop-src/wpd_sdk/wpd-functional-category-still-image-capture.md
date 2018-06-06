---
Description: WPD\_FUNCTIONAL\_CATEGORY\_STILL\_IMAGE\_CAPTURE
ms.assetid: fb434927-1548-4c6e-bfb7-3a99eef62a4a
title: WPD\_FUNCTIONAL\_CATEGORY\_STILL\_IMAGE\_CAPTURE
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_FUNCTIONAL\_CATEGORY\_STILL\_IMAGE\_CAPTURE

A WPD\_FUNCTIONAL\_CATEGORY\_STILL\_IMAGE\_CAPTURE functional object encapsulates still-image capture functionality on a device, such as a camera or camera attachment.



| Property Name                                                                                                            | Required or Optional                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](object-properties.md#wpd-object-id)                                                                   | Required, read-only. A client cannot set this property, even at creation time.                                                                         |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md#wpd-object-parent-id)                                                    | Required.                                                                                                                                              |
| [WPD\_OBJECT\_NAME](object-properties.md#wpd-object-name)                                                               | Required.                                                                                                                                              |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md#wpd-object-persistent-unique-id)                             | Required, read-only. A client cannot set this property, even at creation time.                                                                         |
| [WPD\_OBJECT\_FORMAT](object-properties.md#wpd-object-format)                                                           | Required.                                                                                                                                              |
| [WPD\_OBJECT\_CONTENT\_TYPE](object-properties.md#wpd-object-content-type)                                              | Required.                                                                                                                                              |
| [WPD\_OBJECT\_ISHIDDEN](object-properties.md#wpd-object-ishidden)                                                       | Required if the object is hidden.                                                                                                                      |
| [WPD\_OBJECT\_ISSYSTEM](object-properties.md#wpd-object-issystem)                                                       | Required if the object is a system object (represents a system file).                                                                                  |
| [WPD\_OBJECT\_SIZE](object-properties.md#wpd-object-size)                                                               | Required if the object has at least one resource.                                                                                                      |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](object-properties.md#wpd-object-original-file-name)                                 | Required if the object represents a file.                                                                                                              |
| [WPD\_OBJECT\_NON\_CONSUMABLE](object-properties.md#wpd-object-non-consumable)                                          | Recommended if the object is not meant for consumption by the device.                                                                                  |
| [WPD\_OBJECT\_REFERENCES](object-properties.md#wpd-object-references)                                                   | Required if the object has references to other objects.                                                                                                |
| [WPD\_OBJECT\_KEYWORDS](object-properties.md#wpd-object-keywords)                                                       | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_SYNC\_ID](object-properties.md#wpd-object-sync-id)                                                        | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](object-properties.md#wpd-object-is-drm-protected)                                     | Required if the object is protected by DRM technology.                                                                                                 |
| [WPD\_OBJECT\_DATE\_CREATED](object-properties.md#wpd-object-date-created)                                              | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_DATE\_MODIFIED](object-properties.md#wpd-object-date-modified)                                            | Recommended.                                                                                                                                           |
| [WPD\_OBJECT\_DATE\_AUTHORED](object-properties.md#wpd-object-date-authored)                                            | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                   | Recommended if the object is referenced by another object.                                                                                             |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](object-properties.md#wpd-object-container-functional-object-id)        | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](object-properties.md#wpd-object-generate-thumbnail-from-resource)    | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_CAN\_DELETE](object-properties.md)                                                                        | Required if the object cannot be deleted.                                                                                                              |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                   | Optional.                                                                                                                                              |
| [WPD\_FUNCTIONAL\_OBJECT\_CATEGORY](miscellaneous-properties.md#wpd-functional-object-category)                         | Required. See [**WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT**](wpd-content-type-functional-object.md) for categories defined by Windows Portable Devices. |
| [WPD\_STILL\_IMAGE\_CAPTURE\_RESOLUTION](still-image-properties.md#wpd-still-image-capture-resolution)                  | Required.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_CAPTURE\_FORMAT](still-image-properties.md#wpd-still-image-capture-format)                          | Required.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_COMPRESSION\_SETTING](still-image-properties.md#wpd-still-image-compression-setting)                | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_WHITE\_BALANCE](still-image-properties.md#wpd-still-image-white-balance)                            | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_RGB\_GAIN](still-image-properties.md#wpd-still-image-rgb-gain)                                      | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FNUMBER](still-image-properties.md#wpd-still-image-fnumber)                                         | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FOCAL\_LENGTH](still-image-properties.md#wpd-still-image-focal-length)                              | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FOCUS\_DISTANCE](still-image-properties.md#wpd-still-image-focus-distance)                          | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FOCUS\_MODE](still-image-properties.md#wpd-still-image-focus-mode)                                  | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_METERING\_MODE](still-image-properties.md#wpd-still-image-exposure-metering-mode)         | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FLASH\_MODE](still-image-properties.md#wpd-still-image-flash-mode)                                  | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_TIME](still-image-properties.md#wpd-still-image-exposure-time)                            | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_PROGRAM\_MODE](still-image-properties.md#wpd-still-image-exposure-program-mode)           | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_INDEX](still-image-properties.md#wpd-still-image-exposure-index)                          | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_BIAS\_COMPENSATION](still-image-properties.md#wpd-still-image-exposure-bias-compensation) | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_CAPTURE\_DELAY](still-image-properties.md#wpd-still-image-capture-delay)                            | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_CAPTURE\_MODE](still-image-properties.md#wpd-still-image-capture-mode)                              | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_CONTRAST](still-image-properties.md#wpd-still-image-contrast)                                       | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_SHARPNESS](still-image-properties.md#wpd-still-image-sharpness)                                     | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_DIGITAL\_ZOOM](still-image-properties.md#wpd-still-image-digital-zoom)                              | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EFFECT\_MODE](still-image-properties.md#wpd-still-image-effect-mode)                                | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_BURST\_NUMBER](still-image-properties.md#wpd-still-image-burst-number)                              | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_BURST\_INTERVAL](still-image-properties.md#wpd-still-image-burst-interval)                          | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_TIMELAPSE\_NUMBER](still-image-properties.md#wpd-still-image-timelapse-number)                      | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_TIMELAPSE\_INTERVAL](still-image-properties.md#wpd-still-image-timelapse-interval)                  | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FOCUS\_METERING\_MODE](still-image-properties.md#wpd-still-image-focus-metering-mode)               | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_UPLOAD\_URL](still-image-properties.md#wpd-still-image-upload-url)                                  | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_ARTIST](still-image-properties.md#wpd-still-image-artist)                                           | Optional.                                                                                                                                              |



 

## Typical Resources

These objects typically do not host resources.

Many of these properties have interconnected effects. For example, if **WPD\_STILL\_IMAGE\_EXPOSURE\_METERING\_MODE** is set to automatic, then the f-stop, exposure time, and exposure meter will be linked; varying one will cause the others to vary.

## Related topics

<dl> <dt>

[**WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT**](wpd-content-type-functional-object.md)
</dt> </dl>

 

 



