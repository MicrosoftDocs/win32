---
Description: 'WPD\_CONTENT\_TYPE\_VIDEO'
ms.assetid: 'd4a6bd98-c28e-487b-95cc-2c73cd44e3b5'
title: 'WPD\_CONTENT\_TYPE\_VIDEO'
---

# WPD\_CONTENT\_TYPE\_VIDEO

An object that describes its type as WPD\_CONTENT\_TYPE\_VIDEO represents a video file.

This type of object supports the following properties.



|                                                                                                                       |                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **Property Name**                                                                                                     | **Required or Optional**                                                                                                     |
| [WPD\_OBJECT\_ID](object-properties.md#wpd-object-id)                                                                | Required, read-only. A client cannot set this property, even at creation time.                                               |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md#wpd-object-parent-id)                                                 | Required.                                                                                                                    |
| [WPD\_OBJECT\_NAME](object-properties.md#wpd-object-name)                                                            | Required if the object represents a file.                                                                                    |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md#wpd-object-persistent-unique-id)                          | Required, read-only. A client cannot set this property, even at creation time.                                               |
| [WPD\_OBJECT\_FORMAT](object-properties.md#wpd-object-format)                                                        | Required.                                                                                                                    |
| [WPD\_OBJECT\_CONTENT\_TYPE](object-properties.md#wpd-object-content-type)                                           | Required.                                                                                                                    |
| [WPD\_OBJECT\_ISHIDDEN](object-properties.md#wpd-object-ishidden)                                                    | Required if the object is hidden.                                                                                            |
| [WPD\_OBJECT\_ISSYSTEM](object-properties.md#wpd-object-issystem)                                                    | Required if the object is a system object (represents a system file).                                                        |
| [WPD\_OBJECT\_SIZE](object-properties.md#wpd-object-size)                                                            | Required if the object has at least one resource.                                                                            |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](object-properties.md#wpd-object-original-file-name)                              | Required if the object represents a file.                                                                                    |
| [WPD\_OBJECT\_NON\_CONSUMABLE](object-properties.md#wpd-object-non-consumable)                                       | Recommended if the object is not meant for consumption by the device.                                                        |
| [WPD\_OBJECT\_REFERENCES](object-properties.md#wpd-object-references)                                                | Required if the object has references to other objects.                                                                      |
| [WPD\_OBJECT\_KEYWORDS](object-properties.md#wpd-object-keywords)                                                    | Optional.                                                                                                                    |
| [WPD\_OBJECT\_SYNC\_ID](object-properties.md#wpd-object-sync-id)                                                     | Optional.                                                                                                                    |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](object-properties.md#wpd-object-is-drm-protected)                                  | Required if the object is protected by DRM technology.                                                                       |
| [WPD\_OBJECT\_DATE\_CREATED](object-properties.md#wpd-object-date-created)                                           | Optional.                                                                                                                    |
| [WPD\_OBJECT\_DATE\_MODIFIED](object-properties.md#wpd-object-date-modified)                                         | Recommended.                                                                                                                 |
| [WPD\_OBJECT\_DATE\_AUTHORED](object-properties.md#wpd-object-date-authored)                                         | Optional.                                                                                                                    |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                                                | Recommended if the object is referenced by another object.                                                                   |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](object-properties.md#wpd-object-container-functional-object-id)     | Optional.                                                                                                                    |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](object-properties.md#wpd-object-generate-thumbnail-from-resource) | Optional.                                                                                                                    |
| [WPD\_OBJECT\_CAN\_DELETE](object-properties.md)                                                                     | Required if the object cannot be deleted.                                                                                    |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                | Optional.                                                                                                                    |
| [WPD\_MEDIA\_TOTAL\_BITRATE](media-properties.md#wpd-media-total-bitrate)                                            | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_BITRATE\_TYPE](media-properties.md#wpd-media-bitrate-type)                                              | Optional.                                                                                                                    |
| [WPD\_MEDIA\_COPYRIGHT](media-properties.md#wpd-media-copyright)                                                     | Optional.                                                                                                                    |
| [WPD\_MEDIA\_SUBSCRIPTION\_CONTENT\_ID](media-properties.md#wpd-media-subscription-content-id)                       | Recommended, if this object represents content from an online subscription service.                                          |
| [WPD\_MEDIA\_USE\_COUNT](media-properties.md#wpd-media-use-count)                                                    | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_SKIP\_COUNT](media-properties.md#wpd-media-skip-count)                                                  | Optional.                                                                                                                    |
| [WPD\_MEDIA\_LAST\_ACCESSED\_TIME](media-properties.md#wpd-media-last-accessed-time)                                 | Optional.                                                                                                                    |
| [WPD\_MEDIA\_PARENTAL\_RATING](media-properties.md#wpd-media-parental-rating)                                        | Optional.                                                                                                                    |
| [WPD\_MEDIA\_META\_GENRE](media-properties.md#wpd-media-meta-genre)                                                  | Optional.                                                                                                                    |
| [WPD\_MEDIA\_COMPOSER](media-properties.md#wpd-media-composer)                                                       | Optional.                                                                                                                    |
| [WPD\_MEDIA\_EFFECTIVE\_RATING](media-properties.md#wpd-media-effective-rating)                                      | Optional.                                                                                                                    |
| [WPD\_MEDIA\_SUB\_TITLE](media-properties.md#wpd-media-sub-title)                                                    | Optional.                                                                                                                    |
| [WPD\_MEDIA\_RELEASE\_DATE](media-properties.md#wpd-media-release-date)                                              | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_SAMPLE\_RATE](media-properties.md#wpd-media-sample-rate)                                                | Optional.                                                                                                                    |
| [WPD\_MEDIA\_STAR\_RATING](media-properties.md#wpd-media-star-rating)                                                | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_USER\_EFFECTIVE\_RATING](media-properties.md#wpd-media-user-effective-rating)                           | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_TITLE](media-properties.md#wpd-media-title)                                                             | Required.                                                                                                                    |
| [WPD\_MEDIA\_DURATION](media-properties.md#wpd-media-duration)                                                       | Required.                                                                                                                    |
| [WPD\_MEDIA\_BUY\_NOW](media-properties.md#wpd-media-buy-now)                                                        | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_ENCODING\_PROFILE](media-properties.md#wpd-media-encoding-profile)                                      | Optional.                                                                                                                    |
| [WPD\_MEDIA\_WIDTH](media-properties.md#wpd-media-width)                                                             | Required.                                                                                                                    |
| [WPD\_MEDIA\_HEIGHT](media-properties.md#wpd-media-height)                                                           | Required.                                                                                                                    |
| [WPD\_MEDIA\_ARTIST](media-properties.md#wpd-media-artist)                                                           | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_SOURCE\_URL](media-properties.md#wpd-media-source-url)                                                  | Recommended.                                                                                                                 |
| [WPD\_MEDIA\_DESTINATION\_URL](media-properties.md#wpd-media-destination-url)                                        | Optional.                                                                                                                    |
| [WPD\_MEDIA\_DESCRIPTION](media-properties.md#wpd-media-description)                                                 | Optional.                                                                                                                    |
| [WPD\_MEDIA\_GENRE](media-properties.md#wpd-media-genre)                                                             | Optional.                                                                                                                    |
| [WPD\_MEDIA\_TIME\_BOOKMARK](media-properties.md#wpd-media-time-bookmark)                                            | Optional.                                                                                                                    |
| [WPD\_MEDIA\_BYTE\_BOOKMARK](media-properties.md#wpd-media-byte-bookmark)                                            | Optional.                                                                                                                    |
| [WPD\_MEDIA\_GUID](media-properties.md#wpd-media-guid)                                                               | Optional.                                                                                                                    |
| [WPD\_MEDIA\_SUB\_DESCRIPTION](media-properties.md#wpd-media-sub-description)                                        | Optional.                                                                                                                    |
| [WPD\_VIDEO\_AUTHOR](video-properties.md#wpd-video-author)                                                           | Optional.                                                                                                                    |
| [WPD\_VIDEO\_RECORDEDTV\_STATION\_NAME](video-properties.md#wpd-video-recordedtv-station-name)                       | Optional.                                                                                                                    |
| [WPD\_VIDEO\_RECORDEDTV\_CHANNEL\_NUMBER](video-properties.md#wpd-video-recordedtv-channel-number)                   | Optional.                                                                                                                    |
| [WPD\_VIDEO\_RECORDEDTV\_REPEAT](video-properties.md#wpd-video-recordedtv-repeat)                                    | Optional.                                                                                                                    |
| [WPD\_VIDEO\_BUFFER\_SIZE](video-properties.md#wpd-video-buffer-size)                                                | Optional.                                                                                                                    |
| [WPD\_VIDEO\_CREDITS](video-properties.md#wpd-video-credits)                                                         | Optional.                                                                                                                    |
| [WPD\_VIDEO\_KEY\_FRAME\_DISTANCE](video-properties.md#wpd-video-key-frame-distance)                                 | Optional.                                                                                                                    |
| [WPD\_VIDEO\_QUALITY\_SETTING](video-properties.md#wpd-video-quality-setting)                                        | Optional.                                                                                                                    |
| [WPD\_VIDEO\_SCAN\_TYPE](video-properties.md#wpd-video-scan-type)                                                    | Required.                                                                                                                    |
| [WPD\_VIDEO\_BITRATE](video-properties.md#wpd-video-bitrate)                                                         | Required.                                                                                                                    |
| [WPD\_VIDEO\_FOURCC\_CODE](video-properties.md#wpd-video-fourcc-code)                                                | Required if the codec is one supported by Microsoft Video for Windows (VFW), Microsoft DirectShow, and Windows Media Format. |
| [WPD\_VIDEO\_FRAMERATE](video-properties.md#wpd-video-framerate)                                                     | Optional.                                                                                                                    |



 

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

 

 



