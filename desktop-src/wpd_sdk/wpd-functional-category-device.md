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
| [WPD\_OBJECT\_ID](object-properties.md#wpd-object-id)                                                                | Required, read-only. A client cannot set this property, even at creation time.                                      |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md#wpd-object-parent-id)                                                 | Required.                                                                                                           |
| [WPD\_OBJECT\_NAME](object-properties.md#wpd-object-name)                                                            | Required.                                                                                                           |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md#wpd-object-persistent-unique-id)                          | Required, read-only. A client cannot set this property, even at creation time.                                      |
| [WPD\_OBJECT\_FORMAT](object-properties.md#wpd-object-format)                                                        | Required.                                                                                                           |
| [WPD\_OBJECT\_CONTENT\_TYPE](object-properties.md#wpd-object-content-type)                                           | Required.                                                                                                           |
| [WPD\_OBJECT\_ISHIDDEN](object-properties.md#wpd-object-ishidden)                                                    | Required if the object is hidden.                                                                                   |
| [WPD\_OBJECT\_ISSYSTEM](object-properties.md#wpd-object-issystem)                                                    | Required if the object is a system object (represents a system file).                                               |
| [WPD\_OBJECT\_SIZE](object-properties.md#wpd-object-size)                                                            | Required if the object has at least one resource.                                                                   |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](object-properties.md#wpd-object-original-file-name)                              | Required if the object represents a file.                                                                           |
| [WPD\_OBJECT\_NON\_CONSUMABLE](object-properties.md#wpd-object-non-consumable)                                       | Recommended if the object is not meant for consumption by the device.                                               |
| [WPD\_OBJECT\_REFERENCES](object-properties.md#wpd-object-references)                                                | Required if the object has references to other objects.                                                             |
| [WPD\_OBJECT\_KEYWORDS](object-properties.md#wpd-object-keywords)                                                    | Optional.                                                                                                           |
| [WPD\_OBJECT\_SYNC\_ID](object-properties.md#wpd-object-sync-id)                                                     | Optional.                                                                                                           |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](object-properties.md#wpd-object-is-drm-protected)                                  | Required if the object is protected by DRM technology.                                                              |
| [WPD\_OBJECT\_DATE\_CREATED](object-properties.md#wpd-object-date-created)                                           | Optional.                                                                                                           |
| [WPD\_OBJECT\_DATE\_MODIFIED](object-properties.md#wpd-object-date-modified)                                         | Recommended.                                                                                                        |
| [WPD\_OBJECT\_DATE\_AUTHORED](object-properties.md#wpd-object-date-authored)                                         | Optional.                                                                                                           |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                | Recommended if the object is referenced by another object.                                                          |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](object-properties.md#wpd-object-container-functional-object-id)     | Optional.                                                                                                           |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](object-properties.md#wpd-object-generate-thumbnail-from-resource) | Optional.                                                                                                           |
| [WPD\_FUNCTIONAL\_OBJECT\_CATEGORY](miscellaneous-properties.md#wpd-functional-object-category)                      | Required.                                                                                                           |
| [WPD\_DEVICE\_SYNC\_PARTNER](device-properties.md#wpd-device-sync-partner)                                           | Optional.                                                                                                           |
| [WPD\_DEVICE\_FIRMWARE\_VERSION](device-properties.md#wpd-device-firmware-version)                                   | Required.                                                                                                           |
| [WPD\_DEVICE\_POWER\_LEVEL](device-properties.md#wpd-device-power-level)                                             | Recommended if device has a battery.                                                                                |
| [WPD\_DEVICE\_POWER\_SOURCE](device-properties.md#wpd-device-power-source)                                           | Recommended.                                                                                                        |
| [WPD\_DEVICE\_PROTOCOL](device-properties.md#wpd-device-protocol)                                                    | Recommended.                                                                                                        |
| [WPD\_DEVICE\_MANUFACTURER](device-properties.md#wpd-device-manufacturer)                                            | Required.                                                                                                           |
| [WPD\_DEVICE\_MODEL](device-properties.md#wpd-device-model)                                                          | Required.                                                                                                           |
| [WPD\_DEVICE\_SERIAL\_NUMBER](device-properties.md#wpd-device-serial-number)                                         | Required.                                                                                                           |
| [WPD\_DEVICE\_SUPPORTS\_NON\_CONSUMABLE](device-properties.md#wpd-device-supports-non-consumable)                    | Required if the device supports non-consumable objects; that is, if the device can be used for simple data storage. |
| [WPD\_DEVICE\_DATETIME](device-properties.md#wpd-device-datetime)                                                    | Optional.                                                                                                           |
| [WPD\_DEVICE\_FRIENDLY\_NAME](device-properties.md#wpd-device-friendly-name)                                         | Recommended.                                                                                                        |
| [WPD\_DEVICE\_SUPPORTED\_DRM\_SCHEMES](device-properties.md#wpd-device-supported-drm-schemes)                        | Recommended if the device supports DRM technology.                                                                  |
| [WPD\_DEVICE\_SUPPORTED\_FORMATS\_ARE\_ORDERED](device-properties.md#wpd-device-supported-formats-are-ordered)       | Recommended if the device supports preferred format ordering.                                                       |
| [WPD\_DEVICE\_TYPE](device-properties.md#wpd-device-type)                                                            | Recommended.                                                                                                        |



 

## Typical Resources

These objects typically do not host resources.

## Related topics

<dl> <dt>

[**WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT**](wpd-content-type-functional-object.md)
</dt> </dl>

 

 



