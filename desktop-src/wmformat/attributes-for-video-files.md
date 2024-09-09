---
title: Attributes for Video Files
description: Attributes for Video Files
ms.assetid: 4250ad27-075e-4daa-bc04-d24ddd2e8252
keywords:
- Windows Media Format SDK,attributes
- Advanced Systems Format (ASF),attributes
- ASF (Advanced Systems Format),attributes
- attributes,video files
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Attributes for Video Files

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section lists the attributes commonly used for video files. It is recommended that you set attributes for files according to these lists to ensure that your files are fully compatible with a wide variety of playback applications. The attributes in this section are listed in three categories: primary, secondary, and tertiary.

Primary attributes convey the most basic information about a file. If you are creating video files for distribution, this is the minimum set of attributes you should use.

Secondary attributes contain common metadata that is important but not universal to all video files.

Tertiary attributes should be included as needed, but are not essential to describing the file.

## Primary Attributes for Video

-   [**Author**](author.md)
-   [**Title**](title.md)
-   [**WM/ContentDistributor**](wm-contentdistributor.md)
-   [**WM/DVDID**](wm-dvdid.md) (if available; otherwise use [**WM/WMCollectionID**](wm-wmcollectionid.md), [**WM/WMCollectionGroupID**](wm-wmcollectiongroupid.md), and [**WM/WMContentID**](wm-wmcontentid.md))
-   [**WM/Genre**](wm-genre.md)
-   [**WM/MediaClassPrimaryID**](wm-mediaprimaryid.md)
-   [**WM/MediaClassSecondaryID**](wm-mediasecondaryid.md)
-   [**WM/Provider**](wm-provider.md)

## Secondary Attributes for Video

-   [**Copyright**](copyright.md)
-   [**WM/Composer**](wm-composer.md)
-   [**WM/Director**](wm-director.md)
-   [**WM/EncodingTime**](wm-encodingtime.md)
-   [**WM/Language**](wm-language.md)
-   [**WM/ParentalRating**](wm-parentalrating.md)
-   [**WM/Producer**](wm-producer.md)
-   [**WM/ToolName**](wm-toolname.md)
-   [**WM/ToolVersion**](wm-toolversion.md)
-   [**WM/WMCollectionGroupID**](wm-wmcollectiongroupid.md)
-   [**WM/WMCollectionID**](wm-wmcollectionid.md)
-   [**WM/WMContentID**](wm-wmcontentid.md)
-   [**WM/Writer**](wm-writer.md)

## Tertiary Attributes for Video

-   [**Description**](description.md)
-   [**WM/AuthorURL**](wm-authorurl.md)
-   [**WM/Conductor**](wm-conductor.md)
-   [**WM/ContentGroupDescription**](wm-contentgroupdescription.md)
-   [**WM/EncodedBy**](wm-encodedby.md)
-   [**WM/EncodingSettings**](wm-encodingsettings.md)
-   [**WM/PartOfSet**](wm-partofset.md)
-   [**WM/Picture**](wmpicture.md)
-   [**WM/PromotionURL**](wm-promotionurl.md)
-   [**WM/Publisher**](wm-publisher.md)
-   [**WM/SubTitle**](wm-subtitle.md)
-   [**WM/UniqueFileIdentifier**](wm-uniquefileidentifier.md)
-   [**WM/UserWebURL**](wm-userweburl.md)

## Related topics

<dl> <dt>

[**Attributes By Type**](attributes-by-type.md)
</dt> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




