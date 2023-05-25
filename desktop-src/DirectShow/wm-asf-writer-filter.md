---
description: WM ASF Writer Filter
ms.assetid: 1b12f65f-8d77-4d38-aad9-92bb15cc0426
title: WM ASF Writer Filter (DirectShow)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM ASF Writer Filter (DirectShow)

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The WM ASF Writer is a wrapper filter for the writer object provided with the Windows Media™ Format SDK. The filter accepts a variable number of input streams and creates an Advanced Systems Format (ASF) file. The filter handles all compression and multiplexing (although the compression mechanism can be bypassed). You can use the WM ASF Writer in various scenarios including digital video (DV) capture, audio recompression, and conversion of Audio-Video Interleaved (AVI) or MPEG multimedia files for network streaming. This filter provides the only way to create Microsoft® Windows Media™ Audio and Windows Media Video files in Microsoft DirectShow.

For more information, see [Creating ASF Files in DirectShow](creating-asf-files-in-directshow.md).



| Label | Value |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter interfaces                        | [**IAMFilterMiscFlags**](/windows/desktop/api/Strmif/nn-strmif-iamfiltermiscflags), [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [**IConfigAsfWriter**](/previous-versions/windows/desktop/api/Dshowasf/nn-dshowasf-iconfigasfwriter), [**IConfigAsfWriter2**](/previous-versions/windows/desktop/api/dshowasf/nn-dshowasf-iconfigasfwriter2), [**IFileSinkFilter2**](/windows/desktop/api/Strmif/nn-strmif-ifilesinkfilter2), [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), **IPersistStream**, **IServiceProvider**, **ISpecifyPropertyPages**In addition, the filter exposes the following Windows Media Format SDK interfaces: **IWMIndexer2**, **IWMHeaderInfo**, **IWMWriterAdvanced2**<br/> |
| Input pin media types                    | Depends on the ASF profile. Typically uncompressed audio and video types, although the filter will accept compressed types if they match the ASF profile.                                                                                                                                                                                                                                                                                                                                             |
| Input pin interfaces                     | [**IAMStreamConfig**](/windows/desktop/api/Strmif/nn-strmif-iamstreamconfig), [**IAMWMBufferPass**](/previous-versions/windows/desktop/api/Dshowasf/nn-dshowasf-iamwmbufferpass), [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), **IServiceProvider**In addition, the pin exposes the following Windows Media Format SDK interface: **IWMStreamConfig2** (through **IServiceProvider**)<br/>                                                                                                                                                                                 |
| Output pin media types                   | Not applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Output pin interfaces                    | Not applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Filter CLSID                             | CLSID\_WMAsfWriter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Property page CLSID                      | CLSID\_AsfWriterProperties                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Executable                               | Qasf.dll                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Merit](merit.md)                       | MERIT\_DO\_NOT\_USE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Filter Category](filter-categories.md) | Not specified                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |



 

## Remarks

The filter requires the Windows Media Format Software Development Kit (SDK) and its underlying dependencies.

The number of input pins on the filter dependings on the profile or profile identifier of the ASF stream.

The input pins support one method from the **IAMStreamConfig** interface: [**IAMStreamConfig::GetFormat**](/windows/desktop/api/Strmif/nf-strmif-iamstreamconfig-getformat). All other methods return E\_NOTIMPL. Call the **GetFormat** method to query the pin's destination compression format, which is defined by the current ASF profile. Use the [**IConfigAsfWriter**](/previous-versions/windows/desktop/api/Dshowasf/nn-dshowasf-iconfigasfwriter) interface to set the profile.

You can use the filter's **IServiceProvider** interface to get a pointer to the **IWMWriterAdvanced2** interface, which is defined in the Windows Media Format SDK. You can use the **IWMWriterAdvanced2** interface to control video deinterlacing when the source video is interlaced. To set the deinterlacing mode, call **IWMWriterAdvanced2::SetInputSetting**. For the *dwInputNum* parameter, use the zero-based index of the video input pin, as enumerated by the [**IEnumPins**](/windows/desktop/api/Strmif/nn-strmif-ienumpins) interface.

The following example shows how to query for this interface:


```C++
// Assume that pAsfWriter is a valid IBaseFilter pointer.
IServiceProvider *pProvider = NULL;
IWMWriterAdvanced2 *pWMWA2 = NULL;

hr = pAsfWriter->QueryInterface(
    IID_IServiceProvider, 
    (void**)&pProvider
    );
if (SUCCEEDED(hr))
{
    hr = pProvider->QueryService(
        IID_IWMWriterAdvanced2,
        IID_IWMWriterAdvanced2, 
        (void**)&pWMWA2
        );
    pProvider->Release();
    if (SUCCEEDED(hr))
    {
        // Use pWMWA2. (Not shown.)
        pWMWA2->Release();
    }
}
```



Applications should not use any of the **IWMWriterAdvanced** methods that the **IWMWriterAdvanced2** interface inherits. Calling any these methods could interere with the operation of the filter.

The only file-writing mode supported by this filter is AM\_FILE\_OVERWRITE. See [**IFileSinkFilter2::GetMode**](/windows/desktop/api/Strmif/nf-strmif-ifilesinkfilter2-getmode).

When the Windows Media Format SDK runtime sends WMT\_STATUS messages to the WM ASF Writer filter, the filter forwards them as [**EC\_WMT\_EVENT**](ec-wmt-event.md) events.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




