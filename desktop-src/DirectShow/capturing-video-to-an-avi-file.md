---
Description: Capturing Video to an AVI File
ms.assetid: 0f5f4a82-4a2e-4c48-b201-bda641cb8619
title: Capturing Video to an AVI File
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Capturing Video to an AVI File

The following illustration shows the simplest possible graph for capturing video to an AVI file.

![avi video capture graph](images/vidcap02.png)

The [AVI Mux](avi-mux-filter.md) filter takes the video stream from the capture pin and packages it into an AVI stream. An audio stream could also be connected to the AVI Mux filter, in which case the mux would interleave the two streams. The [File Writer](file-writer-filter.md) filter writes the AVI stream to disk.

To build the graph, start by calling the [**ICaptureGraphBuilder2::SetOutputFileName**](/windows/win32/Strmif/nf-strmif-icapturegraphbuilder2-setoutputfilename?branch=master) method, as follows:


```C++
IBaseFilter *pMux;
hr = pBuild->SetOutputFileName(
    &amp;MEDIASUBTYPE_Avi,  // Specifies AVI for the target file.
    L"C:\\Example.avi", // File name.
    &amp;pMux,              // Receives a pointer to the mux.
    NULL);              // (Optional) Receives a pointer to the file sink.
```



The first parameter specifies the file type — in this case, AVI. The second parameter gives the file name. For AVI, the SetOutputFileName method cocreates the AVI Mux filter and the File Writer filter and adds them to the graph. It also sets the file name on the File Writer filter, by calling the [**IFileSinkFilter::SetFileName**](/windows/win32/Strmif/nf-strmif-ifilesinkfilter-setfilename?branch=master) method, and connects the two filters. The method returns a pointer to the AVI Mux in the third parameter. Optionally, it returns a pointer to the [**IFileSinkFilter**](/windows/win32/Strmif/nn-strmif-ifilesinkfilter?branch=master) interface in the fourth parameter. If you don't need this interface, you can set this parameter to **NULL**, as shown in the previous example.

Next, call the [**ICaptureGraphBuilder2::RenderStream**](/windows/win32/Strmif/nf-strmif-icapturegraphbuilder2-renderstream?branch=master) method to connect the capture filter to the AVI Mux, as follows:


```C++
hr = pBuild->RenderStream(
    &amp;PIN_CATEGORY_CAPTURE, // Pin category.
    &amp;MEDIATYPE_Video,      // Media type.
    pCap,                  // Capture filter.
    NULL,                  // Intermediate filter (optional).
    pMux);                 // Mux or file sink filter.

// Release the mux filter.
pMux->Release();
```



The first parameter gives the pin category, which is PIN\_CATEGORY\_CAPTURE for capture. The second parameter gives the media type. The third parameter is a pointer to the capture filter's [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master) interface. The fourth parameter is optional; it lets you route the video stream through an intermediate filter, such as an encoder, before passing it to the mux filter. Otherwise, set this parameter to **NULL**, as shown in the previous example. The fifth parameter is the pointer to the mux filter. This pointer is obtained by calling the SetOutputFileName method.

To capture audio, call RenderStream with the media type MEDIATYPE\_Audio. If you are capturing audio and video from two separate devices, it is a good idea to make the audio stream the master stream. This helps to prevent drift between the two streams, because the AVI Mux filter adjust the playback rate on the video stream to match the audio stream. To set the master stream, call the [**IConfigAviMux::SetMasterStream**](/windows/win32/Strmif/nf-strmif-iconfigavimux-setmasterstream?branch=master) method on the AVI Mux filter:


```C++
IConfigAviMux *pConfigMux = NULL;
hr = pMux->QueryInterface(IID_IConfigAviMux, (void**)&amp;pConfigMux);
if (SUCCEEDED(hr))
{
    pConfigMux->SetMasterStream(1);
    pConfigMux->Release();
}
```



The parameter to SetMasterStream is the stream number, which is determined by the order in which you call RenderStream. For example, if you call RenderStream first for video and then for audio, the video is stream 0 and the audio is stream 1.

You may also want to set how the AVI Mux filter interleaves the audio and video streams, by calling the [**IConfigInterleaving::put\_Mode**](/windows/win32/Strmif/nf-strmif-iconfiginterleaving-put_mode?branch=master) method.


```C++
IConfigInterleaving *pInterleave = NULL;
hr = pMux->QueryInterface(IID_IConfigInterleaving, (void**)&amp;pInterleave);
if (SUCCEEDED(hr))
{
    pInterleave->put_Mode(INTERLEAVE_CAPTURE);
    pInterleave->Release();
}
```



With the INTERLEAVE\_CAPTURE flag, the AVI Mux performs interleaving at a rate that is suitable for video capture. You can also use INTERLEAVE\_NONE, which means no interleaving — the AVI Mux will simply write the data in the order that it arrives. The INTERLEAVE\_FULL flag means the AVI Mux performs full interleaving; however, this mode is less suitable for video capture because it requires the most overheard.

Encoding the Video Stream

You can encode the video stream by inserting an encoder filter between the capture filter and the AVI Mux filter. Use the [System Device Enumerator](system-device-enumerator.md) or the [Filter Mapper](filter-mapper.md) to select an encoder filter. (For more information, see [Enumerating Devices and Filters](enumerating-devices-and-filters.md).)

Specify the encoder filter as the fourth parameter to RenderStream, shown in bold in the following example:


```C++
IBaseFilter *pEncoder;
/* Create the encoder filter (not shown). */
// Add it to the filter graph.
pGraph->AddFilter(pEncoder, L"Encoder);

/* Call SetOutputFileName as shown previously. */

// Render the stream.
hr = pBuild->RenderStream(&amp;PIN_CATEGORY_CAPTURE, &amp;MEDIATYPE_Video, 
    pCap, 
pEncoder, pMux);
pEncoder->Release();
```



The encoder filter might support [**IAMVideoCompression**](/windows/win32/Strmif/nn-strmif-iamvideocompression?branch=master) or other interfaces for setting the encoding parameters. For a list of possible interfaces, see [File Encoding and Decoding Interfaces](file-encoding-and-decoding-interfaces.md).

## Related topics

<dl> <dt>

[Capturing Video to a File](capturing-video-to-a-file.md)
</dt> </dl>

 

 



