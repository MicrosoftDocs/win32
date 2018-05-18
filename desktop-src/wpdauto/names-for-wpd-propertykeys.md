---
title: Names for WPD PROPERTYKEYs
description: The following table lists the names that WPD Automation assigns to WPD PROPERTY KEYs.
ms.assetid: 'eb6a5d4d-369a-408a-ba2f-54264471fb5a'
keywords: ["WPD Automation,WPD PROPERTYKEYs", "WPD Automation,names for WPD PROPERTYKEYs", "Windows Portable Devices (WPD),WPD Automation", "WPD (Windows Portable Devices),WPD Automation", "Windows Portable Devices (WPD),PROPERTYKEYs", "WPD (Windows Portable Devices),PROPERTYKEYs", "Windows Portable Devices (WPD),names for WPD PROPERTYKEYs", "WPD (Windows Portable Devices),names for WPD PROPERTYKEYs", "WPD PROPERTYKEYs,list of", "PROPERTYKEYs,list of"]
---

# Names for WPD PROPERTYKEYs

The following table lists the names that WPD Automation assigns to WPD PROPERTY KEYs. Properties are accessed by their WPD Automation names when using the **Device.WPDProperty**, **Storage.WPDProperty**, and **Service.WPDProperty** properties. For a list of required WPD properties for each object, see the [**Device.WPDProperty**](device-wpdproperty.md), [**Storage.WPDProperty**](storage-wpdproperty.md), and [**Service.WPDProperty**](service-wpdproperty.md) reference pages.

For example, the WPD-defined property WPD\_OBJECT\_NAME would be accessed from a **Service** object like this: `service.ObjectName`.



