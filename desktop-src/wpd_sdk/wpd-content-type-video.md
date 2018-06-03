---
Description: WPD\_CONTENT\_TYPE\_VIDEO
ms.assetid: d4a6bd98-c28e-487b-95cc-2c73cd44e3b5
title: WPD\_CONTENT\_TYPE\_VIDEO
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_CONTENT\_TYPE\_VIDEO

An object that describes its type as WPD\_CONTENT\_TYPE\_VIDEO represents a video file.

This type of object supports the following properties.



|                                                                                                                       |                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **Property Name**                                                                                                     | **Required or Optional**                                                                                                     |
| [WPD\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_ID)                                                                | Required, read-only. A client cannot set this property, even at creation time.                                               |
| [WPD\_OBJECT\_PARENT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PARENT\_ID)                                                 | Required.                                                                                                                    |
| [WPD\_OBJECT\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_NAME)                                                            | Required if the object represents a file.                                                                                    |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID)                          | Required, read-only. A client cannot set this property, even at creation time.                                               |
| [WPD\_OBJECT\_FORMAT](https://www.bing.com/search?q=WPD\_OBJECT\_FORMAT)                                                        | Required.                                                                                                                    |
| [WPD\_OBJECT\_CONTENT\_TYPE](https://www.bing.com/search?q=WPD\_OBJECT\_CONTENT\_TYPE)                                           | Required.                                                                                                                    |
| [WPD\_OBJECT\_ISHIDDEN](https://www.bing.com/search?q=WPD\_OBJECT\_ISHIDDEN)                                                    | Required if the object is hidden.                                                                                            |
| [WPD\_OBJECT\_ISSYSTEM](https://www.bing.com/search?q=WPD\_OBJECT\_ISSYSTEM)                                                    | Required if the object is a system object (represents a system file).                                                        |
| [WPD\_OBJECT\_SIZE](https://www.bing.com/search?q=WPD\_OBJECT\_SIZE)                                                            | Required if the object has at least one resource.                                                                            |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_ORIGINAL\_FILE\_NAME)                              | Required if the object represents a file.                                                                                    |
| [WPD\_OBJECT\_NON\_CONSUMABLE](https://www.bing.com/search?q=WPD\_OBJECT\_NON\_CONSUMABLE)                                       | Recommended if the object is not meant for consumption by the device.                                                        |
| [WPD\_OBJECT\_REFERENCES](https://www.bing.com/search?q=WPD\_OBJECT\_REFERENCES)                                                | Required if the object has references to other objects.                                                                      |
| [WPD\_OBJECT\_KEYWORDS](https://www.bing.com/search?q=WPD\_OBJECT\_KEYWORDS)                                                    | Optional.                                                                                                                    |
| [WPD\_OBJECT\_SYNC\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_SYNC\_ID)                                                     | Optional.                                                                                                                    |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](https://www.bing.com/search?q=WPD\_OBJECT\_IS\_DRM\_PROTECTED)                                  | Required if the object is protected by DRM technology.                                                                       |
| [WPD\_OBJECT\_DATE\_CREATED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_CREATED)                                           | Optional.                                                                                                                    |
| [WPD\_OBJECT\_DATE\_MODIFIED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_MODIFIED)                                         | Recommended.                                                                                                                 |
| [WPD\_OBJECT\_DATE\_AUTHORED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_AUTHORED)                                         | Optional.                                                                                                                    |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                | Recommended if the object is referenced by another object.                                                                   |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID)     | Optional.                                                                                                                    |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](https://www.bing.com/search?q=WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE) | Optional.                                                                                                                    |
| [WPD\_OBJECT\_CAN\_DELETE](object-properties.md)                                                                     | Required if the object cannot be deleted.                                                                                    |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                | Optional.                                                                                                                    |
| [WPD\_MEDIA\_TOTAL\_BITRATE](https://www.bing.com/search?q=WPD\_MEDIA\_TOTAL\_BITRATE)                                            | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_BITRATE\_TYPE](https://www.bing.com/search?q=WPD\_MEDIA\_BITRATE\_TYPE)                                              | Optional.                                                                                                                    |
| [WPD\_MEDIA\_COPYRIGHT](https://www.bing.com/search?q=WPD\_MEDIA\_COPYRIGHT)                                                     | Optional.                                                                                                                    |
| [WPD\_MEDIA\_SUBSCRIPTION\_CONTENT\_ID](https://www.bing.com/search?q=WPD\_MEDIA\_SUBSCRIPTION\_CONTENT\_ID)                       | Recommended, if this object represents content from an online subscription service.                                          |
| [WPD\_MEDIA\_USE\_COUNT](https://www.bing.com/search?q=WPD\_MEDIA\_USE\_COUNT)                                                    | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_SKIP\_COUNT](https://www.bing.com/search?q=WPD\_MEDIA\_SKIP\_COUNT)                                                  | Optional.                                                                                                                    |
| [WPD\_MEDIA\_LAST\_ACCESSED\_TIME](https://www.bing.com/search?q=WPD\_MEDIA\_LAST\_ACCESSED\_TIME)                                 | Optional.                                                                                                                    |
| [WPD\_MEDIA\_PARENTAL\_RATING](https://www.bing.com/search?q=WPD\_MEDIA\_PARENTAL\_RATING)                                        | Optional.                                                                                                                    |
| [WPD\_MEDIA\_META\_GENRE](https://www.bing.com/search?q=WPD\_MEDIA\_META\_GENRE)                                                  | Optional.                                                                                                                    |
| [WPD\_MEDIA\_COMPOSER](https://www.bing.com/search?q=WPD\_MEDIA\_COMPOSER)                                                       | Optional.                                                                                                                    |
| [WPD\_MEDIA\_EFFECTIVE\_RATING](https://www.bing.com/search?q=WPD\_MEDIA\_EFFECTIVE\_RATING)                                      | Optional.                                                                                                                    |
| [WPD\_MEDIA\_SUB\_TITLE](https://www.bing.com/search?q=WPD\_MEDIA\_SUB\_TITLE)                                                    | Optional.                                                                                                                    |
| [WPD\_MEDIA\_RELEASE\_DATE](https://www.bing.com/search?q=WPD\_MEDIA\_RELEASE\_DATE)                                              | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_SAMPLE\_RATE](https://www.bing.com/search?q=WPD\_MEDIA\_SAMPLE\_RATE)                                                | Optional.                                                                                                                    |
| [WPD\_MEDIA\_STAR\_RATING](https://www.bing.com/search?q=WPD\_MEDIA\_STAR\_RATING)                                                | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_USER\_EFFECTIVE\_RATING](https://www.bing.com/search?q=WPD\_MEDIA\_USER\_EFFECTIVE\_RATING)                           | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_TITLE](https://www.bing.com/search?q=WPD\_MEDIA\_TITLE)                                                             | Required.                                                                                                                    |
| [WPD\_MEDIA\_DURATION](https://www.bing.com/search?q=WPD\_MEDIA\_DURATION)                                                       | Required.                                                                                                                    |
| [WPD\_MEDIA\_BUY\_NOW](https://www.bing.com/search?q=WPD\_MEDIA\_BUY\_NOW)                                                        | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_ENCODING\_PROFILE](https://www.bing.com/search?q=WPD\_MEDIA\_ENCODING\_PROFILE)                                      | Optional.                                                                                                                    |
| [WPD\_MEDIA\_WIDTH](https://www.bing.com/search?q=WPD\_MEDIA\_WIDTH)                                                             | Required.                                                                                                                    |
| [WPD\_MEDIA\_HEIGHT](https://www.bing.com/search?q=WPD\_MEDIA\_HEIGHT)                                                           | Required.                                                                                                                    |
| [WPD\_MEDIA\_ARTIST](https://www.bing.com/search?q=WPD\_MEDIA\_ARTIST)                                                           | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_SOURCE\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_SOURCE\_URL)                                                  | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_DESTINATION\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_DESTINATION\_URL)                                        | Optional.                                                                                                                    |
| [WPD\_MEDIA\_DESCRIPTION](https://www.bing.com/search?q=WPD\_MEDIA\_DESCRIPTION)                                                 | Optional.                                                                                                                    |
| [WPD\_MEDIA\_GENRE](https://www.bing.com/search?q=WPD\_MEDIA\_GENRE)                                                             | Optional.                                                                                                                    |
| [WPD\_MEDIA\_TIME\_BOOKMARK](https://www.bing.com/search?q=WPD\_MEDIA\_TIME\_BOOKMARK)                                            | Optional.                                                                                                                    |
| [WPD\_MEDIA\_BYTE\_BOOKMARK](https://www.bing.com/search?q=WPD\_MEDIA\_BYTE\_BOOKMARK)                                            | Optional.                                                                                                                    |
| [WPD\_MEDIA\_GUID](https://www.bing.com/search?q=WPD\_MEDIA\_GUID)                                                               | Optional.                                                                                                                    |
| [WPD\_MEDIA\_SUB\_DESCRIPTION](https://www.bing.com/search?q=WPD\_MEDIA\_SUB\_DESCRIPTION)                                        | Optional.                                                                                                                    |
| [WPD\_VIDEO\_AUTHOR](https://www.bing.com/search?q=WPD\_VIDEO\_AUTHOR)                                                           | Optional.                                                                                                                    |
| [WPD\_VIDEO\_RECORDEDTV\_STATION\_NAME](https://www.bing.com/search?q=WPD\_VIDEO\_RECORDEDTV\_STATION\_NAME)                       | Optional.                                                                                                                    |
| [WPD\_VIDEO\_RECORDEDTV\_CHANNEL\_NUMBER](https://www.bing.com/search?q=WPD\_VIDEO\_RECORDEDTV\_CHANNEL\_NUMBER)                   | Optional.                                                                                                                    |
| [WPD\_VIDEO\_RECORDEDTV\_REPEAT](https://www.bing.com/search?q=WPD\_VIDEO\_RECORDEDTV\_REPEAT)                                    | Optional.                                                                                                                    |
| [WPD\_VIDEO\_BUFFER\_SIZE](https://www.bing.com/search?q=WPD\_VIDEO\_BUFFER\_SIZE)                                                | Optional.                                                                                                                    |
| [WPD\_VIDEO\_CREDITS](https://www.bing.com/search?q=WPD\_VIDEO\_CREDITS)                                                         | Optional.                                                                                                                    |
| [WPD\_VIDEO\_KEY\_FRAME\_DISTANCE](https://www.bing.com/search?q=WPD\_VIDEO\_KEY\_FRAME\_DISTANCE)                                 | Optional.                                                                                                                    |
| [WPD\_VIDEO\_QUALITY\_SETTING](https://www.bing.com/search?q=WPD\_VIDEO\_QUALITY\_SETTING)                                        | Optional.                                                                                                                    |
| [WPD\_VIDEO\_SCAN\_TYPE](https://www.bing.com/search?q=WPD\_VIDEO\_SCAN\_TYPE)                                                    | Required.                                                                                                                    |
| [WPD\_VIDEO\_BITRATE](https://www.bing.com/search?q=WPD\_VIDEO\_BITRATE)                                                         | Required.                                                                                                                    |
| [WPD\_VIDEO\_FOURCC\_CODE](https://www.bing.com/search?q=WPD\_VIDEO\_FOURCC\_CODE)                                                | Required if the codec is one supported by Microsoft Video for Windows (VFW), Microsoft DirectShow, and Windows Media Format. |
| [WPD\_VIDEO\_FRAMERATE](https://www.bing.com/search?q=WPD\_VIDEO\_FRAMERATE)                                                     | Optional.                                                                                                                    |



 

## Typical Resources

These objects typically include the following resources.



| Resource Name                                              | Required or Optional       | Description                                                          |
|------------------------------------------------------------|----------------------------|----------------------------------------------------------------------|
| [**WPD\_RESOURCE\_DEFAULT**](wpd-resource-default.md)     | Required.                  | Contains the video (file) data.                                      |
| [**WPD\_RESOURCE\_THUMBNAIL**](wpd-resource-thumbnail.md) | Recommended, if available. | Contains the key frame or other nonblank sample frame for the video. |



 

## Related topics

<dl> <dt>

[**Requirements for Objects**](requirements-for-objects.md)
</dt> </dl>

 

 



