---
description: WPD\_CONTENT\_TYPE\_SERVICE
ms.assetid: 87c4c228-69e0-4b55-b91f-fe6e561f6d18
title: WPD_CONTENT_TYPE_SERVICE
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_CONTENT\_TYPE\_SERVICE

An object that describes its type as WPD\_CONTENT\_TYPE\_SERVICE represents a device service.

This type of object supports the following properties.



| Property Name                                                                                        | Required or Optional                                                           |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](object-properties.md)                                               | Required, read-only. A client cannot set this property, even at creation time. |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md)                                | Required.                                                                      |
| [WPD\_OBJECT\_NAME](object-properties.md)                                           | Required if the object represents a file.                                      |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md)         | Required, read-only. A client cannot set this property, even at creation time. |
| [WPD\_OBJECT\_ISHIDDEN](object-properties.md)                                   | Required if the service should not be shown to the user.                       |
| [WPD\_OBJECT\_ISSYSTEM](object-properties.md)                                   | Required if the object is a system object (represents a system file).          |
| [WPD\_FUNCTIONAL\_OBJECT\_CATEGORY](object-properties.md) | Required. This represents the device service type.                             |
| [WPD\_SERVICE\_VERSION](object-properties.md)           | Required.                                                                      |
| [WPD\_STORAGE\_TYPE](object-properties.md)                                                          | Required if the service is used to store objects.                              |
| [WPD\_STORAGE\_CAPACITY](object-properties.md)                                                      | Required if the service is used to store objects.                              |



 

## Typical Resources

These objects do not host resources.

## Related topics

<dl> <dt>

[**Requirements for Objects**](requirements-for-objects.md)
</dt> </dl>

 

 



