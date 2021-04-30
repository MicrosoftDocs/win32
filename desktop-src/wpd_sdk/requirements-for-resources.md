---
description: Requirements for Resources
ms.assetid: 6b654cd6-7e9f-4e12-a687-4110e600ba7b
title: Requirements for Resources
ms.topic: article
ms.date: 05/31/2018
---

# Requirements for Resources

Windows Portable Devices defines the following resource categories as **PROPERTYKEY** values. These values are used to describe individual resources in an object. The *pid* member of the property key can be different to describe different resources of the same type for all types except **WPD\_RESOURCE\_DEFAULT**, which can only describe one resource. The linked description page for each resource type lists the attributes supported by that resource.



| Resource PROPERTYKEY                                                | Description                                                                                                    |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**WPD\_RESOURCE\_DEFAULT**](wpd-resource-default.md)              | Specifies the whole file behind the object. This is the only required resource for any object with a resource. |
| [**WPD\_RESOURCE\_ALBUM\_ART**](wpd-resource-album-art.md)         | Specifies an image that represents the album artwork for the object.                                           |
| [**WPD\_RESOURCE\_AUDIO\_CLIP**](wpd-resource-audio-clip.md)       | Specifies an audio clip for the object.                                                                        |
| [**WPD\_RESOURCE\_CONTACT\_PHOTO**](wpd-resource-contact-photo.md) | Specifies an image that represents a photo of the individual referred to in the contact object.                |
| [**WPD\_RESOURCE\_GENERIC**](wpd-resource-generic.md)              | A generic resource of undefined data type. This should be treated as a byte array.                             |
| [**WPD\_RESOURCE\_ICON**](wpd-resource-icon.md)                    | An icon.                                                                                                       |
| [**WPD\_RESOURCE\_THUMBNAIL**](wpd-resource-thumbnail.md)          | A thumbnail image.                                                                                             |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 



