---
description: WPD\_FUNCTIONAL\_CATEGORY\_SMS
ms.assetid: dbb536a6-9c12-459d-8098-ebe4fc4c8f2f
title: WPD_FUNCTIONAL_CATEGORY_SMS
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_FUNCTIONAL\_CATEGORY\_SMS

A WPD\_FUNCTIONAL\_CATEGORY\_SMS functional object encapsulates short message service functionality (commonly called "text messaging") on the device.



| Property Name                                                                                                         | Required or Optional                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](object-properties.md)                                                                | Required, read-only. A client cannot set this property, even at creation time.                                                                         |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md)                                                 | Required.                                                                                                                                              |
| [WPD\_OBJECT\_NAME](object-properties.md)                                                            | Required.                                                                                                                                              |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md)                          | Required, read-only. A client cannot set this property, even at creation time.                                                                         |
| [WPD\_OBJECT\_FORMAT](object-properties.md)                                                        | Required.                                                                                                                                              |
| [WPD\_OBJECT\_CONTENT\_TYPE](object-properties.md)                                           | Required.                                                                                                                                              |
| [WPD\_OBJECT\_ISHIDDEN](object-properties.md)                                                    | Required if the object is hidden.                                                                                                                      |
| [WPD\_OBJECT\_ISSYSTEM](object-properties.md)                                                    | Required if the object is a system object (represents a system file).                                                                                  |
| [WPD\_OBJECT\_SIZE](object-properties.md)                                                            | Required if the object has at least one resource.                                                                                                      |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](object-properties.md)                              | Required if the object represents a file.                                                                                                              |
| [WPD\_OBJECT\_NON\_CONSUMABLE](object-properties.md)                                       | Recommended if the object is not meant for consumption by the device.                                                                                  |
| [WPD\_OBJECT\_REFERENCES](object-properties.md)                                                | Required if the object has references to other objects.                                                                                                |
| [WPD\_OBJECT\_KEYWORDS](object-properties.md)                                                    | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_SYNC\_ID](object-properties.md)                                                     | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](object-properties.md)                                  | Required if the object is protected by DRM technology.                                                                                                 |
| [WPD\_OBJECT\_DATE\_CREATED](object-properties.md)                                           | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_DATE\_MODIFIED](object-properties.md)                                         | Recommended.                                                                                                                                           |
| [WPD\_OBJECT\_DATE\_AUTHORED](object-properties.md)                                         | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                | Recommended if the object is referenced by another object.                                                                                             |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](object-properties.md)     | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](object-properties.md) | Optional.                                                                                                                                              |
| [WPD\_OBJECT\_CAN\_DELETE](object-properties.md)                                                                     | Required if the object cannot be deleted.                                                                                                              |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                | Optional.                                                                                                                                              |
| [WPD\_FUNCTIONAL\_OBJECT\_CATEGORY](miscellaneous-properties.md)                      | Required. See [**WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT**](wpd-content-type-functional-object.md) for categories defined by Windows Portable Devices. |
| [WPD\_SMS\_PROVIDER](sms-properties.md)                                                             | Required.                                                                                                                                              |
| [WPD\_SMS\_TIMEOUT](sms-properties.md)                                                               | Required.                                                                                                                                              |
| [WPD\_SMS\_MAX\_PAYLOAD](sms-properties.md)                                                      | Required.                                                                                                                                              |
| [WPD\_SMS\_ENCODING](sms-properties.md)                                                             | Required.                                                                                                                                              |



 

## Typical Resources

These objects typically do not host resources.

## Related topics

<dl> <dt>

[**WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT**](wpd-content-type-functional-object.md)
</dt> </dl>

 

 