| WPD PROPERTYKEY                                  | WPD Automation Name                 |
|--------------------------------------------------|-------------------------------------|
| WPD\_RESOURCE\_DEFAULT                           | Data                                |
| WPD\_RESOURCE\_CONTACT\_PHOTO                    | ContactPhoto                        |
| WPD\_RESOURCE\_THUMBNAIL                         | Thumbnail                           |
| WPD\_RESOURCE\_ICON                              | Icon                                |
| WPD\_RESOURCE\_AUDIO\_CLIP                       | AudioClip                           |
| WPD\_RESOURCE\_ALBUM\_ART                        | AlbumArt                            |
| WPD\_RESOURCE\_GENERIC                           | Generic                             |
| WPD\_RESOURCE\_VIDEO\_CLIP                       | VideoClip                           |
| WPD\_RESOURCE\_BRANDING\_ART                     | BrandingArt                         |
| WPD\_OBJECT\_ID                                  | ObjectId                            |
| WPD\_OBJECT\_PARENT\_ID                          | ObjectParentId                      |
| WPD\_OBJECT\_NAME                                | ObjectName                          |
| WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID              | ObjectPersistentUniqueId            |
| WPD\_OBJECT\_FORMAT                              | ObjectFormat                        |
| WPD\_OBJECT\_CONTENT\_TYPE                       | ObjectContentType                   |
| WPD\_OBJECT\_ISHIDDEN                            | ObjectIsHidden                      |
| WPD\_OBJECT\_ISSYSTEM                            | ObjectIsSystem                      |
| WPD\_OBJECT\_SIZE                                | ObjectSize                          |
| WPD\_OBJECT\_ORIGINAL\_FILE\_NAME                | ObjectOriginalFileName              |
| WPD\_OBJECT\_NON\_CONSUMABLE                     | ObjectNonConsumable                 |
| WPD\_OBJECT\_REFERENCES                          | ObjectReferences                    |
| WPD\_OBJECT\_KEYWORDS                            | ObjectKeywords                      |
| WPD\_OBJECT\_SYNC\_ID                            | ObjectSyncId                        |
| WPD\_OBJECT\_IS\_DRM\_PROTECTED                  | ObjectIsDrmProtected                |
| WPD\_OBJECT\_DATE\_CREATED                       | ObjectDateCreated                   |
| WPD\_OBJECT\_DATE\_MODIFIED                      | ObjectDateModified                  |
| WPD\_OBJECT\_DATE\_AUTHORED                      | ObjectDateAuthored                  |
| WPD\_OBJECT\_BACK\_REFERENCES                    | ObjectBackReferences                |
| WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID   | ObjectContainerFunctionalObjectId   |
| WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE | ObjectGenerateThumbnailFromResource |
| WPD\_OBJECT\_HINT\_LOCATION\_DISPLAY\_NAME       | ObjectHintLocationDisplayName       |
| WPD\_OBJECT\_CAN\_DELETE                         | ObjectCanDelete                     |
| WPD\_OBJECT\_LANGUAGE\_LOCALE                    | ObjectLanguageLocale                |
| WPD\_FUNCTIONAL\_OBJECT\_CATEGORY                | FunctionalObjectCategory            |
| WPD\_FOLDER\_CONTENT\_TYPES\_ALLOWED             | FolderContentTypesAllowed           |
| WPD\_IMAGE\_BITDEPTH                             | ImageBitdepth                       |
| WPD\_IMAGE\_CROPPED\_STATUS                      | ImageCroppedStatus                  |
| WPD\_IMAGE\_COLOR\_CORRECTED\_STATUS             | ImageColorCorrectedStatus           |
| WPD\_IMAGE\_FNUMBER                              | ImageFnumber                        |
| WPD\_IMAGE\_EXPOSURE\_TIME                       | ImageExposureTime                   |
| WPD\_IMAGE\_EXPOSURE\_INDEX                      | ImageExposureIndex                  |
| WPD\_IMAGE\_HORIZONTAL\_RESOLUTION               | ImageHorizontalResolution           |
| WPD\_IMAGE\_VERTICAL\_RESOLUTION                 | ImageVerticalResolution             |
| WPD\_MEDIA\_TOTAL\_BITRATE                       | MediaTotalBitrate                   |
| WPD\_MEDIA\_BITRATE\_TYPE                        | MediaBitrateType                    |
| WPD\_MEDIA\_COPYRIGHT                            | MediaCopyright                      |
| WPD\_MEDIA\_SUBSCRIPTION\_CONTENT\_ID            | MediaSubscriptionContentId          |
| WPD\_MEDIA\_USE\_COUNT                           | MediaUseCount                       |
| WPD\_MEDIA\_SKIP\_COUNT                          | MediaSkipCount                      |
| WPD\_MEDIA\_LAST\_ACCESSED\_TIME                 | MediaLastAccessedTime               |
| WPD\_MEDIA\_PARENTAL\_RATING                     | MediaParentalRating                 |
| WPD\_MEDIA\_META\_GENRE                          | MediaMetaGenre                      |
| WPD\_MEDIA\_COMPOSER                             | MediaComposer                       |
| WPD\_MEDIA\_EFFECTIVE\_RATING                    | MediaEffectiveRating                |
| WPD\_MEDIA\_SUB\_TITLE                           | MediaSubTitle                       |
| WPD\_MEDIA\_RELEASE\_DATE                        | MediaReleaseDate                    |
| WPD\_MEDIA\_SAMPLE\_RATE                         | MediaSampleRate                     |
| WPD\_MEDIA\_STAR\_RATING                         | MediaStarRating                     |
| WPD\_MEDIA\_USER\_EFFECTIVE\_RATING              | MediaUserEffectiveRating            |
| WPD\_MEDIA\_TITLE                                | MediaTitle                          |
| WPD\_MEDIA\_DURATION                             | MediaDuration                       |
| WPD\_MEDIA\_BUY\_NOW                             | MediaBuyNow                         |
| WPD\_MEDIA\_ENCODING\_PROFILE                    | MediaEncodingProfile                |



 

## Related topics

<dl> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[WPD Automation Reference](wpd-automation-reference.md)
</dt> </dl>

 

 




