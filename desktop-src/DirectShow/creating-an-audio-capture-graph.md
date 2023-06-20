---
description: Creating an Audio Capture Graph
ms.assetid: 2302bb40-a5db-473a-afeb-71905ac41f47
title: Creating an Audio Capture Graph
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating an Audio Capture Graph

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The first step for an audio capture application is to build a filter graph. The configuration of the graph depends on the type of file that you want to create.

-   Audio-only AVI file: Audio Capture Filter to [AVI Mux](avi-mux-filter.md) filter, and AVI Mux to [File Writer](file-writer-filter.md) filter.
-   WAV file: Audio Capture Filter to [WavDest Filter Sample](wavdest-filter-sample.md) to File Writer Filter
-   Windows Media Audio (.wma) file: Audio Capture Filter to [WM ASF Writer](wm-asf-writer-filter.md) filter.

The WavDest filter is provided as an SDK sample. To use it, you must build and register the filter.

To use the ASF Writer filter, you must install the Windows Media SDK and obtain a software key to unlock the filter. For more information, see [Using Windows Media in DirectShow](using-windows-media-in-directshow.md).

You can build the filter graph using the [Capture Graph Builder](capture-graph-builder.md) object, or you can build the graph "manually"; that is, have the application programmatically add and connect each filter. This article describes the manual approach. For more information about using the Capture Graph Builder, see [Video Capture](video-capture.md). Much of the information in that article applies to audio-only graphs.

Adding the Audio Capture Device

Because the Audio Capture Filter communicates with a specific hardware device, you cannot simply call **CoCreateInstance** to create the filter. Instead, use the [System Device Enumerator](system-device-enumerator.md) to enumerate all of the devices in the "Audio Capture Sources" category, which is identified by the class identifier CLSID\_AudioInputDeviceCategory.

The System Device Enumerator returns a list of monikers for the devices; each moniker's friendly name corresponds to the name of the device. Choose one of the returned monikers and use it to create an instance of the Audio Capture Filter for that device. Add the filter to the filter graph. The user's preferred audio recording device appears first in the moniker list. (The user selects a preferred device by clicking Sounds and Multimedia in Control Panel.)

For more information, see [Using the System Device Enumerator](using-the-system-device-enumerator.md).

To specify which input to capture from, obtain the [**IAMAudioInputMixer**](/windows/desktop/api/Strmif/nn-strmif-iamaudioinputmixer) interface from the Audio Capture filter and call the **put\_Enable** method to specify the input. One limitation of this method, however, is that different hardware devices may use different strings to identify their inputs. For example, one card may use "Microphone" to identify the microphone input and another card may use "Mic". To determine the string identifier for a given input, use the Windows Multimedia functions [**waveOutOpen**](/previous-versions//dd743866(v=vs.85)), [**mixerOpen**](/previous-versions//dd757308(v=vs.85)), and [**mixerGetLineInfo**](/previous-versions//dd757303(v=vs.85)). See the MSDN topic [Mixer Device Queries](/windows/desktop/Multimedia/mixer-device-queries) for more information.

Adding the Multiplexer and the File Writer

An audio capture graph must contain a multiplexer and a file writer.

A *multiplexer* is a filter that combines one or more streams into a single stream with a particular format. For example, the AVI Mux filter combines audio and video streams into an interleaved AVI stream. For audio capture, there is typically only a single audio stream, but the audio data must still be packaged into a format that can be saved to disk, which requires a multiplexer. The choice of multiplexer depends on the target format:

-   AVI: AVI Multiplexer
-   WAV: WavDest
-   WMA: ASF Writer

A *file writer* is a filter that writes incoming data to a file. For AVI or WAV files, use the [File Writer Filter](file-writer-filter.md). For WMA files, the ASF Writer acts as both multiplexer and file writer.

After you create the filters and add them to the graph, connect the Audio Capture Filter's output pin to the multiplexer's input pin, and connect the multiplexer's output pin to the filter writer's input pin (assuming these are separate filters). To specify the file name, query the file writer for the [**IFileSinkFilter**](/windows/desktop/api/Strmif/nn-strmif-ifilesinkfilter) interface and call the [**IFileSinkFilter::SetFileName**](/windows/desktop/api/Strmif/nf-strmif-ifilesinkfilter-setfilename) method.

### Example Code

The following example shows how to build an audio capture graph using the WavDest filter. The same principles apply for the other file types.


```C++
IBaseFilter *pSrc = NULL, *pWaveDest = NULL, *pWriter = NULL;
IFileSinkFilter *pSink= NULL;
IGraphBuilder *pGraph;

// Create the Filter Graph Manager.
hr = CoCreateInstance(CLSID_FilterGraph, NULL, CLSCTX_INPROC_SERVER,
    IID_IGraphBuilder, (void**)&pGraph);

// This example omits error handling.

// Not shown: Use the System Device Enumerator to create the 
// audio capture filter.

// Add the audio capture filter to the filter graph. 
hr = pGraph->AddFilter(pSrc, L"Capture");

// Add the WavDest and the File Writer.
hr = AddFilterByCLSID(pGraph, CLSID_WavDest, L"WavDest", &pWaveDest);
hr = AddFilterByCLSID(pGraph, CLSID_FileWriter, L"File Writer", &pWriter);

// Set the file name.
hr = pWriter->QueryInterface(IID_IFileSinkFilter, (void**)&pSink);
hr = pSink->SetFileName(L"C:\\MyWavFile.wav", NULL);

// Connect the filters.
hr = ConnectFilters(pGraph, pSrc, pWaveDest);
hr = ConnectFilters(pGraph, pWaveDest, pWriter);

// Not shown: Release interface pointers.

```



This example uses the `AddFilterByCLSID` function described in [Add a Filter by CLSID](add-a-filter-by-clsid.md), and the `ConnectFilters` function described in [Connect Two Filters](connect-two-filters.md). Neither of these is a DirectShow API.

## Related topics

<dl> <dt>

[Audio Capture](audio-capture.md)
</dt> </dl>

 

 
