---
description: Working with Media Buffers
ms.assetid: c7e079e0-99f3-4bff-9163-1c5a022c14ae
title: Working with Media Buffers (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Working with Media Buffers (Microsoft Media Foundation)

This topic describes how to use the [**IMFMediaBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer) interface to access the data in a media buffer. All media buffers expose **IMFMediaBuffer**, which is designed for any type of data. Uncompressed video frames are a special case, described in the topic [Uncompressed Video Buffers](uncompressed-video-buffers.md).

## Buffer Size

A media buffer has two sizes associated with it:

-   The *maximum length* is the physical size of the memory that is allocated for the buffer. This value is set when the buffer is created and does not change during the lifetime of the buffer. The maximum length indicates how much data can be stored in the buffer. To find the maximum size, call [**IMFMediaBuffer::GetMaxLength**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-getmaxlength).

-   The *current length* is the amount of valid data that is currently in the buffer. When the buffer is first allocated, the current length is zero, because there is no valid data in the buffer. If you write any data to the buffer, you must update the current length by calling [**IMFMediaBuffer::SetCurrentLength**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-setcurrentlength). For example, if you write 100 bytes of data into the buffer, call **SetCurrentLength** with the value 100. If you read data from a media buffer, call [**IMFMediaBuffer::GetCurrentLength**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-getcurrentlength) to find out how much data is currently in the buffer. Do not read past the current length. The current length can never exceed the maximum length of the buffer.

## Accessing the Buffer Memory

To access the memory in the buffer, call [**IMFMediaBuffer::Lock**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-lock). This method returns a pointer to the start of the memory block. It also returns the maximum length and the current length. When you are done using the pointer, call [**IMFMediaBuffer::Unlock**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-unlock).

To write data into a media buffer:

1.  Call [**IMFMediaBuffer::Lock**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-lock) to get a pointer to the memory. The method also returns the buffer's maximum length.
2.  Write your data into the memory, up to the buffer's maximum length.
3.  Call [**IMFMediaBuffer::SetCurrentLength**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-setcurrentlength) to update the current length. Set the current length equal to the amount of data that you wrote in step 2.
4.  Call [**IMFMediaBuffer::Unlock**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-unlock) to unlock the buffer.

To read data from a media buffer:

1.  Call [**IMFMediaBuffer::Lock**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-lock) to get a pointer to the memory. The method also returns the buffer's current length (the amount of valid data in the buffer).
2.  Read the contents of the memory, up to the current length.
3.  Call [**IMFMediaBuffer::Unlock**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-unlock) to unlock the buffer.

## Creating System Memory Buffers

The system memory buffer is a media buffer that manages a block of system memory. To create an instance of this object, call [**MFCreateMemoryBuffer**](/windows/desktop/api/mfapi/nf-mfapi-mfcreatememorybuffer) or [**MFCreateAlignedMemoryBuffer**](/windows/desktop/api/mfapi/nf-mfapi-mfcreatealignedmemorybuffer) and specify a buffer size. Both functions allocate a block of memory and return an [**IMFMediaBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer) pointer. The memory is automatically released when the media buffer's reference count reaches zero and the object is destroyed.

The following example shows how to create a system memory buffer and write to the buffer.


```C++
HRESULT CreateSystemMemoryBuffer(
    BYTE *pSrc, 
    DWORD cbData, 
    IMFMediaBuffer **ppBuffer
    )
{
    HRESULT hr = S_OK;
    BYTE *pData = NULL;

    IMFMediaBuffer *pBuffer = NULL;

    // Create the media buffer.
    hr = MFCreateMemoryBuffer(
        cbData,   // Amount of memory to allocate, in bytes.
        &pBuffer        
        );

    // Lock the buffer to get a pointer to the memory.
    if (SUCCEEDED(hr))
    {
        hr = pBuffer->Lock(&pData, NULL, NULL);
    }

    if (SUCCEEDED(hr))
    {
        memcpy_s(pData, cbData, pSrc, cbData);
    }

    // Update the current length.
    if (SUCCEEDED(hr))
    {
        hr = pBuffer->SetCurrentLength(cbData);
    }

    // Unlock the buffer.
    if (pData)
    {
        hr = pBuffer->Unlock();
    }

    if (SUCCEEDED(hr))
    {
        *ppBuffer = pBuffer;
        (*ppBuffer)->AddRef();
    }

    return hr;
}
```



## Related topics

<dl> <dt>

[Media Buffers](media-buffers.md)
</dt> <dt>

[Media Foundation Platform APIs](media-foundation-platform-apis.md)
</dt> </dl>

 

 



