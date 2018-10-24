---
Description: This topic lists the most common metadata properties for media files.
ms.assetid: 35187720-413a-45a0-8558-918f7c3161e1
title: Metadata Properties for Media Files
ms.author: windowssdkdev
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

The Shell property system defines a set of common metadata properties for all types of shell objects. A subset of these are applicable to media files. The following table lists the most common Shell properties for media. Media files might support additional properties not listed here. Also, not every file format supports every property listed. For a complete list of Shell properties, see [Shell Properties](https://msdn.microsoft.com/library/Ff521730(v=VS.85).aspx).



| PROPERTYKEY                                                              | Shell Name                                                                                    | Description                                                                                                                                                                                               | Data Type    |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [MFPKEY\_Content\_DLNA\_Profile\_ID](mfpkey-content-dlna-profile-id.md) | None                                                                                          | Digital Living Network Alliance (DLNA) profile identifier.                                                                                                                                                | VT\_LPWSTR   |
| **PKEY\_Audio\_ChannelCount**                                            | [System.Audio.ChannelCount](https://msdn.microsoft.com/en-us/library/Bb787782(v=VS.85).aspx)                       | Number of audio channels.                                                                                                                                                                                 | VT\_UI4      |
| **PKEY\_Audio\_EncodingBitrate**                                         | [System.Audio.EncodingBitrate](https://msdn.microsoft.com/en-us/library/Bb773922(v=VS.85).aspx)                 | Average audio bit rate, in bits per second.                                                                                                                                                               | VT\_UI4      |
| **PKEY\_Audio\_Format**                                                  | [System.Audio.Format](https://msdn.microsoft.com/en-us/library/Bb773924(v=VS.85).aspx)                                   | Audio subtype ([**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)) expressed as a string.                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Audio\_IsVariableBitRate**                                       | [System.Audio.IsVariableBitRate](https://msdn.microsoft.com/en-us/library/Bb773926(v=VS.85).aspx)             | Indicates whether the audio stream uses variable bit-rate encoding.                                                                                                                                       | VT\_BOOL     |
| **PKEY\_Audio\_PeakValue**                                               | [System.Audio.PeakValue](https://msdn.microsoft.com/en-us/library/Bb773928(v=VS.85).aspx)                             | Peak volume level of audio content.                                                                                                                                                                       | VT\_UI4      |
| **PKEY\_Audio\_SampleRate**                                              | [System.Audio.SampleRate](https://msdn.microsoft.com/en-us/library/Bb773930(v=VS.85).aspx)                           | Audio sample rate in samples per second. Equivalent to the [**MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND**](mf-mt-audio-samples-per-second-attribute.md) attribute in the media type.                           | VT\_UI4      |
| **PKEY\_Audio\_SampleSize**                                              | [System.Audio.SampleSize](https://msdn.microsoft.com/en-us/library/Bb773932(v=VS.85).aspx)                           | Number of bits per audio sample. Equivalent to the [**MF\_MT\_AUDIO\_BITS\_PER\_SAMPLE**](mf-mt-audio-bits-per-sample-attribute.md) attribute in the media type.                                         | VT\_UI4      |
| **PKEY\_Audio\_StreamNumber**                                            | [System.Audio.StreamNumber](https://msdn.microsoft.com/en-us/library/Bb773936(v=VS.85).aspx)                       | Identifier of the audio stream.                                                                                                                                                                           | VT\_UI4      |
| **PKEY\_Author**                                                         | [System.Author](https://msdn.microsoft.com/en-us/library/Bb760652(v=VS.85).aspx)                                               | Author.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Comment**                                                        | [System.Comment](https://msdn.microsoft.com/en-us/library/Bb760658(v=VS.85).aspx)                                             | A comment attached to a file, typically added by a user.                                                                                                                                                  | VT\_LPWSTR   |
| **PKEY\_Copyright**                                                      | [System.Copyright](https://msdn.microsoft.com/en-us/library/Bb760671(v=VS.85).aspx)                                         | Copyright information.                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_DRM\_IsProtected**                                               | [System.DRM.IsProtected](https://msdn.microsoft.com/en-us/library/Bb760607(v=VS.85).aspx)                             | Indicates whether the content is protected using digital rights management (DRM).                                                                                                                         | VT\_BOOL     |
| **PKEY\_Keywords**                                                       | [System.Keywords](https://msdn.microsoft.com/en-us/library/Bb787519(v=VS.85).aspx)                                           | Keywords.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Language**                                                       | [System.Language](https://msdn.microsoft.com/en-us/library/Bb787525(v=VS.85).aspx)                                           | Language.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_AuthorUrl**                                               | [System.Media.AuthorUrl](https://msdn.microsoft.com/en-us/library/Bb787376(v=VS.85).aspx)                             | URL of the author's website.                                                                                                                                                                              | VT\_LPWSTR   |
| **PKEY\_Media\_AverageLevel**                                            | [System.Media.AverageLevel](https://msdn.microsoft.com/en-us/library/Bb787378(v=VS.85).aspx)                       | Average volume level of audio content.                                                                                                                                                                    | VT\_UI4      |
| **PKEY\_Media\_ClassPrimaryID**                                          | [System.Media.ClassPrimaryID](https://msdn.microsoft.com/en-us/library/Bb787380(v=VS.85).aspx)                   | The string representation of a GUID that identifies the primary class of media. For valid values, see the documentation for the [**WM/MediaClassPrimaryID**](https://msdn.microsoft.com/en-us/library/Dd757959(v=VS.85).aspx) attribute.       | VT\_LPWSTR   |
| **PKEY\_Media\_ClassSecondaryID**                                        | [System.Media.ClassSecondaryID](https://msdn.microsoft.com/en-us/library/Bb787382(v=VS.85).aspx)               | The string representation of a GUID that identifies the secondary class of media. For valid values, see the documentation for the [**WM/MediaClassSecondaryID**](https://msdn.microsoft.com/en-us/library/Dd757960(v=VS.85).aspx) attribute. | VT\_LPWSTR   |
| **PKEY\_Media\_CollectionGroupID**                                       | [System.Media.CollectionGroupID](https://msdn.microsoft.com/en-us/library/Bb787384(v=VS.85).aspx)             | The string representation of a GUID that identifies the collection group.                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_CollectionID**                                            | [System.Media.CollectionID](https://msdn.microsoft.com/en-us/library/Bb787386(v=VS.85).aspx)                       | The string representation of a GUID that identifies the collection.                                                                                                                                       | VT\_LPWSTR   |
| **PKEY\_Media\_ContentDistributor**                                      | [System.Media.ContentDistributor](https://msdn.microsoft.com/en-us/library/Bb787388(v=VS.85).aspx)           | Distributor of the content.                                                                                                                                                                               | VT\_LPWSTR   |
| **PKEY\_Media\_ContentID**                                               | [System.Media.ContentID](https://msdn.microsoft.com/en-us/library/Bb787390(v=VS.85).aspx)                             | The string representation of a GUID that identifies the collection.                                                                                                                                       | VT\_LPWSTR   |
| **PKEY\_Media\_DateEncoded**                                             | [System.Media.DateEncoded](https://msdn.microsoft.com/en-us/library/Bb787395(v=VS.85).aspx)                         | Time when the content was encoded.                                                                                                                                                                        | VT\_FILETIME |
| **PKEY\_Media\_DateReleased**                                            | [System.Media.DateReleased](https://msdn.microsoft.com/en-us/library/Bb787397(v=VS.85).aspx)                       | Original release date.                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Media\_Duration**                                                | [System.Media.Duration](https://msdn.microsoft.com/en-us/library/Bb787399(v=VS.85).aspx)                               | Duration, in 100-nanosecond units. Equivalent to the [**MF\_PD\_DURATION**](mf-pd-duration-attribute.md) attribute in the presentation descriptor.                                                       | VT\_UI8      |
| **PKEY\_Media\_DVDID**                                                   | [System.Media.DVDID](https://msdn.microsoft.com/en-us/library/Bb787400(v=VS.85).aspx)                                     | Digital video disc identifier (DVDID).                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Media\_EncodedBy**                                               | [System.Media.EncodedBy](https://msdn.microsoft.com/en-us/library/Bb787401(v=VS.85).aspx)                             | Name of the person or group that encoded the content.                                                                                                                                                     | VT\_LPWSTR   |
| **PKEY\_Media\_EncodingSettings**                                        | [System.Media.EncodingSettings](https://msdn.microsoft.com/en-us/library/Bb787402(v=VS.85).aspx)               | Description of the settings used to encode the content.                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Media\_MCDI**                                                    | [System.Media.MCDI](https://msdn.microsoft.com/en-us/library/Bb787404(v=VS.85).aspx)                                       | Music CD identifier. This value is used to identify a CD.                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_MetadataContentProvider**                                 | [System.Media.MetadataContentProvider](https://msdn.microsoft.com/en-us/library/Bb787405(v=VS.85).aspx) | Name of the metadata content provider. (For example, metadata might be provided by a commercial service.)                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_Producer**                                                | [System.Media.Producer](https://msdn.microsoft.com/en-us/library/Bb787406(v=VS.85).aspx)                               | Name of the producer of the content.                                                                                                                                                                      | VT\_LPWSTR   |
| **PKEY\_Media\_PromotionUrl**                                            | [System.Media.PromotionUrl](https://msdn.microsoft.com/en-us/library/Bb787407(v=VS.85).aspx)                       | URL of a website offering a promotion related to the content.                                                                                                                                             | VT\_LPWSTR   |
| **PKEY\_Media\_ProviderRating**                                          | [System.Media.ProviderRating](https://msdn.microsoft.com/en-us/library/Bb787409(v=VS.85).aspx)                   | Rating of the content as assigned by the metadata content provider.                                                                                                                                       | VT\_LPWSTR   |
| **PKEY\_Media\_ProviderStyle**                                           | [System.Media.ProviderStyle](https://msdn.microsoft.com/en-us/library/Bb787410(v=VS.85).aspx)                     | Style or genre of the content as assigned by the metadata content provider.                                                                                                                               | VT\_LPWSTR   |
| **PKEY\_Media\_Publisher**                                               | [System.Media.Publisher](https://msdn.microsoft.com/en-us/library/Bb787411(v=VS.85).aspx)                             | Publisher.                                                                                                                                                                                                | VT\_LPWSTR   |
| **PKEY\_Media\_SubTitle**                                                | [System.Media.SubTitle](https://msdn.microsoft.com/en-us/library/Bb787414(v=VS.85).aspx)                               | Subtitle.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_UniqueFileIdentifier**                                    | [System.Media.UniqueFileIdentifier](https://msdn.microsoft.com/en-us/library/Bb787416(v=VS.85).aspx)       | A generic string that can be to identify the file.                                                                                                                                                        | VT\_LPWSTR   |
| **PKEY\_Media\_Writer**                                                  | [System.Media.Writer](https://msdn.microsoft.com/en-us/library/Bb787422(v=VS.85).aspx)                                   | Writer.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Media\_Year**                                                    | [System.Media.Year](https://msdn.microsoft.com/en-us/library/Bb787424(v=VS.85).aspx)                                       | Year the content was published.                                                                                                                                                                           | VT\_UI4      |
| **PKEY\_Music\_AlbumArtist**                                             | [System.Music.AlbumArtist](https://msdn.microsoft.com/en-us/library/Bb787290(v=VS.85).aspx)                         | Primary artist for the album. This attribute can be used to distinguish the primary artist for an album from an artist who collaborated on a particular track.                                            | VT\_LPWSTR   |
| **PKEY\_Music\_AlbumTitle**                                              | [System.Music.AlbumTitle](https://msdn.microsoft.com/en-us/library/Bb787292(v=VS.85).aspx)                           | Album title.                                                                                                                                                                                              | VT\_LPWSTR   |
| **PKEY\_Music\_Artist**                                                  | [System.Music.Artist](https://msdn.microsoft.com/en-us/library/Bb787294(v=VS.85).aspx)                                   | Artist.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Music\_BeatsPerMinute**                                          | [System.Music.BeatsPerMinute](https://msdn.microsoft.com/en-us/library/Bb787296(v=VS.85).aspx)                   | Beats per minute.                                                                                                                                                                                         | VT\_LPWSTR   |
| **PKEY\_Music\_Composer**                                                | [System.Music.Composer](https://msdn.microsoft.com/en-us/library/Bb787298(v=VS.85).aspx)                               | Composer.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Music\_Conductor**                                               | [System.Music.Conductor](https://msdn.microsoft.com/en-us/library/Bb787300(v=VS.85).aspx)                             | Conductor.                                                                                                                                                                                                | VT\_LPWSTR   |
| **PKEY\_Music\_ContentGroupDescription**                                 | [System.Music.ContentGroupDescription](https://msdn.microsoft.com/en-us/library/Bb787302(v=VS.85).aspx) | Description of the content group (for example, boxed set or series).                                                                                                                                      | VT\_LPWSTR   |
| **PKEY\_Music\_Genre**                                                   | [System.Music.Genre](https://msdn.microsoft.com/en-us/library/Bb787304(v=VS.85).aspx)                                     | Genre.                                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Music\_InitialKey**                                              | [System.Music.InitialKey](https://msdn.microsoft.com/en-us/library/Bb787306(v=VS.85).aspx)                           | The initial key of the music.                                                                                                                                                                             | VT\_LPWSTR   |
| **PKEY\_Music\_IsCompilation**                                           | [System.Music.IsCompilation](https://msdn.microsoft.com/en-us/library/Dd807136(v=VS.85).aspx)                     | Indicates whether the music file is part of a compilation.                                                                                                                                                | VT\_BOOL     |
| **PKEY\_Music\_Lyrics**                                                  | [System.Music.Lyrics](https://msdn.microsoft.com/en-us/library/Bb787308(v=VS.85).aspx)                                   | Lyrics.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Music\_Mood**                                                    | [System.Music.Mood](https://msdn.microsoft.com/en-us/library/Bb787310(v=VS.85).aspx)                                       | Mood.                                                                                                                                                                                                     | VT\_LPWSTR   |
| **PKEY\_Music\_PartOfSet**                                               | [System.Music.PartOfSet](https://msdn.microsoft.com/en-us/library/Bb787312(v=VS.85).aspx)                             | The part number and the total number of parts in the set to which the file belongs, separated by a slash.                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Music\_Period**                                                  | [System.Music.Period](https://msdn.microsoft.com/en-us/library/Bb787314(v=VS.85).aspx)                                   | Period.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Music\_TrackNumber**                                             | [System.Music.TrackNumber](https://msdn.microsoft.com/en-us/library/Bb787318(v=VS.85).aspx)                         | Track number.                                                                                                                                                                                             | VT\_UI4      |
| **PKEY\_ParentalRating**                                                 | [System.ParentalRating](https://msdn.microsoft.com/en-us/library/Bb787538(v=VS.85).aspx)                               | Parental rating.                                                                                                                                                                                          | VT\_LPWSTR   |
| **PKEY\_ParentalRatingReason**                                           | [System.ParentalRatingReason](https://msdn.microsoft.com/en-us/library/Bb787540(v=VS.85).aspx)                   | Reasons for the assigned parental rating.                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Rating**                                                         | [System.Rating](https://msdn.microsoft.com/en-us/library/Bb787554(v=VS.85).aspx)                                               | User rating.                                                                                                                                                                                              | VT\_UI4      |
| **PKEY\_ThumbnailStream**                                                | [System.ThumbnailStream](https://msdn.microsoft.com/en-us/library/Bb787582(v=VS.85).aspx)                             | Thumbnail image.                                                                                                                                                                                          | VT\_STREAM   |
| **PKEY\_Title**                                                          | [System.Title](https://msdn.microsoft.com/en-us/library/Bb787584(v=VS.85).aspx)                                                 | Title.                                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Video\_Compression**                                             | [System.Video.Compression](https://msdn.microsoft.com/en-us/library/Bb760032(v=VS.85).aspx)                         | Video subtype ([**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)) expressed as a string.                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Video\_Director**                                                | [System.Video.Director](https://msdn.microsoft.com/en-us/library/Bb760040(v=VS.85).aspx)                               | Director.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Video\_EncodingBitrate**                                         | [System.Video.EncodingBitrate](https://msdn.microsoft.com/en-us/library/Bb760049(v=VS.85).aspx)                 | Average video bit rate, in bits per second.                                                                                                                                                               | VT\_UI4      |
| **PKEY\_Video\_FourCC**                                                  | [System.Video.FourCC](https://msdn.microsoft.com/en-us/library/Bb760055(v=VS.85).aspx)                                   | The **FOURCC** of the video encoding format. Applies only if the video subtype can be expressed as a **FOURCC** value.                                                                                    | VT\_UI4      |
| **PKEY\_Video\_FrameHeight**                                             | [System.Video.FrameHeight](https://msdn.microsoft.com/en-us/library/Bb760057(v=VS.85).aspx)                         | Video frame height.                                                                                                                                                                                       | VT\_UI4      |
| **PKEY\_Video\_FrameRate**                                               | [System.Video.FrameRate](https://msdn.microsoft.com/en-us/library/Bb760066(v=VS.85).aspx)                             | Video frame rate, expressed as frames per second × 1000.                                                                                                                                                  | VT\_UI4      |
| **PKEY\_Video\_FrameWidth**                                              | [System.Video.FrameWidth](https://msdn.microsoft.com/en-us/library/Bb760077(v=VS.85).aspx)                           | Video frame width.                                                                                                                                                                                        | VT\_UI4      |
| **PKEY\_Video\_HorizontalAspectRatio**                                   | [System.Video.HorizontalAspectRatio](https://msdn.microsoft.com/en-us/library/Bb760084(v=VS.85).aspx)     | The horizontal component of the pixel aspect ratio. (Equivalent to the numerator of the [**MF\_MT\_PIXEL\_ASPECT\_RATIO**](mf-mt-pixel-aspect-ratio-attribute.md) attribute in the media type.)          | VT\_UI4      |
| **PKEY\_Video\_IsStereo**                                                | [System.Video.IsStereo](https://msdn.microsoft.com/library/Mt744507(v=VS.85).aspx)                                     | Indicates whether the video stream contains stereo video content.                                                                                                                                         | VT\_BOOL     |
| **PKEY\_Video\_StreamNumber**                                            | [System.Video.StreamNumber](https://msdn.microsoft.com/en-us/library/Bb760114(v=VS.85).aspx)                       | Identifier of the video stream.                                                                                                                                                                           | VT\_UI4      |
| **PKEY\_Video\_TotalBitrate**                                            | [System.Video.TotalBitrate](https://msdn.microsoft.com/en-us/library/Bb760124(v=VS.85).aspx)                       | Total data rate for all video and audio streams, in bits per second. (Applies only to files with at least one video stream.)                                                                              | VT\_UI4      |
| **PKEY\_Video\_VerticalAspectRatio**                                     | [System.Video.VerticalAspectRatio](https://msdn.microsoft.com/en-us/library/Bb760128(v=VS.85).aspx)         | The vertical component of the pixel aspect ratio. (Equivalent to the denominator of the [**MF\_MT\_PIXEL\_ASPECT\_RATIO**](mf-mt-pixel-aspect-ratio-attribute.md) attribute in the media type.)          | VT\_UI4      |



 

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
| **PKEY\_Audio\_IsVariableBitRate**       | [**IsVBR**](https://msdn.microsoft.com/en-us/library/Dd743276(v=VS.85).aspx)                                           |
| **PKEY\_Audio\_PeakValue**               | [**PeakValue**](https://msdn.microsoft.com/en-us/library/Dd757565(v=VS.85).aspx)                                   |
| **PKEY\_Author**                         | [**Author**](https://msdn.microsoft.com/en-us/library/Dd743073(v=VS.85).aspx)                                         |
| **PKEY\_Comment**                        | [**Description**](https://msdn.microsoft.com/en-us/library/Dd757024(v=VS.85).aspx)                               |
| **PKEY\_Copyright**                      | [**Copyright**](https://msdn.microsoft.com/en-us/library/Dd757009(v=VS.85).aspx)                                   |
| **PKEY\_DRM\_IsProtected**               | [**Is\_Protected**](https://msdn.microsoft.com/en-us/library/Dd743277(v=VS.85).aspx)                            |
| **PKEY\_Keywords**                       | [**WM/Category**](https://msdn.microsoft.com/en-us/library/Dd757902(v=VS.85).aspx)                               |
| **PKEY\_Language**                       | [**WM/Language**](https://msdn.microsoft.com/en-us/library/Dd757940(v=VS.85).aspx)                               |
| **PKEY\_Media\_AuthorUrl**               | [**WM/AuthorURL**](https://msdn.microsoft.com/en-us/library/Dd757899(v=VS.85).aspx)                             |
| **PKEY\_Media\_AverageLevel**            | [**AverageLevel**](https://msdn.microsoft.com/en-us/library/Dd743075(v=VS.85).aspx)                             |
| **PKEY\_Media\_ClassPrimaryID**          | [**WM/MediaClassPrimaryID**](https://msdn.microsoft.com/en-us/library/Dd757959(v=VS.85).aspx)              |
| **PKEY\_Media\_ClassSecondaryID**        | [**WM/MediaClassSecondaryID**](https://msdn.microsoft.com/en-us/library/Dd757960(v=VS.85).aspx)          |
| **PKEY\_Media\_CollectionGroupID**       | [**WM/WMCollectionGroupID**](https://msdn.microsoft.com/en-us/library/Dd758019(v=VS.85).aspx)         |
| **PKEY\_Media\_CollectionID**            | [**WM/WMCollectionID**](https://msdn.microsoft.com/en-us/library/Dd758020(v=VS.85).aspx)                   |
| **PKEY\_Media\_ContentDistributor**      | [**WM/ContentDistributor**](https://msdn.microsoft.com/en-us/library/Dd757909(v=VS.85).aspx)           |
| **PKEY\_Media\_ContentID**               | [**WM/WMContentID**](https://msdn.microsoft.com/en-us/library/Dd758021(v=VS.85).aspx)                         |
| **PKEY\_Media\_DateEncoded**             | [**WM/EncodingTime**](https://msdn.microsoft.com/en-us/library/Dd757916(v=VS.85).aspx)                       |
| **PKEY\_Media\_DateReleased**            | [**WM/OriginalReleaseTime**](https://msdn.microsoft.com/en-us/library/Dd757970(v=VS.85).aspx)         |
| **PKEY\_Media\_DVDID**                   | [**WM/DVDID**](https://msdn.microsoft.com/en-us/library/Dd757913(v=VS.85).aspx)                                     |
| **PKEY\_Media\_EncodedBy**               | [**WM/EncodedBy**](https://msdn.microsoft.com/en-us/library/Dd757914(v=VS.85).aspx)                             |
| **PKEY\_Media\_EncodingSettings**        | [**WM/EncodingSettings**](https://msdn.microsoft.com/en-us/library/Dd757915(v=VS.85).aspx)               |
| **PKEY\_Media\_MCDI**                    | [**WM/MCDI**](https://msdn.microsoft.com/en-us/library/Dd757945(v=VS.85).aspx)                                       |
| **PKEY\_Media\_MetadataContentProvider** | [**WM/Provider**](https://msdn.microsoft.com/en-us/library/Dd757983(v=VS.85).aspx)                               |
| **PKEY\_Media\_Producer**                | [**WM/Producer**](https://msdn.microsoft.com/en-us/library/Dd757980(v=VS.85).aspx)                               |
| **PKEY\_Media\_PromotionUrl**            | [**WM/PromotionURL**](https://msdn.microsoft.com/en-us/library/Dd757981(v=VS.85).aspx)                       |
| **PKEY\_Media\_ProviderRating**          | [**WM/ProviderRating**](https://msdn.microsoft.com/en-us/library/Dd757985(v=VS.85).aspx)                   |
| **PKEY\_Media\_ProviderStyle**           | [**WM/ProviderStyle**](https://msdn.microsoft.com/en-us/library/Dd757986(v=VS.85).aspx)                     |
| **PKEY\_Media\_Publisher**               | [**WM/Publisher**](https://msdn.microsoft.com/en-us/library/Dd757987(v=VS.85).aspx)                             |
| **PKEY\_Media\_SubTitle**                | [**WM/SubTitleDescription**](https://msdn.microsoft.com/en-us/library/Dd757998(v=VS.85).aspx)         |
| **PKEY\_Media\_UniqueFileIdentifier**    | [**WM/UniqueFileIdentifier**](https://msdn.microsoft.com/en-us/library/Dd758007(v=VS.85).aspx)       |
| **PKEY\_Media\_Writer**                  | [**WM/Writer**](https://msdn.microsoft.com/en-us/library/Dd758024(v=VS.85).aspx)                                   |
| **PKEY\_Media\_Year**                    | [**WM/Year**](https://msdn.microsoft.com/en-us/library/Dd758027(v=VS.85).aspx)                                       |
| **PKEY\_Music\_AlbumArtist**             | [**WM/AlbumArtist**](https://msdn.microsoft.com/en-us/library/Dd757890(v=VS.85).aspx)                         |
| **PKEY\_Music\_AlbumTitle**              | [**WM/AlbumTitle**](https://msdn.microsoft.com/en-us/library/Dd757892(v=VS.85).aspx)                           |
| **PKEY\_Music\_Artist**                  | [**Author**](https://msdn.microsoft.com/en-us/library/Dd743073(v=VS.85).aspx)                                         |
| **PKEY\_Music\_BeatsPerMinute**          | [**WM/BeatsPerMinute**](https://msdn.microsoft.com/en-us/library/Dd757901(v=VS.85).aspx)                   |
| **PKEY\_Music\_Composer**                | [**WM/Composer**](https://msdn.microsoft.com/en-us/library/Dd757906(v=VS.85).aspx)                               |
| **PKEY\_Music\_Conductor**               | [**WM/Conductor**](https://msdn.microsoft.com/en-us/library/Dd757907(v=VS.85).aspx)                             |
| **PKEY\_Music\_ContentGroupDescription** | [**WM/ContentGroupDescription**](https://msdn.microsoft.com/en-us/library/Dd757910(v=VS.85).aspx) |
| **PKEY\_Music\_Genre**                   | [**WM/Genre**](https://msdn.microsoft.com/en-us/library/Dd757917(v=VS.85).aspx)                                     |
| **PKEY\_Music\_InitialKey**              | [**WM/InitialKey**](https://msdn.microsoft.com/en-us/library/Dd757938(v=VS.85).aspx)                           |
| **PKEY\_Music\_IsCompilation**           | **WM/IsCompilation**                                                  |
| **PKEY\_Music\_Lyrics**                  | [**WM/Lyrics**](https://msdn.microsoft.com/en-us/library/Dd757943(v=VS.85).aspx)                                   |
| **PKEY\_Music\_Mood**                    | [**WM/Mood**](https://msdn.microsoft.com/en-us/library/Dd757965(v=VS.85).aspx)                                       |
| **PKEY\_Music\_PartOfSet**               | [**WM/PartOfSet**](https://msdn.microsoft.com/en-us/library/Dd757974(v=VS.85).aspx)                             |
| **PKEY\_Music\_Period**                  | [**WM/Period**](https://msdn.microsoft.com/en-us/library/Dd757976(v=VS.85).aspx)                                   |
| **PKEY\_Music\_TrackNumber**             | [**WM/TrackNumber**](https://msdn.microsoft.com/en-us/library/Dd758006(v=VS.85).aspx)                         |
| **PKEY\_ParentalRating**                 | [**WM/ParentalRating**](https://msdn.microsoft.com/en-us/library/Dd757972(v=VS.85).aspx)                   |
| **PKEY\_ParentalRatingReason**           | [**WM/ParentalRatingReason**](https://msdn.microsoft.com/en-us/library/Dd757973(v=VS.85).aspx)       |
| **PKEY\_Rating**                         | [**WM/SharedUserRating**](https://msdn.microsoft.com/en-us/library/Dd757992(v=VS.85).aspx)               |
| **PKEY\_ThumbnailStream**                | [**WM/Picture**](https://msdn.microsoft.com/library/Dd757832(v=VS.85).aspx)                       |
| **PKEY\_Title**                          | [**Title**](https://msdn.microsoft.com/en-us/library/Dd743755(v=VS.85).aspx)                                           |
| **PKEY\_Video\_Director**                | [**WM/Director**](https://msdn.microsoft.com/en-us/library/Dd757911(v=VS.85).aspx)                               |



 

## Related topics

<dl> <dt>

[Media Metadata](media-metadata.md)
</dt> <dt>

[Shell Metadata Providers](shell-metadata-providers.md)
</dt> </dl>

 

 



