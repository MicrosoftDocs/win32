---
title: WM ASF Writer Filter (Windows Media Format 11 SDK)
description: Learn about the WM ASF Writer filter for the Windows Media Format 11 SDK. Review filter information and see related topics.
ms.assetid: a902c92e-836d-492c-b2d2-89c216125774
keywords:
- Windows Media Format SDK,WM ASF Writer
- DirectShow,WM ASF Writer
- QASF filters,WM ASF Writer
- WM ASF Writer,about
- Advanced Systems Format (ASF),WM ASF Writer
- ASF (Advanced Systems Format),WM ASF Writer
ms.topic: article
ms.date: 05/31/2018
---

# WM ASF Writer Filter (Windows Media Format 11 SDK)

The WM ASF Writer filter accepts a variable number of input streams and creates an ASF file. The filter handles all compression and multiplexing (although the compression mechanism can be bypassed). You can use the WM ASF Writer filter in various scenarios including digital video (DV) capture, audio recompression, and conversion of Audio-Video Interleaved (AVI) or MPEG digital media files for network streaming. This filter provides the only way to create Microsoft Windows Media Audio and Windows Media Video files in DirectShow.

For more information, see [Creating ASF Files in DirectShow](creating-asf-files-in-directshow.md).

The following table contains information about the WM ASF Writer filter, such as the interfaces and media types it supports.



| Filter Information                       |  Types                                                                                                                                                                                                                       |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter interfaces      | **IAMFilterMiscFlags**, **IBaseFilter**, **IConfigAsfWriter**, **IFileSinkFilter2**, IMediaSeeking, IPersistStream, IServiceProvider, ISpecifyPropertyPages, **IWMIndexer2**, **IWMHeaderInfo**, **IWMWriterAdvanced2** |
| Input pin media types  | Dependent on the profile. Typically uncompressed types like MEDIATYPE\_Audio or MEDIATYPE\_Video, although compressed types can be accepted if they match the profile                                                   |
| Input pin interfaces   | **IPin**, **IMemInputPin**, **IAMStreamConfig**, **IServiceProvider**, **IAMWMBufferPass**, **IWMStreamConfig2** (through **IServiceProvider**)                                                                         |
| Output pin media types | Not applicable                                                                                                                                                                                                          |
| Output pin interfaces  | Not applicable                                                                                                                                                                                                          |
| Filter CLSID           | CLSID\_WMAsfWriter                                                                                                                                                                                                      |
| Property page CLSID    | CLSID\_WMAsfWriterProperties                                                                                                                                                                                            |
| Executable             | Qasf.dll                                                                                                                                                                                                                |
| Merit                  | MERIT\_DO\_NOT\_USE                                                                                                                                                                                                     |
| Filter Category        | Not specified                                                                                                                                                                                                           |



 

## Remarks

The number of input pins on the filter depends on the profile that is passed to the filter. One pin of the appropriate media type is created for each stream defined in the profile.

The input pins support one method from the **IAMStreamConfig** interface: **IAMStreamConfig::GetFormat**. All other methods return E\_NOTIMPL. Call the **GetFormat** method to query the pin's destination compression format, which is defined by the current profile. Use the [**IConfigAsfWriter**](/previous-versions/windows/desktop/legacy/dd743205(v=vs.85)) interface to set the profile.

The filter's **IServiceProvider** interface enables applications to retrieve the [**IWMWriterAdvanced2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced2) interface, which is defined in the Windows Media Format SDK. The **IWMWriterAdvanced2** interface controls video deinterlacing, and is useful if the input is an [*interlaced*](wmformat-glossary.md) source, such as DV (digital video). Use the **GetInputSetting** and **SetInputSetting** methods to control deinterlacing. It is not recommended that clients use any of the other methods on this interface. This interface can only be obtained after the filter has been added to the filter graph. The following example shows how to query for this interface:


```C++
// Assume that m_pGraph is a valid IGraphBuilder interface pointer,
// and that pAsfWriter points to the IBaseFilter interface
// on the WM ASF Writer filter.

IServiceProvider *pProvider = NULL;
IWMWriterAdvanced2 *pWMWA2 = NULL;

hr = m_pGraph->AddFilter(pAsfWriter, L"WM ASF Writer");
...
hr = pAsfWriter->QueryInterface(IID_IServiceProvider, (void**)&pProvider)
if (SUCCEEDED(hr))
{
    hr = pProvider->QueryService(IID_IWMWriterAdvanced2,
        IID_IWMWriterAdvanced2, (void**)&pWMWA2);
    pProvider->Release();
}

```



## Related topics

<dl> <dt>

[**DirectShow QASF Reference**](directshow-qasf-reference.md)
</dt> </dl>

 

 
