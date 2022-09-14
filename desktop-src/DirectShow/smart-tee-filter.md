---
description: Smart Tee Filter
ms.assetid: 25bfbd62-b6be-4d1f-aa4c-77798bbb9fc9
title: Smart Tee Filter
ms.topic: article
ms.date: 05/31/2018
---

# Smart Tee Filter

The Smart Tee filter is used in video capture graphs to split the video stream into a preview stream and a capture stream. This is done without any additional data copying. The output pins support whatever media types are supported on the downstream connection.

The Smart Tee filter is useful when a video capture filter does not provide separate pins for capture and preview. The Smart Tee filter delivers preview data only if doing so does not hurt capture performance. It also removes the time stamps from the preview stream. The capture graph builder automatically inserts the Smart Tee filter when needed. For more information, see [Combining Video Capture and Preview](combining-video-capture-and-preview.md).

The following illustration shows a typical capture graph that uses the Smart Tee filter.

![using the smart tee filter](images/smarttee.png)



| Label | Value |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)                                                                             |
| Input Pin Media Types                    | MEDIATYPE\_Video, MEDIASUBTYPE\_NULL                                                                           |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)         |
| Output Pin Media Types                   | MEDIATYPE\_Video, MEDIASUBTYPE\_NULL                                                                           |
| Output Pin Interfaces                    | [**IAMStreamControl**](/windows/desktop/api/Strmif/nn-strmif-iamstreamcontrol), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol) |
| Filter CLSID                             | CLSID\_SmartTee                                                                                                |
| Property Page CLSID                      | No property page.                                                                                              |
| Executable                               | qcap.dll                                                                                                       |
| [Merit](merit.md)                       | MERIT\_DO\_NOT\_USE                                                                                            |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                  |



 

## Remarks

The capture pin is output pin 0, and the preview pin is output pin 1.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



