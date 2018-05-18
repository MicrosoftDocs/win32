---
Description: DMO Wrapper Filter
ms.assetid: 'ffa6234d-9040-4838-8f51-0cf87df40a5c'
title: DMO Wrapper Filter
---

# DMO Wrapper Filter

The DMO Wrapper filter enables a DirectShow application to use a [DirectX Media Object](directx-media-objects.md) (DMO) within a filter graph. The filter wraps the DMO and handles all the details of using the DMO, such as passing data to and from the DMO. Also, the filter aggregates the DMO, so the application can query the filter for any COM interfaces that the DMO exposes.



|                                          |                                                                                                                                                                                                                                                    |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](ibasefilter.md), [**IDMOWrapperFilter**](idmowrapperfilter.md), [**IPersistStream**](https://msdn.microsoft.com/library/windows/desktop/ms690091)                                                                                                                       |
| Input Pin Media Types                    | See Remarks                                                                                                                                                                                                                                        |
| Input Pin Interfaces                     | [**IMemInputPin**](imeminputpin.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md)                                                                                                                                             |
| Output Pin Media Types                   | See Remarks                                                                                                                                                                                                                                        |
| Output Pin Interfaces                    | [**IAMStreamConfig**](iamstreamconfig.md), [**IAMVideoCompression**](iamvideocompression.md), [**IMediaPosition**](imediaposition.md), [**IMediaSeeking**](imediaseeking.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md) |
| Filter CLSID                             | CLSID\_DMOWrapperFilter                                                                                                                                                                                                                            |
| Property Page CLSID                      | No property page                                                                                                                                                                                                                                   |
| Executable                               | Qasf.dll                                                                                                                                                                                                                                           |
| [Merit](merit.md)                       | See Remarks                                                                                                                                                                                                                                        |
| [Filter Category](filter-categories.md) | See Remarks                                                                                                                                                                                                                                        |



 

## Remarks

### Limitations

The DMO Wrapper has the following limitations:

-   It does not support DMOs with zero inputs, multiple inputs, or zero outputs. (It does support DMOs with one input and multiple outputs.)
-   It does not support custom transports. All data transport is done through the [**IMemInputPin**](imeminputpin.md) interface.
-   It does not use the **IMediaObjectInPlace** interface; all processing is done using [**IMediaObject**](imediaobject.md) methods.

### Pins

For each input stream on the DMO, the filter creates a corresponding input pin. For each output stream, it creates a corresponding output pin. The media types that each pin supports depends on the DMO

### Encoder Interfaces

If the DMO is a video encoder or an audio encoder, the output pin exposes the [**IAMStreamConfig**](iamstreamconfig.md) interface. If the DMO is a video encoder, the output pin also exposes the [**IAMVideoCompression**](iamvideocompression.md) interface. In both cases, if the DMO supports the interface, the pin delegates to the DMO. Otherwise, the pin provides its own implementation.

### Streaming

The filter uses the [**IMemInputPin**](imeminputpin.md) interface to handle all streaming. It does not support [**IAsyncReader**](iasyncreader.md) connections. The filter calls [**IMediaObject::ProcessOutput**](imediaobject-processoutput.md) on the DMO only when it receives data from upstream (including end-of-stream notifications). Therefore, it does not support DMOs with zero input streams.

### Seeking

All seek requests are passed to the upstream filter, through the first input pin on the DMO Wrapper. For multiple-output DMOs, this means that the upstream filter might receive multiple seek requests when the application seeks the graph.

### Merit

DirectShow assigns all DMOs a default merit value of **MERIT\_NORMAL** + 0x800. This value falls between **MERIT\_NORMAL** and **MERIT\_PREFERRED**. Decoder filters generally have a merit value of **MERIT\_NORMAL**. Therefore, the filter graph manager will usually select a DMO decoder over a decoder filter. To override the default merit value, add a registry entry to the DMO's registry key in HKEY\_CLASSES\_ROOT\\CLSID. Include a **DWORD** value named "Merit" whose value specifies the merit.

### Category

The DMO Wrapper filter does not appear by itself in any category. When it wraps a DMO, it appears in the DirectShow category that corresponds to the DMO's category, under the name of the DMO.

### Buffers

The DMO Wrapper filter passes media buffers to the DMO which expose the [**IMediaBuffer**](imediabuffer.md) interface.

In Windows Vista or later, the media buffers also expose the IServiceProvider interface. The DMO can use this interface to get a pointer to the media sample that is associated with the buffer. Use the service identifier **IID\_IMediaSample**. A video DMO can use the media sample's [**IMediaSample2**](imediasample2.md) interface to set interlace flags on the sample. The following code shows how to get the pointer to the media sample:


```C++
IServiceProvider *pSp = NULL;
IMediaSample2 *pSample2 = NULL;
HRESULT hr = S_OK;

hr = pBuffer->QueryInterface(IID_IServiceProvider, (void**)&amp;pSp);
if (SUCCEEDED(hr))
{
    hr = pSp->QueryService(
        IID_IMediaSample,  // Service identifier.
        IID_IMediaSample2, // Interface identifier.
        (void**)&amp;pSample2
        );
    if (SUCCEEDED(hr))
    {
        // Set flags (not shown).
        pSample2->Release();
    }
    pSp->Release();
}
```



For more information about per-sample interlace flags, see [**AM\_SAMPLE2\_PROPERTIES Structure**](am-sample2-properties.md).

### Quality Control

If the DMO exposes the [**IDMOQualityControl**](idmoqualitycontrol.md) interface, the filter translates [**IQualityControl::Notify**](iqualitycontrol-notify.md) calls on its output pin into [**IDMOQualityControl::SetNow**](idmoqualitycontrol-setnow.md) calls on the DMO. The *rtNow* parameter of **SetNow** is calculated as the sum of the **TimeStamp** and **Late** members of the [**Quality**](quality.md) structure.

### Using the Fiter in GraphEdit

In GraphEdit, the DMO Wrapper filter does not appear under its own name. Instead, each registered DMO is listed under the appropriate filter category. When you add a DMO through the **Insert Filters** dialog, GraphEdit creates the DMO Wrapper filter and configures it to use that DMO.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[DirectX Media Objects](directx-media-objects.md)
</dt> </dl>

 

 



