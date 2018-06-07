---
Description: This topic lists the most common metadata properties for media files.
ms.assetid: 35187720-413a-45a0-8558-918f7c3161e1
title: Metadata Properties for Media Files
ms.technology: desktop
ms.prod: windows
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

The Shell property system defines a set of common metadata properties for all types of shell objects. A subset of these are applicable to media files. The following table lists the most common Shell properties for media. Media files might support additional properties not listed here. Also, not every file format supports every property listed. For a complete list of Shell properties, see [Shell Properties](https://www.bing.com/search?q=Shell+Properties).



| PROPERTYKEY                                                              | Shell Name                                                                                    | Description                                                                                                                                                                                               | Data Type    |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [MFPKEY\_Content\_DLNA\_Profile\_ID](mfpkey-content-dlna-profile-id.md) | None                                                                                          | Digital Living Network Alliance (DLNA) profile identifier.                                                                                                                                                | VT\_LPWSTR   |
| **PKEY\_Audio\_ChannelCount**                                            | [System.Audio.ChannelCount](https://msdn.microsoft.com/8a028167-dc0f-4ed9-a710-568caf1b9a47)                       | Number of audio channels.                                                                                                                                                                                 | VT\_UI4      |
| **PKEY\_Audio\_EncodingBitrate**                                         | [System.Audio.EncodingBitrate](https://msdn.microsoft.com/570711c2-ef9b-4b3a-9b5f-94a6601fa3d4)                 | Average audio bit rate, in bits per second.                                                                                                                                                               | VT\_UI4      |
| **PKEY\_Audio\_Format**                                                  | [System.Audio.Format](https://msdn.microsoft.com/58cb9e95-7ac8-42f1-ad2a-a3979ec800eb)                                   | Audio subtype ([**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)) expressed as a string.                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Audio\_IsVariableBitRate**                                       | [System.Audio.IsVariableBitRate](https://msdn.microsoft.com/42f5b22f-b734-4766-b34b-fe9750df032a)             | Indicates whether the audio stream uses variable bit-rate encoding.                                                                                                                                       | VT\_BOOL     |
| **PKEY\_Audio\_PeakValue**                                               | [System.Audio.PeakValue](https://msdn.microsoft.com/576070e9-8f7a-4df7-ba3a-0872aa96a0ab)                             | Peak volume level of audio content.                                                                                                                                                                       | VT\_UI4      |
| **PKEY\_Audio\_SampleRate**                                              | [System.Audio.SampleRate](https://msdn.microsoft.com/534f157c-6982-4423-b8e7-66591c0cb184)                           | Audio sample rate in samples per second. Equivalent to the [**MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND**](mf-mt-audio-samples-per-second-attribute.md) attribute in the media type.                           | VT\_UI4      |
| **PKEY\_Audio\_SampleSize**                                              | [System.Audio.SampleSize](https://msdn.microsoft.com/abbfd194-e800-46c3-b961-1cf3f5d59c82)                           | Number of bits per audio sample. Equivalent to the [**MF\_MT\_AUDIO\_BITS\_PER\_SAMPLE**](mf-mt-audio-bits-per-sample-attribute.md) attribute in the media type.                                         | VT\_UI4      |
| **PKEY\_Audio\_StreamNumber**                                            | [System.Audio.StreamNumber](https://msdn.microsoft.com/bb5e0d48-b7ea-487d-8063-daa9196fee7a)                       | Identifier of the audio stream.                                                                                                                                                                           | VT\_UI4      |
| **PKEY\_Author**                                                         | [System.Author](https://msdn.microsoft.com/07a411c2-9e88-4d14-b9f7-e3a5d8d1630e)                                               | Author.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Comment**                                                        | [System.Comment](https://msdn.microsoft.com/3ca38760-e979-48ba-b87f-5dc742e046af)                                             | A comment attached to a file, typically added by a user.                                                                                                                                                  | VT\_LPWSTR   |
| **PKEY\_Copyright**                                                      | [System.Copyright](https://msdn.microsoft.com/95efb9c4-af3d-4a24-9670-60bacf61dfce)                                         | Copyright information.                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_DRM\_IsProtected**                                               | [System.DRM.IsProtected](https://msdn.microsoft.com/50b3ada0-bdf7-4c61-8cfc-17fbb4a7d1e6)                             | Indicates whether the content is protected using digital rights management (DRM).                                                                                                                         | VT\_BOOL     |
| **PKEY\_Keywords**                                                       | [System.Keywords](https://msdn.microsoft.com/427ed6c9-88cb-4b33-998f-663b59e677c9)                                           | Keywords.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Language**                                                       | [System.Language](https://msdn.microsoft.com/fc25ebaa-42f6-42fc-8a3e-7704dbfbc0d8)                                           | Language.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_AuthorUrl**                                               | [System.Media.AuthorUrl](https://msdn.microsoft.com/b8891bae-31da-48f6-b4e6-18799a199c9a)                             | URL of the author's website.                                                                                                                                                                              | VT\_LPWSTR   |
| **PKEY\_Media\_AverageLevel**                                            | [System.Media.AverageLevel](https://msdn.microsoft.com/e5500ae2-f250-4b27-8eaa-bff8c2f7c797)                       | Average volume level of audio content.                                                                                                                                                                    | VT\_UI4      |
| **PKEY\_Media\_ClassPrimaryID**                                          | [System.Media.ClassPrimaryID](https://msdn.microsoft.com/f7662562-6036-4b3c-9c24-b12afb9255a0)                   | The string representation of a GUID that identifies the primary class of media. For valid values, see the documentation for the [**WM/MediaClassPrimaryID**](https://msdn.microsoft.com/1d01e273-e6ec-49f1-90af-5c2ae171b199) attribute.       | VT\_LPWSTR   |
| **PKEY\_Media\_ClassSecondaryID**                                        | [System.Media.ClassSecondaryID](https://msdn.microsoft.com/79c197b5-a551-4e17-ab92-6eac99da4647)               | The string representation of a GUID that identifies the secondary class of media. For valid values, see the documentation for the [**WM/MediaClassSecondaryID**](https://msdn.microsoft.com/3d1429bc-f168-4b25-9d26-c1c28b852160) attribute. | VT\_LPWSTR   |
| **PKEY\_Media\_CollectionGroupID**                                       | [System.Media.CollectionGroupID](https://msdn.microsoft.com/1ef5de55-2cf8-4ed3-ad79-25856058fb03)             | The string representation of a GUID that identifies the collection group.                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_CollectionID**                                            | [System.Media.CollectionID](https://msdn.microsoft.com/8e404517-6406-4c53-81d5-b20cafbc393f)                       | The string representation of a GUID that identifies the collection.                                                                                                                                       | VT\_LPWSTR   |
| **PKEY\_Media\_ContentDistributor**                                      | [System.Media.ContentDistributor](https://msdn.microsoft.com/b4c65279-e94e-48d2-bd6c-60980cacc154)           | Distributor of the content.                                                                                                                                                                               | VT\_LPWSTR   |
| **PKEY\_Media\_ContentID**                                               | [System.Media.ContentID](https://msdn.microsoft.com/8ac9047d-5995-4492-aa4f-4a56a947191e)                             | The string representation of a GUID that identifies the collection.                                                                                                                                       | VT\_LPWSTR   |
| **PKEY\_Media\_DateEncoded**                                             | [System.Media.DateEncoded](https://msdn.microsoft.com/22d7aee7-6f52-48cd-80d3-746a6ca7ba86)                         | Time when the content was encoded.                                                                                                                                                                        | VT\_FILETIME |
| **PKEY\_Media\_DateReleased**                                            | [System.Media.DateReleased](https://msdn.microsoft.com/7a947320-ae05-4b17-82bc-f6100a0450da)                       | Original release date.                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Media\_Duration**                                                | [System.Media.Duration](https://msdn.microsoft.com/5548f421-6475-4419-b677-5d9eb625a373)                               | Duration, in 100-nanosecond units. Equivalent to the [**MF\_PD\_DURATION**](mf-pd-duration-attribute.md) attribute in the presentation descriptor.                                                       | VT\_UI8      |
| **PKEY\_Media\_DVDID**                                                   | [System.Media.DVDID](https://msdn.microsoft.com/2de30c3a-f982-4a65-bb25-a76b99d9ee13)                                     | Digital video disc identifier (DVDID).                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Media\_EncodedBy**                                               | [System.Media.EncodedBy](https://msdn.microsoft.com/04bcdc5a-ba44-4b9c-ae87-fee50250d18b)                             | Name of the person or group that encoded the content.                                                                                                                                                     | VT\_LPWSTR   |
| **PKEY\_Media\_EncodingSettings**                                        | [System.Media.EncodingSettings](https://msdn.microsoft.com/c59af6a9-93f9-4b05-95fa-2b5b06a89b55)               | Description of the settings used to encode the content.                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Media\_MCDI**                                                    | [System.Media.MCDI](https://msdn.microsoft.com/a653c29b-6c6c-4e26-9f7d-94a2dbb48113)                                       | Music CD identifier. This value is used to identify a CD.                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_MetadataContentProvider**                                 | [System.Media.MetadataContentProvider](https://msdn.microsoft.com/6fb4f43b-e274-4be5-a128-5b20ad3c4203) | Name of the metadata content provider. (For example, metadata might be provided by a commercial service.)                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_Producer**                                                | [System.Media.Producer](https://msdn.microsoft.com/9cc672b2-75ea-4733-aaa3-0c4fd5afb4f6)                               | Name of the producer of the content.                                                                                                                                                                      | VT\_LPWSTR   |
| **PKEY\_Media\_PromotionUrl**                                            | [System.Media.PromotionUrl](https://msdn.microsoft.com/a0e464a0-ff43-43a8-87f7-2fef17ca15eb)                       | URL of a website offering a promotion related to the content.                                                                                                                                             | VT\_LPWSTR   |
| **PKEY\_Media\_ProviderRating**                                          | [System.Media.ProviderRating](https://msdn.microsoft.com/72e29588-cb22-443f-a404-f192fe680207)                   | Rating of the content as assigned by the metadata content provider.                                                                                                                                       | VT\_LPWSTR   |
| **PKEY\_Media\_ProviderStyle**                                           | [System.Media.ProviderStyle](https://msdn.microsoft.com/e5334993-c621-4e26-a317-e2639b7e490e)                     | Style or genre of the content as assigned by the metadata content provider.                                                                                                                               | VT\_LPWSTR   |
| **PKEY\_Media\_Publisher**                                               | [System.Media.Publisher](https://msdn.microsoft.com/64de54af-6900-4361-a7b5-f29fbd5cd0e0)                             | Publisher.                                                                                                                                                                                                | VT\_LPWSTR   |
| **PKEY\_Media\_SubTitle**                                                | [System.Media.SubTitle](https://msdn.microsoft.com/e98bf6ca-0572-419b-8bc0-bc0239f8a6ff)                               | Subtitle.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Media\_UniqueFileIdentifier**                                    | [System.Media.UniqueFileIdentifier](https://msdn.microsoft.com/0fe07c66-3d9c-4368-8fbd-23cb486757cc)       | A generic string that can be to identify the file.                                                                                                                                                        | VT\_LPWSTR   |
| **PKEY\_Media\_Writer**                                                  | [System.Media.Writer](https://msdn.microsoft.com/a9ef9c5b-dc7b-4d1a-b47f-093d4f37bba4)                                   | Writer.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Media\_Year**                                                    | [System.Media.Year](https://msdn.microsoft.com/87080e50-1233-4300-8fbc-cd897d9aecbd)                                       | Year the content was published.                                                                                                                                                                           | VT\_UI4      |
| **PKEY\_Music\_AlbumArtist**                                             | [System.Music.AlbumArtist](https://msdn.microsoft.com/6b951418-9076-42ca-9ed5-4e260e8c19bc)                         | Primary artist for the album. This attribute can be used to distinguish the primary artist for an album from an artist who collaborated on a particular track.                                            | VT\_LPWSTR   |
| **PKEY\_Music\_AlbumTitle**                                              | [System.Music.AlbumTitle](https://msdn.microsoft.com/7335e246-3a3e-4610-8db5-baddb0b80901)                           | Album title.                                                                                                                                                                                              | VT\_LPWSTR   |
| **PKEY\_Music\_Artist**                                                  | [System.Music.Artist](https://msdn.microsoft.com/99094e2f-e3be-4561-b0a5-4ad3934cd1d8)                                   | Artist.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Music\_BeatsPerMinute**                                          | [System.Music.BeatsPerMinute](https://msdn.microsoft.com/ebf92204-d615-4bcc-a181-f98a9396abf5)                   | Beats per minute.                                                                                                                                                                                         | VT\_LPWSTR   |
| **PKEY\_Music\_Composer**                                                | [System.Music.Composer](https://msdn.microsoft.com/60eda2b4-2631-41dc-94ee-181a69e9c5f4)                               | Composer.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Music\_Conductor**                                               | [System.Music.Conductor](https://msdn.microsoft.com/cb04c41f-35e3-4483-9bc5-5e4f2e45042f)                             | Conductor.                                                                                                                                                                                                | VT\_LPWSTR   |
| **PKEY\_Music\_ContentGroupDescription**                                 | [System.Music.ContentGroupDescription](https://msdn.microsoft.com/a2725816-eea0-4e49-9134-8f6bcc00c72a) | Description of the content group (for example, boxed set or series).                                                                                                                                      | VT\_LPWSTR   |
| **PKEY\_Music\_Genre**                                                   | [System.Music.Genre](https://msdn.microsoft.com/c1adbc13-5069-4760-901c-d5ca47913695)                                     | Genre.                                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Music\_InitialKey**                                              | [System.Music.InitialKey](https://msdn.microsoft.com/34ee1164-b23b-4fe4-ba66-0e963278d710)                           | The initial key of the music.                                                                                                                                                                             | VT\_LPWSTR   |
| **PKEY\_Music\_IsCompilation**                                           | [System.Music.IsCompilation](https://msdn.microsoft.com/E3FD56F1-8886-408b-BDF2-7499AAF5AF97)                     | Indicates whether the music file is part of a compilation.                                                                                                                                                | VT\_BOOL     |
| **PKEY\_Music\_Lyrics**                                                  | [System.Music.Lyrics](https://msdn.microsoft.com/ae7edb4e-f362-49c2-83ab-c2b832d279e5)                                   | Lyrics.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Music\_Mood**                                                    | [System.Music.Mood](https://msdn.microsoft.com/6c5ceb65-128c-4fb1-b6a5-1af298656f69)                                       | Mood.                                                                                                                                                                                                     | VT\_LPWSTR   |
| **PKEY\_Music\_PartOfSet**                                               | [System.Music.PartOfSet](https://msdn.microsoft.com/29696a6f-cd2c-40c4-a7a6-ca32ac80beae)                             | The part number and the total number of parts in the set to which the file belongs, separated by a slash.                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Music\_Period**                                                  | [System.Music.Period](https://msdn.microsoft.com/141ea422-d844-4e1c-9ef5-3b5ff27024f7)                                   | Period.                                                                                                                                                                                                   | VT\_LPWSTR   |
| **PKEY\_Music\_TrackNumber**                                             | [System.Music.TrackNumber](https://msdn.microsoft.com/0007f7e0-4b62-453a-adc5-cccf1e916f12)                         | Track number.                                                                                                                                                                                             | VT\_UI4      |
| **PKEY\_ParentalRating**                                                 | [System.ParentalRating](https://msdn.microsoft.com/db5fb8a2-719f-4bef-9ab1-0856945ed240)                               | Parental rating.                                                                                                                                                                                          | VT\_LPWSTR   |
| **PKEY\_ParentalRatingReason**                                           | [System.ParentalRatingReason](https://msdn.microsoft.com/0cd6b665-faf8-4fc5-9625-7d5edbdf7e2f)                   | Reasons for the assigned parental rating.                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Rating**                                                         | [System.Rating](https://msdn.microsoft.com/a6288d29-1ef3-4da1-bd30-577336ab6817)                                               | User rating.                                                                                                                                                                                              | VT\_UI4      |
| **PKEY\_ThumbnailStream**                                                | [System.ThumbnailStream](https://msdn.microsoft.com/7ffdf9e4-69b1-4946-8867-73696cd241e0)                             | Thumbnail image.                                                                                                                                                                                          | VT\_STREAM   |
| **PKEY\_Title**                                                          | [System.Title](https://msdn.microsoft.com/8fb948d6-2677-4e5d-b283-8757c3df574d)                                                 | Title.                                                                                                                                                                                                    | VT\_LPWSTR   |
| **PKEY\_Video\_Compression**                                             | [System.Video.Compression](https://msdn.microsoft.com/fdd3fce9-f507-4581-bd68-74a854581200)                         | Video subtype ([**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)) expressed as a string.                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Video\_Director**                                                | [System.Video.Director](https://msdn.microsoft.com/dd992d16-bd12-49e6-843b-f4a30aab33b6)                               | Director.                                                                                                                                                                                                 | VT\_LPWSTR   |
| **PKEY\_Video\_EncodingBitrate**                                         | [System.Video.EncodingBitrate](https://msdn.microsoft.com/2465dd92-6ab4-4a1f-abd4-1d2abca6f9ce)                 | Average video bit rate, in bits per second.                                                                                                                                                               | VT\_UI4      |
| **PKEY\_Video\_FourCC**                                                  | [System.Video.FourCC](https://msdn.microsoft.com/c5054fc6-1273-4491-8fb9-30c4b8fc663f)                                   | The **FOURCC** of the video encoding format. Applies only if the video subtype can be expressed as a **FOURCC** value.                                                                                    | VT\_UI4      |
| **PKEY\_Video\_FrameHeight**                                             | [System.Video.FrameHeight](https://msdn.microsoft.com/83c26a8a-7724-4566-bc3e-3a26a7cc9223)                         | Video frame height.                                                                                                                                                                                       | VT\_UI4      |
| **PKEY\_Video\_FrameRate**                                               | [System.Video.FrameRate](https://msdn.microsoft.com/cd5a2ae0-43ef-44e4-aa70-bca33baf2a56)                             | Video frame rate, expressed as frames per second × 1000.                                                                                                                                                  | VT\_UI4      |
| **PKEY\_Video\_FrameWidth**                                              | [System.Video.FrameWidth](https://msdn.microsoft.com/e44999c8-cd0e-4653-a191-a7a7ea8e6bec)                           | Video frame width.                                                                                                                                                                                        | VT\_UI4      |
| **PKEY\_Video\_HorizontalAspectRatio**                                   | [System.Video.HorizontalAspectRatio](https://msdn.microsoft.com/bf490821-2838-46e7-8460-03f7c64c9292)     | The horizontal component of the pixel aspect ratio. (Equivalent to the numerator of the [**MF\_MT\_PIXEL\_ASPECT\_RATIO**](mf-mt-pixel-aspect-ratio-attribute.md) attribute in the media type.)          | VT\_UI4      |
| **PKEY\_Video\_IsStereo**                                                | [System.Video.IsStereo](https://www.bing.com/search?q=System.Video.IsStereo)                                     | Indicates whether the video stream contains stereo video content.                                                                                                                                         | VT\_BOOL     |
| **PKEY\_Video\_StreamNumber**                                            | [System.Video.StreamNumber](https://msdn.microsoft.com/796206ab-d69c-4dd5-a408-2ecb5cde243f)                       | Identifier of the video stream.                                                                                                                                                                           | VT\_UI4      |
| **PKEY\_Video\_TotalBitrate**                                            | [System.Video.TotalBitrate](https://msdn.microsoft.com/7667da66-261c-4627-8322-2c939738659b)                       | Total data rate for all video and audio streams, in bits per second. (Applies only to files with at least one video stream.)                                                                              | VT\_UI4      |
| **PKEY\_Video\_VerticalAspectRatio**                                     | [System.Video.VerticalAspectRatio](https://msdn.microsoft.com/b463b51e-3e00-4f80-a7b9-f5ff5432b7ef)         | The vertical component of the pixel aspect ratio. (Equivalent to the denominator of the [**MF\_MT\_PIXEL\_ASPECT\_RATIO**](mf-mt-pixel-aspect-ratio-attribute.md) attribute in the media type.)          | VT\_UI4      |



 

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
| **PKEY\_Audio\_IsVariableBitRate**       | [**IsVBR**](https://msdn.microsoft.com/13bd2400-c8f8-4074-8702-498543e42a63)                                           |
| **PKEY\_Audio\_PeakValue**               | [**PeakValue**](https://msdn.microsoft.com/885f6d4c-661a-4681-96b6-c1a282c8bf18)                                   |
| **PKEY\_Author**                         | [**Author**](https://msdn.microsoft.com/fdad5790-42b6-449c-a24c-aa0718d33e5d)                                         |
| **PKEY\_Comment**                        | [**Description**](https://msdn.microsoft.com/b9a1dcb1-9e8a-49a0-8dd5-388c929645c3)                               |
| **PKEY\_Copyright**                      | [**Copyright**](https://msdn.microsoft.com/4c5bdb9d-9dcd-42a5-bf03-b83bfd73135e)                                   |
| **PKEY\_DRM\_IsProtected**               | [**Is\_Protected**](https://msdn.microsoft.com/6fe63d9b-67ec-47a8-ba20-657434c7a15b)                            |
| **PKEY\_Keywords**                       | [**WM/Category**](https://msdn.microsoft.com/3a07aa7f-64dd-4274-8720-dec49e29eca4)                               |
| **PKEY\_Language**                       | [**WM/Language**](https://msdn.microsoft.com/840f95b0-c8f2-4da6-9a76-3870b2325a42)                               |
| **PKEY\_Media\_AuthorUrl**               | [**WM/AuthorURL**](https://msdn.microsoft.com/00abc2ec-4c12-45c2-b063-a4d814f88b35)                             |
| **PKEY\_Media\_AverageLevel**            | [**AverageLevel**](https://msdn.microsoft.com/e6270ac8-5de3-4dee-824c-ba25fdd272c8)                             |
| **PKEY\_Media\_ClassPrimaryID**          | [**WM/MediaClassPrimaryID**](https://msdn.microsoft.com/1d01e273-e6ec-49f1-90af-5c2ae171b199)              |
| **PKEY\_Media\_ClassSecondaryID**        | [**WM/MediaClassSecondaryID**](https://msdn.microsoft.com/3d1429bc-f168-4b25-9d26-c1c28b852160)          |
| **PKEY\_Media\_CollectionGroupID**       | [**WM/WMCollectionGroupID**](https://msdn.microsoft.com/5cfa1747-ce3b-4e8d-bcce-84fb719123e8)         |
| **PKEY\_Media\_CollectionID**            | [**WM/WMCollectionID**](https://msdn.microsoft.com/088fe2d7-e2d9-42a3-8deb-1d7948ff7df9)                   |
| **PKEY\_Media\_ContentDistributor**      | [**WM/ContentDistributor**](https://msdn.microsoft.com/813574e0-e6e1-4acd-b9ca-faab41db00a5)           |
| **PKEY\_Media\_ContentID**               | [**WM/WMContentID**](https://msdn.microsoft.com/b46d02f4-04f5-430a-b3f7-0f80e03bed2c)                         |
| **PKEY\_Media\_DateEncoded**             | [**WM/EncodingTime**](https://msdn.microsoft.com/63da9392-264d-40bb-99fd-56db93801941)                       |
| **PKEY\_Media\_DateReleased**            | [**WM/OriginalReleaseTime**](https://msdn.microsoft.com/80410ee0-9ccb-4674-867f-160dcece00b9)         |
| **PKEY\_Media\_DVDID**                   | [**WM/DVDID**](https://msdn.microsoft.com/c49d4d93-377e-4378-932e-7b98fe2b7ba8)                                     |
| **PKEY\_Media\_EncodedBy**               | [**WM/EncodedBy**](https://msdn.microsoft.com/13c4d8c6-6dca-4f2c-a76f-a127004a8aaf)                             |
| **PKEY\_Media\_EncodingSettings**        | [**WM/EncodingSettings**](https://msdn.microsoft.com/f60c9641-74f1-41d5-959f-96f4050e8435)               |
| **PKEY\_Media\_MCDI**                    | [**WM/MCDI**](https://msdn.microsoft.com/cb16c62b-b9e0-4676-b1bb-ff26a2e09cb7)                                       |
| **PKEY\_Media\_MetadataContentProvider** | [**WM/Provider**](https://msdn.microsoft.com/94d1f87e-f5b5-4898-b717-8b7494456f26)                               |
| **PKEY\_Media\_Producer**                | [**WM/Producer**](https://msdn.microsoft.com/48934f4f-6c8f-4a45-be3f-cb88efc0d936)                               |
| **PKEY\_Media\_PromotionUrl**            | [**WM/PromotionURL**](https://msdn.microsoft.com/0a1514a6-a77a-447c-9de7-fb390bd48b6d)                       |
| **PKEY\_Media\_ProviderRating**          | [**WM/ProviderRating**](https://msdn.microsoft.com/3fd6ec6e-568c-4568-9502-d02c1c9a894b)                   |
| **PKEY\_Media\_ProviderStyle**           | [**WM/ProviderStyle**](https://msdn.microsoft.com/3bf6811e-a527-4ec7-b330-6e0eabab485a)                     |
| **PKEY\_Media\_Publisher**               | [**WM/Publisher**](https://msdn.microsoft.com/d83ae7cc-ee28-409c-9afe-69571d58f3e7)                             |
| **PKEY\_Media\_SubTitle**                | [**WM/SubTitleDescription**](https://msdn.microsoft.com/75e845bd-ec1d-4420-9ae1-479633eec821)         |
| **PKEY\_Media\_UniqueFileIdentifier**    | [**WM/UniqueFileIdentifier**](https://msdn.microsoft.com/3f90dd5c-0f3d-451a-a454-f8d7f25b6201)       |
| **PKEY\_Media\_Writer**                  | [**WM/Writer**](https://msdn.microsoft.com/3450c584-3bd4-4df3-a401-f260f543fb98)                                   |
| **PKEY\_Media\_Year**                    | [**WM/Year**](https://msdn.microsoft.com/02a4a2da-737c-4ac2-992c-4da9fc7ba26c)                                       |
| **PKEY\_Music\_AlbumArtist**             | [**WM/AlbumArtist**](https://msdn.microsoft.com/53675c06-313b-41f8-971b-ccd18f37e987)                         |
| **PKEY\_Music\_AlbumTitle**              | [**WM/AlbumTitle**](https://msdn.microsoft.com/8b003634-7459-4586-9947-530c07dbc80a)                           |
| **PKEY\_Music\_Artist**                  | [**Author**](https://msdn.microsoft.com/fdad5790-42b6-449c-a24c-aa0718d33e5d)                                         |
| **PKEY\_Music\_BeatsPerMinute**          | [**WM/BeatsPerMinute**](https://msdn.microsoft.com/08ea6f9c-e21b-4d68-b325-633b8c6ccf04)                   |
| **PKEY\_Music\_Composer**                | [**WM/Composer**](https://msdn.microsoft.com/ec606961-0196-4a11-81f7-066496e6e413)                               |
| **PKEY\_Music\_Conductor**               | [**WM/Conductor**](https://msdn.microsoft.com/12c58716-7b91-4014-9741-575a017cf7f1)                             |
| **PKEY\_Music\_ContentGroupDescription** | [**WM/ContentGroupDescription**](https://msdn.microsoft.com/0884f33e-4417-4c8b-8e0a-d79fff423395) |
| **PKEY\_Music\_Genre**                   | [**WM/Genre**](https://msdn.microsoft.com/50279c96-e8f2-40a3-9d5b-5827eb91b61e)                                     |
| **PKEY\_Music\_InitialKey**              | [**WM/InitialKey**](https://msdn.microsoft.com/f298f860-95e3-4dee-8fec-771da4a3744d)                           |
| **PKEY\_Music\_IsCompilation**           | **WM/IsCompilation**                                                  |
| **PKEY\_Music\_Lyrics**                  | [**WM/Lyrics**](https://msdn.microsoft.com/3b4356ba-0feb-4cc5-8629-f45d39ac4113)                                   |
| **PKEY\_Music\_Mood**                    | [**WM/Mood**](https://msdn.microsoft.com/04a56354-e326-4c42-b124-249fa4d95ce7)                                       |
| **PKEY\_Music\_PartOfSet**               | [**WM/PartOfSet**](https://msdn.microsoft.com/a7facc38-776b-40c5-a93a-71d0e2effa2d)                             |
| **PKEY\_Music\_Period**                  | [**WM/Period**](https://msdn.microsoft.com/16c9d862-8d38-40cc-ae04-178cdea1f750)                                   |
| **PKEY\_Music\_TrackNumber**             | [**WM/TrackNumber**](https://msdn.microsoft.com/cd338cd9-a5de-4311-8089-1d5d90570f69)                         |
| **PKEY\_ParentalRating**                 | [**WM/ParentalRating**](https://msdn.microsoft.com/c2cb5c33-7ca1-4401-99a0-c9528b9b2c25)                   |
| **PKEY\_ParentalRatingReason**           | [**WM/ParentalRatingReason**](https://msdn.microsoft.com/ee786737-3e3a-41d0-8a18-edf46ac93496)       |
| **PKEY\_Rating**                         | [**WM/SharedUserRating**](https://msdn.microsoft.com/a9715d1c-f697-4231-a127-81c00e808030)               |
| **PKEY\_ThumbnailStream**                | [**WM/Picture**](https://www.bing.com/search?q=**WM/Picture**)                       |
| **PKEY\_Title**                          | [**Title**](https://msdn.microsoft.com/f79336bc-51f0-479b-8f58-938478ea6d4f)                                           |
| **PKEY\_Video\_Director**                | [**WM/Director**](https://msdn.microsoft.com/1bbb640a-9d8c-4e03-b4ce-706aabe772d5)                               |



 

## Related topics

<dl> <dt>

[Media Metadata](media-metadata.md)
</dt> <dt>

[Shell Metadata Providers](shell-metadata-providers.md)
</dt> </dl>

 

 



