---
description: Setting Video Compression Properties
ms.assetid: 2be03a2c-39a5-46da-9bbc-af42c08150ab
title: Setting Video Compression Properties
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Setting Video Compression Properties

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Video compression filters can support the [**IAMVideoCompression**](/windows/desktop/api/Strmif/nn-strmif-iamvideocompression) interface on their output pins. Use this interface to set compression properties, such as the key frame rate, the number of predicted (P) frames per key frame, and the relative compression quality.

First, call the [**IBaseFilter::EnumPins**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-enumpins) method to find the filter's output pin, and query the pin for the interface. Some filters may not support the interface at all. Others may expose the interface but not support every compression property. To determine which properties are supported, call [**IAMVideoCompression::GetInfo**](/windows/desktop/api/Strmif/nf-strmif-iamvideocompression-getinfo). This method returns several pieces of information:

-   A set of capabilities flags
-   A descriptive string and version-number string
-   Default values for key frame rate, P frame rate, and quality (when supported)

The method has the following syntax:


```C++
hr = pCompress->GetInfo(pszVersion, &cbVersion, pszDesc, &cbDesc, 
         &lKeyFrame, &lPFrame, &dblQuality, &lCap);
```



The *pszVersion* and *pszDesc* parameters are wide-character buffers that receive the version string and description string. The *cbVersion* and *cbDesc* parameters receive the required buffer sizes in bytes (not characters). The *lKeyFrame*, *lPFrame*, and *dblQuality* parameters receive the default values for the key frame rate, P frame rate, and quality. Quality is expressed as a floating-point number from 0.0 to 1.0. The *lCap* parameter receives a bitwise **OR** of the capabilities flags, which are defined by the [**CompressionCaps**](/windows/desktop/api/strmif/ne-strmif-compressioncaps) enumerated type.

Any of these parameters can be **NULL**, in which case the method ignores that parameter. For example, to allocate buffers for the version and description strings, first call the method with **NULL** in the first and third parameters. Use the returned values for *cbVersion* and *cbDesc* to allocate the buffers and then call the method again:


```C++
int cbVersion, cbDesc; // Size in bytes, not characters!
hr = pCompress->GetInfo(0, &cbVersion, 0, &cbDesc, 0, 0, 0, 0);
if (SUCCEEDED(hr))
{
    WCHAR *pszVersion = new WCHAR[cbVersion/2]; // Wide character = 2 bytes
    WCHAR *pszDesc = new WCHAR[cbDesc/2];
    hr = pCompress->GetInfo(pszVersion, 0, pszDesc, 0, 0, 0, 0, 0);
}
```



The value of *lCap* indicates which of the other **IAMVideoCompression** methods the filter supports. For example, if *lCap* contains the CompressionCaps\_CanKeyFrame flag, you can call [**IAMVideoCompression::get\_KeyFrameRate**](/windows/desktop/api/Strmif/nf-strmif-iamvideocompression-get_keyframerate) to get the key frame rate and [**IAMVideoCompression::put\_KeyFrameRate**](/windows/desktop/api/Strmif/nf-strmif-iamvideocompression-put_keyframerate) to set the key frame rate. A negative value indicates that the filter will use the default value, as obtained from [**IAMVideoCompression::GetInfo**](/windows/desktop/api/Strmif/nf-strmif-iamvideocompression-getinfo). For example:


```C++
if (lCap & CompressionCaps_CanKeyFrame)
{
    hr = pCompress->get_KeyFrameRate(&lKeyFrame);
    if (FAILED(hr) || lKeyFrame < 0)
    {
        lKeyFrame = lDefaultKeyFrame; // From GetInfo.
    }
}
```



The following code example tries to find the **IAMVideoCompression** interface on the output pin. If it succeeds, it retrieves the default and actual values for the compression properties:


```C++
HRESULT hr = E_FAIL;
IEnumPins *pEnum = NULL;
IPin *pPin = NULL;
IAMVideoCompression *pCompress = NULL;

// Find the pin that supports IAMVideoCompression (if any).
pFilter->EnumPins(&pEnum);
while (S_OK == pEnum->Next(1, &pPin, NULL))
{
    hr = pPin->QueryInterface(IID_IAMVideoCompression, (void**)&pCompress);
    pPin->Release();
    if (SUCCEEDED(hr)) // Found the interface.
    {
        break;
    }
}
if (SUCCEEDED(hr)) 
{
    long lCap;                     // Capability flags
    long lKeyFrame, lPFrame;       // Real values
    double m_Quality;
    long lKeyFrameDef, lPFrameDef; // Default values
    double QualityDef;
    
    // Get default values and capabilities.
    hr = pCompress->GetInfo(0, 0, 0, 0, &KeyFrameDef, &lPFrameDef,
             &QualityDef, &lCap);
    if (SUCCEEDED(hr))
    {
        // Get actual values where possible.
        if (lCap & CompressionCaps_CanKeyFrame)
        {
            hr = pCompress->get_KeyFrameRate(&lKeyFrame);
            if (FAILED(hr) || lKeyFrame < 0)
                lKeyFrame = lKeyFrameDef;
        }
        if (lCap & CompressionCaps_CanBFrame)
        {
            hr = pCompress->get_PFramesPerKeyFrame(&lPFrame);
            if (FAILED(hr) || lPFrame < 0)
                lPFrame = lPFrameDef;
        }
        if (lCap & CompressionCaps_CanQuality)
        {
            hr = pCompress->get_Quality(&Quality);
            if (FAILED(hr) || Quality < 0)
                Quality = QualityDef;
        }
    }
}
```



> [!Note]  
> If you are using the [**ICaptureGraphBuilder2**](/windows/desktop/api/Strmif/nn-strmif-icapturegraphbuilder2) interface to build your graph, you can obtain the **IAMVideoCompression** interface by calling [**ICaptureGraphBuilder2::FindInterface**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-findinterface), instead of using **IBaseFilter::EnumPins**. The **FindInterface** method is a helper method that searches filters and pins in the graph for a specified interface.

 

 

 



