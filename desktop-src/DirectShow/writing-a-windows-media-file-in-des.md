---
description: Writing a Windows Media File in DES
ms.assetid: 741ebcbc-62fb-4c7f-845f-a361f5b63f8c
title: Writing a Windows Media File in DES
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Writing a Windows Media File in DES

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

This section describes how to write a Windows Media file using [DirectShow Editing Services](directshow-editing-services.md) (DES).

> [!IMPORTANT]
> Do not use the Smart Render Engine to write Windows Media files. Always use the Basic Render Engine (CLSID\_RenderEngine).

 

To write a Windows Media file, do the following:

1.  Call **SetSite** on the render engine, with a pointer to your key provider.
2.  Build the front end of the graph. (See [Rendering a Project](rendering-a-project.md).)
3.  Create the [WM ASF Writer](wm-asf-writer-filter.md) filter and add it to the graph.
4.  Use the [**IFileSinkFilter**](/windows/desktop/api/Strmif/nn-strmif-ifilesinkfilter) interface on the WM ASF Writer filter to set the file name.
5.  Configure the WM ASF Writer to use a Windows Media profile. Each profile has a predefined number of streams. You must choose a profile that matches the groups in your project.

    The [**IConfigAsfWriter**](/previous-versions/windows/desktop/api/Dshowasf/nn-dshowasf-iconfigasfwriter) interface contains a few different methods for setting the profile. For example, the **ConfigureFilterUsingProfileGuid** method specifies a system profile as a GUID. Or, you can use Windows Media Format methods to get an **IWMProfile** pointer and then call [**IConfigAsfWriter::ConfigureFilterUsingProfile**](/previous-versions/windows/desktop/api/Dshowasf/nf-dshowasf-iconfigasfwriter-configurefilterusingprofile). For more information, see [Configuring the ASF Writer](configuring-the-asf-writer.md).

6.  Connect the front end to the ASF Writer. The front end of the graph contains one output pin for each group. Assuming that you specified a compatible profile, the ASF Writer should have a matching set of input pins. Connect each output pin to the corresponding input pin. The easiest way to do this is using the [**ICaptureGraphBuilder2::RenderStream**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-renderstream) method. First, create a new instance of the [Capture Graph Builder](capture-graph-builder.md) and initialize it with a pointer to the Filter Graph Manager:

    ```C++
    ICaptureGraphBuilder2 *pBuild = 0;
    hr = CoCreateInstance(CLSID_CaptureGraphBuilder2, 0, CLSCTX_INPROC_SERVER,
        IID_ICaptureGraphBuilder2, (void**)&pBuild);
    pBuild->SetFiltergraph(pGraph); 
    ```

    

    Next, retrieve the output pin for each group by calling the [**IRenderEngine::GetGroupOutputPin**](irenderengine-getgroupoutputpin.md) method. Call **RenderStream** to connect the pin to the ASF Writer:

    ```C++
    long cGroups = 0;
    hr = pTimeline->GetGroupCount(&cGroups);
    for (long i = 0; i < cGroups; i++)
    {
        IPin *pPin;
        hr = pRenderEngine->GetGroupOutputPin(i, &pPin);
        if (SUCCEEDED(hr))
        {
            hr = pBuild->RenderStream(0, 0, pPin, 0, pASF);
        }
        pPin->Release();
    }
    pBuild->Release
    ```

    

## Related topics

<dl> <dt>

[Using Windows Media With DirectShow Editing Services](using-windows-media-with-directshow-editing-services.md)
</dt> </dl>

 

 



