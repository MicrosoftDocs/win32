---
Description: Working with Media Samples
ms.assetid: '10b547b1-6624-4d49-9852-a5fff4eb70e7'
title: Working with Media Samples
---

# Working with Media Samples

This topic describes how to use the [**IMFSample**](imfsample.md) interface to manipulate media sample objects. For a general overview of media samples, see [Media Samples](media-samples.md).

To create a new media sample, call the [**MFCreateSample**](mfcreatesample.md) function. Initially, the sample's buffer list is empty. To add a buffer to the end of the list, call [**IMFSample::AddBuffer**](imfsample-addbuffer.md).

The following code shows how to create a sample and add a buffer to it.


```C++
HRESULT CreateMediaSample(DWORD cbData, IMFSample **ppSample)
{
    HRESULT hr = S_OK;

    IMFSample *pSample = NULL;
    IMFMediaBuffer *pBuffer = NULL;

    hr = MFCreateSample(&amp;pSample);

    if (SUCCEEDED(hr))
    {
        hr = MFCreateMemoryBuffer(cbData, &amp;pBuffer);
    }

    if (SUCCEEDED(hr))
    {
        hr = pSample->AddBuffer(pBuffer);
    }

    if (SUCCEEDED(hr))
    {
        *ppSample = pSample;
        (*ppSample)->AddRef();
    }

    SafeRelease(&amp;pSample);
    SafeRelease(&amp;pBuffer);
    return hr;
}
```



The recommended way to get the buffers from the sample is to call [**IMFSample::ConvertToContiguousBuffer**](imfsample-converttocontiguousbuffer.md). This method returns a single continguous buffer.

To iterate through the buffers in the list, start by calling [**IMFSample::GetBufferCount**](imfsample-getbuffercount.md). This method returns the number of buffers. Then call [**IMFSample::GetBufferByIndex**](imfsample-getbufferbyindex.md) and specify the index of the buffer to retrieve. Buffers are indexed from zero.

The following code shows how to iterate through the buffers in a sample.


```C++
IMFMediaBuffer *pBuffer = NULL;
DWORD cBuffers = 0;

hr = pSample->GetBufferCount(&amp;cBuffers);

if (SUCCEEDED(hr))
{
    for (DWORD i = 0; i < cBuffers; i++)
    {
        hr = pSample->GetBufferByIndex(i, &amp;pBuffer);

        // Use buffer (not shown).

        SafeRelease(&amp;pBuffer);

        if (FAILED(hr))
        {
            break;
        }
    }
}
```



Samples have a time stamp and a duration. The time stamp indicates when the data in the sample should be rendered, relative to the presentation clock. The duration is the length of time for which the data should be rendered. Typically the component that generates the data sets the initial time stamp and duration. These values might get modified by the Media Session. To set the time stamp, call [**IMFSample::SetSampleTime**](imfsample-setsampletime.md). To set the duration, call [**IMFSample::SetSampleDuration**](imfsample-setsampleduration.md).

Samples can also have attributes, which contain additional information about the sample. For a list of sample attributes, see [Sample Attributes](sample-attributes.md). To set and retrieve attributes, use the [**IMFAttributes Interface**](imfattributes.md), which [**IMFSample**](imfsample.md) inherits.

## Related topics

<dl> <dt>

[Media Samples](media-samples.md)
</dt> <dt>

[Media Buffers](media-buffers.md)
</dt> </dl>

 

 



