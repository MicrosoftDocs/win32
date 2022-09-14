---
description: Working with Media Samples
ms.assetid: 10b547b1-6624-4d49-9852-a5fff4eb70e7
title: Working with Media Samples
ms.topic: article
ms.date: 05/31/2018
---

# Working with Media Samples

This topic describes how to use the [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) interface to manipulate media sample objects. For a general overview of media samples, see [Media Samples](media-samples.md).

To create a new media sample, call the [**MFCreateSample**](/windows/desktop/api/mfapi/nf-mfapi-mfcreatesample) function. Initially, the sample's buffer list is empty. To add a buffer to the end of the list, call [**IMFSample::AddBuffer**](/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-addbuffer).

The following code shows how to create a sample and add a buffer to it.


```C++
HRESULT CreateMediaSample(DWORD cbData, IMFSample **ppSample)
{
    HRESULT hr = S_OK;

    IMFSample *pSample = NULL;
    IMFMediaBuffer *pBuffer = NULL;

    hr = MFCreateSample(&pSample);

    if (SUCCEEDED(hr))
    {
        hr = MFCreateMemoryBuffer(cbData, &pBuffer);
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

    SafeRelease(&pSample);
    SafeRelease(&pBuffer);
    return hr;
}
```



The recommended way to get the buffers from the sample is to call [**IMFSample::ConvertToContiguousBuffer**](/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-converttocontiguousbuffer). This method returns a single continguous buffer.

To iterate through the buffers in the list, start by calling [**IMFSample::GetBufferCount**](/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-getbuffercount). This method returns the number of buffers. Then call [**IMFSample::GetBufferByIndex**](/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-getbufferbyindex) and specify the index of the buffer to retrieve. Buffers are indexed from zero.

The following code shows how to iterate through the buffers in a sample.


```C++
IMFMediaBuffer *pBuffer = NULL;
DWORD cBuffers = 0;

hr = pSample->GetBufferCount(&cBuffers);

if (SUCCEEDED(hr))
{
    for (DWORD i = 0; i < cBuffers; i++)
    {
        hr = pSample->GetBufferByIndex(i, &pBuffer);

        // Use buffer (not shown).

        SafeRelease(&pBuffer);

        if (FAILED(hr))
        {
            break;
        }
    }
}
```



Samples have a time stamp and a duration. The time stamp indicates when the data in the sample should be rendered, relative to the presentation clock. The duration is the length of time for which the data should be rendered. Typically the component that generates the data sets the initial time stamp and duration. These values might get modified by the Media Session. To set the time stamp, call [**IMFSample::SetSampleTime**](/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-setsampletime). To set the duration, call [**IMFSample::SetSampleDuration**](/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-setsampleduration).

Samples can also have attributes, which contain additional information about the sample. For a list of sample attributes, see [Sample Attributes](sample-attributes.md). To set and retrieve attributes, use the [**IMFAttributes Interface**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes), which [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) inherits.

## Related topics

<dl> <dt>

[Media Samples](media-samples.md)
</dt> <dt>

[Media Buffers](media-buffers.md)
</dt> </dl>

 

 



