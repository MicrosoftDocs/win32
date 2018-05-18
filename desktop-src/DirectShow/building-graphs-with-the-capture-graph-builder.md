---
Description: Building Graphs with the Capture Graph Builder
ms.assetid: '0329c4f0-ee6f-423e-b38b-169204e3a31c'
title: Building Graphs with the Capture Graph Builder
---

# Building Graphs with the Capture Graph Builder

Despite its name, the Capture Graph Builder is useful for building many kinds of custom filter graphs, not only capture graphs. This article provides a brief overview of how to use this object.

The Capture Graph Builder exposes the [**ICaptureGraphBuilder2**](icapturegraphbuilder2.md) interface. Start by calling [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615) to create the Capture Graph Builder and the Filter Graph Manager. Then initialize the Capture Graph Builder by calling [**ICaptureGraphBuilder2::SetFiltergraph**](icapturegraphbuilder2-setfiltergraph.md) with a pointer to the Filter Graph Manager, as follows:


```C++
IGraphBuilder *pGraph = NULL;
ICaptureGraphBuilder2 *pBuilder = NULL;

// Create the Filter Graph Manager.
HRESULT hr =  CoCreateInstance(CLSID_FilterGraph, NULL,
    CLSCTX_INPROC_SERVER, IID_IGraphBuilder, (void **)&amp;pGraph);

if (SUCCEEDED(hr))
{
    // Create the Capture Graph Builder.
    hr = CoCreateInstance(CLSID_CaptureGraphBuilder2, NULL,
        CLSCTX_INPROC_SERVER, IID_ICaptureGraphBuilder2, 
        (void **)&amp;pBuilder);
    if (SUCCEEDED(hr))
    {
        pBuilder->SetFiltergraph(pGraph);
    }
};
```



## Connecting Filters

The [**ICaptureGraphBuilder2::RenderStream**](icapturegraphbuilder2-renderstream.md) method connects two or three filters together in a chain. Generally, the method works best when each filter has no more than one input pin or output pin of the same type. This discussion begins by ignoring the first two parameters of **RenderStream** and focusing on the last three parameters. The third parameter is an [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) pointer, which can specify either a filter (as an [**IBaseFilter**](ibasefilter.md) interface pointer) or an output pin (as an [**IPin**](ipin.md) interface pointer). The fourth and fifth parameters specify **IBaseFilter** pointers. The **RenderStream** method connects all three filters in a chain. For example, suppose that *A*, *B*, and *C* are filters. Assume for now that each filter has exactly one input pin and one output pin. The following call connects A to B, and then B to C:

<dl> `RenderStream(NULL, NULL, A, B, C)`  
</dl>

All connections are "intelligent," meaning that additional filters are added to the graph as needed. For details, see [Intelligent Connect](intelligent-connect.md). To connect just two filters, set the middle value to **NULL**. For example, this call connects A to C:

<dl> `RenderStream(NULL, NULL, A, NULL, C)`  
</dl>

You can create longer chains by calling the method twice:

<dl> `RenderStream(NULL, NULL, A, B, C)`  
`RenderStream(NULL, NULL, C, D, E)`  
</dl>

If the last parameter is **NULL**, the method automatically locates a default renderer. It uses the [Video Renderer](video-renderer-filter.md) for video and the [DirectSound Renderer](directsound-renderer-filter.md) for audio. Thus:

<dl> `RenderStream(NULL, NULL, A, NULL, NULL)`  
</dl>

is equivalent to

<dl> `RenderStream(NULL, NULL, A, NULL, R)`  
</dl>

where *R* is the appropriate renderer. To connect the Video Mixing Renderer filter instead of the Video Renderer, however, you must specify it explicitly.

If you specify a filter in the third parameter, rather than a pin, you may need to indicate which output pin should be used for the connection. That is the purpose of the method's first two parameters. The first parameter applies only to capture filters. It specifies a GUID that indicates a pin category. For a complete list of categories, see [Pin Property Set](pin-property-set.md). Two of the categories are valid for all capture filters:

-   **PIN\_CATEGORY\_CAPTURE**
-   **PIN\_CATEGORY\_PREVIEW**

If a capture filter does not supply separate pins for capture and preview, the [**RenderStream**](icapturegraphbuilder2-renderstream.md) method inserts a [Smart Tee](smart-tee-filter.md) filter, which splits the stream into a capture stream and a preview stream. From the application's standpoint, you can simply treat all capture filters as having separate pins and ignore the underlying topology of the graph.

For file capture, connect the capture pin to a mux filter. For live preview, connect the preview pin to a renderer. If you switch the two categories, the graph might drop an excessive number of frames during the file capture; but if the graph is connected properly, it drops preview frames as needed in order to maintain throughput on the capture stream.

