---
description: WPD\_CONTENT\_TYPE\_AUDIO
ms.assetid: a3d84878-489b-489a-a67e-0e4d25ddd3f7
title: WPD_CONTENT_TYPE_AUDIO
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_CONTENT\_TYPE\_AUDIO

An object that describes its type as WPD\_CONTENT\_TYPE\_AUDIO represents an audio file, such as a Windows Media Audio (WMA) or MP3 file.

This type of object supports the following properties.



| Property Name                                                                                                         | Required or Optional                                                               |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](object-properties.md)                                                                | Required, read-only. A client cannot set this property, even at creation time.     |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md)                                                 | Required.                                                                          |
| [WPD\_OBJECT\_NAME](object-properties.md)                                                            | Required if the object represents a file.                                          |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md)                          | Required, read-only. A client cannot set this property, even at creation time.     |
| [WPD\_OBJECT\_FORMAT](object-properties.md)                                                        | Required.                                                                          |
| [WPD\_OBJECT\_CONTENT\_TYPE](object-properties.md)                                           | Required.                                                                          |
| [WPD\_OBJECT\_ISHIDDEN](object-properties.md)                                                    | Required if the object is hidden.                                                  |
| [WPD\_OBJECT\_ISSYSTEM](object-properties.md)                                                    | Required if the object is a system object (represents a system file).              |
| [WPD\_OBJECT\_SIZE](object-properties.md)                                                            | Required if the object has at least one resource.                                  |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](object-properties.md)                              | Required if the object represents a file.                                          |
| [WPD\_OBJECT\_NON\_CONSUMABLE](object-properties.md)                                       | Recommended if the object is not meant for consumption by the device.              |
| [WPD\_OBJECT\_REFERENCES](object-properties.md)                                                | Required if the object has references to other objects.                            |
| [WPD\_OBJECT\_KEYWORDS](object-properties.md)                                                    | Optional.                                                                          |
| [WPD\_OBJECT\_SYNC\_ID](object-properties.md)                                                     | Optional.                                                                          |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](object-properties.md)                                  | Required if the object is protected by DRM technology.                             |
| [WPD\_OBJECT\_DATE\_CREATED](object-properties.md)                                           | Optional.                                                                          |
| [WPD\_OBJECT\_DATE\_MODIFIED](object-properties.md)                                         | Recommended.                                                                       |
| [WPD\_OBJECT\_DATE\_AUTHORED](object-properties.md)                                         | Optional.                                                                          |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                | Recommended if the object is referenced by another object.                         |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](object-properties.md)     | Optional.                                                                          |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](object-properties.md) | Optional.                                                                          |
| [WPD\_OBJECT\_CAN\_DELETE](object-properties.md)                                                                     | Required if the object can be deleted.                                             |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                | Optional.                                                                          |
| [WPD\_MEDIA\_TOTAL\_BITRATE](media-properties.md)                                            | Recommended.                                                                       |
| [WPD\_MEDIA\_BITRATE\_TYPE](media-properties.md)                                              | Optional.                                                                          |
| [WPD\_MEDIA\_COPYRIGHT](media-properties.md)                                                     | Optional.                                                                          |
| [WPD\_MEDIA\_SUBSCRIPTION\_CONTENT\_ID](media-properties.md)                       | Recommended if this object represents content from an online subscription service. |
| [WPD\_MEDIA\_USE\_COUNT](media-properties.md)                                                    | Recommended.                                                                       |
| [WPD\_MEDIA\_SKIP\_COUNT](media-properties.md)                                                  | Optional.                                                                          |
| [WPD\_MEDIA\_LAST\_ACCESSED\_TIME](media-properties.md)                                 | Optional.                                                                          |
| [WPD\_MEDIA\_PARENTAL\_RATING](media-properties.md)                                        | Optional.                                                                          |
| [WPD\_MEDIA\_META\_GENRE](media-properties.md)                                                  | Optional.                                                                          |
| [WPD\_MEDIA\_COMPOSER](media-properties.md)                                                       | Optional.                                                                          |
| [WPD\_MEDIA\_EFFECTIVE\_RATING](media-properties.md)                                      | Optional.                                                                          |
| [WPD\_MEDIA\_SUB\_TITLE](media-properties.md)                                                    | Optional.                                                                          |
| [WPD\_MEDIA\_RELEASE\_DATE](media-properties.md)                                              | Recommended.                                                                       |
| [WPD\_MEDIA\_SAMPLE\_RATE](media-properties.md)                                                | Optional.                                                                          |
| [WPD\_MEDIA\_STAR\_RATING](media-properties.md)                                                | Recommended.                                                                       |
| [WPD\_MEDIA\_USER\_EFFECTIVE\_RATING](media-properties.md)                           | Recommended.                                                                       |
| [WPD\_MEDIA\_TITLE](media-properties.md)                                                             | Required.                                                                          |
| [WPD\_MEDIA\_DURATION](media-properties.md)                                                       | Required.                                                                          |
| [WPD\_MEDIA\_BUY\_NOW](media-properties.md)                                                        | Recommended.                                                                       |
| [WPD\_MEDIA\_ENCODING\_PROFILE](media-properties.md)                                      | Optional.                                                                          |
| [WPD\_MEDIA\_ARTIST](media-properties.md)                                                                            | Recommended.                                                                       |
| [WPD\_MEDIA\_ALBUM\_ARTIST](media-properties.md)                                                                     | Recommended.                                                                       |
| [WPD\_MEDIA\_SOURCE\_URL](media-properties.md)                                                                       | Optional.                                                                          |
| [WPD\_MEDIA\_DESTINATION\_URL](media-properties.md)                                                                  | Optional.                                                                          |
| [WPD\_MEDIA\_DESCRIPTION](media-properties.md)                                                                       | Optional.                                                                          |
| [WPD\_MEDIA\_GENRE](media-properties.md)                                                                             | Optional.                                                                          |
| [WPD\_MEDIA\_TIME\_BOOKMARK](media-properties.md)                                                                    | Optional.                                                                          |
| [WPD\_MEDIA\_BYTE\_BOOKMARK](media-properties.md)                                                                    | Optional.                                                                          |
| [WPD\_MEDIA\_GUID](media-properties.md)                                                                              | Optional.                                                                          |
| [WPD\_MEDIA\_SUB\_DESCRIPTION](media-properties.md)                                                                  | Optional.                                                                          |
| [WPD\_MUSIC\_ALBUM](music-properties.md)                                                             | Recommended.                                                                       |
| [WPD\_MUSIC\_TRACK](music-properties.md)                                                             | Recommended.                                                                       |
| [WPD\_MUSIC\_LYRICS](music-properties.md)                                                           | Optional.                                                                          |
| [WPD\_MUSIC\_MOOD](music-properties.md)                                                               | Optional.                                                                          |
| [WPD\_AUDIO\_BITRATE](audio-properties.md)                                                         | Recommended.                                                                       |
| [WPD\_AUDIO\_CHANNEL\_COUNT](audio-properties.md)                                            | Optional.                                                                          |
| [WPD\_AUDIO\_FORMAT\_CODE](audio-properties.md)                                                | Optional.                                                                          |
| [WPD\_AUDIO\_BIT\_DEPTH](audio-properties.md)                                                    | Optional.                                                                          |
| [WPD\_AUDIO\_BLOCK\_ALIGNMENT](audio-properties.md)                                        | Optional.                                                                          |



 

## Typical Resources

These objects typically include the following resources.



| Resource Name                                               | Required or Optional       | Description                                        |
|-------------------------------------------------------------|----------------------------|----------------------------------------------------|
| [**WPD\_RESOURCE\_DEFAULT**](wpd-resource-default.md)      | Optional.                  | Contains the complete audio file.                  |
| [**WPD\_RESOURCE\_ALBUM\_ART**](wpd-resource-album-art.md) | Recommended, if available. | Contains the picture for the album.                |
| [**WPD\_RESOURCE\_AUDIOCLIP**](wpd-resource-audio-clip.md) | Optional.                  | Contains a sample clip of the complete audio file. |



 

## Related topics

<dl> <dt>

[**Requirements for Objects**](requirements-for-objects.md)
</dt> </dl>

 

 



