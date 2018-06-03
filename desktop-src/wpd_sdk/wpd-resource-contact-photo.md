---
Description: Specifies an image that represents a photo of the individual referred to in the contact object.
ms.assetid: e26487d8-cd21-4d4a-ba68-ae915eff1304
title: WPD\_RESOURCE\_CONTACT\_PHOTO
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_RESOURCE\_CONTACT\_PHOTO

Specifies an image that represents a photo of the individual referred to in the contact object.

This type of resource must support the following attributes.



| Attribute Name                                                                                                            | Required or Optional                                   |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| [WPD\_MEDIA\_WIDTH](https://www.bing.com/search?q=WPD\_MEDIA\_WIDTH)                                                                 | Required.                                              |
| [WPD\_MEDIA\_HEIGHT](https://www.bing.com/search?q=WPD\_MEDIA\_HEIGHT)                                                               | Required.                                              |
| [WPD\_RESOURCE\_ATTRIBUTE\_TOTAL\_SIZE](https://www.bing.com/search?q=WPD\_RESOURCE\_ATTRIBUTE\_TOTAL\_SIZE)              | Required.                                              |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_READ](https://www.bing.com/search?q=WPD\_RESOURCE\_ATTRIBUTE\_CAN\_READ)                                     | Required if clients can read this resource.            |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_WRITE](https://www.bing.com/search?q=WPD\_RESOURCE\_ATTRIBUTE\_CAN\_WRITE)                                   | Required if clients can write to this resource.        |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_DELETE](https://www.bing.com/search?q=WPD\_RESOURCE\_ATTRIBUTE\_CAN\_DELETE)                                 | Required if clients can delete this resource.          |
| [WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_READ\_BUFFER\_SIZE](https://www.bing.com/search?q=WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_READ\_BUFFER\_SIZE)   | Required if clients have read access to the resource.  |
| [WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_WRITE\_BUFFER\_SIZE](https://www.bing.com/search?q=WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_WRITE\_BUFFER\_SIZE) | Required if clients have write access to the resource. |
| [WPD\_RESOURCE\_ATTRIBUTE\_FORMAT](https://www.bing.com/search?q=WPD\_RESOURCE\_ATTRIBUTE\_FORMAT)                       | Required.                                              |
| [WPD\_RESOURCE\_ATTRIBUTE\_RESOURCE\_KEY](resource-attribute-properties.md)                                              | Recommended.                                           |



 

## See also

<dl> <dt>

[**Requirements for Resources**](requirements-for-resources.md)
</dt> </dl>

 

 



