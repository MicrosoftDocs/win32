---
description: WPD\_CONTENT\_TYPE\_IMAGE
ms.assetid: 87342ac7-3f4d-4ed2-99f1-843a79032c6e
title: WPD_CONTENT_TYPE_IMAGE
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_CONTENT\_TYPE\_IMAGE

An object that describes its type as WPD\_CONTENT\_TYPE\_IMAGE represents a still image.

This type of object supports the following properties.



| Property Name                                                                                                         | Required or Optional                                                                             |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](object-properties.md)                                                                | Required, read-only. A client cannot set this property, even at creation time.                   |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md)                                                 | Required.                                                                                        |
| [WPD\_OBJECT\_NAME](object-properties.md)                                                            | Required if the object represents a file.                                                        |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md)                          | Required, read-only. A client cannot set this property, even at creation time.                   |
| [WPD\_OBJECT\_FORMAT](object-properties.md)                                                        | Required.                                                                                        |
| [WPD\_OBJECT\_CONTENT\_TYPE](object-properties.md)                                           | Required.                                                                                        |
| [WPD\_OBJECT\_ISHIDDEN](object-properties.md)                                                    | Required if the object is hidden.                                                                |
| [WPD\_OBJECT\_ISSYSTEM](object-properties.md)                                                    | Required if the object is a system object (represents a system file).                            |
| [WPD\_OBJECT\_SIZE](object-properties.md)                                                            | Required if the object has at least one resource.                                                |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](object-properties.md)                              | Required if the object represents a file.                                                        |
| [WPD\_OBJECT\_NON\_CONSUMABLE](object-properties.md)                                       | Recommended if the object is not meant for consumption by the device.                            |
| [WPD\_OBJECT\_REFERENCES](object-properties.md)                                                | Required if the object has references to other objects.                                          |
| [WPD\_OBJECT\_KEYWORDS](object-properties.md)                                                    | Optional.                                                                                        |
| [WPD\_OBJECT\_SYNC\_ID](object-properties.md)                                                     | Optional.                                                                                        |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](object-properties.md)                                  | Required if the object is protected by DRM technology.                                           |
| [WPD\_OBJECT\_DATE\_CREATED](object-properties.md)                                           | Optional.                                                                                        |
| [WPD\_OBJECT\_DATE\_MODIFIED](object-properties.md)                                         | Recommended.                                                                                     |
| [WPD\_OBJECT\_DATE\_AUTHORED](object-properties.md)                                         | Optional.                                                                                        |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                | Recommended if the object is referenced by another object.                                       |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](object-properties.md)     | Optional.                                                                                        |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](object-properties.md) | Optional.                                                                                        |
| [WPD\_IMAGE\_BITDEPTH](image-properties.md)                                                       | Recommended.                                                                                     |
| [WPD\_IMAGE\_CROPPED\_STATUS](image-properties.md)                                          | Optional.                                                                                        |
| [WPD\_IMAGE\_COLOR\_CORRECTED\_STATUS](image-properties.md)                         | Optional.                                                                                        |
| [WPD\_IMAGE\_FNUMBER](image-properties.md)                                                                           | Optional.                                                                                        |
| [WPD\_IMAGE\_EXPOSURE\_TIME](image-properties.md)                                                                    | Optional.                                                                                        |
| [WPD\_IMAGE\_EXPOSURE\_INDEX](image-properties.md)                                                                   | Optional.                                                                                        |
| [WPD\_IMAGE\_HORIZONTAL\_RESOLUTION](image-properties.md)                                                            | Optional.                                                                                        |
| [WPD\_IMAGE\_VERTICAL\_RESOLUTION](image-properties.md)                                                              | Optional.                                                                                        |
| [WPD\_MEDIA\_COPYRIGHT](media-properties.md)                                                     | Optional.                                                                                        |
| [WPD\_MEDIA\_WIDTH](media-properties.md)                                                             | Required.                                                                                        |
| [WPD\_MEDIA\_HEIGHT](media-properties.md)                                                           | Required.                                                                                        |
| [WPD\_MEDIA\_ARTIST](media-properties.md)                                                                            | Recommended.                                                                                     |
| [WPD\_MEDIA\_ALBUM\_ARTIST](media-properties.md)                                                                     | Recommended. This property identifies the person, or people, who originally created this object. |
| [WPD\_MEDIA\_SOURCE\_URL](media-properties.md)                                                                       | Optional.                                                                                        |
| [WPD\_MEDIA\_DESTINATION\_URL](media-properties.md)                                                                  | Optional.                                                                                        |
| [WPD\_MEDIA\_DESCRIPTION](media-properties.md)                                                                       | Optional.                                                                                        |
| [WPD\_MEDIA\_GENRE](media-properties.md)                                                                             | Optional.                                                                                        |
| [WPD\_MEDIA\_BYTE\_BOOKMARK](media-properties.md)                                                                    | Optional.                                                                                        |
| [WPD\_MEDIA\_GUID](media-properties.md)                                                                              | Optional.                                                                                        |
| [WPD\_MEDIA\_SUB\_DESCRIPTION](media-properties.md)                                                                  | Optional.                                                                                        |



 

## Typical Resources

These objects typically include the following resources.



| Resource Name                                                 | Required or Optional | Description                                                                              |
|---------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------|
| [**WPD\_RESOURCE\_DEFAULT**](wpd-resource-default.md)        | Required.            | Contains the image data.                                                                 |
| [**WPD\_RESOURCE\_THUMBNAIL**](wpd-resource-thumbnail.md)    | Recommended.         | Contains the thumbnail for the image.                                                    |
| [**WPD\_RESOURCE\_AUDIO\_CLIP**](wpd-resource-audio-clip.md) | Optional.            | If this image has an associated audio annotation, this resource contains the audio data. |



 

## Related topics

<dl> <dt>

[**Requirements for Objects**](requirements-for-objects.md)
</dt> </dl>

 

 



