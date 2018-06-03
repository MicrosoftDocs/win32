---
Description: Service Object
ms.assetid: 4ce4e7f7-579d-41a5-a4e1-935ba0afce83
title: Service Object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Service Object

The service object must support the following properties.



| Property Name                                                                                                                      | Required or Optional                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](https://msdn.microsoft.com/library/windows/hardware/ff597893#wpd-object-id)                                                         | Required. .                                                                           |
| [WPD\_OBJECT\_PARENT\_ID](https://msdn.microsoft.com/library/windows/hardware/ff597893#wpd-object-parent-id)                                   | Required.                                                                             |
| [WPD\_OBJECT\_NAME](https://msdn.microsoft.com/library/windows/hardware/ff597893#wpd-object-name)                                                   | Required.                                                                             |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](https://msdn.microsoft.com/library/windows/hardware/ff597893#wpd-object-persistent-unique-id) | Required.                                                                             |
| [WPD\_OBJECT\_ISHIDDEN](https://msdn.microsoft.com/library/windows/hardware/ff597893#wpd-object-ishidden)                                       | Required if the service object should not be shown to the user.                       |
| [WPD\_OBJECT\_ISSYSTEM](https://msdn.microsoft.com/library/windows/hardware/ff597893#wpd-object-issystem)                                       | Required if the object is a system object (for example, it represents a system file). |
| [WPD\_FUNCTIONAL\_OBJECT\_CATEGORY](https://msdn.microsoft.com/library/windows/hardware/ff597893#wpd-functional-object-category)     | Required. This represents the Device Service type, such as SERVICE Contacts.          |
| [WPD\_SERVICE\_VERSION](https://msdn.microsoft.com/library/windows/hardware/ff597893#wpd-service-version)                                       | Required.                                                                             |
| [WPD\_STORAGE\_TYPE](https://msdn.microsoft.com/library/windows/hardware/ff597893#wpd-storage-type)                                                | Required if the service is used to store objects.                                     |
| [WPD\_STORAGE\_CAPACITY](https://msdn.microsoft.com/library/windows/hardware/ff597865#wpd-storage-capacity)                                    | Required if the service is used to store objects.                                     |



 

## Typical Resources

These objects typically do not host resources.

## Typical Formats

The following list identifies typical formats used by the Service object. However, this object is not limited to these formats.

-   WPD\_OBJECT\_FORMAT\_UNSPECIFIED

## Related topics

<dl> <dt>

[**Requirements for Objects**](requirements-for-objects.md)
</dt> </dl>

 

 



