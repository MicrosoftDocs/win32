---
description: Specifies an audio clip for the object.
ms.assetid: 24c15df0-4190-4c75-b89b-0c73d645c9ca
title: WPD_RESOURCE_AUDIO_CLIP
ms.topic: reference
ms.date: 05/31/2018
---

# WPD\_RESOURCE\_AUDIO\_CLIP

Specifies an audio clip for the object.

This type of resource must support the following attributes.



| Attribute Name                                                                                                            | Required or Optional                                   |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| [WPD\_AUDIO\_BITRATE](audio-properties.md)                                                             | Recommended.                                           |
| [WPD\_AUDIO\_CHANNEL\_COUNT](audio-properties.md)                                                | Optional.                                              |
| [WPD\_AUDIO\_FORMAT\_CODE](audio-properties.md)                                                    | Optional.                                              |
| [WPD\_AUDIO\_BIT\_DEPTH](audio-properties.md)                                                        | Optional.                                              |
| [WPD\_AUDIO\_BLOCK\_ALIGNMENT](audio-properties.md)                                            | Optional.                                              |
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

 

 



