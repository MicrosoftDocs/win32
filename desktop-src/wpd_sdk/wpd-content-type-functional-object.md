---
description: WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT
ms.assetid: 112de70b-afcc-4fba-b74f-c33bd759d517
title: WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT

An object that describes its type as WPD\_CONTENT\_FUNCTIONAL\_OBJECT represents a functional object, encapsulating device functionality.

All functional objects, no matter what type, support the following properties. (If you define a custom functional object, it must also support these properties.)



| Property Name                                                                                                         | Required or Optional                                                                  |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](object-properties.md)                                                                | Required, read-only. A client cannot set this property, even at creation time.        |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md)                                                 | Required.                                                                             |
| [WPD\_OBJECT\_NAME](object-properties.md)                                                            | Required.                                                                             |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md)                          | Required, read-only. A client cannot set this property, even at creation time.        |
| [WPD\_OBJECT\_FORMAT](object-properties.md)                                                        | Required.                                                                             |
| [WPD\_OBJECT\_CONTENT\_TYPE](object-properties.md)                                           | Required.                                                                             |
| [WPD\_OBJECT\_ISHIDDEN](object-properties.md)                                                    | Required if the object is hidden.                                                     |
| [WPD\_OBJECT\_ISSYSTEM](object-properties.md)                                                    | Required if the object is a system object (represents a system file).                 |
| [WPD\_OBJECT\_SIZE](object-properties.md)                                                            | Required if the object has at least one resource.                                     |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](object-properties.md)                              | Required if the object represents a file.                                             |
| [WPD\_OBJECT\_NON\_CONSUMABLE](object-properties.md)                                       | Recommended if the object is not meant for consumption by the device.                 |
| [WPD\_OBJECT\_REFERENCES](object-properties.md)                                                | Required if the object has references to other objects.                               |
| [WPD\_OBJECT\_KEYWORDS](object-properties.md)                                                    | Optional.                                                                             |
| [WPD\_OBJECT\_SYNC\_ID](object-properties.md)                                                     | Optional.                                                                             |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](object-properties.md)                                  | Required if the object is protected by DRM technology.                                |
| [WPD\_OBJECT\_DATE\_CREATED](object-properties.md)                                           | Optional.                                                                             |
| [WPD\_OBJECT\_DATE\_MODIFIED](object-properties.md)                                         | Recommended.                                                                          |
| [WPD\_OBJECT\_DATE\_AUTHORED](object-properties.md)                                         | Optional.                                                                             |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                | Recommended if the object is referenced by another object.                            |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](object-properties.md)     | Optional.                                                                             |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](object-properties.md) | Optional.                                                                             |
| [WPD\_OBJECT\_CAN\_DELETE](object-properties.md)                                                                     | Required if the object cannot be deleted.                                             |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                | Optional.                                                                             |
| [WPD\_FUNCTIONAL\_OBJECT\_CATEGORY](miscellaneous-properties.md)                      | Required. See the following table for categories defined by Windows Portable Devices. |



 

## Typical Resources

These objects typically do not host resources.

## Functional Object Categories

Functional objects can be grouped into categories, depending on their functions. A category is described by the WPD\_FUNCTIONAL\_OBJECT\_CATEGORY property (a GUID value). The category determines which additional properties are supported.

The following table describes the categories defined by Windows Portable Devices. See the description of the category to learn what additional properties and resources the object supports.



| Functional Category                                                                                        | Description                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WPD\_FUNCTIONAL\_CATEGORY\_ALL**](wpd-functional-category-all.md)                                      | This functional category is valid only as a parameter for certain query functions (to indicate that all functional object types are acceptable), and is not a reported functional category by the driver. |
| [**WPD\_FUNCTIONAL\_CATEGORY\_AUDIO\_CAPTURE**](wpd-functional-category-audio-capture.md)                 | The object encapsulates audio capture functionality on the device, for example, a voice recorder or other audio recording component.                                                                      |
| [**WPD\_FUNCTIONAL\_CATEGORY\_DEVICE**](wpd-functional-category-device.md)                                | The object encapsulates the device (that is, the top-most object of the device).                                                                                                                          |
| [**WPD\_FUNCTIONAL\_CATEGORY\_NETWORK\_CONFIGURATION**](wpd-functional-category-network-configuration.md) | The object encapsulates network-configuration functionality for the device, for example, WiFi profiles or partnerships.                                                                                   |
| [**WPD\_FUNCTIONAL\_CATEGORY\_RENDERING\_INFORMATION**](wpd-functional-category-rendering-information.md) | The object describes the types of media files that the device is able to play.                                                                                                                            |
| [**WPD\_FUNCTIONAL\_CATEGORY\_SMS**](wpd-functional-category-sms.md)                                      | The object encapsulates short message service functionality (commonly called "text messaging") on the device.                                                                                             |
| [**WPD\_FUNCTIONAL\_CATEGORY\_STILL\_IMAGE\_CAPTURE**](wpd-functional-category-still-image-capture.md)    | The object encapsulates still image capture functionality on a device such as a camera or camera attachment.                                                                                              |
| [**WPD\_FUNCTIONAL\_CATEGORY\_STORAGE**](wpd-functional-category-storage.md)                              | The object encapsulates physical file storage on the device.                                                                                                                                              |
| [**WPD\_FUNCTIONAL\_CATEGORY\_VIDEO\_CAPTURE**](wpd-functional-category-video-capture.md)                 | The object encapsulates video capture functionality on the device, for example, a video recorder component. An application uses this object to gain programmatic control.                                 |



 

## Related topics

<dl> <dt>

[**Requirements for Objects**](requirements-for-objects.md)
</dt> </dl>

 

 



