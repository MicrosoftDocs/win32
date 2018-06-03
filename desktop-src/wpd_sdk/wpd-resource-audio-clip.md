---
Description: Specifies an audio clip for the object.
ms.assetid: 24c15df0-4190-4c75-b89b-0c73d645c9ca
title: WPD\_RESOURCE\_AUDIO\_CLIP
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_RESOURCE\_AUDIO\_CLIP

Specifies an audio clip for the object.

This type of resource must support the following attributes.



| Attribute Name                                                                                                            | Required or Optional                                   |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| [WPD\_AUDIO\_BITRATE](https://www.bing.com/search?q=WPD\_AUDIO\_BITRATE)                                                             | Recommended.                                           |
| [WPD\_AUDIO\_CHANNEL\_COUNT](https://www.bing.com/search?q=WPD\_AUDIO\_CHANNEL\_COUNT)                                                | Optional.                                              |
| [WPD\_AUDIO\_FORMAT\_CODE](https://www.bing.com/search?q=WPD\_AUDIO\_FORMAT\_CODE)                                                    | Optional.                                              |
| [WPD\_AUDIO\_BIT\_DEPTH](https://www.bing.com/search?q=WPD\_AUDIO\_BIT\_DEPTH)                                                        | Optional.                                              |
| [WPD\_AUDIO\_BLOCK\_ALIGNMENT](https://www.bing.com/search?q=WPD\_AUDIO\_BLOCK\_ALIGNMENT)                                            | Optional.                                              |
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

 

 



