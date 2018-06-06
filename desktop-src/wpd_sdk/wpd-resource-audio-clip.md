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
| [WPD\_AUDIO\_BITRATE](audio-properties.md#wpd-audio-bitrate)                                                             | Recommended.                                           |
| [WPD\_AUDIO\_CHANNEL\_COUNT](audio-properties.md#wpd-audio-channel-count)                                                | Optional.                                              |
| [WPD\_AUDIO\_FORMAT\_CODE](audio-properties.md#wpd-audio-format-code)                                                    | Optional.                                              |
| [WPD\_AUDIO\_BIT\_DEPTH](audio-properties.md#wpd-audio-bit-depth)                                                        | Optional.                                              |
| [WPD\_AUDIO\_BLOCK\_ALIGNMENT](audio-properties.md#wpd-audio-block-alignment)                                            | Optional.                                              |
| [WPD\_RESOURCE\_ATTRIBUTE\_TOTAL\_SIZE](resource-attribute-properties.md#wpd-resource-attribute-total-size)              | Required.                                              |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_READ](attributes.md#wpd-resource-attribute-can-read)                                     | Required if clients can read this resource.            |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_WRITE](attributes.md#wpd-resource-attribute-can-write)                                   | Required if clients can write to this resource.        |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_DELETE](attributes.md#wpd-resource-attribute-can-delete)                                 | Required if clients can delete this resource.          |
| [WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_READ\_BUFFER\_SIZE](attributes.md#wpd-resource-attribute-optimal-read-buffer-size)   | Required if clients have read access to the resource.  |
| [WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_WRITE\_BUFFER\_SIZE](attributes.md#wpd-resource-attribute-optimal-write-buffer-size) | Required if clients have write access to the resource. |
| [WPD\_RESOURCE\_ATTRIBUTE\_FORMAT](resource-attribute-properties.md#wpd-resource-attribute-format)                       | Required.                                              |
| [WPD\_RESOURCE\_ATTRIBUTE\_RESOURCE\_KEY](resource-attribute-properties.md)                                              | Recommended.                                           |



 

## See also

<dl> <dt>

[**Requirements for Resources**](requirements-for-resources.md)
</dt> </dl>

 

 



