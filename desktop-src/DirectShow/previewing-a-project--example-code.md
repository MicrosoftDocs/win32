---
description: 'Previewing a Project: Example Code'
ms.assetid: 8a4af82a-5611-4c53-8de8-04eaefd51df9
title: 'Previewing a Project: Example Code'
ms.topic: article
ms.date: 05/31/2018
---

# Previewing a Project: Example Code

\[This API is not supported and may be altered or unavailable in the future.\]

The following code example shows how to load and preview a [DirectShow Editing Services](directshow-editing-services.md) project. Error checking is omitted for clarity.


```C++
#include <dshow.h>
#include <qedit.h>

// Preview a timeline.
void PreviewTL(IAMTimeline *pTL, IRenderEngine *pRender) 
{
    HRESULT hr;
    IGraphBuilder   *pGraph = NULL;
    IMediaControl   *pControl = NULL;
    IMediaEvent     *pEvent = NULL;

    // Build the graph.
    hr = pRender->SetTimelineObject(pTL);
    hr = pRender->ConnectFrontEnd( );
    hr = pRender->RenderOutputPins( );

    // Run the graph.
    hr = pRender->GetFilterGraph(&pGraph);
    pGraph->QueryInterface(IID_IMediaControl, (void **)&pControl);
    pGraph->QueryInterface(IID_IMediaEvent, (void **)&pEvent);
    hr = pControl->Run();

    long evCode;
    hr = pEvent->WaitForCompletion(INFINITE, &evCode);
    pControl->Stop();

    // Clean up.
    pEvent->Release();
    pControl->Release();
    pGraph->Release();
}

void main( void )
{
    HRESULT         hr;
    IAMTimeline     *pTL = NULL;
    IRenderEngine   *pRender = NULL; 
    IXml2Dex        *pXML = NULL; 

    CoInitialize(NULL);
    hr = CoCreateInstance(CLSID_AMTimeline, NULL, CLSCTX_INPROC_SERVER, 
                IID_IAMTimeline, (void**)&pTL);
    hr = CoCreateInstance(CLSID_Xml2Dex, NULL, CLSCTX_INPROC_SERVER, 
                IID_IXml2Dex, (void**)&pXML);
    hr = CoCreateInstance(CLSID_RenderEngine, NULL, CLSCTX_INPROC_SERVER,
                IID_IRenderEngine, (void**)&pRender);

    // Load a project file.
    BSTR bstrFile = SysAllocStringLen(OLESTR("C:\\example.xtl"), 15);
    hr = pXML->ReadXMLFile(pTL, bstrFile); 
    SysFreeString(bstrFile);
    pXML->Release();

    PreviewTL(pTL, pRender);

    // Clean up.    
    pRender->ScrapIt();
    pTL->Release();
    pRender->Release();
    CoUninitialize();
}
```



## Related topics

<dl> <dt>

[Loading and Previewing a Project](loading-and-previewing-a-project.md)
</dt> </dl>

 

 



