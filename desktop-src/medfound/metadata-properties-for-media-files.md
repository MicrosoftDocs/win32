---
description: This topic lists the most common metadata properties for media files.
ms.assetid: 35187720-413a-45a0-8558-918f7c3161e1
title: Metadata Properties for Media Files
ms.topic: article
ms.date: 05/31/2018
---

# Metadata Properties for Media Files

This topic lists the most common metadata properties for media files.

-   [Common Media Properties](#common-media-properties)
-   [Media Sharing Properties](#media-sharing-properties)
-   [Windows Media Format SDK Mappings](#windows-media-format-sdk-mappings)
-   [Related topics](#related-topics)

## Common Media Properties

The Shell property system defines a set of common metadata properties for all types of shell objects. A subset of these are applicable to media files. The following table lists the most common Shell properties for media. Media files might support additional properties not listed here. Also, not every file format supports every property listed. For a complete list of Shell properties, see [Shell Properties](/previous-versions//ff521730(v=vs.85)).



| PROPERTYKEY                                                              | Shell Name                                                                                    | Description                                                                                                                                                                                               | Data Type    |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [MFPKEY\_Content\_DLNA\_Profile\_ID](mfpkey-content-dlna-profile-id.md) | None                                                                                          | Digital Living Network Alliance (DLNA) profile identifier.                                                                                                                                                | VT\_LPWSTR   |
| **PKEY\_Audio\_ChannelCount**                                            | [System.Audio.ChannelCount](../properties/props-system-audio-channelcount.md)                       | Number of audio channels.                                                                                                                                                                                 | VT\_UI4      |
| **PKEY\_Audio\_EncodingBitrate**                                         | [System.Audio.EncodingBitrate](../properties/props-system-audio-encodingbitrate.md)                 | Average audio bit rate, in bits per second.                                                                                                                                                               | VT\_UI4      |
| **PKEY\_Audio\_Format**                                                  | [System.Audio.Format](../properties/props-system-audio-format.md)                                   | Audio subtype ([**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)) expressed as a string.                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Audio\_IsVariableBitRate**                                       | [System.Audio.IsVariableBitRate](../properties/props-system-audio-isvariablebitrate.md)             | Indicates whether the audio stream uses variable bit-rate encoding.                                                                                                                                       | VT\_BOOL     |
| **PKEY\_Audio\_PeakValue**                                               | [System.Audio.PeakValue](../properties/props-system-audio-peakvalue.md)                             | Peak volume level of audio content.                                                                                                                                                                       | VT\_UI4      |
| **PKEY\_Audio\_SampleRate**                                              | [System.Audio.SampleRate](../properties/props-system-audio-samplerate.md)                           | Audio sample rate in samples per second. Equivalent to the [**MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND**](mf-mt-audio-samples-per-second-attribute.md) attribute in the media type.                           | VT\_UI4      |
| **PKEY\_Audio\_SampleSize**                                              | [System.Audio.SampleSize](../properties/props-system-audio-samplesize.md)                           | Number of bits per audio sample. Equivalent to the [**MF\_MT\_AUDIO\_BITS\_PER\_SAMPLE**](mf-mt-audio-bits-per-sample-attribute.md) attribute in the media type.                                         | VT\_UI4      |
| **PKEY\_Audio\_StreamNumber**                                            | [System.Audio.StreamNumber](../properties/props-system-audio-streamnumber.md)                       | Identifier of the audio stream.                                                                                                                                                                           | VT\_UI4      |
| **PKEY\_Author**                                                         | [System.Author](../properties/props-system-author.md)                                               | Author.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Comment**                                                        | [System.Comment](../properties/props-system-comment.md)                                             | A comment attached to a file, typically added by a user.                                                                                                                                                  | VT\_LPWSTR   |
| **PKEY\_Copyright**                                                      | [System.Copyright](../properties/props-system-copyright.md)                                         | Copyright information.                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_DRM\_IsProtected**                                               | [System.DRM.IsProtected](../properties/props-system-drm-isprotected.md)                             | Indicates whether the content is protected using digital rights management (DRM).                                                                                                                         | VT\_BOOL     |
| **PKEY\_Keywords**                                                       | [System.Keywords](../properties/props-system-keywords.md)                                           | Keywords.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Language**                                                       | [System.Language](../properties/props-system-language.md)                                           | Language.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_AuthorUrl**                                               | [System.Media.AuthorUrl](../properties/props-system-media-authorurl.md)                             | URL of the author's website.                                                                                                                                                                              | VT\_LPWSTR   |
| **PKEY\_Media\_AverageLevel**                                            | [System.Media.AverageLevel](../properties/props-system-media-averagelevel.md)                       | Average volume level of audio content.                                                                                                                                                                    | VT\_UI4      |
| **PKEY\_Media\_ClassPrimaryID**                                          | [System.Media.ClassPrimaryID](../properties/props-system-media-classprimaryid.md)                   | The string representation of a GUID that identifies the primary class of media. For valid values, see the documentation for the [**WM/MediaClassPrimaryID**](../wmformat/wm-mediaprimaryid.md) attribute.       | VT\_LPWSTR   |
| **PKEY\_Media\_ClassSecondaryID**                                        | [System.Media.ClassSecondaryID](../properties/props-system-media-classsecondaryid.md)               | The string representation of a GUID that identifies the secondary class of media. For valid values, see the documentation for the [**WM/MediaClassSecondaryID**](../wmformat/wm-mediasecondaryid.md) attribute. | VT\_LPWSTR   |
| **PKEY\_Media\_CollectionGroupID**                                       | [System.Media.CollectionGroupID](../properties/props-system-media-collectiongroupid.md)             | The string representation of a GUID that identifies the collection group.                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_CollectionID**                                            | [System.Media.CollectionID](../properties/props-system-media-collectionid.md)                       | The string representation of a GUID that identifies the collection.                                                                                                                                       | VT\_LPWSTR   |
| **PKEY\_Media\_ContentDistributor**                                      | [System.Media.ContentDistributor](../properties/props-system-media-contentdistributor.md)           | Distributor of the content.                                                                                                                                                                               | VT\_LPWSTR   |
| **PKEY\_Media\_ContentID**                                               | [System.Media.ContentID](../properties/props-system-media-contentid.md)                             | The string representation of a GUID that identifies the collection.                                                                                                                                       | VT\_LPWSTR   |
| **PKEY\_Media\_DateEncoded**                                             | [System.Media.DateEncoded](../properties/props-system-media-dateencoded.md)                         | Time when the content was encoded.                                                                                                                                                                        | VT\_FILETIME |
| **PKEY\_Media\_DateReleased**                                            | [System.Media.DateReleased](../properties/props-system-media-datereleased.md)                       | Original release date.                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Media\_Duration**                                                | [System.Media.Duration](../properties/props-system-media-duration.md)                               | Duration, in 100-nanosecond units. Equivalent to the [**MF\_PD\_DURATION**](mf-pd-duration-attribute.md) attribute in the presentation descriptor.                                                       | VT\_UI8      |
| **PKEY\_Media\_DVDID**                                                   | [System.Media.DVDID](../properties/props-system-media-dvdid.md)                                     | Digital video disc identifier (DVDID).                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Media\_EncodedBy**                                               | [System.Media.EncodedBy](../properties/props-system-media-encodedby.md)                             | Name of the person or group that encoded the content.                                                                                                                                                     | VT\_LPWSTR   |
| **PKEY\_Media\_EncodingSettings**                                        | [System.Media.EncodingSettings](../properties/props-system-media-encodingsettings.md)               | Description of the settings used to encode the content.                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Media\_MCDI**                                                    | [System.Media.MCDI](../properties/props-system-media-mcdi.md)                                       | Music CD identifier. This value is used to identify a CD.                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_MetadataContentProvider**                                 | [System.Media.MetadataContentProvider](../properties/props-system-media-metadatacontentprovider.md) | Name of the metadata content provider. (For example, metadata might be provided by a commercial service.)                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_Producer**                                                | [System.Media.Producer](../properties/props-system-media-producer.md)                               | Name of the producer of the content.                                                                                                                                                                      | VT\_LPWSTR   |
| **PKEY\_Media\_PromotionUrl**                                            | [System.Media.PromotionUrl](../properties/props-system-media-promotionurl.md)                       | URL of a website offering a promotion related to the content.                                                                                                                                             | VT\_LPWSTR   |
| **PKEY\_Media\_ProviderRating**                                          | [System.Media.ProviderRating](../properties/props-system-media-providerrating.md)                   | Rating of the content as assigned by the metadata content provider.                                                                                                                                       | VT\_LPWSTR   |
| **PKEY\_Media\_ProviderStyle**                                           | [System.Media.ProviderStyle](../properties/props-system-media-providerstyle.md)                     | Style or genre of the content as assigned by the metadata content provider.                                                                                                                               | VT\_LPWSTR   |
| **PKEY\_Media\_Publisher**                                               | [System.Media.Publisher](../properties/props-system-media-publisher.md)                             | Publisher.                                                                                                                                                                                                | VT\_LPWSTR   |
| **PKEY\_Media\_SubTitle**                                                | [System.Media.SubTitle](../properties/props-system-media-subtitle.md)                               | Subtitle.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_UniqueFileIdentifier**                                    | [System.Media.UniqueFileIdentifier](../properties/props-system-media-uniquefileidentifier.md)       | A generic string that can be to identify the file.                                                                                                                                                        | VT\_LPWSTR   |
| **PKEY\_Media\_Writer**                                                  | [System.Media.Writer](../properties/props-system-media-writer.md)                                   | Writer.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Media\_Year**                                                    | [System.Media.Year](../properties/props-system-media-year.md)                                       | Year the content was published.                                                                                                                                                                           | VT\_UI4      |
| **PKEY\_Music\_AlbumArtist**                                             | [System.Music.AlbumArtist](../properties/props-system-music-albumartist.md)                         | Primary artist for the album. This attribute can be used to distinguish the primary artist for an album from an artist who collaborated on a particular track.                                            | VT\_LPWSTR   |
| **PKEY\_Music\_AlbumTitle**                                              | [System.Music.AlbumTitle](../properties/props-system-music-albumtitle.md)                           | Album title.                                                                                                                                                                                              | VT\_LPWSTR   |
| **PKEY\_Music\_Artist**                                                  | [System.Music.Artist](../properties/props-system-music-artist.md)                                   | Artist.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Music\_BeatsPerMinute**                                          | [System.Music.BeatsPerMinute](../properties/props-system-music-beatsperminute.md)                   | Beats per minute.                                                                                                                                                                                         | VT\_LPWSTR   |
| **PKEY\_Music\_Composer**                                                | [System.Music.Composer](../properties/props-system-music-composer.md)                               | Composer.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Music\_Conductor**                                               | [System.Music.Conductor](../properties/props-system-music-conductor.md)                             | Conductor.                                                                                                                                                                                                | VT\_LPWSTR   |
| **PKEY\_Music\_ContentGroupDescription**                                 | [System.Music.ContentGroupDescription](../properties/props-system-music-contentgroupdescription.md) | Description of the content group (for example, boxed set or series).                                                                                                                                      | VT\_LPWSTR   |
| **PKEY\_Music\_Genre**                                                   | [System.Music.Genre](../properties/props-system-music-genre.md)                                     | Genre.                                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Music\_InitialKey**                                              | [System.Music.InitialKey](../properties/props-system-music-initialkey.md)                           | The initial key of the music.                                                                                                                                                                             | VT\_LPWSTR   |
| **PKEY\_Music\_IsCompilation**                                           | [System.Music.IsCompilation](../properties/props-system-music-iscompilation.md)                     | Indicates whether the music file is part of a compilation.                                                                                                                                                | VT\_BOOL     |
| **PKEY\_Music\_Lyrics**                                                  | [System.Music.Lyrics](../properties/props-system-music-lyrics.md)                                   | Lyrics.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Music\_Mood**                                                    | [System.Music.Mood](../properties/props-system-music-mood.md)                                       | Mood.                                                                                                                                                                                                     | VT\_LPWSTR   |
| **PKEY\_Music\_PartOfSet**                                               | [System.Music.PartOfSet](../properties/props-system-music-partofset.md)                             | The part number and the total number of parts in the set to which the file belongs, separated by a slash.                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Music\_Period**                                                  | [System.Music.Period](../properties/props-system-music-period.md)                                   | Period.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Music\_TrackNumber**                                             | [System.Music.TrackNumber](../properties/props-system-music-tracknumber.md)                         | Track number.                                                                                                                                                                                             | VT\_UI4      |
| **PKEY\_ParentalRating**                                                 | [System.ParentalRating](../properties/props-system-parentalrating.md)                               | Parental rating.                                                                                                                                                                                          | VT\_LPWSTR   |
| **PKEY\_ParentalRatingReason**                                           | [System.ParentalRatingReason](../properties/props-system-parentalratingreason.md)                   | Reasons for the assigned parental rating.                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Rating**                                                         | [System.Rating](../properties/props-system-rating.md)                                               | User rating.                                                                                                                                                                                              | VT\_UI4      |
| **PKEY\_ThumbnailStream**                                                | [System.ThumbnailStream](../properties/props-system-thumbnailstream.md)                             | Thumbnail image.                                                                                                                                                                                          | VT\_STREAM   |
| **PKEY\_Title**                                                          | [System.Title](../properties/props-system-title.md)                                                 | Title.                                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Video\_Compression**                                             | [System.Video.Compression](../properties/props-system-video-compression.md)                         | Video subtype ([**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)) expressed as a string.                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Video\_Director**                                                | [System.Video.Director](../properties/props-system-video-director.md)                               | Director.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Video\_EncodingBitrate**                                         | [System.Video.EncodingBitrate](../properties/props-system-video-encodingbitrate.md)                 | Average video bit rate, in bits per second.                                                                                                                                                               | VT\_UI4      |
| **PKEY\_Video\_FourCC**                                                  | [System.Video.FourCC](../properties/props-system-video-fourcc.md)                                   | The **FOURCC** of the video encoding format. Applies only if the video subtype can be expressed as a **FOURCC** value.                                                                                    | VT\_UI4      |
| **PKEY\_Video\_FrameHeight**                                             | [System.Video.FrameHeight](../properties/props-system-video-frameheight.md)                         | Video frame height.                                                                                                                                                                                       | VT\_UI4      |
| **PKEY\_Video\_FrameRate**                                               | [System.Video.FrameRate](../properties/props-system-video-framerate.md)                             | Video frame rate, expressed as frames per second × 1000.                                                                                                                                                  | VT\_UI4      |
| **PKEY\_Video\_FrameWidth**                                              | [System.Video.FrameWidth](../properties/props-system-video-framewidth.md)                           | Video frame width.                                                                                                                                                                                        | VT\_UI4      |
| **PKEY\_Video\_HorizontalAspectRatio**                                   | [System.Video.HorizontalAspectRatio](../properties/props-system-video-horizontalaspectratio.md)     | The horizontal component of the pixel aspect ratio. (Equivalent to the numerator of the [**MF\_MT\_PIXEL\_ASPECT\_RATIO**](mf-mt-pixel-aspect-ratio-attribute.md) attribute in the media type.)          | VT\_UI4      |
| **PKEY\_Video\_IsStereo**                                                | [System.Video.IsStereo](/previous-versions//mt744507(v=vs.85))                                     | Indicates whether the video stream contains stereo video content.                                                                                                                                         | VT\_BOOL     |
| **PKEY\_Video\_StreamNumber**                                            | [System.Video.StreamNumber](../properties/props-system-video-streamnumber.md)                       | Identifier of the video stream.                                                                                                                                                                           | VT\_UI4      |
| **PKEY\_Video\_TotalBitrate**                                            | [System.Video.TotalBitrate](../properties/props-system-video-totalbitrate.md)                       | Total data rate for all video and audio streams, in bits per second. (Applies only to files with at least one video stream.)                                                                              | VT\_UI4      |
| **PKEY\_Video\_VerticalAspectRatio**                                     | [System.Video.VerticalAspectRatio](../properties/props-system-video-verticalaspectratio.md)         | The vertical component of the pixel aspect ratio. (Equivalent to the denominator of the [**MF\_MT\_PIXEL\_ASPECT\_RATIO**](mf-mt-pixel-aspect-ratio-attribute.md) attribute in the media type.)          | VT\_UI4      |



 

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
| **PKEY\_Audio\_IsVariableBitRate**       | [**IsVBR**](../wmformat/isvbr.md)                                           |
| **PKEY\_Audio\_PeakValue**               | [**PeakValue**](../wmformat/peakvalue.md)                                   |
| **PKEY\_Author**                         | [**Author**](../wmformat/author.md)                                         |
| **PKEY\_Comment**                        | [**Description**](../wmformat/description.md)                               |
| **PKEY\_Copyright**                      | [**Copyright**](../wmformat/copyright.md)                                   |
| **PKEY\_DRM\_IsProtected**               | [**Is\_Protected**](../wmformat/is-protected.md)                            |
| **PKEY\_Keywords**                       | [**WM/Category**](../wmformat/wm-category.md)                               |
| **PKEY\_Language**                       | [**WM/Language**](../wmformat/wm-language.md)                               |
| **PKEY\_Media\_AuthorUrl**               | [**WM/AuthorURL**](../wmformat/wm-authorurl.md)                             |
| **PKEY\_Media\_AverageLevel**            | [**AverageLevel**](../wmformat/averagelevel.md)                             |
| **PKEY\_Media\_ClassPrimaryID**          | [**WM/MediaClassPrimaryID**](../wmformat/wm-mediaprimaryid.md)              |
| **PKEY\_Media\_ClassSecondaryID**        | [**WM/MediaClassSecondaryID**](../wmformat/wm-mediasecondaryid.md)          |
| **PKEY\_Media\_CollectionGroupID**       | [**WM/WMCollectionGroupID**](../wmformat/wm-wmcollectiongroupid.md)         |
| **PKEY\_Media\_CollectionID**            | [**WM/WMCollectionID**](../wmformat/wm-wmcollectionid.md)                   |
| **PKEY\_Media\_ContentDistributor**      | [**WM/ContentDistributor**](../wmformat/wm-contentdistributor.md)           |
| **PKEY\_Media\_ContentID**               | [**WM/WMContentID**](../wmformat/wm-wmcontentid.md)                         |
| **PKEY\_Media\_DateEncoded**             | [**WM/EncodingTime**](../wmformat/wm-encodingtime.md)                       |
| **PKEY\_Media\_DateReleased**            | [**WM/OriginalReleaseTime**](../wmformat/wm-originalreleasetime.md)         |
| **PKEY\_Media\_DVDID**                   | [**WM/DVDID**](../wmformat/wm-dvdid.md)                                     |
| **PKEY\_Media\_EncodedBy**               | [**WM/EncodedBy**](../wmformat/wm-encodedby.md)                             |
| **PKEY\_Media\_EncodingSettings**        | [**WM/EncodingSettings**](../wmformat/wm-encodingsettings.md)               |
| **PKEY\_Media\_MCDI**                    | [**WM/MCDI**](../wmformat/wm-mcdi.md)                                       |
| **PKEY\_Media\_MetadataContentProvider** | [**WM/Provider**](../wmformat/wm-provider.md)                               |
| **PKEY\_Media\_Producer**                | [**WM/Producer**](../wmformat/wm-producer.md)                               |
| **PKEY\_Media\_PromotionUrl**            | [**WM/PromotionURL**](../wmformat/wm-promotionurl.md)                       |
| **PKEY\_Media\_ProviderRating**          | [**WM/ProviderRating**](../wmformat/wm-providerrating.md)                   |
| **PKEY\_Media\_ProviderStyle**           | [**WM/ProviderStyle**](../wmformat/wm-providerstyle.md)                     |
| **PKEY\_Media\_Publisher**               | [**WM/Publisher**](../wmformat/wm-publisher.md)                             |
| **PKEY\_Media\_SubTitle**                | [**WM/SubTitleDescription**](../wmformat/wm-subtitledescription.md)         |
| **PKEY\_Media\_UniqueFileIdentifier**    | [**WM/UniqueFileIdentifier**](../wmformat/wm-uniquefileidentifier.md)       |
| **PKEY\_Media\_Writer**                  | [**WM/Writer**](../wmformat/wm-writer.md)                                   |
| **PKEY\_Media\_Year**                    | [**WM/Year**](../wmformat/wm-year.md)                                       |
| **PKEY\_Music\_AlbumArtist**             | [**WM/AlbumArtist**](../wmformat/wm-albumartist.md)                         |
| **PKEY\_Music\_AlbumTitle**              | [**WM/AlbumTitle**](../wmformat/wm-albumtitle.md)                           |
| **PKEY\_Music\_Artist**                  | [**Author**](../wmformat/author.md)                                         |
| **PKEY\_Music\_BeatsPerMinute**          | [**WM/BeatsPerMinute**](../wmformat/wm-beatsperminute.md)                   |
| **PKEY\_Music\_Composer**                | [**WM/Composer**](../wmformat/wm-composer.md)                               |
| **PKEY\_Music\_Conductor**               | [**WM/Conductor**](../wmformat/wm-conductor.md)                             |
| **PKEY\_Music\_ContentGroupDescription** | [**WM/ContentGroupDescription**](../wmformat/wm-contentgroupdescription.md) |
| **PKEY\_Music\_Genre**                   | [**WM/Genre**](../wmformat/wm-genre.md)                                     |
| **PKEY\_Music\_InitialKey**              | [**WM/InitialKey**](../wmformat/wm-initialkey.md)                           |
| **PKEY\_Music\_IsCompilation**           | **WM/IsCompilation**                                                  |
| **PKEY\_Music\_Lyrics**                  | [**WM/Lyrics**](../wmformat/wm-lyrics.md)                                   |
| **PKEY\_Music\_Mood**                    | [**WM/Mood**](../wmformat/wm-mood.md)                                       |
| **PKEY\_Music\_PartOfSet**               | [**WM/PartOfSet**](../wmformat/wm-partofset.md)                             |
| **PKEY\_Music\_Period**                  | [**WM/Period**](../wmformat/wm-period.md)                                   |
| **PKEY\_Music\_TrackNumber**             | [**WM/TrackNumber**](../wmformat/wm-tracknumber.md)                         |
| **PKEY\_ParentalRating**                 | [**WM/ParentalRating**](../wmformat/wm-parentalrating.md)                   |
| **PKEY\_ParentalRatingReason**           | [**WM/ParentalRatingReason**](../wmformat/wm-parentalratingreason.md)       |
| **PKEY\_Rating**                         | [**WM/SharedUserRating**](../wmformat/wm-shareduserrating.md)               |
| **PKEY\_ThumbnailStream**                | [**WM/Picture**](../wmformat/wmpicture.md)                       |
| **PKEY\_Title**                          | [**Title**](../wmformat/title.md)                                           |
| **PKEY\_Video\_Director**                | [**WM/Director**](../wmformat/wm-director.md)                               |



 

## Related topics

<dl> <dt>

[Media Metadata](media-metadata.md)
</dt> <dt>

[Shell Metadata Providers](shell-metadata-providers.md)
</dt> </dl>

 

 
