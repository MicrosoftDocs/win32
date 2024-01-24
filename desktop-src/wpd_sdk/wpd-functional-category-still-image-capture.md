---
description: WPD\_FUNCTIONAL\_CATEGORY\_STILL\_IMAGE\_CAPTURE
ms.assetid: fb434927-1548-4c6e-bfb7-3a99eef62a4a
title: WPD_FUNCTIONAL_CATEGORY_STILL_IMAGE_CAPTURE
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_FUNCTIONAL\_CATEGORY\_STILL\_IMAGE\_CAPTURE

A WPD\_FUNCTIONAL\_CATEGORY\_STILL\_IMAGE\_CAPTURE functional object encapsulates still-image capture functionality on a device, such as a camera or camera attachment.



| Property Name                                                                                                            | Required or Optional                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](object-properties.md)                                                                   | Required, read-only. A client cannot set this property, even at creation time.                                                                         |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md)                                                    | Required.                                                                                                                                              |
| [WPD\_OBJECT\_NAME](object-properties.md)                                                               | Required.                                                                                                                                              |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md)                             | Required, read-only. A client cannot set this property, even at creation time.                                                                         |
| [WPD\_OBJECT\_FORMAT](object-properties.md)                                                           | Required.                                                                                                                                              |
| [WPD\_OBJECT\_CONTENT\_TYPE](object-properties.md)                                              | Required.                                                                                                                                              |
| [WPD\_OBJECT\_ISHIDDEN](object-properties.md)                                                       | Required if the object is hidden.                                                                                                                      |
| [WPD\_OBJECT\_ISSYSTEM](object-properties.md)                                                       | Required if the object is a system object (represents a system file).                                                                                  |
| [WPD\_OBJECT\_SIZE](object-properties.md)                                                               | Required if the object has at least one resource.                                                                                                      |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](object-properties.md)                                 | Required if the object represents a file.                                                                                                              |
| [WPD\_OBJECT\_NON\_CONSUMABLE](object-properties.md)                                          | Recommended if the object is not meant for consumption by the device.                                                                                  |
| [WPD\_OBJECT\_REFERENCES](object-properties.md)                                                   | Required if the object has references to other objects.                                                                                                |
| [WPD\_OBJECT\_KEYWORDS](object-properties.md)                                                       | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_SYNC\_ID](object-properties.md)                                                        | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](object-properties.md)                                     | Required if the object is protected by DRM technology.                                                                                                 |
| [WPD\_OBJECT\_DATE\_CREATED](object-properties.md)                                              | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_DATE\_MODIFIED](object-properties.md)                                            | Recommended.                                                                                                                                           |
| [WPD\_OBJECT\_DATE\_AUTHORED](object-properties.md)                                            | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                   | Recommended if the object is referenced by another object.                                                                                             |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](object-properties.md)        | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](object-properties.md)    | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_CAN\_DELETE](object-properties.md)                                                                        | Required if the object cannot be deleted.                                                                                                              |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                   | Optional.                                                                                                                                              |
| [WPD\_FUNCTIONAL\_OBJECT\_CATEGORY](miscellaneous-properties.md)                         | Required. See [**WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT**](wpd-content-type-functional-object.md) for categories defined by Windows Portable Devices. |
| [WPD\_STILL\_IMAGE\_CAPTURE\_RESOLUTION](still-image-properties.md)                  | Required.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_CAPTURE\_FORMAT](still-image-properties.md)                          | Required.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_COMPRESSION\_SETTING](still-image-properties.md)                | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_WHITE\_BALANCE](still-image-properties.md)                            | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_RGB\_GAIN](still-image-properties.md)                                      | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FNUMBER](still-image-properties.md)                                         | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FOCAL\_LENGTH](still-image-properties.md)                              | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FOCUS\_DISTANCE](still-image-properties.md)                          | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FOCUS\_MODE](still-image-properties.md)                                  | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_METERING\_MODE](still-image-properties.md)         | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FLASH\_MODE](still-image-properties.md)                                  | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_TIME](still-image-properties.md)                            | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_PROGRAM\_MODE](still-image-properties.md)           | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_INDEX](still-image-properties.md)                          | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_BIAS\_COMPENSATION](still-image-properties.md) | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_CAPTURE\_DELAY](still-image-properties.md)                            | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_CAPTURE\_MODE](still-image-properties.md)                              | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_CONTRAST](still-image-properties.md)                                       | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_SHARPNESS](still-image-properties.md)                                     | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_DIGITAL\_ZOOM](still-image-properties.md)                              | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EFFECT\_MODE](still-image-properties.md)                                | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_BURST\_NUMBER](still-image-properties.md)                              | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_BURST\_INTERVAL](still-image-properties.md)                          | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_TIMELAPSE\_NUMBER](still-image-properties.md)                      | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_TIMELAPSE\_INTERVAL](still-image-properties.md)                  | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FOCUS\_METERING\_MODE](still-image-properties.md)               | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_UPLOAD\_URL](still-image-properties.md)                                  | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_ARTIST](still-image-properties.md)                                           | Optional.                                                                                                                                              |



 

## Typical Resources

These objects typically do not host resources.

Many of these properties have interconnected effects. For example, if **WPD\_STILL\_IMAGE\_EXPOSURE\_METERING\_MODE** is set to automatic, then the f-stop, exposure time, and exposure meter will be linked; varying one will cause the others to vary.

## Related topics

<dl> <dt>

[**WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT**](wpd-content-type-functional-object.md)
</dt> </dl>

 

 



