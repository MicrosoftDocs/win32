---
description: About the WM ASF Reader Filter
ms.assetid: e698c0da-88b2-497a-8a25-9d3b76c85a7d
title: About the WM ASF Reader Filter
ms.topic: article
ms.date: 05/31/2018
---

# About the WM ASF Reader Filter

Playback of ASF files is handled by the [WM ASF Reader](wm-asf-reader-filter.md) filter. When the WM ASF Reader reads a file, it automatically creates an output pin for each stream, including web streams, script command streams, and any other type of arbitrary stream. In the case of multiple bit rate files, pins are created only for the currently selected streams. To play an ASF file with the WM ASF Reader filter, call [**IGraphBuilder::RenderFile**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-renderfile) or [**IGraphBuilder::AddSourceFilter**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-addsourcefilter).

The WM ASF Reader supports the DirectShow [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) interface, which enables applications to perform temporal seeking within the file. However, playback at speeds other than 1.0 (as specified in [**IMediaSeeking::SetRate**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-setrate)) is not supported.

The WM ASF Reader filter also exposes several Windows Media Format SDK interfaces as described in the following table. These interfaces are documented in the Windows Media Format SDK documentation.



| Interface                                             | How exposed                                 | Comments                                                                                                                       |
|-------------------------------------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**IWMDRMReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmreader)             | Through **IServiceProvider** on the filter. | Provided for applications that need to play content protected by Digital Rights Management (DRM)..                             |
| [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo)           | **QueryInterface** on the filter.           | Provided so that applications can read file and content attributes, as well as marker and script information and metadata.     |
| [**IWMReaderAdvanced**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced)   | **QueryInterface** on the filter.           | Partially implemented on the filter so that applications can access the informational methods on the WM Reader object.         |
| [**IWMReaderAdvanced2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced2) | **QueryInterface** on the filter.           | Partially implemented on the filter so that applications can access the informational methods on the Format SDK Reader Object. |



 

## Related topics

<dl> <dt>

[Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md)
</dt> </dl>

 

 



