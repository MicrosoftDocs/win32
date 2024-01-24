---
description: Service Object
ms.assetid: 4ce4e7f7-579d-41a5-a4e1-935ba0afce83
title: Service Object
ms.topic: article
ms.date: 05/31/2018
---

# Service Object

The service object must support the following properties.



| Property Name                                                                                                                      | Required or Optional                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](/previous-versions/windows/hardware/drivers/ff597893(v=vs.85))                                                         | Required. .                                                                           |
| [WPD\_OBJECT\_PARENT\_ID](/previous-versions/windows/hardware/drivers/ff597893(v=vs.85))                                   | Required.                                                                             |
| [WPD\_OBJECT\_NAME](/previous-versions/windows/hardware/drivers/ff597893(v=vs.85))                                                   | Required.                                                                             |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](/previous-versions/windows/hardware/drivers/ff597893(v=vs.85)) | Required.                                                                             |
| [WPD\_OBJECT\_ISHIDDEN](/previous-versions/windows/hardware/drivers/ff597893(v=vs.85))                                       | Required if the service object should not be shown to the user.                       |
| [WPD\_OBJECT\_ISSYSTEM](/previous-versions/windows/hardware/drivers/ff597893(v=vs.85))                                       | Required if the object is a system object (for example, it represents a system file). |
| [WPD\_FUNCTIONAL\_OBJECT\_CATEGORY](/previous-versions/windows/hardware/drivers/ff597893(v=vs.85))     | Required. This represents the Device Service type, such as SERVICE Contacts.          |
| [WPD\_SERVICE\_VERSION](/previous-versions/windows/hardware/drivers/ff597893(v=vs.85))                                       | Required.                                                                             |
| [WPD\_STORAGE\_TYPE](/previous-versions/windows/hardware/drivers/ff597893(v=vs.85))                                                | Required if the service is used to store objects.                                     |
| [WPD\_STORAGE\_CAPACITY](/previous-versions/windows/hardware/drivers/ff597865(v=vs.85))                                    | Required if the service is used to store objects.                                     |



 

## Typical Resources

These objects typically do not host resources.

## Typical Formats

The following list identifies typical formats used by the Service object. However, this object is not limited to these formats.

-   WPD\_OBJECT\_FORMAT\_UNSPECIFIED

## Related topics

<dl> <dt>

[**Requirements for Objects**](requirements-for-objects.md)
</dt> </dl>

 

 
