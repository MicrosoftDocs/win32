---
description: Specifies a small picture&\#8212;typically a smaller version of a larger picture in the object.
ms.assetid: ad1eac9d-b182-49b2-bd2c-2d76e2026d80
title: WPD_RESOURCE_THUMBNAIL
ms.topic: reference
ms.date: 05/31/2018
---

# WPD\_RESOURCE\_THUMBNAIL

Specifies a small picture—typically a smaller version of a larger picture in the object.

This type of resource must support the following attributes.



| Attribute Name                                                                                                            | Required or Optional                                   |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| [WPD\_MEDIA\_WIDTH](media-properties.md)                                                                 | Required.                                              |
| [WPD\_MEDIA\_HEIGHT](media-properties.md)                                                               | Required.                                              |
| [WPD\_RESOURCE\_ATTRIBUTE\_TOTAL\_SIZE](resource-attribute-properties.md)              | Required.                                              |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_READ](attributes.md)                                     | Required if clients can read this resource.            |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_WRITE](attributes.md)                                   | Required if clients can write to this resource.        |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_DELETE](attributes.md)                                 | Required if clients can delete this resource.          |
| [WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_READ\_BUFFER\_SIZE](attributes.md)   | Required if clients have read access to the resource.  |
| [WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_WRITE\_BUFFER\_SIZE](attributes.md) | Required if clients have write access to the resource. |
| [WPD\_RESOURCE\_ATTRIBUTE\_FORMAT](resource-attribute-properties.md)                       | Required.                                              |
| [WPD\_RESOURCE\_ATTRIBUTE\_RESOURCE\_KEY](resource-attribute-properties.md)                                              | Recommended.                                           |



 

## See also

<dl> <dt>

[**Requirements for Resources**](requirements-for-resources.md)
</dt> </dl>

 

 



