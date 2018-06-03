---
Description: WPD\_CONTENT\_TYPE\_CONTACT
ms.assetid: 3ff6191f-d3c0-4bd3-946e-c3fbf68f368c
title: WPD\_CONTENT\_TYPE\_CONTACT
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_CONTENT\_TYPE\_CONTACT

An object that describes its type as WPD\_CONTENT\_TYPE\_CONTACT represents personal contact data.

This type of object supports the following properties.



| Property Name                                                                                                                   | Required or Optional                                                           |
|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_ID)                                                                          | Required, read-only. A client cannot set this property, even at creation time. |
| [WPD\_OBJECT\_PARENT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PARENT\_ID)                                                           | Required.                                                                      |
| [WPD\_OBJECT\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_NAME)                                                                      | Required if the object represents a file.                                      |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID)                                    | Required, read-only. A client cannot set this property, even at creation time. |
| [WPD\_OBJECT\_FORMAT](https://www.bing.com/search?q=WPD\_OBJECT\_FORMAT)                                                                  | Required.                                                                      |
| [WPD\_OBJECT\_CONTENT\_TYPE](https://www.bing.com/search?q=WPD\_OBJECT\_CONTENT\_TYPE)                                                     | Required.                                                                      |
| [WPD\_OBJECT\_ISHIDDEN](https://www.bing.com/search?q=WPD\_OBJECT\_ISHIDDEN)                                                              | Required if the object is hidden.                                              |
| [WPD\_OBJECT\_ISSYSTEM](https://www.bing.com/search?q=WPD\_OBJECT\_ISSYSTEM)                                                              | Required if the object is a system object (represents a system file).          |
| [WPD\_OBJECT\_SIZE](https://www.bing.com/search?q=WPD\_OBJECT\_SIZE)                                                                      | Required if the object has at least one resource.                              |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_ORIGINAL\_FILE\_NAME)                                        | Required if the object represents a file.                                      |
| [WPD\_OBJECT\_NON\_CONSUMABLE](https://www.bing.com/search?q=WPD\_OBJECT\_NON\_CONSUMABLE)                                                 | Recommended if the object is not meant for consumption by the device.          |
| [WPD\_OBJECT\_REFERENCES](https://www.bing.com/search?q=WPD\_OBJECT\_REFERENCES)                                                          | Required if the object has references to other objects.                        |
| [WPD\_OBJECT\_KEYWORDS](https://www.bing.com/search?q=WPD\_OBJECT\_KEYWORDS)                                                              | Optional.                                                                      |
| [WPD\_OBJECT\_SYNC\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_SYNC\_ID)                                                               | Optional.                                                                      |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](https://www.bing.com/search?q=WPD\_OBJECT\_IS\_DRM\_PROTECTED)                                            | Required if the object is protected by DRM technology.                         |
| [WPD\_OBJECT\_DATE\_CREATED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_CREATED)                                                     | Optional.                                                                      |
| [WPD\_OBJECT\_DATE\_MODIFIED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_MODIFIED)                                                   | Recommended.                                                                   |
| [WPD\_OBJECT\_DATE\_AUTHORED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_AUTHORED)                                                   | Optional.                                                                      |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                          | Recommended if the object is referenced by another object.                     |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID)               | Optional.                                                                      |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](https://www.bing.com/search?q=WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE)           | Optional.                                                                      |
| [WPD\_CONTACT\_DISPLAY\_NAME](https://www.bing.com/search?q=WPD\_CONTACT\_DISPLAY\_NAME)                                                  | Required.                                                                      |
| [WPD\_OBJECT\_CAN\_DELETE](object-properties.md)                                                                               | Required if the object cannot be deleted.                                      |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                          | Optional.                                                                      |
| [WPD\_CONTACT\_DISPLAY\_NAME](contact-properties.md)                                                                           | Required.                                                                      |
| [WPD\_CONTACT\_FIRST\_NAME](https://www.bing.com/search?q=WPD\_CONTACT\_FIRST\_NAME)                                                      | Recommended.                                                                   |
| [WPD\_CONTACT\_MIDDLE\_NAMES](https://www.bing.com/search?q=WPD\_CONTACT\_MIDDLE\_NAMES)                                                  | Recommended.                                                                   |
| [WPD\_CONTACT\_LAST\_NAME](https://www.bing.com/search?q=WPD\_CONTACT\_LAST\_NAME)                                                        | Recommended.                                                                   |
| [WPD\_CONTACT\_PREFIX](https://www.bing.com/search?q=WPD\_CONTACT\_PREFIX)                                                               | Recommended.                                                                   |
| [WPD\_CONTACT\_SUFFIX](https://www.bing.com/search?q=WPD\_CONTACT\_SUFFIX)                                                               | Recommended.                                                                   |
| [WPD\_CONTACT\_PHONETIC\_FIRST\_NAME](https://www.bing.com/search?q=WPD\_CONTACT\_PHONETIC\_FIRST\_NAME)                                   | Optional.                                                                      |
| [WPD\_CONTACT\_PHONETIC\_LAST\_NAME](https://www.bing.com/search?q=WPD\_CONTACT\_PHONETIC\_LAST\_NAME)                                     | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_FULL\_POSTAL\_ADDRESS](https://www.bing.com/search?q=WPD\_CONTACT\_PERSONAL\_FULL\_POSTAL\_ADDRESS)                | Recommended.                                                                   |
| [WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_LINE1](https://www.bing.com/search?q=WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_LINE1)              | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_LINE2](https://www.bing.com/search?q=WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_LINE2)              | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_CITY](https://www.bing.com/search?q=WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_CITY)                | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_REGION](https://www.bing.com/search?q=WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_REGION)            | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_POSTAL\_CODE](https://www.bing.com/search?q=WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_POSTAL\_CODE) | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_COUNTRY](https://www.bing.com/search?q=WPD\_CONTACT\_PERSONAL\_POSTAL\_ADDRESS\_COUNTRY)          | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_FULL\_POSTAL\_ADDRESS](https://www.bing.com/search?q=WPD\_CONTACT\_BUSINESS\_FULL\_POSTAL\_ADDRESS)                | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_LINE1](https://www.bing.com/search?q=WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_LINE1)              | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_LINE2](https://www.bing.com/search?q=WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_LINE2)              | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_CITY](https://www.bing.com/search?q=WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_CITY)                | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_REGION](https://www.bing.com/search?q=WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_REGION)            | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_POSTAL\_CODE](https://www.bing.com/search?q=WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_POSTAL\_CODE) | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_COUNTRY](https://www.bing.com/search?q=WPD\_CONTACT\_BUSINESS\_POSTAL\_ADDRESS\_COUNTRY)          | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_FULL\_POSTAL\_ADDRESS](https://www.bing.com/search?q=WPD\_CONTACT\_OTHER\_FULL\_POSTAL\_ADDRESS)                      | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_LINE1](https://www.bing.com/search?q=WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_LINE1)                    | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_LINE2](https://www.bing.com/search?q=WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_LINE2)                    | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_CITY](https://www.bing.com/search?q=WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_CITY)                      | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_REGION](https://www.bing.com/search?q=WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_REGION)                  | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_POSTAL\_CODE](https://www.bing.com/search?q=WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_POSTAL\_CODE)       | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_POSTAL\_COUNTRY](https://www.bing.com/search?q=WPD\_CONTACT\_OTHER\_POSTAL\_ADDRESS\_POSTAL\_COUNTRY) | Optional.                                                                      |
| [WPD\_CONTACT\_PRIMARY\_EMAIL\_ADDRESS](https://www.bing.com/search?q=WPD\_CONTACT\_PRIMARY\_EMAIL\_ADDRESS)                               | Recommended.                                                                   |
| [WPD\_CONTACT\_PERSONAL\_EMAIL](https://www.bing.com/search?q=WPD\_CONTACT\_PERSONAL\_EMAIL)                                              | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_EMAIL2](https://www.bing.com/search?q=WPD\_CONTACT\_PERSONAL\_EMAIL2)                                            | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_EMAIL](https://www.bing.com/search?q=WPD\_CONTACT\_BUSINESS\_EMAIL)                                              | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_EMAIL2](https://www.bing.com/search?q=WPD\_CONTACT\_BUSINESS\_EMAIL2)                                            | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_EMAILS](https://www.bing.com/search?q=WPD\_CONTACT\_OTHER\_EMAILS)                                                  | Optional.                                                                      |
| [WPD\_CONTACT\_PRIMARY\_PHONE](https://www.bing.com/search?q=WPD\_CONTACT\_PRIMARY\_PHONE)                                                | Recommended.                                                                   |
| [WPD\_CONTACT\_PERSONAL\_PHONE](https://www.bing.com/search?q=WPD\_CONTACT\_PERSONAL\_PHONE)                                              | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_PHONE2](https://www.bing.com/search?q=WPD\_CONTACT\_PERSONAL\_PHONE2)                                            | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_PHONE](https://www.bing.com/search?q=WPD\_CONTACT\_BUSINESS\_PHONE)                                              | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_PHONE2](https://www.bing.com/search?q=WPD\_CONTACT\_BUSINESS\_PHONE2)                                            | Optional.                                                                      |
| [WPD\_CONTACT\_MOBILE\_PHONE](https://www.bing.com/search?q=WPD\_CONTACT\_MOBILE\_PHONE)                                                  | Optional.                                                                      |
| [WPD\_CONTACT\_MOBILE\_PHONE2](https://www.bing.com/search?q=WPD\_CONTACT\_MOBILE\_PHONE2)                                                | Optional.                                                                      |
| [WPD\_CONTACT\_PERSONAL\_FAX](https://www.bing.com/search?q=WPD\_CONTACT\_PERSONAL\_FAX)                                                  | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_FAX](https://www.bing.com/search?q=WPD\_CONTACT\_BUSINESS\_FAX)                                                  | Optional.                                                                      |
| [WPD\_CONTACT\_PAGER](https://www.bing.com/search?q=WPD\_CONTACT\_PAGER)                                                                 | Optional.                                                                      |
| [WPD\_CONTACT\_OTHER\_PHONES](https://www.bing.com/search?q=WPD\_CONTACT\_OTHER\_PHONES)                                                  | Optional.                                                                      |
| [WPD\_CONTACT\_PRIMARY\_WEB\_ADDRESS](https://www.bing.com/search?q=WPD\_CONTACT\_PRIMARY\_WEB\_ADDRESS)                                   | Recommended.                                                                   |
| [WPD\_CONTACT\_PERSONAL\_WEB\_ADDRESS](https://www.bing.com/search?q=WPD\_CONTACT\_PERSONAL\_WEB\_ADDRESS)                                 | Optional.                                                                      |
| [WPD\_CONTACT\_BUSINESS\_WEB\_ADDRESS](https://www.bing.com/search?q=WPD\_CONTACT\_BUSINESS\_WEB\_ADDRESS)                                 | Optional.                                                                      |
| [WPD\_CONTACT\_INSTANT\_MESSENGER](https://www.bing.com/search?q=WPD\_CONTACT\_INSTANT\_MESSENGER)                                        | Recommended                                                                    |
| [WPD\_CONTACT\_INSTANT\_MESSENGER2](https://www.bing.com/search?q=WPD\_CONTACT\_INSTANT\_MESSENGER2)                                      | Optional.                                                                      |
| [WPD\_CONTACT\_INSTANT\_MESSENGER3](https://www.bing.com/search?q=WPD\_CONTACT\_INSTANT\_MESSENGER3)                                      | Optional.                                                                      |
| [WPD\_CONTACT\_COMPANY\_NAME](https://www.bing.com/search?q=WPD\_CONTACT\_COMPANY\_NAME)                                                  | Optional.                                                                      |
| [WPD\_CONTACT\_PHONETIC\_COMPANY\_NAME](https://www.bing.com/search?q=WPD\_CONTACT\_PHONETIC\_COMPANY\_NAME)                               | Optional                                                                       |
| [WPD\_CONTACT\_ROLE](https://www.bing.com/search?q=WPD\_CONTACT\_ROLE)                                                                   | Optional.                                                                      |
| [WPD\_CONTACT\_BIRTHDATE](https://www.bing.com/search?q=WPD\_CONTACT\_BIRTHDATE)                                                         | Optional.                                                                      |
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

 

 



