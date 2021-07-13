---
description: SAMI (CC) Parser Filter
ms.assetid: 9b09dd86-3c22-4565-82a0-106d5ca2e42d
title: SAMI (CC) Parser Filter
ms.topic: article
ms.date: 05/31/2018
---

# SAMI (CC) Parser Filter

Parses captioning data from Synchronized Accessible Media Interchange (SAMI) files.

SAMI is a text format similar to HTML, and is used for encoding time-based captions. This filter converts SAMI data into a text stream. Each sample in the stream contains one caption entry, along with format information. The time stamps on the samples are generated from the time information in the SAMI file.

This filter is designed to be used with the [Internal Script Command Renderer](internal-script-command-renderer-filter.md) filter. The Internal Script Command Renderer receives the text samples and sends them to the application, in the form of event notifications. For more information, see the Remarks section.



| Label | Value |
|------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMStreamSelect**](/windows/desktop/api/Strmif/nn-strmif-iamstreamselect), [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)                           |
| Input Pin Media Types                    | MEDIATYPE\_Stream                                                                                        |
| Input Pin Interfaces                     | [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)                                         |
| Output Pin Media Types                   | MEDIATYPE\_Text, MEDIASUBTYPE\_NULL                                                                      |
| Output Pin Interfaces                    | [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol) |
| Filter CLSID                             | {33FACFE0-A9BE-11D0-A520-00A0D10129C0}                                                                   |
| Property Page CLSID                      | No property page                                                                                         |
| Executable                               | quartz.dll                                                                                               |
| [Merit](merit.md)                       | MERIT\_UNLIKELY                                                                                          |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                            |



 

## Remarks

The following is a simple SAMI file:


```C++
<SAMI>
<Head>
<STYLE TYPE="text/css"> <!--
    .ENCC {Name: English; lang:en-US; SAMI_TYPE: CC;}
    .FRCC {Name: French; lang:fr-FR; SAMI_TYPE: CC;}
    #NORMAL {Name: Normal; font-family: arial;}
    #GREENTEXT {Name: GreenText; color:green; font-family: verdana;}
-->
</STYLE>
</Head>
<BODY>
<Sync Start=1000>
    <P CLASS="ENCC">One
    <P CLASS="FRCC">Un

<Sync Start=2000>
    <P CLASS="ENCC">Two
    <P CLASS="FRCC">Deux

<Sync Start=3000>
    <P CLASS="ENCC">Three
    <P CLASS="FRCC">Trois
</BODY>
</SAMI>
```



The **STYLE** tag defines two language settings, English (.ENCC) and French (.FRCC). It also defines two styles, \#NORMAL and \#GREENTEXT. Each **SYNC** tag defines the start time for a caption, in milliseconds. The **P** tags contain the caption text, while the **CLASS** attribute specifies the language setting to which the caption applies.

For each language and style, the filter creates a logical stream. At any time, exactly one language stream and one style stream are enabled. When the filter generates a sample, it selects the caption for the current language and applies the current style. By default, the first language and style declared in the file are enabled. An application can use the [**IAMStreamSelect::Enable**](/windows/desktop/api/Strmif/nf-strmif-iamstreamselect-enable) method to enable a different stream.

With the default settings, the first caption in the example file produces the following output:


```C++
<P STYLE=" Name: English; lang:en-US; SAMI_TYPE: CC; Name: Normal; font-family: arial;">One
```



If the output goes to the Internal Script Command Renderer, that filter sends an [**EC\_OLE\_EVENT**](ec-ole-event.md) event notification. The second event parameter is a BSTR with the caption text. The application can retrieve the event and display the caption.

The following example shows how to render a SAMI file, retrieve stream information, enable streams, and display caption text. The example assumes that the previous SAMI file is saved as C:\\Sami\_test\_file.sami.

For brevity, this example used hard-coded stream indexes when it calls the **IAMStreamSelect::Enable** method. It also performs minimal error checking.


```C++
void __cdecl main()
{
    HRESULT hr;
    IGraphBuilder *pGraph;
    IMediaControl *pMediaControl;
    IMediaEventEx *pEv;
    IBaseFilter   *pSAMI;

    CoInitialize(NULL);
    
    // Create the filter graph manager.
    CoCreateInstance(CLSID_FilterGraph, NULL, CLSCTX_INPROC, 
                        IID_IGraphBuilder, (void **)&pGraph);
    pGraph->QueryInterface(IID_IMediaControl, (void **)&pMediaControl);
    pGraph->QueryInterface(IID_IMediaEventEx, (void**)&pEv);

    // Create the graph and find the SAMI parser.
    pGraph->RenderFile(L"C:\\Sami_test_file.sami", NULL);
    hr = pGraph->FindFilterByName(L"SAMI (CC) Parser", &pSAMI);
    if (SUCCEEDED(hr)) 
    {
        IAMStreamSelect *pStrm = NULL;
        hr = pSAMI->QueryInterface(IID_IAMStreamSelect, (void**)&pStrm);
        if (SUCCEEDED(hr)) 
        {
            DWORD dwStreams = 0;
            pStrm->Count(&dwStreams);
            printf("Stream count: %d\n", dwStreams);

            // Select French and "GreenText"
            hr = pStrm->Enable(1, AMSTREAMSELECTENABLE_ENABLE);
            hr = pStrm->Enable(3, AMSTREAMSELECTENABLE_ENABLE);

            // Print the name of each logical stream.
            for (DWORD index = 0; index < dwStreams; index++)
            {
                DWORD dwFlags;
                WCHAR *wszName;
                hr = pStrm->Info(index, NULL, &dwFlags, NULL, NULL,
                    &wszName, NULL, NULL);
                if (hr == S_OK)
                {
                    wprintf(L"Stream %d: %s [%s]\n", index, wszName, 
                        (dwFlags ?  L"ENABLED" : L"DISABLED"));
                    CoTaskMemFree(wszName);
                }
            }
            pStrm->Release();
        }
        pSAMI->Release();
    }

    // Run the graph and display the captions.
    pMediaControl->Run();
    while (1)
    {
        long evCode, lParam1, lParam2;
        pEv->GetEvent(&evCode, &lParam1, &lParam2, 100);
        
        if (evCode == EC_OLE_EVENT) {
            wprintf(L"%s\n", (BSTR)lParam2);
        }
        pEv->FreeEventParams(evCode, lParam1, lParam2);

        if (evCode == EC_USERABORT || evCode == EC_COMPLETE || evCode == EC_ERRORABORT)
            break;
    }

    // Clean up.
    pMediaControl->Release();
    pEv->Release();
    pGraph->Release();
    CoUninitialize();
}
```



This filter uses the [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader) interface to pull samples from the source filter. Therefore, it does not support the [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) interface on its input pin.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



