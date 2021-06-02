---
title: Reading ASF Files in DirectShow (Windows Media Format 11 SDK)
description: Reading ASF Files in DirectShow
ms.assetid: eec2c91f-1762-4798-91d0-d68ec2160d6a
keywords:
- Windows Media Format SDK,DirectShow
- Windows Media Format SDK,reading ASF files
- Windows Media Format SDK,WM ASF Reader filter
- Windows Media Format SDK,IMediaSeeking interface
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- Advanced Systems Format (ASF),reading files
- ASF (Advanced Systems Format),reading files
- Advanced Systems Format (ASF),WM ASF Reader filter
- ASF (Advanced Systems Format),WM ASF Reader filter
- Advanced Systems Format (ASF),IMediaSeeking interface
- ASF (Advanced Systems Format),IMediaSeeking interface
- DirectShow,reading ASF files
- DirectShow,WM ASF Reader filter
- DirectShow,IMediaSeeking interface
- WM ASF Reader filter
- IMediaSeeking
ms.topic: article
ms.date: 05/31/2018
---

# Reading ASF Files in DirectShow (Windows Media Format 11 SDK)

Playback of ASF files is handled by the [WM ASF Reader](wm-asf-reader-filter.md) filter. When the WM ASF Reader reads a file, it automatically creates an output pin for each stream, including Web streams, script command streams, and any other type of arbitrary stream. In the case of multiple bit rate files, pins are created only for the currently selected streams.

The WM ASF Reader supports the DirectShow **IMediaSeeking** interface, which enables applications to perform temporal seeking within the file. However, playback at speeds other than 1.0 (as specified in **IMediaSeeking::SetRate**) is not supported.

The filter also exposes several Windows Media Format SDK interfaces as described in the following table.



| Interface                                        | How exposed                            | Comments                                                                                                                                                                                    |
|--------------------------------------------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMDRMReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmreader)             | Through **IServiceProvider** on filter | Provided for applications that need to play content protected by Digital Rights Management (DRM). This interface can also be used to obtain other interfaces on the Reader Object directly. |
| [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo)           | **QueryInterface** on filter           | Provided so that applications can read file and content attributes, as well as marker and script information and metadata.                                                                  |
| [**IWMReaderAdvanced**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced)   | **QueryInterface** on filter           | Partially implemented on the filter so that applications can access the informational methods on the WM Reader object.                                                                      |
| [**IWMReaderAdvanced2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced2) | **QueryInterface** on filter           | Partially implemented on the filter so that applications can access the informational methods on the Reader Object.                                                                         |



 

The [WM ASF Reader](wm-asf-reader-filter.md) filter was first made available in DirectShow 8.0. The version of the filter that ships with DirectShow 8.1 and 9.0 supports version 7.*x* of the Windows Media Format SDK. The most recent version of the filter, along with the other QASF components, ships with and supports the Windows Media Format 9 Series SDK, and later versions, and it supersedes the filter in DirectX 9.0. If you install the Windows Media Format SDK after installing the DirectX 8.*x* or 9.*x* SDK, you will overwrite the DirectX version of qasf.dll with the 9 Series version. This should not present any problems except possibly in one scenario where it will result in different behavior in the DirectShow **IGraphBuilder::RenderFile** method. The Windows Media Format 9 Series SDK version of the WM ASF Reader is the default source filter for the .asf, .wmv, and .wma file name extensions. This means that the WM ASF Reader is automatically created and added to the filter graph by the Filter Graph Manager in methods such as **IGraphBuilder::RenderFile** or **IGraphBuilder::AddSourceFilter** when a file of this type is specified. In DirectX 9.0 and earlier, and Windows XP Service Pack 1 and earlier, the **RenderFile** method uses the older Windows Media Source Filter. This behavior was maintained to ensure backward compatibility with applications that used the Windows Media Player 6.4. For more information about the legacy Windows Media Source Filter, see the DirectShow SDK Documentation.

To play an ASF file with Windows Media–based content using the WM ASF Reader, the three primary steps are to create an instance of the Filter Graph Manager, call **IGraphBuilder::RenderFile** to create the graph, and then call **IMediaControl::Run** to play the file. The following code example is a complete program that plays an ASF file using DirectShow. To run this example, you must have the DirectX SDK installed and your build environment must be configured according to the instructions in the DirectShow SDK documentation topic "Setting Up the Build Environment." Also, you must specify a file on your computer in the call to **RenderFile**.


```C++
#include <dshow.h>
#include <stdio.h>

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

    // Create the Filter Graph Manager and query for interfaces.
    hr = CoCreateInstance(CLSID_FilterGraph, NULL, CLSCTX_INPROC_SERVER, 
                        IID_IGraphBuilder, (void **)&pGraph);
    if (FAILED(hr))
    {
        printf("ERROR - Could not create the Filter Graph Manager.");
        return;
    }

    hr = pGraph->QueryInterface(IID_IMediaControl, (void **)&pControl);
    hr = pGraph->QueryInterface(IID_IMediaEvent, (void **)&pEvent);

    // Build the graph. IMPORTANT: Change this string to a file
    // on your system.
    hr = pGraph->RenderFile(L"test.wmv", NULL);
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



Note that the application code for this simple example never references the WM ASF Reader specifically. That filter is created, connected, run, and eventually released by the Filter Graph Manager. In many scenarios, however, you may want to configure the WM ASF Reader before beginning playback.

 

 




