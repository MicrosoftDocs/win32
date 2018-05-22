---
Description: 'WPD\_CONTENT\_TYPE\_SERVICE'
ms.assetid: '87c4c228-69e0-4b55-b91f-fe6e561f6d18'
title: 'WPD\_CONTENT\_TYPE\_SERVICE'
---

# WPD\_CONTENT\_TYPE\_SERVICE

An object that describes its type as WPD\_CONTENT\_TYPE\_SERVICE represents a device service.

This type of object supports the following properties.



| Property Name                                                                                        | Required or Optional                                                           |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](object-properties.md#wpd-object-id)                                               | Required, read-only. A client cannot set this property, even at creation time. |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md#wpd-object-parent-id)                                | Required.                                                                      |
| [WPD\_OBJECT\_NAME](object-properties.md#wpd-object-name)                                           | Required if the object represents a file.                                      |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md#wpd-object-persistent-unique-id)         | Required, read-only. A client cannot set this property, even at creation time. |
| [WPD\_OBJECT\_ISHIDDEN](object-properties.md#wpd-object-ishidden)                                   | Required if the service should not be shown to the user.                       |
| [WPD\_OBJECT\_ISSYSTEM](object-properties.md#wpd-object-issystem)                                   | Required if the object is a system object (represents a system file).          |
| [WPD\_FUNCTIONAL\_OBJECT\_CATEGORY](object-properties.md#wpd-object-container-functional-object-id) | Required. This represents the device service type.                             |
| [WPD\_SERVICE\_VERSION](object-properties.md#wpd-object-generate-thumbnail-from-resource)           | Required.                                                                      |
| [WPD\_STORAGE\_TYPE](object-properties.md)                                                          | Required if the service is used to store objects.                              |
| [WPD\_STORAGE\_CAPACITY](object-properties.md)                                                      | Required if the service is used to store objects.                              |



 

## Typical Resources

These objects do not host resources.

## Related topics

<dl> <dt>

[**Requirements for Objects**](requirements-for-objects.md)
</dt> </dl>

 

 



