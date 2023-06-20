---
description: Previewing the Project
ms.assetid: 00d72a39-f848-47ea-8460-8b826684eeea
title: Previewing the Project
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Previewing the Project

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

To preview the project, you need a component called a *render engine*, which builds a DirectShow filter graph from a timeline. The filter graph is what actually renders the project. You can use the render engine to preview a project or to write the final output file.

This article does not go into detail about the render engine. For preview, you only need a few method calls. You can find a more thorough discussion, including how to write output files, in [Rendering a Project](rendering-a-project.md). The following code example shows how to construct a preview graph.


```C++
IRenderEngine *pRender = NULL; 
hr = CoCreateInstance(CLSID_RenderEngine, NULL, CLSCTX_INPROC_SERVER,
            IID_IRenderEngine, (void**) &pRender);

hr = pRender->SetTimelineObject(pTL);
hr = pRender->ConnectFrontEnd( );
hr = pRender->RenderOutputPins( );
```



Create the render engine using the **CoCreateInstance** function. Then call the following methods on the render engine's [**IRenderEngine**](irenderengine.md) interface:

-   [**SetTimelineObject**](irenderengine-settimelineobject.md). Specifies the timeline to use.
-   [**ConnectFrontEnd**](irenderengine-connectfrontend.md). Builds a partial filter graph, with one output pin for each group in the timeline.
-   [**RenderOutputPins**](irenderengine-renderoutputpins.md). Completes the preview graph by connecting each output pin to a video or audio renderer.

Once the graph is built, you can preview the project by running the graph, as you would with any DirectShow filter graph. First, obtain a pointer to the filter graph by calling the [**IRenderEngine::GetFilterGraph**](irenderengine-getfiltergraph.md) method.


```C++
IGraphBuilder   *pGraph = NULL;
hr = pRender->GetFilterGraph(&pGraph);
```



Query the filter graph for the [**IMediaControl**](/windows/desktop/api/Control/nn-control-imediacontrol) and [**IMediaEvent**](/windows/desktop/api/Control/nn-control-imediaevent) interfaces. Use these two interfaces to run the graph and wait for playback to complete. For an explanation of how to use these interfaces, see [How To Play a File](how-to-play-a-file.md) and [Responding to Events](responding-to-events.md). The following code shows one way to use these interfaces.


```C++
IMediaControl   *pControl = NULL;
IMediaEvent     *pEvent = NULL;
long evCode;
pGraph->QueryInterface(IID_IMediaControl, (void **)&pControl);
pGraph->QueryInterface(IID_IMediaEvent, (void **)&pEvent);
hr = pControl->Run();
hr = pEvent->WaitForCompletion(INFINITE, &evCode);
pControl->Stop();
```



The code in this example blocks program execution until playback completes, because of the INFINITE parameter in the [**IMediaEvent::WaitForCompletion**](/windows/desktop/api/Control/nf-control-imediaevent-waitforcompletion) method call. If something goes wrong during playback, however, it could cause the program to stop responding. In a real application, use a message loop to wait for playback to complete. It's also recommended that you provide the user with a way to interrupt playback.

When you finish using the render engine, always call the [**IRenderEngine::ScrapIt**](irenderengine-scrapit.md) method. This method deletes the filter graph and releases any resources held by the render engine.


```C++
pRender->ScrapIt();
```



## Related topics

<dl> <dt>

[Loading and Previewing a Project](loading-and-previewing-a-project.md)
</dt> </dl>

 

 



