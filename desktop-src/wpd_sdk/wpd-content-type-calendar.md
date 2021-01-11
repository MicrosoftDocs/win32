---
description: WPD\_CONTENT\_TYPE\_CALENDAR
ms.assetid: b5fccaa8-03c7-4998-be46-82fc6aeb308b
title: WPD_CONTENT_TYPE_CALENDAR
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_CONTENT\_TYPE\_CALENDAR

An object that describes its type as WPD\_CONTENT\_TYPE\_CALENDAR represents a calendar. The object can be a file that contains calendar information or a folder that contains other calendar-related objects, such as tasks, appointments, and so on.

This type of object supports the following properties.



| Property Name                                                                                                         | Required or Optional                                                  |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](object-properties.md)                                                                | Required.                                                             |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md)                                                 | Required.                                                             |
| [WPD\_OBJECT\_NAME](object-properties.md)                                                            | Required if the object represents a file.                             |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md)                          | Required.                                                             |
| [WPD\_OBJECT\_FORMAT](object-properties.md)                                                        | Required.                                                             |
| [WPD\_OBJECT\_CONTENT\_TYPE](object-properties.md)                                           | Required.                                                             |
| [WPD\_OBJECT\_ISHIDDEN](object-properties.md)                                                    | Required if the object is hidden.                                     |
| [WPD\_OBJECT\_ISSYSTEM](object-properties.md)                                                    | Required if the object is a system object (represents a system file). |
| [WPD\_OBJECT\_SIZE](object-properties.md)                                                            | Required if the object has at least one resource.                     |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](object-properties.md)                              | Required if the object represents a file.                             |
| [WPD\_OBJECT\_NON\_CONSUMABLE](object-properties.md)                                       | Recommended if the object is not meant for consumption by the device. |
| [WPD\_OBJECT\_REFERENCES](object-properties.md)                                                | Required if the object has references to other objects.               |
| [WPD\_OBJECT\_KEYWORDS](object-properties.md)                                                    | Optional.                                                             |
| [WPD\_OBJECT\_SYNC\_ID](object-properties.md)                                                     | Optional.                                                             |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](object-properties.md)                                  | Required if the object is protected by DRM technology.                |
| [WPD\_OBJECT\_DATE\_CREATED](object-properties.md)                                           | Optional.                                                             |
| [WPD\_OBJECT\_DATE\_MODIFIED](object-properties.md)                                         | Recommended.                                                          |
| [WPD\_OBJECT\_DATE\_AUTHORED](object-properties.md)                                         | Optional.                                                             |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                     | Recommended if the object is referenced by another object.            |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](object-properties.md)     | Optional.                                                             |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](object-properties.md) | Optional.                                                             |
| [WPD\_OBJECT\_CAN\_DELETE](object-properties.md)                                               | Required if the object can be deleted.                                |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                | Optional.                                                             |



 

## Typical Resources

These objects typically include the following resources.



| Resource Name                                          | Required or Optional                             | Description        |
|--------------------------------------------------------|--------------------------------------------------|--------------------|
| [**WPD\_RESOURCE\_DEFAULT**](wpd-resource-default.md) | Required if the object is backed by binary data. | Contains the data. |



 

## Related topics

<dl> <dt>

[**Requirements for Objects**](requirements-for-objects.md)
</dt> </dl>

 

 



