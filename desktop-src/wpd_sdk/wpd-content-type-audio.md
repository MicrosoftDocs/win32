---
Description: WPD\_CONTENT\_TYPE\_AUDIO
ms.assetid: a3d84878-489b-489a-a67e-0e4d25ddd3f7
title: WPD\_CONTENT\_TYPE\_AUDIO
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_CONTENT\_TYPE\_AUDIO

An object that describes its type as WPD\_CONTENT\_TYPE\_AUDIO represents an audio file, such as a Windows Media Audio (WMA) or MP3 file.

This type of object supports the following properties.



| Property Name                                                                                                         | Required or Optional                                                               |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_ID)                                                                | Required, read-only. A client cannot set this property, even at creation time.     |
| [WPD\_OBJECT\_PARENT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PARENT\_ID)                                                 | Required.                                                                          |
| [WPD\_OBJECT\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_NAME)                                                            | Required if the object represents a file.                                          |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID)                          | Required, read-only. A client cannot set this property, even at creation time.     |
| [WPD\_OBJECT\_FORMAT](https://www.bing.com/search?q=WPD\_OBJECT\_FORMAT)                                                        | Required.                                                                          |
| [WPD\_OBJECT\_CONTENT\_TYPE](https://www.bing.com/search?q=WPD\_OBJECT\_CONTENT\_TYPE)                                           | Required.                                                                          |
| [WPD\_OBJECT\_ISHIDDEN](https://www.bing.com/search?q=WPD\_OBJECT\_ISHIDDEN)                                                    | Required if the object is hidden.                                                  |
| [WPD\_OBJECT\_ISSYSTEM](https://www.bing.com/search?q=WPD\_OBJECT\_ISSYSTEM)                                                    | Required if the object is a system object (represents a system file).              |
| [WPD\_OBJECT\_SIZE](https://www.bing.com/search?q=WPD\_OBJECT\_SIZE)                                                            | Required if the object has at least one resource.                                  |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_ORIGINAL\_FILE\_NAME)                              | Required if the object represents a file.                                          |
| [WPD\_OBJECT\_NON\_CONSUMABLE](https://www.bing.com/search?q=WPD\_OBJECT\_NON\_CONSUMABLE)                                       | Recommended if the object is not meant for consumption by the device.              |
| [WPD\_OBJECT\_REFERENCES](https://www.bing.com/search?q=WPD\_OBJECT\_REFERENCES)                                                | Required if the object has references to other objects.                            |
| [WPD\_OBJECT\_KEYWORDS](https://www.bing.com/search?q=WPD\_OBJECT\_KEYWORDS)                                                    | Optional.                                                                          |
| [WPD\_OBJECT\_SYNC\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_SYNC\_ID)                                                     | Optional.                                                                          |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](https://www.bing.com/search?q=WPD\_OBJECT\_IS\_DRM\_PROTECTED)                                  | Required if the object is protected by DRM technology.                             |
| [WPD\_OBJECT\_DATE\_CREATED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_CREATED)                                           | Optional.                                                                          |
| [WPD\_OBJECT\_DATE\_MODIFIED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_MODIFIED)                                         | Recommended.                                                                       |
| [WPD\_OBJECT\_DATE\_AUTHORED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_AUTHORED)                                         | Optional.                                                                          |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                | Recommended if the object is referenced by another object.                         |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID)     | Optional.                                                                          |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](https://www.bing.com/search?q=WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE) | Optional.                                                                          |
| [WPD\_OBJECT\_CAN\_DELETE](object-properties.md)                                                                     | Required if the object can be deleted.                                             |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                | Optional.                                                                          |
| [WPD\_MEDIA\_TOTAL\_BITRATE](https://www.bing.com/search?q=WPD\_MEDIA\_TOTAL\_BITRATE)                                            | Recommended.                                                                       |
| [WPD\_MEDIA\_BITRATE\_TYPE](https://www.bing.com/search?q=WPD\_MEDIA\_BITRATE\_TYPE)                                              | Optional.                                                                          |
| [WPD\_MEDIA\_COPYRIGHT](https://www.bing.com/search?q=WPD\_MEDIA\_COPYRIGHT)                                                     | Optional.                                                                          |
| [WPD\_MEDIA\_SUBSCRIPTION\_CONTENT\_ID](https://www.bing.com/search?q=WPD\_MEDIA\_SUBSCRIPTION\_CONTENT\_ID)                       | Recommended if this object represents content from an online subscription service. |
| [WPD\_MEDIA\_USE\_COUNT](https://www.bing.com/search?q=WPD\_MEDIA\_USE\_COUNT)                                                    | Recommended.                                                                       |
| [WPD\_MEDIA\_SKIP\_COUNT](https://www.bing.com/search?q=WPD\_MEDIA\_SKIP\_COUNT)                                                  | Optional.                                                                          |
| [WPD\_MEDIA\_LAST\_ACCESSED\_TIME](https://www.bing.com/search?q=WPD\_MEDIA\_LAST\_ACCESSED\_TIME)                                 | Optional.                                                                          |
| [WPD\_MEDIA\_PARENTAL\_RATING](https://www.bing.com/search?q=WPD\_MEDIA\_PARENTAL\_RATING)                                        | Optional.                                                                          |
| [WPD\_MEDIA\_META\_GENRE](https://www.bing.com/search?q=WPD\_MEDIA\_META\_GENRE)                                                  | Optional.                                                                          |
| [WPD\_MEDIA\_COMPOSER](https://www.bing.com/search?q=WPD\_MEDIA\_COMPOSER)                                                       | Optional.                                                                          |
| [WPD\_MEDIA\_EFFECTIVE\_RATING](https://www.bing.com/search?q=WPD\_MEDIA\_EFFECTIVE\_RATING)                                      | Optional.                                                                          |
| [WPD\_MEDIA\_SUB\_TITLE](https://www.bing.com/search?q=WPD\_MEDIA\_SUB\_TITLE)                                                    | Optional.                                                                          |
| [WPD\_MEDIA\_RELEASE\_DATE](https://www.bing.com/search?q=WPD\_MEDIA\_RELEASE\_DATE)                                              | Recommended.                                                                       |
| [WPD\_MEDIA\_SAMPLE\_RATE](https://www.bing.com/search?q=WPD\_MEDIA\_SAMPLE\_RATE)                                                | Optional.                                                                          |
| [WPD\_MEDIA\_STAR\_RATING](https://www.bing.com/search?q=WPD\_MEDIA\_STAR\_RATING)                                                | Recommended.                                                                       |
| [WPD\_MEDIA\_USER\_EFFECTIVE\_RATING](https://www.bing.com/search?q=WPD\_MEDIA\_USER\_EFFECTIVE\_RATING)                           | Recommended.                                                                       |
| [WPD\_MEDIA\_TITLE](https://www.bing.com/search?q=WPD\_MEDIA\_TITLE)                                                             | Required.                                                                          |
| [WPD\_MEDIA\_DURATION](https://www.bing.com/search?q=WPD\_MEDIA\_DURATION)                                                       | Required.                                                                          |
| [WPD\_MEDIA\_BUY\_NOW](https://www.bing.com/search?q=WPD\_MEDIA\_BUY\_NOW)                                                        | Recommended.                                                                       |
| [WPD\_MEDIA\_ENCODING\_PROFILE](https://www.bing.com/search?q=WPD\_MEDIA\_ENCODING\_PROFILE)                                      | Optional.                                                                          |
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
| [WPD\_MUSIC\_ALBUM](https://www.bing.com/search?q=WPD\_MUSIC\_ALBUM)                                                             | Recommended.                                                                       |
| [WPD\_MUSIC\_TRACK](https://www.bing.com/search?q=WPD\_MUSIC\_TRACK)                                                             | Recommended.                                                                       |
| [WPD\_MUSIC\_LYRICS](https://www.bing.com/search?q=WPD\_MUSIC\_LYRICS)                                                           | Optional.                                                                          |
| [WPD\_MUSIC\_MOOD](https://www.bing.com/search?q=WPD\_MUSIC\_MOOD)                                                               | Optional.                                                                          |
| [WPD\_AUDIO\_BITRATE](https://www.bing.com/search?q=WPD\_AUDIO\_BITRATE)                                                         | Recommended.                                                                       |
| [WPD\_AUDIO\_CHANNEL\_COUNT](https://www.bing.com/search?q=WPD\_AUDIO\_CHANNEL\_COUNT)                                            | Optional.                                                                          |
| [WPD\_AUDIO\_FORMAT\_CODE](https://www.bing.com/search?q=WPD\_AUDIO\_FORMAT\_CODE)                                                | Optional.                                                                          |
| [WPD\_AUDIO\_BIT\_DEPTH](https://www.bing.com/search?q=WPD\_AUDIO\_BIT\_DEPTH)                                                    | Optional.                                                                          |
| [WPD\_AUDIO\_BLOCK\_ALIGNMENT](https://www.bing.com/search?q=WPD\_AUDIO\_BLOCK\_ALIGNMENT)                                        | Optional.                                                                          |



 

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

 

 



