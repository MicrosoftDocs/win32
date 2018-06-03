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
| [WPD\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_ID)                                                                   | Required, read-only. A client cannot set this property, even at creation time.                                                                         |
| [WPD\_OBJECT\_PARENT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PARENT\_ID)                                                    | Required.                                                                                                                                              |
| [WPD\_OBJECT\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_NAME)                                                               | Required.                                                                                                                                              |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID)                             | Required, read-only. A client cannot set this property, even at creation time.                                                                         |
| [WPD\_OBJECT\_FORMAT](https://www.bing.com/search?q=WPD\_OBJECT\_FORMAT)                                                           | Required.                                                                                                                                              |
| [WPD\_OBJECT\_CONTENT\_TYPE](https://www.bing.com/search?q=WPD\_OBJECT\_CONTENT\_TYPE)                                              | Required.                                                                                                                                              |
| [WPD\_OBJECT\_ISHIDDEN](https://www.bing.com/search?q=WPD\_OBJECT\_ISHIDDEN)                                                       | Required if the object is hidden.                                                                                                                      |
| [WPD\_OBJECT\_ISSYSTEM](https://www.bing.com/search?q=WPD\_OBJECT\_ISSYSTEM)                                                       | Required if the object is a system object (represents a system file).                                                                                  |
| [WPD\_OBJECT\_SIZE](https://www.bing.com/search?q=WPD\_OBJECT\_SIZE)                                                               | Required if the object has at least one resource.                                                                                                      |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_ORIGINAL\_FILE\_NAME)                                 | Required if the object represents a file.                                                                                                              |
| [WPD\_OBJECT\_NON\_CONSUMABLE](https://www.bing.com/search?q=WPD\_OBJECT\_NON\_CONSUMABLE)                                          | Recommended if the object is not meant for consumption by the device.                                                                                  |
| [WPD\_OBJECT\_REFERENCES](https://www.bing.com/search?q=WPD\_OBJECT\_REFERENCES)                                                   | Required if the object has references to other objects.                                                                                                |
| [WPD\_OBJECT\_KEYWORDS](https://www.bing.com/search?q=WPD\_OBJECT\_KEYWORDS)                                                       | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_SYNC\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_SYNC\_ID)                                                        | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](https://www.bing.com/search?q=WPD\_OBJECT\_IS\_DRM\_PROTECTED)                                     | Required if the object is protected by DRM technology.                                                                                                 |
| [WPD\_OBJECT\_DATE\_CREATED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_CREATED)                                              | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_DATE\_MODIFIED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_MODIFIED)                                            | Recommended.                                                                                                                                           |
| [WPD\_OBJECT\_DATE\_AUTHORED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_AUTHORED)                                            | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                   | Recommended if the object is referenced by another object.                                                                                             |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID)        | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](https://www.bing.com/search?q=WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE)    | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_CAN\_DELETE](object-properties.md)                                                                        | Required if the object cannot be deleted.                                                                                                              |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                   | Optional.                                                                                                                                              |
| [WPD\_FUNCTIONAL\_OBJECT\_CATEGORY](https://www.bing.com/search?q=WPD\_FUNCTIONAL\_OBJECT\_CATEGORY)                         | Required. See [**WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT**](wpd-content-type-functional-object.md) for categories defined by Windows Portable Devices. |
| [WPD\_STILL\_IMAGE\_CAPTURE\_RESOLUTION](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_CAPTURE\_RESOLUTION)                  | Required.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_CAPTURE\_FORMAT](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_CAPTURE\_FORMAT)                          | Required.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_COMPRESSION\_SETTING](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_COMPRESSION\_SETTING)                | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_WHITE\_BALANCE](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_WHITE\_BALANCE)                            | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_RGB\_GAIN](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_RGB\_GAIN)                                      | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FNUMBER](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_FNUMBER)                                         | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FOCAL\_LENGTH](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_FOCAL\_LENGTH)                              | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FOCUS\_DISTANCE](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_FOCUS\_DISTANCE)                          | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FOCUS\_MODE](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_FOCUS\_MODE)                                  | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_METERING\_MODE](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_EXPOSURE\_METERING\_MODE)         | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FLASH\_MODE](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_FLASH\_MODE)                                  | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_TIME](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_EXPOSURE\_TIME)                            | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_PROGRAM\_MODE](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_EXPOSURE\_PROGRAM\_MODE)           | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_INDEX](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_EXPOSURE\_INDEX)                          | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EXPOSURE\_BIAS\_COMPENSATION](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_EXPOSURE\_BIAS\_COMPENSATION) | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_CAPTURE\_DELAY](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_CAPTURE\_DELAY)                            | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_CAPTURE\_MODE](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_CAPTURE\_MODE)                              | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_CONTRAST](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_CONTRAST)                                       | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_SHARPNESS](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_SHARPNESS)                                     | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_DIGITAL\_ZOOM](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_DIGITAL\_ZOOM)                              | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_EFFECT\_MODE](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_EFFECT\_MODE)                                | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_BURST\_NUMBER](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_BURST\_NUMBER)                              | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_BURST\_INTERVAL](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_BURST\_INTERVAL)                          | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_TIMELAPSE\_NUMBER](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_TIMELAPSE\_NUMBER)                      | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_TIMELAPSE\_INTERVAL](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_TIMELAPSE\_INTERVAL)                  | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_FOCUS\_METERING\_MODE](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_FOCUS\_METERING\_MODE)               | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_UPLOAD\_URL](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_UPLOAD\_URL)                                  | Optional.                                                                                                                                              |
| [WPD\_STILL\_IMAGE\_ARTIST](https://www.bing.com/search?q=WPD\_STILL\_IMAGE\_ARTIST)                                           | Optional.                                                                                                                                              |



 

## Typical Resources

These objects typically do not host resources.

Many of these properties have interconnected effects. For example, if **WPD\_STILL\_IMAGE\_EXPOSURE\_METERING\_MODE** is set to automatic, then the f-stop, exposure time, and exposure meter will be linked; varying one will cause the others to vary.

## Related topics

<dl> <dt>

[**WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT**](wpd-content-type-functional-object.md)
</dt> </dl>

 

 



