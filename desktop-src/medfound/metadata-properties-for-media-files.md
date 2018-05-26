---
Description: This topic lists the most common metadata properties for media files.
ms.assetid: 35187720-413a-45a0-8558-918f7c3161e1
title: Metadata Properties for Media Files
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Metadata Properties for Media Files

This topic lists the most common metadata properties for media files.

-   [Common Media Properties](#common-media-properties)
-   [Media Sharing Properties](#media-sharing-properties)
-   [Windows Media Format SDK Mappings](#windows-media-format-sdk-mappings)
-   [Related topics](#related-topics)

## Common Media Properties

The Shell property system defines a set of common metadata properties for all types of shell objects. A subset of these are applicable to media files. The following table lists the most common Shell properties for media. Media files might support additional properties not listed here. Also, not every file format supports every property listed. For a complete list of Shell properties, see [Shell Properties](shell.shell_properties_bumper).



| PROPERTYKEY                                                              | Shell Name                                                                                    | Description                                                                                                                                                                                               | Data Type    |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [MFPKEY\_Content\_DLNA\_Profile\_ID](mfpkey-content-dlna-profile-id.md) | None                                                                                          | Digital Living Network Alliance (DLNA) profile identifier.                                                                                                                                                | VT\_LPWSTR   |
| **PKEY\_Audio\_ChannelCount**                                            | [System.Audio.ChannelCount](properties.props_System_Audio_ChannelCount)                       | Number of audio channels.                                                                                                                                                                                 | VT\_UI4      |
| **PKEY\_Audio\_EncodingBitrate**                                         | [System.Audio.EncodingBitrate](properties.props_System_Audio_EncodingBitrate)                 | Average audio bit rate, in bits per second.                                                                                                                                                               | VT\_UI4      |
| **PKEY\_Audio\_Format**                                                  | [System.Audio.Format](properties.props_System_Audio_Format)                                   | Audio subtype ([**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)) expressed as a string.                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Audio\_IsVariableBitRate**                                       | [System.Audio.IsVariableBitRate](properties.props_System_Audio_IsVariableBitRate)             | Indicates whether the audio stream uses variable bit-rate encoding.                                                                                                                                       | VT\_BOOL     |
| **PKEY\_Audio\_PeakValue**                                               | [System.Audio.PeakValue](properties.props_System_Audio_PeakValue)                             | Peak volume level of audio content.                                                                                                                                                                       | VT\_UI4      |
| **PKEY\_Audio\_SampleRate**                                              | [System.Audio.SampleRate](properties.props_System_Audio_SampleRate)                           | Audio sample rate in samples per second. Equivalent to the [**MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND**](mf-mt-audio-samples-per-second-attribute.md) attribute in the media type.                           | VT\_UI4      |
| **PKEY\_Audio\_SampleSize**                                              | [System.Audio.SampleSize](properties.props_System_Audio_SampleSize)                           | Number of bits per audio sample. Equivalent to the [**MF\_MT\_AUDIO\_BITS\_PER\_SAMPLE**](mf-mt-audio-bits-per-sample-attribute.md) attribute in the media type.                                         | VT\_UI4      |
| **PKEY\_Audio\_StreamNumber**                                            | [System.Audio.StreamNumber](properties.props_System_Audio_StreamNumber)                       | Identifier of the audio stream.                                                                                                                                                                           | VT\_UI4      |
| **PKEY\_Author**                                                         | [System.Author](properties.props_System_Author)                                               | Author.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Comment**                                                        | [System.Comment](properties.props_System_Comment)                                             | A comment attached to a file, typically added by a user.                                                                                                                                                  | VT\_LPWSTR   |
| **PKEY\_Copyright**                                                      | [System.Copyright](properties.props_System_Copyright)                                         | Copyright information.                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_DRM\_IsProtected**                                               | [System.DRM.IsProtected](properties.props_System_DRM_IsProtected)                             | Indicates whether the content is protected using digital rights management (DRM).                                                                                                                         | VT\_BOOL     |
| **PKEY\_Keywords**                                                       | [System.Keywords](properties.props_System_Keywords)                                           | Keywords.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Language**                                                       | [System.Language](properties.props_System_Language)                                           | Language.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_AuthorUrl**                                               | [System.Media.AuthorUrl](properties.props_System_Media_AuthorUrl)                             | URL of the author's website.                                                                                                                                                                              | VT\_LPWSTR   |
| **PKEY\_Media\_AverageLevel**                                            | [System.Media.AverageLevel](properties.props_System_Media_AverageLevel)                       | Average volume level of audio content.                                                                                                                                                                    | VT\_UI4      |
| **PKEY\_Media\_ClassPrimaryID**                                          | [System.Media.ClassPrimaryID](properties.props_System_Media_ClassPrimaryID)                   | The string representation of a GUID that identifies the primary class of media. For valid values, see the documentation for the [**WM/MediaClassPrimaryID**](wmformat.wm_mediaprimaryid) attribute.       | VT\_LPWSTR   |
| **PKEY\_Media\_ClassSecondaryID**                                        | [System.Media.ClassSecondaryID](properties.props_System_Media_ClassSecondaryID)               | The string representation of a GUID that identifies the secondary class of media. For valid values, see the documentation for the [**WM/MediaClassSecondaryID**](wmformat.wm_mediasecondaryid) attribute. | VT\_LPWSTR   |
| **PKEY\_Media\_CollectionGroupID**                                       | [System.Media.CollectionGroupID](properties.props_System_Media_CollectionGroupID)             | The string representation of a GUID that identifies the collection group.                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_CollectionID**                                            | [System.Media.CollectionID](properties.props_System_Media_CollectionID)                       | The string representation of a GUID that identifies the collection.                                                                                                                                       | VT\_LPWSTR   |
| **PKEY\_Media\_ContentDistributor**                                      | [System.Media.ContentDistributor](properties.props_System_Media_ContentDistributor)           | Distributor of the content.                                                                                                                                                                               | VT\_LPWSTR   |
| **PKEY\_Media\_ContentID**                                               | [System.Media.ContentID](properties.props_System_Media_ContentID)                             | The string representation of a GUID that identifies the collection.                                                                                                                                       | VT\_LPWSTR   |
| **PKEY\_Media\_DateEncoded**                                             | [System.Media.DateEncoded](properties.props_System_Media_DateEncoded)                         | Time when the content was encoded.                                                                                                                                                                        | VT\_FILETIME |
| **PKEY\_Media\_DateReleased**                                            | [System.Media.DateReleased](properties.props_System_Media_DateReleased)                       | Original release date.                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Media\_Duration**                                                | [System.Media.Duration](properties.props_System_Media_Duration)                               | Duration, in 100-nanosecond units. Equivalent to the [**MF\_PD\_DURATION**](mf-pd-duration-attribute.md) attribute in the presentation descriptor.                                                       | VT\_UI8      |
| **PKEY\_Media\_DVDID**                                                   | [System.Media.DVDID](properties.props_System_Media_DVDID)                                     | Digital video disc identifier (DVDID).                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Media\_EncodedBy**                                               | [System.Media.EncodedBy](properties.props_System_Media_EncodedBy)                             | Name of the person or group that encoded the content.                                                                                                                                                     | VT\_LPWSTR   |
| **PKEY\_Media\_EncodingSettings**                                        | [System.Media.EncodingSettings](properties.props_System_Media_EncodingSettings)               | Description of the settings used to encode the content.                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Media\_MCDI**                                                    | [System.Media.MCDI](properties.props_System_Media_MCDI)                                       | Music CD identifier. This value is used to identify a CD.                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_MetadataContentProvider**                                 | [System.Media.MetadataContentProvider](properties.props_System_Media_MetadataContentProvider) | Name of the metadata content provider. (For example, metadata might be provided by a commercial service.)                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_Producer**                                                | [System.Media.Producer](properties.props_System_Media_Producer)                               | Name of the producer of the content.                                                                                                                                                                      | VT\_LPWSTR   |
| **PKEY\_Media\_PromotionUrl**                                            | [System.Media.PromotionUrl](properties.props_System_Media_PromotionUrl)                       | URL of a website offering a promotion related to the content.                                                                                                                                             | VT\_LPWSTR   |
| **PKEY\_Media\_ProviderRating**                                          | [System.Media.ProviderRating](properties.props_System_Media_ProviderRating)                   | Rating of the content as assigned by the metadata content provider.                                                                                                                                       | VT\_LPWSTR   |
| **PKEY\_Media\_ProviderStyle**                                           | [System.Media.ProviderStyle](properties.props_System_Media_ProviderStyle)                     | Style or genre of the content as assigned by the metadata content provider.                                                                                                                               | VT\_LPWSTR   |
| **PKEY\_Media\_Publisher**                                               | [System.Media.Publisher](properties.props_System_Media_Publisher)                             | Publisher.                                                                                                                                                                                                | VT\_LPWSTR   |
| **PKEY\_Media\_SubTitle**                                                | [System.Media.SubTitle](properties.props_System_Media_SubTitle)                               | Subtitle.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_UniqueFileIdentifier**                                    | [System.Media.UniqueFileIdentifier](properties.props_System_Media_UniqueFileIdentifier)       | A generic string that can be to identify the file.                                                                                                                                                        | VT\_LPWSTR   |
| **PKEY\_Media\_Writer**                                                  | [System.Media.Writer](properties.props_System_Media_Writer)                                   | Writer.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Media\_Year**                                                    | [System.Media.Year](properties.props_System_Media_Year)                                       | Year the content was published.                                                                                                                                                                           | VT\_UI4      |
| **PKEY\_Music\_AlbumArtist**                                             | [System.Music.AlbumArtist](properties.props_System_Music_AlbumArtist)                         | Primary artist for the album. This attribute can be used to distinguish the primary artist for an album from an artist who collaborated on a particular track.                                            | VT\_LPWSTR   |
| **PKEY\_Music\_AlbumTitle**                                              | [System.Music.AlbumTitle](properties.props_System_Music_AlbumTitle)                           | Album title.                                                                                                                                                                                              | VT\_LPWSTR   |
| **PKEY\_Music\_Artist**                                                  | [System.Music.Artist](properties.props_System_Music_Artist)                                   | Artist.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Music\_BeatsPerMinute**                                          | [System.Music.BeatsPerMinute](properties.props_System_Music_BeatsPerMinute)                   | Beats per minute.                                                                                                                                                                                         | VT\_LPWSTR   |
| **PKEY\_Music\_Composer**                                                | [System.Music.Composer](properties.props_System_Music_Composer)                               | Composer.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Music\_Conductor**                                               | [System.Music.Conductor](properties.props_System_Music_Conductor)                             | Conductor.                                                                                                                                                                                                | VT\_LPWSTR   |
| **PKEY\_Music\_ContentGroupDescription**                                 | [System.Music.ContentGroupDescription](properties.props_System_Music_ContentGroupDescription) | Description of the content group (for example, boxed set or series).                                                                                                                                      | VT\_LPWSTR   |
| **PKEY\_Music\_Genre**                                                   | [System.Music.Genre](properties.props_System_Music_Genre)                                     | Genre.                                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Music\_InitialKey**                                              | [System.Music.InitialKey](properties.props_System_Music_InitialKey)                           | The initial key of the music.                                                                                                                                                                             | VT\_LPWSTR   |
| **PKEY\_Music\_IsCompilation**                                           | [System.Music.IsCompilation](properties.props_System_Music_IsCompilation)                     | Indicates whether the music file is part of a compilation.                                                                                                                                                | VT\_BOOL     |
| **PKEY\_Music\_Lyrics**                                                  | [System.Music.Lyrics](properties.props_System_Music_Lyrics)                                   | Lyrics.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Music\_Mood**                                                    | [System.Music.Mood](properties.props_System_Music_Mood)                                       | Mood.                                                                                                                                                                                                     | VT\_LPWSTR   |
| **PKEY\_Music\_PartOfSet**                                               | [System.Music.PartOfSet](properties.props_System_Music_PartOfSet)                             | The part number and the total number of parts in the set to which the file belongs, separated by a slash.                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Music\_Period**                                                  | [System.Music.Period](properties.props_System_Music_Period)                                   | Period.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Music\_TrackNumber**                                             | [System.Music.TrackNumber](properties.props_System_Music_TrackNumber)                         | Track number.                                                                                                                                                                                             | VT\_UI4      |
| **PKEY\_ParentalRating**                                                 | [System.ParentalRating](properties.props_System_ParentalRating)                               | Parental rating.                                                                                                                                                                                          | VT\_LPWSTR   |
| **PKEY\_ParentalRatingReason**                                           | [System.ParentalRatingReason](properties.props_System_ParentalRatingReason)                   | Reasons for the assigned parental rating.                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Rating**                                                         | [System.Rating](properties.props_System_Rating)                                               | User rating.                                                                                                                                                                                              | VT\_UI4      |
| **PKEY\_ThumbnailStream**                                                | [System.ThumbnailStream](properties.props_System_ThumbnailStream)                             | Thumbnail image.                                                                                                                                                                                          | VT\_STREAM   |
| **PKEY\_Title**                                                          | [System.Title](properties.props_System_Title)                                                 | Title.                                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Video\_Compression**                                             | [System.Video.Compression](properties.props_System_Video_Compression)                         | Video subtype ([**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)) expressed as a string.                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Video\_Director**                                                | [System.Video.Director](properties.props_System_Video_Director)                               | Director.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Video\_EncodingBitrate**                                         | [System.Video.EncodingBitrate](properties.props_System_Video_EncodingBitrate)                 | Average video bit rate, in bits per second.                                                                                                                                                               | VT\_UI4      |
| **PKEY\_Video\_FourCC**                                                  | [System.Video.FourCC](properties.props_System_Video_FourCC)                                   | The **FOURCC** of the video encoding format. Applies only if the video subtype can be expressed as a **FOURCC** value.                                                                                    | VT\_UI4      |
| **PKEY\_Video\_FrameHeight**                                             | [System.Video.FrameHeight](properties.props_System_Video_FrameHeight)                         | Video frame height.                                                                                                                                                                                       | VT\_UI4      |
| **PKEY\_Video\_FrameRate**                                               | [System.Video.FrameRate](properties.props_System_Video_FrameRate)                             | Video frame rate, expressed as frames per second × 1000.                                                                                                                                                  | VT\_UI4      |
| **PKEY\_Video\_FrameWidth**                                              | [System.Video.FrameWidth](properties.props_System_Video_FrameWidth)                           | Video frame width.                                                                                                                                                                                        | VT\_UI4      |
| **PKEY\_Video\_HorizontalAspectRatio**                                   | [System.Video.HorizontalAspectRatio](properties.props_System_Video_HorizontalAspectRatio)     | The horizontal component of the pixel aspect ratio. (Equivalent to the numerator of the [**MF\_MT\_PIXEL\_ASPECT\_RATIO**](mf-mt-pixel-aspect-ratio-attribute.md) attribute in the media type.)          | VT\_UI4      |
| **PKEY\_Video\_IsStereo**                                                | [System.Video.IsStereo](properties.system_video_isstereo)                                     | Indicates whether the video stream contains stereo video content.                                                                                                                                         | VT\_BOOL     |
| **PKEY\_Video\_StreamNumber**                                            | [System.Video.StreamNumber](properties.props_System_Video_StreamNumber)                       | Identifier of the video stream.                                                                                                                                                                           | VT\_UI4      |
| **PKEY\_Video\_TotalBitrate**                                            | [System.Video.TotalBitrate](properties.props_System_Video_TotalBitrate)                       | Total data rate for all video and audio streams, in bits per second. (Applies only to files with at least one video stream.)                                                                              | VT\_UI4      |
| **PKEY\_Video\_VerticalAspectRatio**                                     | [System.Video.VerticalAspectRatio](properties.props_System_Video_VerticalAspectRatio)         | The vertical component of the pixel aspect ratio. (Equivalent to the denominator of the [**MF\_MT\_PIXEL\_ASPECT\_RATIO**](mf-mt-pixel-aspect-ratio-attribute.md) attribute in the media type.)          | VT\_UI4      |



 

## Media Sharing Properties

To make a media file compatible with the Media Sharing feature, the property handler should expose the following metadata properties. These properties enable the Media Sharing service to offer the proper options to transcode the content into different formats or bit rates.

-   [MFPKEY\_Content\_DLNA\_Profile\_ID](mfpkey-content-dlna-profile-id.md)
-   **PKEY\_Audio\_ChannelCount**
-   **PKEY\_Audio\_EncodingBitrate**
-   **PKEY\_Audio\_Format**
-   **PKEY\_Audio\_SampleRate** (optional)
-   **PKEY\_Audio\_SampleSize** (optional)
-   **PKEY\_DRM\_IsProtected** (required for DRM content)
-   **PKEY\_Media\_Duration**
-   **PKEY\_Video\_Compression**
-   **PKEY\_Video\_EncodingBitrate**
-   **PKEY\_Video\_FOURCC**
-   **PKEY\_Video\_FrameHeight**
-   **PKEY\_Video\_FrameRate** (optional)
-   **PKEY\_Video\_FrameWidth**
-   **PKEY\_Video\_TotalBitrate**

The **PKEY\_DRM\_IsProtected** property is required if the content is protected using DRM. Otherwise, this property is optional.

The **PKEY\_Audio\_SampleRate**, **PKEY\_Audio\_SampleSize**, and **PKEY\_Video\_FrameRate** properties are optional. The Media Sharing service will expose them if they are available.

Properties in the **PKEY\_Audio\_\*** group apply only to files with an audio stream, and properties in the **PKEY\_Video\_\*** group apply only to files with a video stream.

## Windows Media Format SDK Mappings

The ASF media source maps the following property keys to ASF header attributes. In some cases, the data types differ between the Shell property and the Format SDK attribute.



| PROPERTYKEY                              | Format SDK Attribute                                                  |
|------------------------------------------|-----------------------------------------------------------------------|
| **PKEY\_Audio\_IsVariableBitRate**       | [**IsVBR**](wmformat.isvbr)                                           |
| **PKEY\_Audio\_PeakValue**               | [**PeakValue**](wmformat.peakvalue)                                   |
| **PKEY\_Author**                         | [**Author**](wmformat.author)                                         |
| **PKEY\_Comment**                        | [**Description**](wmformat.description)                               |
| **PKEY\_Copyright**                      | [**Copyright**](wmformat.copyright)                                   |
| **PKEY\_DRM\_IsProtected**               | [**Is\_Protected**](wmformat.is_protected)                            |
| **PKEY\_Keywords**                       | [**WM/Category**](wmformat.wm_category)                               |
| **PKEY\_Language**                       | [**WM/Language**](wmformat.wm_language)                               |
| **PKEY\_Media\_AuthorUrl**               | [**WM/AuthorURL**](wmformat.wm_authorurl)                             |
| **PKEY\_Media\_AverageLevel**            | [**AverageLevel**](wmformat.averagelevel)                             |
| **PKEY\_Media\_ClassPrimaryID**          | [**WM/MediaClassPrimaryID**](wmformat.wm_mediaprimaryid)              |
| **PKEY\_Media\_ClassSecondaryID**        | [**WM/MediaClassSecondaryID**](wmformat.wm_mediasecondaryid)          |
| **PKEY\_Media\_CollectionGroupID**       | [**WM/WMCollectionGroupID**](wmformat.wm_wmcollectiongroupid)         |
| **PKEY\_Media\_CollectionID**            | [**WM/WMCollectionID**](wmformat.wm_wmcollectionid)                   |
| **PKEY\_Media\_ContentDistributor**      | [**WM/ContentDistributor**](wmformat.wm_contentdistributor)           |
| **PKEY\_Media\_ContentID**               | [**WM/WMContentID**](wmformat.wm_wmcontentid)                         |
| **PKEY\_Media\_DateEncoded**             | [**WM/EncodingTime**](wmformat.wm_encodingtime)                       |
| **PKEY\_Media\_DateReleased**            | [**WM/OriginalReleaseTime**](wmformat.wm_originalreleasetime)         |
| **PKEY\_Media\_DVDID**                   | [**WM/DVDID**](wmformat.wm_dvdid)                                     |
| **PKEY\_Media\_EncodedBy**               | [**WM/EncodedBy**](wmformat.wm_encodedby)                             |
| **PKEY\_Media\_EncodingSettings**        | [**WM/EncodingSettings**](wmformat.wm_encodingsettings)               |
| **PKEY\_Media\_MCDI**                    | [**WM/MCDI**](wmformat.wm_mcdi)                                       |
| **PKEY\_Media\_MetadataContentProvider** | [**WM/Provider**](wmformat.wm_provider)                               |
| **PKEY\_Media\_Producer**                | [**WM/Producer**](wmformat.wm_producer)                               |
| **PKEY\_Media\_PromotionUrl**            | [**WM/PromotionURL**](wmformat.wm_promotionurl)                       |
| **PKEY\_Media\_ProviderRating**          | [**WM/ProviderRating**](wmformat.wm_providerrating)                   |
| **PKEY\_Media\_ProviderStyle**           | [**WM/ProviderStyle**](wmformat.wm_providerstyle)                     |
| **PKEY\_Media\_Publisher**               | [**WM/Publisher**](wmformat.wm_publisher)                             |
| **PKEY\_Media\_SubTitle**                | [**WM/SubTitleDescription**](wmformat.wm_subtitledescription)         |
| **PKEY\_Media\_UniqueFileIdentifier**    | [**WM/UniqueFileIdentifier**](wmformat.wm_uniquefileidentifier)       |
| **PKEY\_Media\_Writer**                  | [**WM/Writer**](wmformat.wm_writer)                                   |
| **PKEY\_Media\_Year**                    | [**WM/Year**](wmformat.wm_year)                                       |
| **PKEY\_Music\_AlbumArtist**             | [**WM/AlbumArtist**](wmformat.wm_albumartist)                         |
| **PKEY\_Music\_AlbumTitle**              | [**WM/AlbumTitle**](wmformat.wm_albumtitle)                           |
| **PKEY\_Music\_Artist**                  | [**Author**](wmformat.author)                                         |
| **PKEY\_Music\_BeatsPerMinute**          | [**WM/BeatsPerMinute**](wmformat.wm_beatsperminute)                   |
| **PKEY\_Music\_Composer**                | [**WM/Composer**](wmformat.wm_composer)                               |
| **PKEY\_Music\_Conductor**               | [**WM/Conductor**](wmformat.wm_conductor)                             |
| **PKEY\_Music\_ContentGroupDescription** | [**WM/ContentGroupDescription**](wmformat.wm_contentgroupdescription) |
| **PKEY\_Music\_Genre**                   | [**WM/Genre**](wmformat.wm_genre)                                     |
| **PKEY\_Music\_InitialKey**              | [**WM/InitialKey**](wmformat.wm_initialkey)                           |
| **PKEY\_Music\_IsCompilation**           | **WM/IsCompilation**                                                  |
| **PKEY\_Music\_Lyrics**                  | [**WM/Lyrics**](wmformat.wm_lyrics)                                   |
| **PKEY\_Music\_Mood**                    | [**WM/Mood**](wmformat.wm_mood)                                       |
| **PKEY\_Music\_PartOfSet**               | [**WM/PartOfSet**](wmformat.wm_partofset)                             |
| **PKEY\_Music\_Period**                  | [**WM/Period**](wmformat.wm_period)                                   |
| **PKEY\_Music\_TrackNumber**             | [**WM/TrackNumber**](wmformat.wm_tracknumber)                         |
| **PKEY\_ParentalRating**                 | [**WM/ParentalRating**](wmformat.wm_parentalrating)                   |
| **PKEY\_ParentalRatingReason**           | [**WM/ParentalRatingReason**](wmformat.wm_parentalratingreason)       |
| **PKEY\_Rating**                         | [**WM/SharedUserRating**](wmformat.wm_shareduserrating)               |
| **PKEY\_ThumbnailStream**                | [**WM/Picture**](wmformat.wm_picture_attribute)                       |
| **PKEY\_Title**                          | [**Title**](wmformat.title)                                           |
| **PKEY\_Video\_Director**                | [**WM/Director**](wmformat.wm_director)                               |



 

## Related topics

<dl> <dt>

[Media Metadata](media-metadata.md)
</dt> <dt>

[Shell Metadata Providers](shell-metadata-providers.md)
</dt> </dl>

 

 



