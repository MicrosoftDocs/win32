---
description: WPD\_CONTENT\_TYPE\_VIDEO
ms.assetid: d4a6bd98-c28e-487b-95cc-2c73cd44e3b5
title: WPD_CONTENT_TYPE_VIDEO
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_CONTENT\_TYPE\_VIDEO

An object that describes its type as WPD\_CONTENT\_TYPE\_VIDEO represents a video file.

This type of object supports the following properties.



|                                                                                                                       |                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **Property Name**                                                                                                     | **Required or Optional**                                                                                                     |
| [WPD\_OBJECT\_ID](object-properties.md)                                                                | Required, read-only. A client cannot set this property, even at creation time.                                               |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md)                                                 | Required.                                                                                                                    |
| [WPD\_OBJECT\_NAME](object-properties.md)                                                            | Required if the object represents a file.                                                                                    |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md)                          | Required, read-only. A client cannot set this property, even at creation time.                                               |
| [WPD\_OBJECT\_FORMAT](object-properties.md)                                                        | Required.                                                                                                                    |
| [WPD\_OBJECT\_CONTENT\_TYPE](object-properties.md)                                           | Required.                                                                                                                    |
| [WPD\_OBJECT\_ISHIDDEN](object-properties.md)                                                    | Required if the object is hidden.                                                                                            |
| [WPD\_OBJECT\_ISSYSTEM](object-properties.md)                                                    | Required if the object is a system object (represents a system file).                                                        |
| [WPD\_OBJECT\_SIZE](object-properties.md)                                                            | Required if the object has at least one resource.                                                                            |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](object-properties.md)                              | Required if the object represents a file.                                                                                    |
| [WPD\_OBJECT\_NON\_CONSUMABLE](object-properties.md)                                       | Recommended if the object is not meant for consumption by the device.                                                        |
| [WPD\_OBJECT\_REFERENCES](object-properties.md)                                                | Required if the object has references to other objects.                                                                      |
| [WPD\_OBJECT\_KEYWORDS](object-properties.md)                                                    | Optional.                                                                                                                    |
| [WPD\_OBJECT\_SYNC\_ID](object-properties.md)                                                     | Optional.                                                                                                                    |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](object-properties.md)                                  | Required if the object is protected by DRM technology.                                                                       |
| [WPD\_OBJECT\_DATE\_CREATED](object-properties.md)                                           | Optional.                                                                                                                    |
| [WPD\_OBJECT\_DATE\_MODIFIED](object-properties.md)                                         | Recommended.                                                                                                                 |
| [WPD\_OBJECT\_DATE\_AUTHORED](object-properties.md)                                         | Optional.                                                                                                                    |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                | Recommended if the object is referenced by another object.                                                                   |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](object-properties.md)     | Optional.                                                                                                                    |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](object-properties.md) | Optional.                                                                                                                    |
| [WPD\_OBJECT\_CAN\_DELETE](object-properties.md)                                                                     | Required if the object cannot be deleted.                                                                                    |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                | Optional.                                                                                                                    |
| [WPD\_MEDIA\_TOTAL\_BITRATE](media-properties.md)                                            | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_BITRATE\_TYPE](media-properties.md)                                              | Optional.                                                                                                                    |
| [WPD\_MEDIA\_COPYRIGHT](media-properties.md)                                                     | Optional.                                                                                                                    |
| [WPD\_MEDIA\_SUBSCRIPTION\_CONTENT\_ID](media-properties.md)                       | Recommended, if this object represents content from an online subscription service.                                          |
| [WPD\_MEDIA\_USE\_COUNT](media-properties.md)                                                    | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_SKIP\_COUNT](media-properties.md)                                                  | Optional.                                                                                                                    |
| [WPD\_MEDIA\_LAST\_ACCESSED\_TIME](media-properties.md)                                 | Optional.                                                                                                                    |
| [WPD\_MEDIA\_PARENTAL\_RATING](media-properties.md)                                        | Optional.                                                                                                                    |
| [WPD\_MEDIA\_META\_GENRE](media-properties.md)                                                  | Optional.                                                                                                                    |
| [WPD\_MEDIA\_COMPOSER](media-properties.md)                                                       | Optional.                                                                                                                    |
| [WPD\_MEDIA\_EFFECTIVE\_RATING](media-properties.md)                                      | Optional.                                                                                                                    |
| [WPD\_MEDIA\_SUB\_TITLE](media-properties.md)                                                    | Optional.                                                                                                                    |
| [WPD\_MEDIA\_RELEASE\_DATE](media-properties.md)                                              | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_SAMPLE\_RATE](media-properties.md)                                                | Optional.                                                                                                                    |
| [WPD\_MEDIA\_STAR\_RATING](media-properties.md)                                                | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_USER\_EFFECTIVE\_RATING](media-properties.md)                           | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_TITLE](media-properties.md)                                                             | Required.                                                                                                                    |
| [WPD\_MEDIA\_DURATION](media-properties.md)                                                       | Required.                                                                                                                    |
| [WPD\_MEDIA\_BUY\_NOW](media-properties.md)                                                        | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_ENCODING\_PROFILE](media-properties.md)                                      | Optional.                                                                                                                    |
| [WPD\_MEDIA\_WIDTH](media-properties.md)                                                             | Required.                                                                                                                    |
| [WPD\_MEDIA\_HEIGHT](media-properties.md)                                                           | Required.                                                                                                                    |
| [WPD\_MEDIA\_ARTIST](media-properties.md)                                                           | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_SOURCE\_URL](media-properties.md)                                                  | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_DESTINATION\_URL](media-properties.md)                                        | Optional.                                                                                                                    |
| [WPD\_MEDIA\_DESCRIPTION](media-properties.md)                                                 | Optional.                                                                                                                    |
| [WPD\_MEDIA\_GENRE](media-properties.md)                                                             | Optional.                                                                                                                    |
| [WPD\_MEDIA\_TIME\_BOOKMARK](media-properties.md)                                            | Optional.                                                                                                                    |
| [WPD\_MEDIA\_BYTE\_BOOKMARK](media-properties.md)                                            | Optional.                                                                                                                    |
| [WPD\_MEDIA\_GUID](media-properties.md)                                                               | Optional.                                                                                                                    |
| [WPD\_MEDIA\_SUB\_DESCRIPTION](media-properties.md)                                        | Optional.                                                                                                                    |
| [WPD\_VIDEO\_AUTHOR](video-properties.md)                                                           | Optional.                                                                                                                    |
| [WPD\_VIDEO\_RECORDEDTV\_STATION\_NAME](video-properties.md)                       | Optional.                                                                                                                    |
| [WPD\_VIDEO\_RECORDEDTV\_CHANNEL\_NUMBER](video-properties.md)                   | Optional.                                                                                                                    |
| [WPD\_VIDEO\_RECORDEDTV\_REPEAT](video-properties.md)                                    | Optional.                                                                                                                    |
| [WPD\_VIDEO\_BUFFER\_SIZE](video-properties.md)                                                | Optional.                                                                                                                    |
| [WPD\_VIDEO\_CREDITS](video-properties.md)                                                         | Optional.                                                                                                                    |
| [WPD\_VIDEO\_KEY\_FRAME\_DISTANCE](video-properties.md)                                 | Optional.                                                                                                                    |
| [WPD\_VIDEO\_QUALITY\_SETTING](video-properties.md)                                        | Optional.                                                                                                                    |
| [WPD\_VIDEO\_SCAN\_TYPE](video-properties.md)                                                    | Required.                                                                                                                    |
| [WPD\_VIDEO\_BITRATE](video-properties.md)                                                         | Required.                                                                                                                    |
| [WPD\_VIDEO\_FOURCC\_CODE](video-properties.md)                                                | Required if the codec is one supported by Microsoft Video for Windows (VFW), Microsoft DirectShow, and Windows Media Format. |
| [WPD\_VIDEO\_FRAMERATE](video-properties.md)                                                     | Optional.                                                                                                                    |



 

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

 

 