The following example shows how to connect both streams:


```C++
// Capture to file:
pBuilder->RenderStream(&amp;PIN_CATEGORY_CAPTURE, NULL, pCapFilter, NULL, pMux);
// Preview:
pBuilder->RenderStream(&amp;PIN_CATEGORY_PREVIEW, NULL, pCapFilter, NULL, NULL);
```



Some capture filters also support closed captions, indicated by **PIN\_CATEGORY\_VBI**. To capture the closed captions to a file, render this category to the mux filter. To view the closed captions in your preview window, connect to the renderer:


```C++
// Capture to file:
pBuilder->RenderStream(&amp;PIN_CATEGORY_VBI, NULL, pCapFilter, NULL, pMux);
// Preview on screen:
pBuilder->RenderStream(&amp;PIN_CATEGORY_VBI, NULL, pCapFilter, NULL, NULL);
```



The second parameter to [**RenderStream**](icapturegraphbuilder2-renderstream.md) identifies the media type, and is typically one of the following:

-   MEDIATYPE\_Audio
-   MEDIATYPE\_Video
-   MEDIATYPE\_Interleaved (DV)

You can use this parameter whenever the filter's output pins support the enumeration of preferred media types. For file sources, the Capture Graph Builder automatically adds a parser filter if needed, and then queries the media types on the parser. (For an example, see [Recompressing an AVI File](recompressing-an-avi-file.md).) Also, if the last filter in the chain has several input pins, the method attempts to enumerate their media types. However, not all filters support this functionality.

## Finding Interfaces on Filters and Pins

After you build a graph, you will typically need to locate various interfaces exposed by filters and pins in the graph. For example, a capture filter might expose the [**IAMDroppedFrames**](iamdroppedframes.md) interface, while the filter's output pins might expose the [**IAMStreamConfig**](iamstreamconfig.md) interface.

The simplest way to find an interface is to use the [**ICaptureGraphBuilder2::FindInterface**](icapturegraphbuilder2-findinterface.md) method. This method walks the graph (filters and pins) until it locates the desired interface. You can specify the starting point for the search, and you can limit the search to filters upstream or downstream from the starting point.

The following example searches for the [**IAMStreamConfig**](iamstreamconfig.md) interface on a video preview pin:


```C++
IAMStreamConfig *pConfig = NULL;
HRESULT hr = pBuild->FindInterface(
    &amp;PIN_CATEGORY_PREVIEW, 
    &amp;MEDIATYPE_Video,
    pVCap, 
    IID_IAMStreamConfig, 
    (void**)&amp;pConfig
);
if (SUCCESSFUL(hr))
{
    /* ... */
    pConfig->Release();
}
```



> [!Note]  
> The topic [Find an Interface on a Filter or Pin](find-an-interface-on-a-filter-or-pin.md) shows an alternative approach that uses the [**IGraphBuilder**](igraphbuilder.md) interface instead of [**ICaptureGraphBuilder2**](icapturegraphbuilder2.md). Which approach to use depends on your application. If your application already uses **ICaptureGraphBuilder2** to build the graph, then [**ICaptureGraphBuilder2::FindInterface**](icapturegraphbuilder2-findinterface.md) is a good approach. Otherwise, consider using the **IGraphBuilder** methods.

 

## Finding Pins

Less commonly, you may need to locate an individual pin on a filter, although in most cases the [**RenderStream**](icapturegraphbuilder2-renderstream.md) and [**FindInterface**](icapturegraphbuilder2-findinterface.md) methods will save you the trouble. If you do need to find a particular pin on a filter, the [**ICaptureGraphBuilder2::FindPin**](icapturegraphbuilder2-findpin.md) helper method is useful. Specify the category, the media type (video or audio), the direction, and whether the pin must be unconnected.

For example, the following code searches for an unconnected video preview pin on a capture filter:


```C++
IPin *pPin = NULL;
hr = pBuild->FindPin(
    pCap,                   // Pointer to the filter to search.
    PINDIR_OUTPUT,          // Search for an output pin.
    &amp;PIN_CATEGORY_PREVIEW,  // Search for a preview pin.
    &amp;MEDIATYPE_Video,       // Search for a video pin.
    TRUE,                   // The pin must be unconnected. 
    0,                      // Return the first matching pin (index 0).
    &amp;pPin);                 // This variable receives the IPin pointer.
if (SUCCESSFUL(hr))
{
    /* ... */
    pPin->Release();
}
```



## Related topics

<dl> <dt>

[Video Capture](video-capture.md)
</dt> </dl>

 

 



