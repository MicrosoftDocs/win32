---
description: Previewing a Project
ms.assetid: '2efa3f25-a93f-4362-b461-b67475e5d78c'
title: Previewing a Project
ms.topic: article
ms.date: 05/31/2018
---

# Previewing a Project

\[This API is not supported and may be altered or unavailable in the future.\]

To preview a project, first call **CoCreateInstance** to create an instance of the Basic Render Engine. The class identifier is CLSID\_RenderEngine. Then call the [**IRenderEngine::SetTimelineObject**](irenderengine-settimelineobject.md) method to specify the timeline that you are rendering.

The first time that you preview the timeline, perform the following calls in the order listed:

1.  Call [**IRenderEngine::SetRenderRange**](irenderengine-setrenderrange.md) to specify which portion of the timeline to preview. (Optional)
2.  Call [**IRenderEngine::ConnectFrontEnd**](irenderengine-connectfrontend.md) to build the front end of the graph.
3.  Call [**IRenderEngine::RenderOutputPins**](irenderengine-renderoutputpins.md). This method connects each output pin to a video renderer or audio renderer, completing the graph.

The following code example shows these steps:


```C++
IRenderEngine *pRender = NULL; 
hr = CoCreateInstance(CLSID_RenderEngine, NULL, 
    CLSCTX_INPROC_SERVER, IID_IRenderEngine, (void**)&pRender);

hr = pRender->SetTimelineObject(pTL);
hr = pRender->ConnectFrontEnd();
hr = pRender->RenderOutputPins();
```



Now run the filter graph. First, call the [**IRenderEngine::GetFilterGraph**](irenderengine-getfiltergraph.md) method to retrieve a pointer to the Filter Graph Manager's [**IGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-igraphbuilder) interface. Then query the Filter Graph Manager for the [**IMediaControl**](/windows/desktop/api/Control/nn-control-imediacontrol) interface and call [**IMediaControl::Run**](/windows/desktop/api/Control/nf-control-imediacontrol-run), as shown in the following code:


```C++
IGraphBuilder   *pGraph = NULL;
IMediaControl   *pControl = NULL;
hr = pRender->GetFilterGraph(&pGraph);
hr = pGraph->QueryInterface(IID_IMediaControl, (void **)&pControl);
hr = pControl->Run();
```



Use the Filter Graph Manager's [**IMediaEventEx**](/windows/desktop/api/Control/nn-control-imediaeventex) interface to wait for the preview to complete. You can also seek the graph using the Filter Graph Manager's [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) interface, just as you would with a file playback graph.

To preview the project again, seek the graph back to time zero and call **Run** again. If you change the contents of the timeline, do the following:

1.  Call **SetRenderRange**. (Optional)
2.  Call **ConnectFrontEnd**.
3.  If the **ConnectFrontEnd** method returns S\_WARN\_OUTPUTRESET, call **RenderOutputPins**. (If **ConnectFrontEnd** returns S\_OK, you can skip this step.)
4.  Seek the graph back to time zero.
5.  Run the graph.

The following example shows these steps:


```C++
hr = pRender->ConnectFrontEnd();
if (hr == S_WARN_OUTPUTRESET)
{
    hr = pRender->RenderOutputPins();
}
LONGLONG llStart = 0; 
hr = pSeek->SetPositions(&llStart, AM_SEEKING_AbsolutePositioning, 0, 0); 
hr = pControl->Run();
```



For a complete example that loads and previews a project file, see [Loading and Previewing a Project](loading-and-previewing-a-project.md).

## Related topics

<dl> <dt>

[Managing Video Editing Projects](managing-video-editing-projects.md)
</dt> <dt>

[Rendering a Project](rendering-a-project.md)
</dt> </dl>

 

 



