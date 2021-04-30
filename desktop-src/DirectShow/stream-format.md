---
description: Stream Format
ms.assetid: 7ed095f2-b541-4b99-8afc-9acba58081cd
title: Stream Format
ms.topic: article
ms.date: 05/31/2018
---

# Stream Format

Both the MSDV and the UVC driver can output two DV formats: interleaved audio-video, or video only. Interleaved audio-video is the original format from the device. The video-only format contains the same data, but the samples are marked as having no audio data. The video-only format exists mainly for compatibility with applications that use Video for Windows. For more information, see [Type-1 vs. Type-2 DV AVI Files](type-1-vs--type-2-dv-avi-files.md).

**MSDV Driver**

The MSDV driver has two output pins. The first output pin sends interleaved data, and the second output pin sends video-only data. Only one output pin can be connected at a time. To select a format, connect the appropriate output pin. You can use the [**IAMStreamConfig**](/windows/desktop/api/Strmif/nn-strmif-iamstreamconfig) interface on the output pin to find the format.

**UVC Driver**

Unlike the MSDV driver, the UVC driver delivers both formats from the same pin. The default format is video-only. To select the format, use the **IAMStreamConfig** interface on the output pin. Call the **GetStreamCaps** method to enumerate the media types on the output pin. For each media type, if the major type matches the desired format, call **SetFormat** and pass in that media type.



| Format                      | Major type             |
|-----------------------------|------------------------|
| Interleaved audio and video | MEDIATYPE\_Interleaved |
| Video only                  | MEDIATYPE\_Video       |



 

The following function sets the format based on the major type GUID.


```C++
HRESULT SetStreamFormat(IAMStreamConfig *pConfig, const GUID& majorType)
{
    if (pConfig == NULL)
    {
        return E_POINTER;
    }

    // Get the number of stream capabilities.
    int count = 0, size = 0;
    HRESULT hr = pConfig->GetNumberOfCapabilities(&count, &size);
    if (FAILED(hr))
    {
        return hr;
    }

    // Allocate memory for the stream capabilities structure.
    BYTE *pCaps = new BYTE[size];
    if (pCaps == NULL)
    {
        return E_OUTOFMEMORY;
    }
    
    // Enumerate the stream capabilities.
    bool bFoundType = false;
    for (int ix = 0; ix < count; ix++)
    {
        AM_MEDIA_TYPE *pmt;
        hr = pConfig->GetStreamCaps(ix, &pmt, pCaps);
        if (FAILED(hr))
        {
            break;
        }
        else if (pmt->majortype == majorType)
        {
            // This is the media type we want.
            bFoundType = true;
            hr = pConfig->SetFormat(pmt);
            DeleteMediaType(pmt);
            break;
        }
        DeleteMediaType(pmt);
    }
    delete [] pCaps;
    if (FAILED(hr))
    {
        return hr;
    }
    return bFoundType ? S_OK : E_FAIL;
}
```



The MSDV driver also supports **IAMStreamConfig**, so you can write code that works for both device types.

## Related topics

<dl> <dt>

[Controlling a DV Camcorder](controlling-a-dv-camcorder.md)
</dt> </dl>

 

 



