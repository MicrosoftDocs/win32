---
description: Mapper Sample
ms.assetid: f795993f-43d7-4b29-905c-12ec3d43a059
title: Mapper Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Mapper Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

This sample demonstrates using the [**IFilterMapper2::EnumMatchingFilters**](/windows/desktop/api/Strmif/nf-strmif-ifiltermapper2-enummatchingfilters) method to locate filters in the registry.

The sample application's UI contains controls that match the parameters of the [**EnumMatchingFilters**](/windows/desktop/api/Strmif/nf-strmif-ifiltermapper2-enummatchingfilters) method, such as minimum merit value, pin categories, and media types. Select the search options that you want, then click the **Search** button to enumerate the filters that match those options.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: \[SDK Root\]\\Samples\\Multimedia\\DirectShow\\Misc\\Mapper.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> <dt>

[Using the Filter Mapper](using-the-filter-mapper.md)
</dt> </dl>

 

 



