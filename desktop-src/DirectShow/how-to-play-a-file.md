---
description: How To Play a File
ms.assetid: 3d8c5d06-8690-4298-a1d1-f21af35bcfd4
title: How To Play a File
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# How To Play a File

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This article is intended to give you the flavor of DirectShow programming. It presents a simple console application that plays an audio or video file. The program is only a few lines long, but it demonstrates some of the power of DirectShow programming.

As the article [Introduction to DirectShow Application Programming](introduction-to-directshow-application-programming.md) describes, a DirectShow application always performs the same basic steps:

1.  Create an instance of the [Filter Graph Manager](filter-graph-manager.md).
2.  Use the Filter Graph Manager to build a filter graph.
3.  Run the graph, causing data to move through the filters.

To compile and link the code in this topic, include the header file Dshow.h and link to the static library file strmiids.lib. For more information, see [Building DirectShow Applications](setting-up-the-build-environment.md).

Start by calling [**CoInitialize**](/windows/desktop/api/objbase/nf-objbase-coinitialize) or [**CoInitializeEx**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex) to initialize the COM library:


```C++
HRESULT hr = CoInitialize(NULL);
if (FAILED(hr))
{
    // Add error-handling code here. (Omitted for clarity.)
}
```



To keep things simple, this example ignores the return value, but you should always check the **HRESULT** value from any method call.

Next, call [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) to create the Filter Graph Manager:


```C++
IGraphBuilder *pGraph;
HRESULT hr = CoCreateInstance(CLSID_FilterGraph, NULL, 
    CLSCTX_INPROC_SERVER, IID_IGraphBuilder, (void **)&pGraph);
```



As shown, the class identifier (CLSID) is CLSID\_FilterGraph. The Filter Graph Manager is provided by an in-process DLL, so the execution context is **CLSCTX\_INPROC\_SERVER**. DirectShow supports the free-threading model, so you can also call [**CoInitializeEx**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex) with the **COINIT\_MULTITHREADED** flag.

The call to [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) returns the [**IGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-igraphbuilder) interface, which mostly contains methods for building the filter graph. Two other interfaces are needed for this example:

-   [**IMediaControl**](/windows/desktop/api/Control/nn-control-imediacontrol) controls streaming. It contains methods for stopping and starting the graph.
-   [**IMediaEvent**](/windows/desktop/api/Control/nn-control-imediaevent) has methods for getting events from the Filter Graph Manager. In this example, the interface is used to wait for playback to complete.

Both of these interfaces are exposed by the Filter Graph Manager. Use the returned [**IGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-igraphbuilder) pointer to query for them:


```C++
IMediaControl *pControl;
IMediaEvent   *pEvent;
hr = pGraph->QueryInterface(IID_IMediaControl, (void **)&pControl);
hr = pGraph->QueryInterface(IID_IMediaEvent, (void **)&pEvent);
```



Now you can build the filter graph. For file playback, this is done by a single method call:


```C++
hr = pGraph->RenderFile(L"C:\\Example.avi", NULL);
```



The [**IGraphBuilder::RenderFile**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-renderfile) method builds a filter graph that can play the specified file. The first parameter is the file name, represented as a wide character (2-byte) string. The second parameter is reserved and must equal **NULL**.

This method can fail if the specified file does not exist, or the file format is not recognized. Assuming that the method succeeds, however, the filter graph is now ready for playback. To run the graph, call the [**IMediaControl::Run**](/windows/desktop/api/Control/nf-control-imediacontrol-run) method:


```C++
hr = pControl->Run();
```



When the filter graph runs, data moves through the filters and is rendered as video and audio. Playback occurs on a separate thread. You can wait for playback to complete by calling the [**IMediaEvent::WaitForCompletion**](/windows/desktop/api/Control/nf-control-imediaevent-waitforcompletion) method:


```C++
long evCode = 0;
pEvent->WaitForCompletion(INFINITE, &evCode);
```



This method blocks until the file is done playing, or until the specified time-out interval elapses. The value INFINITE means the application blocks indefinitely until the file is done playing. For a more realistic example of event handling, see [Responding to Events](responding-to-events.md).

When the application is finished, release the interface pointers and close the COM library:


```C++
pControl->Release();
pEvent->Release();
pGraph->Release();
CoUninitialize();
```



## Example Code

Here is the complete code for the example described in this article:


```C++
#include <dshow.h>
void main(void)
{
    IGraphBuilder *pGraph = NULL;
    IMediaControl *pControl = NULL;
    IMediaEvent   *pEvent = NULL;

    // Initialize the COM library.
    HRESULT hr = CoInitialize(NULL);
    if (FAILED(hr))
    {
        printf("ERROR - Could not initialize COM library");
        return;
    }

    // Create the filter graph manager and query for interfaces.
    hr = CoCreateInstance(CLSID_FilterGraph, NULL, CLSCTX_INPROC_SERVER, 
                        IID_IGraphBuilder, (void **)&pGraph);
    if (FAILED(hr))
    {
        printf("ERROR - Could not create the Filter Graph Manager.");
        return;
    }

    hr = pGraph->QueryInterface(IID_IMediaControl, (void **)&pControl);
    hr = pGraph->QueryInterface(IID_IMediaEvent, (void **)&pEvent);

    // Build the graph. IMPORTANT: Change this string to a file on your system.
    hr = pGraph->RenderFile(L"C:\\Example.avi", NULL);
    if (SUCCEEDED(hr))
    {
        // Run the graph.
        hr = pControl->Run();
        if (SUCCEEDED(hr))
        {
            // Wait for completion.
            long evCode;
            pEvent->WaitForCompletion(INFINITE, &evCode);

            // Note: Do not use INFINITE in a real application, because it
            // can block indefinitely.
        }
    }
    pControl->Release();
    pEvent->Release();
    pGraph->Release();
    CoUninitialize();
}
```



## Related topics

<dl> <dt>

[Basic DirectShow Tasks](basic-directshow-tasks.md)
</dt> </dl>

 

 
