---
Description: WPD\_FUNCTIONAL\_CATEGORY\_DEVICE
ms.assetid: 64b34490-1cb5-4915-ae1c-77bd4ab79ad7
title: WPD\_FUNCTIONAL\_CATEGORY\_DEVICE
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_FUNCTIONAL\_CATEGORY\_DEVICE

A WPD\_FUNCTIONAL\_CATEGORY\_DEVICE functional object encapsulates the device (that is, the top-most object of the device). If a device implements this functional category, it should support these properties in addition to the properties listed for the [device object](device-object.md).



| Property Name                                                                                                         | Required or Optional                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_ID)                                                                | Required, read-only. A client cannot set this property, even at creation time.                                      |
| [WPD\_OBJECT\_PARENT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PARENT\_ID)                                                 | Required.                                                                                                           |
| [WPD\_OBJECT\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_NAME)                                                            | Required.                                                                                                           |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID)                          | Required, read-only. A client cannot set this property, even at creation time.                                      |
| [WPD\_OBJECT\_FORMAT](https://www.bing.com/search?q=WPD\_OBJECT\_FORMAT)                                                        | Required.                                                                                                           |
| [WPD\_OBJECT\_CONTENT\_TYPE](https://www.bing.com/search?q=WPD\_OBJECT\_CONTENT\_TYPE)                                           | Required.                                                                                                           |
| [WPD\_OBJECT\_ISHIDDEN](https://www.bing.com/search?q=WPD\_OBJECT\_ISHIDDEN)                                                    | Required if the object is hidden.                                                                                   |
| [WPD\_OBJECT\_ISSYSTEM](https://www.bing.com/search?q=WPD\_OBJECT\_ISSYSTEM)                                                    | Required if the object is a system object (represents a system file).                                               |
| [WPD\_OBJECT\_SIZE](https://www.bing.com/search?q=WPD\_OBJECT\_SIZE)                                                            | Required if the object has at least one resource.                                                                   |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_ORIGINAL\_FILE\_NAME)                              | Required if the object represents a file.                                                                           |
| [WPD\_OBJECT\_NON\_CONSUMABLE](https://www.bing.com/search?q=WPD\_OBJECT\_NON\_CONSUMABLE)                                       | Recommended if the object is not meant for consumption by the device.                                               |
| [WPD\_OBJECT\_REFERENCES](https://www.bing.com/search?q=WPD\_OBJECT\_REFERENCES)                                                | Required if the object has references to other objects.                                                             |
| [WPD\_OBJECT\_KEYWORDS](https://www.bing.com/search?q=WPD\_OBJECT\_KEYWORDS)                                                    | Optional.                                                                                                           |
| [WPD\_OBJECT\_SYNC\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_SYNC\_ID)                                                     | Optional.                                                                                                           |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](https://www.bing.com/search?q=WPD\_OBJECT\_IS\_DRM\_PROTECTED)                                  | Required if the object is protected by DRM technology.                                                              |
| [WPD\_OBJECT\_DATE\_CREATED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_CREATED)                                           | Optional.                                                                                                           |
| [WPD\_OBJECT\_DATE\_MODIFIED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_MODIFIED)                                         | Recommended.                                                                                                        |
| [WPD\_OBJECT\_DATE\_AUTHORED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_AUTHORED)                                         | Optional.                                                                                                           |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                | Recommended if the object is referenced by another object.                                                          |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID)     | Optional.                                                                                                           |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](https://www.bing.com/search?q=WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE) | Optional.                                                                                                           |
| [WPD\_FUNCTIONAL\_OBJECT\_CATEGORY](https://www.bing.com/search?q=WPD\_FUNCTIONAL\_OBJECT\_CATEGORY)                      | Required.                                                                                                           |
| [WPD\_DEVICE\_SYNC\_PARTNER](https://www.bing.com/search?q=WPD\_DEVICE\_SYNC\_PARTNER)                                           | Optional.                                                                                                           |
| [WPD\_DEVICE\_FIRMWARE\_VERSION](https://www.bing.com/search?q=WPD\_DEVICE\_FIRMWARE\_VERSION)                                   | Required.                                                                                                           |
| [WPD\_DEVICE\_POWER\_LEVEL](https://www.bing.com/search?q=WPD\_DEVICE\_POWER\_LEVEL)                                             | Recommended if device has a battery.                                                                                |
| [WPD\_DEVICE\_POWER\_SOURCE](https://www.bing.com/search?q=WPD\_DEVICE\_POWER\_SOURCE)                                           | Recommended.                                                                                                        |
| [WPD\_DEVICE\_PROTOCOL](https://www.bing.com/search?q=WPD\_DEVICE\_PROTOCOL)                                                    | Recommended.                                                                                                        |
| [WPD\_DEVICE\_MANUFACTURER](https://www.bing.com/search?q=WPD\_DEVICE\_MANUFACTURER)                                            | Required.                                                                                                           |
| [WPD\_DEVICE\_MODEL](https://www.bing.com/search?q=WPD\_DEVICE\_MODEL)                                                          | Required.                                                                                                           |
| [WPD\_DEVICE\_SERIAL\_NUMBER](https://www.bing.com/search?q=WPD\_DEVICE\_SERIAL\_NUMBER)                                         | Required.                                                                                                           |
| [WPD\_DEVICE\_SUPPORTS\_NON\_CONSUMABLE](https://www.bing.com/search?q=WPD\_DEVICE\_SUPPORTS\_NON\_CONSUMABLE)                    | Required if the device supports non-consumable objects; that is, if the device can be used for simple data storage. |
| [WPD\_DEVICE\_DATETIME](https://www.bing.com/search?q=WPD\_DEVICE\_DATETIME)                                                    | Optional.                                                                                                           |
| [WPD\_DEVICE\_FRIENDLY\_NAME](https://www.bing.com/search?q=WPD\_DEVICE\_FRIENDLY\_NAME)                                         | Recommended.                                                                                                        |
| [WPD\_DEVICE\_SUPPORTED\_DRM\_SCHEMES](https://www.bing.com/search?q=WPD\_DEVICE\_SUPPORTED\_DRM\_SCHEMES)                        | Recommended if the device supports DRM technology.                                                                  |
| [WPD\_DEVICE\_SUPPORTED\_FORMATS\_ARE\_ORDERED](https://www.bing.com/search?q=WPD\_DEVICE\_SUPPORTED\_FORMATS\_ARE\_ORDERED)       | Recommended if the device supports preferred format ordering.                                                       |
| [WPD\_DEVICE\_TYPE](https://www.bing.com/search?q=WPD\_DEVICE\_TYPE)                                                            | Recommended.                                                                                                        |



 

## Typical Resources

These objects typically do not host resources.

## Related topics

<dl> <dt>

[**WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT**](wpd-content-type-functional-object.md)
</dt> </dl>

 

 



