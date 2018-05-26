---
Description: About the WM ASF Reader Filter
ms.assetid: e698c0da-88b2-497a-8a25-9d3b76c85a7d
title: About the WM ASF Reader Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About the WM ASF Reader Filter

Playback of ASF files is handled by the [WM ASF Reader](wm-asf-reader-filter.md) filter. When the WM ASF Reader reads a file, it automatically creates an output pin for each stream, including web streams, script command streams, and any other type of arbitrary stream. In the case of multiple bit rate files, pins are created only for the currently selected streams. To play an ASF file with the WM ASF Reader filter, call [**IGraphBuilder::RenderFile**](/windows/win32/Strmif/nf-strmif-igraphbuilder-renderfile?branch=master) or [**IGraphBuilder::AddSourceFilter**](/windows/win32/Strmif/nf-strmif-igraphbuilder-addsourcefilter?branch=master).

The WM ASF Reader supports the DirectShow [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master) interface, which enables applications to perform temporal seeking within the file. However, playback at speeds other than 1.0 (as specified in [**IMediaSeeking::SetRate**](/windows/win32/Strmif/nf-strmif-imediaseeking-setrate?branch=master)) is not supported.

The WM ASF Reader filter also exposes several Windows Media Format SDK interfaces as described in the following table. These interfaces are documented in the Windows Media Format SDK documentation.



| Interface                                             | How exposed                                 | Comments                                                                                                                       |
|-------------------------------------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**IWMDRMReader**](https://msdn.microsoft.com/library/windows/desktop/dd798339)             | Through **IServiceProvider** on the filter. | Provided for applications that need to play content protected by Digital Rights Management (DRM)..                             |
| [**IWMHeaderInfo**](https://msdn.microsoft.com/library/windows/desktop/dd798504)           | **QueryInterface** on the filter.           | Provided so that applications can read file and content attributes, as well as marker and script information and metadata.     |
| [**IWMReaderAdvanced**](https://msdn.microsoft.com/library/windows/desktop/dd757429)   | **QueryInterface** on the filter.           | Partially implemented on the filter so that applications can access the informational methods on the WM Reader object.         |
| [**IWMReaderAdvanced2**](https://msdn.microsoft.com/library/windows/desktop/dd757430) | **QueryInterface** on the filter.           | Partially implemented on the filter so that applications can access the informational methods on the Format SDK Reader Object. |



 

## Related topics

<dl> <dt>

[Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md)
</dt> </dl>

 

 



