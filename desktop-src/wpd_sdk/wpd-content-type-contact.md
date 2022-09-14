---
description: WPD\_CONTENT\_TYPE\_CONTACT
ms.assetid: 3ff6191f-d3c0-4bd3-946e-c3fbf68f368c
title: WPD_CONTENT_TYPE_CONTACT
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_CONTENT\_TYPE\_CONTACT

An object that describes its type as WPD\_CONTENT\_TYPE\_CONTACT represents personal contact data.

This type of object supports the following properties.



| Property Name                                                                                                                   | Required or Optional                                                           |
|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](object-properties.md)                                                                          | Required, read-only. A client cannot set this property, even at creation time. |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md)                                                           | Required.                                                                      |
| [WPD\_OBJECT\_NAME](object-properties.md)                                                                      | Required if the object represents a file.                                      |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md)                                    | Required, read-only. A client cannot set this property, even at creation time. |
| [WPD\_OBJECT\_FORMAT](object-properties.md)                                                                  | Required.                                                                      |
| [WPD\_OBJECT\_CONTENT\_TYPE](object-properties.md)                                                     | Required.                                                                      |
| [WPD\_OBJECT\_ISHIDDEN](object-properties.md)                                                              | Required if the object is hidden.                                              |
| [WPD\_OBJECT\_ISSYSTEM](object-properties.md)                                                              | Required if the object is a system object (represents a system file).          |
| [WPD\_OBJECT\_SIZE](object-properties.md)                                                                      | Required if the object has at least one resource.                              |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](object-properties.md)                                        | Required if the object represents a file.                                      |
| [WPD\_OBJECT\_NON\_CONSUMABLE](object-properties.md)                                                 | Recommended if the object is not meant for consumption by the device.          |
| [WPD\_OBJECT\_REFERENCES](object-properties.md)                                                          | Required if the object has references to other objects.                        |
| [WPD\_OBJECT\_KEYWORDS](object-properties.md)                                                              | Optional.                                                                      |
| [WPD\_OBJECT\_SYNC\_ID](object-properties.md)                                                               | Optional.                                                                      |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](object-properties.md)                                            | Required if the object is protected by DRM technology.                         |
| [WPD\_OBJECT\_DATE\_CREATED](object-properties.md)                                                     | Optional.                                                                      |
| [WPD\_OBJECT\_DATE\_MODIFIED](object-properties.md)                                                   | Recommended.                                                                   |
| [WPD\_OBJECT\_DATE\_AUTHORED](object-properties.md)                                                   | Optional.                                                                      |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                          | Recommended if the object is referenced by another object.                     |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](object-properties.md)               | Optional.                                                                      |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](object-properties.md)           | Optional.                                                                      |
| [WPD\_CONTACT\_DISPLAY\_NAME](contact-properties.md)                                                  | Required.                                                                      |
| [WPD\_OBJECT\_CAN\_DELETE](object-properties.md)                                                                               | Required if the object cannot be deleted.                                      |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                          | Optional.                                                                      |
| [WPD\_CONTACT\_DISPLAY\_NAME](contact-properties.md)                                                                           | Required.                                                                      |
| [WPD\_CONTACT\_FIRST\_NAME](contact-properties.md)                                                      | Recommended.                                                                   |
| [WPD\_CONTACT\_MIDDLE\_NAMES](contact-properties.md)                                                  | Recommended.                                                                   |
| [WPD\_CONTACT\_LAST\_NAME](contact-properties.md)                                                        | Recommended.                                                                   |
| [WPD\_CONTACT\_PREFIX](contact-properties.md)                                                               | Recommended.                                                                   |
| [WPD\_CONTACT\_SUFFIX](contact-properties.md)                                                               | Recommended.                                                                   |
| [WPD\_CONTACT\_PHONETIC\_FIRST\_NAME](contact-properties.md)                                   | Optional.                                                                      |
| [WPD\_CONTACT\_PHONETIC\_LAST\_NAME](contact-properties.md)                                     | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_FULL\_POSTAL\_ADDRESS](contact-properties.md)                | Recommended.                                                                   |
| [WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_LINE1](contact-properties.md)              | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_LINE2](contact-properties.md)              | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_CITY](contact-properties.md)                | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_REGION](contact-properties.md)            | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_POSTAL\_CODE](contact-properties.md) | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_COUNTRY](contact-properties.md)          | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_FULL\_POSTAL\_ADDRESS](contact-properties.md)                | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_LINE1](contact-properties.md)              | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_LINE2](contact-properties.md)              | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_CITY](contact-properties.md)                | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_REGION](contact-properties.md)            | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_POSTAL\_CODE](contact-properties.md) | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_COUNTRY](contact-properties.md)          | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_FULL\_POSTAL\_ADDRESS](contact-properties.md)                      | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_LINE1](contact-properties.md)                    | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_LINE2](contact-properties.md)                    | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_CITY](contact-properties.md)                      | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_REGION](contact-properties.md)                  | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_POSTAL\_CODE](contact-properties.md)       | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_POSTAL\_COUNTRY](contact-properties.md) | Optional.                                                                      |
| [WPD\_CONTACT\_PRIMARY\_EMAIL\_ADDRESS](contact-properties.md)                               | Recommended.                                                                   |
| [WPD\_CONTACT\_PERSONAL\_EMAIL](contact-properties.md)                                              | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_EMAIL2](contact-properties.md)                                            | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_EMAIL](contact-properties.md)                                              | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_EMAIL2](contact-properties.md)                                            | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_EMAILS](contact-properties.md)                                                  | Optional.                                                                      |
| [WPD\_CONTACT\_PRIMARY\_PHONE](contact-properties.md)                                                | Recommended.                                                                   |
| [WPD\_CONTACT\_PERSONAL\_PHONE](contact-properties.md)                                              | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_PHONE2](contact-properties.md)                                            | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_PHONE](contact-properties.md)                                              | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_PHONE2](contact-properties.md)                                            | Optional.                                                                      |
| [WPD\_CONTACT\_MOBILE\_PHONE](contact-properties.md)                                                  | Optional.                                                                      |
| [WPD\_CONTACT\_MOBILE\_PHONE2](contact-properties.md)                                                | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_FAX](contact-properties.md)                                                  | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_FAX](contact-properties.md)                                                  | Optional.                                                                      |
| [WPD\_CONTACT\_PAGER](contact-properties.md)                                                                 | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_PHONES](contact-properties.md)                                                  | Optional.                                                                      |
| [WPD\_CONTACT\_PRIMARY\_WEB\_ADDRESS](contact-properties.md)                                   | Recommended.                                                                   |
| [WPD\_CONTACT\_PERSONAL\_WEB\_ADDRESS](contact-properties.md)                                 | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_WEB\_ADDRESS](contact-properties.md)                                 | Optional.                                                                      |
| [WPD\_CONTACT\_INSTANT\_MESSENGER](contact-properties.md)                                        | Recommended                                                                    |
| [WPD\_CONTACT\_INSTANT\_MESSENGER2](contact-properties.md)                                      | Optional.                                                                      |
| [WPD\_CONTACT\_INSTANT\_MESSENGER3](contact-properties.md)                                      | Optional.                                                                      |
| [WPD\_CONTACT\_COMPANY\_NAME](contact-properties.md)                                                  | Optional.                                                                      |
| [WPD\_CONTACT\_PHONETIC\_COMPANY\_NAME](contact-properties.md)                               | Optional                                                                       |
| [WPD\_CONTACT\_ROLE](contact-properties.md)                                                                   | Optional.                                                                      |
| [WPD\_CONTACT\_BIRTHDATE](contact-properties.md)                                                         | Optional.                                                                      |
| [WPD\_CONTACT\_PRIMARY\_FAX](contact-properties.md)                                                                            | Optional.                                                                      |
| [WPD\_CONTACT\_SPOUSE](contact-properties.md)                                                                                  | Optional.                                                                      |
| [WPD\_CONTACT\_CHILDREN](contact-properties.md)                                                                                | Optional.                                                                      |
| [WPD\_CONTACT\_ASSISTANT](contact-properties.md)                                                                               | Optional.                                                                      |
| [WPD\_CONTACT\_ANNIVERSARY\_DATE](contact-properties.md)                                                                       | Optional.                                                                      |
| [WPD\_CONTACT\_RINGTONE](contact-properties.md)                                                                                | Optional.                                                                      |
| [WPD\_COMMON\_INFORMATION\_NOTES](object-properties.md)                                                                        | Optional.                                                                      |



 

## Typical Resources

These objects typically include the following resources.



| Resource Name                                                       | Required or Optional       | Description                        |
|---------------------------------------------------------------------|----------------------------|------------------------------------|
| [**WPD\_RESOURCE\_DEFAULT**](wpd-resource-default.md)              | Optional.                  | Contains the contact data.         |
| [**WPD\_RESOURCE\_CONTACT\_PHOTO**](wpd-resource-contact-photo.md) | Recommended, if available. | Contains a picture of the contact. |



 

## Related topics

<dl> <dt>

[**Requirements for Objects**](requirements-for-objects.md)
</dt> </dl>

 

 



