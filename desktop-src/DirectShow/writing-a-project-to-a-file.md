---
description: Writing a Project to a File
ms.assetid: 84499e4f-4f45-4aa6-aa89-d95c3b6b47d0
title: Writing a Project to a File
ms.topic: article
ms.date: 05/31/2018
---

# Writing a Project to a File

\[This API is not supported and may be altered or unavailable in the future.\]

This article describes how to write a [DirectShow Editing Services](directshow-editing-services.md) project to a file. First it describes how to write a file with the basic render engine. Then it describes smart recompression with the smart render engine.

For an overview of how DirectShow Editing Services renders projects, see [About the Render Engines](about-the-render-engines.md).

**Using the Basic Render Engine**

Start by building the front end of the graph, as follows:

1.  Create the render engine.
2.  Specify the timeline.
3.  Set the render range. (Optional)
4.  Build the front end of the graph.

The following code example shows these steps.


```C++
IRenderEngine *pRender = NULL; 
hr = CoCreateInstance(CLSID_RenderEngine, NULL, CLSCTX_INPROC,
    IID_IRenderEngine, (void**) &pRender);

hr = pRender->SetTimelineObject(pTL);
hr = pRender->ConnectFrontEnd( );
```



Next, add multiplexer and file-writing filters to the filter graph. The easiest way to do this is with the [Capture Graph Builder](capture-graph-builder.md), a DirectShow component for building capture graphs. The capture graph builder exposes the [**ICaptureGraphBuilder2**](/windows/desktop/api/Strmif/nn-strmif-icapturegraphbuilder2) interface. Perform the following steps:

1.  Create an instance of the capture graph builder.
2.  Obtain a pointer to the graph and pass it to the graph builder.
3.  Specify the name and media type of the output file. This step also obtains a pointer to the mux filter, which is required later.

The following code example shows these steps.


```C++
CoCreateInstance(CLSID_CaptureGraphBuilder2, NULL, CLSCTX_INPROC, 
    IID_ICaptureGraphBuilder2, (void **)&pBuilder);

// Get a pointer to the graph front end.
IGraphBuilder *pGraph;
pRender->GetFilterGraph(&pGraph);
pBuilder->SetFiltergraph(pGraph);

// Create the file-writing section.
IBaseFilter *pMux;
pBuilder->SetOutputFileName(&MEDIASUBTYPE_Avi, 
    OLESTR("Output.avi"), &pMux, NULL);
```



Finally, connect the output pins on the front end to the mux filter.

1.  Retrieve the number of groups.
2.  For each pin, obtain a pointer to the pin.
3.  Optionally, create an instance of a compression filter to compress the stream. The type of compressor will depend on the media type of the group. You can use the [System Device Enumerator](system-device-enumerator.md) to enumerate the available compression filters. For more information, see [Enumerating Devices and Filters](enumerating-devices-and-filters.md).
4.  Optionally, set compression parameters such as the key-frame rate. This step is discussed in detail later in the article.
5.  Call [**ICaptureGraphBuilder2::RenderStream**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-renderstream). This method takes pointers to the pin, the compression filter (if any), and the multiplexer.

The following code example shows how to connect the output pins.


```C++
long NumGroups;
pTimeline->GetGroupCount(&NumGroups);

// Loop through the groups and get the output pins.
for (i = 0; i < NumGroups; i++)
{
    IPin *pPin;
    if (pRender->GetGroupOutputPin(i, &pPin) == S_OK) 
    {
        IBaseFilter *pCompressor;
        // Create a compressor filter. (Not shown.)
        // Set compression parameters. (Not shown.)

        // Connect the pin.
        pBuilder->RenderStream(NULL, NULL, pPin, pCompressor, pMux);
        pCompressor->Release();
        pPin->Release();
    }
}
```



To set compression parameters (step 4, previously), use the [**IAMVideoCompression**](/windows/desktop/api/Strmif/nn-strmif-iamvideocompression) interface. This interface is exposed on the output pins of compression filters. Enumerate the compression filter's pins, and query each output pin for **IAMVideoCompression**. (For information about enumerating pins, see [Enumerating Pins](enumerating-pins.md).) Be sure to release all the interface pointers that you obtained during this step.

After you build the filter graph, call the [**IMediaControl::Run**](/windows/desktop/api/Control/nf-control-imediacontrol-run) method on the filter graph manager. As the filter graph runs, it writes the data to a file. Use event notification to wait for playback to complete. (See [Responding to Events](responding-to-events.md).) When playback finishes, you must explicitly call [**IMediaControl::Stop**](/windows/desktop/api/Control/nf-control-imediacontrol-stop) to stop the filter graph. Otherwise, the file is not written correctly.

**Using the Smart Render Engine**

To get the benefits of smart recompression, use the smart render engine in place of the basic render engine. The steps in building the graph are almost the same. The major difference is that compression is handled in the front end of the graph, not in the file-writing section.

> [!IMPORTANT]
> Do not use the smart render engine to read or write Windows Media files.

 

Each video group has a property that specifies the compression format for that group. The compression format must exactly match the group's uncompressed format in height, width, bit depth, and frame rate. The smart render engine uses the compression format when it constructs the graph. Before you set the compression format, make sure to set the uncompressed format for that group by calling [**IAMTimelineGroup::SetMediaType**](iamtimelinegroup-setmediatype.md).

To set a group's compression format, call the [**IAMTimelineGroup::SetSmartRecompressFormat**](iamtimelinegroup-setsmartrecompressformat.md) method. This method takes a pointer to an [**SCompFmt0**](scompfmt0.md) structure. The **SCompFmt0** structure has two members: **nFormatId**, which must be zero, and **MediaType**, which is an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure. Initialize the **AM\_MEDIA\_TYPE** structure with the format information.

> [!Note]  
> If you want the final project to have the same format as one of your source files, you can get the AM\_MEDIA\_TYPE structure directly from the source file, using the media detector. See [**IMediaDet::get\_StreamMediaType**](imediadet-get-streammediatype.md).

 

Cast the [**SCompFmt0**](scompfmt0.md) variable to a pointer of type **long**, as shown in the following example.


```C++
SCompFmt0 *pFormat = new SCompFmt0;
memset(pFormat, 0, sizeof(SCompFmt0));
pFormat->nFormatId = 0;

// Initialize pFormat->MediaType. (Not shown.)

pGroup->SetSmartRecompressFormat( (long*) pFormat );
```



The smart render engine automatically searches for a compatible compression filter. You can also specify a compression filter for a group by calling [**ISmartRenderEngine::SetGroupCompressor**](ismartrenderengine-setgroupcompressor.md).

To build the graph, use the same steps that were described for the Basic Render Engine in the previous section. The only differences are the following:

-   Use the smart render engine, not the basic render engine. The class identifier is CLSID\_SmartRenderEngine.
-   Set compression parameters after you build the front end but before you render the output pins. Call the [**ISmartRenderEngine::GetGroupCompressor**](ismartrenderengine-getgroupcompressor.md) method to obtain a pointer to a group's compression filter. Then query for the [**IAMVideoCompression**](/windows/desktop/api/Strmif/nn-strmif-iamvideocompression) interface, as described previously.
-   When you render the output pins, there is no need to insert a compression filter. The stream is already compressed.

## Related topics

<dl> <dt>

[Rendering a Project](rendering-a-project.md)
</dt> </dl>

 

 



