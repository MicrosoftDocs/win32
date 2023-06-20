---
title: To Enumerate Input Formats
description: To Enumerate Input Formats
ms.assetid: 482adfc4-d9ed-403d-912b-1a5a70baf04c
keywords:
- Advanced Systems Format (ASF),enumerating input formats
- ASF (Advanced Systems Format),enumerating input formats
- profiles,enumerating input formats
- codecs,enumerating input formats
- Advanced Systems Format (ASF),input format enumerations
- ASF (Advanced Systems Format),input format enumerations
- profiles,input format enumerations
- codecs,input format enumerations
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Enumerate Input Formats

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Each of the Windows Media codecs accepts one or more types of input media for compression. The Windows Media Format SDK enables you to input a wider variety of formats than those supported by the codecs. The SDK does this by performing pre-processing transformations on the inputs when necessary, such as resizing video frames or resampling audio. In any case, you must ensure that the input formats for the files you write match the data you send to the writer. Each codec has a default input media format that is set in the writer when the profile is loaded. You can examine the default input format by calling [**IWMWriter::GetInputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-getinputprops).

The video codecs support the following formats: IYUV, I420, YV12, YUY2, UYVY, YVYU, YVU9, RGB 32, RGB 24, RGB 565, RGB 555, and RGB 8. The audio codecs support PCM audio.

To enumerate the input formats supported by a codec, perform the following steps:

1.  Create a writer object and set a profile to use. For more information about setting profiles in the writer, see [To Use Profiles with the Writer](to-use-profiles-with-the-writer.md).
2.  Identify the input number for which you want to check the formats. For more information about identifying input numbers, see [To Identify Inputs By Number](to-identify-inputs-by-number.md).
3.  Retrieve the total number of input formats supported by the desired input by calling [**IWMWriter::GetInputFormatCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmwriter-getinputformatcount).
4.  Loop through all of the supported input formats, performing the following steps for each.
    -   Retrieve the [**IWMInputMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwminputmediaprops) interface for the input format by calling [**IWMWriter::GetInputFormat**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-getinputformat).
    -   Retrieve the [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure for the input format. Call [**IWMMediaProps::GetMediaType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmediaprops-getmediatype), passing **NULL** for the *pType* parameter to get the size of the structure. Then allocate memory to hold the structure and call **GetMediaType** again to get the structure. [**IWMInputMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwminputmediaprops) inherits from [**IWMMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmediaprops), so you can make the calls to **GetMediaType** from the instance of **IWMInputMediaProps** retrieved in the previous step.
    -   The format described in the [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure contains all of the pertinent information about the input format. The basic format of the media is identified by **WM\_MEDIA\_TYPE.subtype**. For video streams, the **pbFormat** member points to a dynamically allocated [**WMVIDEOINFOHEADER**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmvideoinfoheader) structure which contains further details about the stream, including rectangle size. The size of the input frames is not required to match exactly a size supported by the codec. If they do not match, the SDK run-time components, in many cases, will automatically resize the input video frames to something the codec can accept.

The following example code finds the input format of the subtype passed as a parameter. For more information about using this code, see [Using the Code Examples](using-the-code-examples.md).


```C++
HRESULT FindInputFormat(IWMWriter* pWriter, 
                       DWORD dwInput,
                       GUID guidSubType,
                       IWMInputMediaProps** ppProps)
{
    DWORD   cFormats = 0;
    DWORD   cbSize   = 0;

    WM_MEDIA_TYPE*      pType  = NULL;
    IWMInputMediaProps* pProps = NULL;

    // Set the ppProps parameter to point to NULL. This will
    //  be used to check the results of the function later.
    *ppProps = NULL;

    // Find the number of formats supported by this input.
    HRESULT hr = pWriter->GetInputFormatCount(dwInput, &cFormats);
    if (FAILED(hr))
    {
        goto Exit;
    }
    // Loop through all of the supported formats.
    for (DWORD formatIndex = 0; formatIndex < cFormats; formatIndex++)
    {
        // Get the input media properties for the input format.
        hr = pWriter->GetInputFormat(dwInput, formatIndex, &pProps);
        if (FAILED(hr))
        {
            goto Exit;
        }
        // Get the size of the media type structure.
        hr = pProps->GetMediaType(NULL, &cbSize);
        if (FAILED(hr))
        {
            goto Exit;
        }
        // Allocate memory for the media type structure.
        pType = (WM_MEDIA_TYPE*) new (std::nothrow) BYTE[cbSize];
        if (pType == NULL)
        {
            hr = E_OUTOFMEMORY;
            goto Exit;
        }
        
        // Get the media type structure.
        hr = pProps->GetMediaType(pType, &cbSize);
        if (FAILED(hr))
        {
            goto Exit;
        }

        if(pType->subtype == guidSubType)
        {
            *ppProps = pProps;
            (*ppProps)->AddRef();
            goto Exit;
        }

        // Clean up for next iteration.
        delete [] pType;
        pType = NULL;
        SAFE_RELEASE(pProps);
    } // End for formatIndex.

    // If execution made it to this point, no matching format was found.
    hr = NS_E_INVALID_INPUT_FORMAT;

Exit:
    delete [] pType;
    SAFE_RELEASE(pProps);
    return hr;
}
```



## Related topics

<dl> <dt>

[**IWMWriter Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriter)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




