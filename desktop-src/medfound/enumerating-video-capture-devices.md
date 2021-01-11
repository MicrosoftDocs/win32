---
description: This topic describes how to enumerate the video capture devices on the users system, and how create an instance of a device.
ms.assetid: b1267478-329b-4e46-a2ed-1ec11d2e2e6d
title: Enumerating Video Capture Devices
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Video Capture Devices

This topic describes how to enumerate the video capture devices on the user's system, and how create an instance of a device.

To enumerate the video capture devices on the system, do the following:

1.  Call [**MFCreateAttributes**](/windows/desktop/api/mfapi/nf-mfapi-mfcreateattributes) to create an attribute store. This function receives an [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) pointer.
2.  Call [**IMFAttributes::SetGUID**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setguid) to set the [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE](mf-devsource-attribute-source-type.md) attribute. Set the attribute value to **MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_GUID**.
3.  Call [**MFEnumDeviceSources**](/windows/desktop/api/mfidl/nf-mfidl-mfenumdevicesources). This function receives an array of [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) pointers and the array size. Each pointer represents a distinct video capture device.

To create an instance of a capture device:

-   Call [**IMFActivate::ActivateObject**](/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-activateobject) to get a pointer to the [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource) interface.

The following code shows these steps:


```C++
HRESULT CreateVideoDeviceSource(IMFMediaSource **ppSource)
{
    *ppSource = NULL;

    IMFMediaSource *pSource = NULL;
    IMFAttributes *pAttributes = NULL;
    IMFActivate **ppDevices = NULL;

    // Create an attribute store to specify the enumeration parameters.
    HRESULT hr = MFCreateAttributes(&pAttributes, 1);
    if (FAILED(hr))
    {
        goto done;
    }

    // Source type: video capture devices
    hr = pAttributes->SetGUID(
        MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE, 
        MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_GUID
        );
    if (FAILED(hr))
    {
        goto done;
    }

    // Enumerate devices.
    UINT32 count;
    hr = MFEnumDeviceSources(pAttributes, &ppDevices, &count);
    if (FAILED(hr))
    {
        goto done;
    }

    if (count == 0)
    {
        hr = E_FAIL;
        goto done;
    }

    // Create the media source object.
    hr = ppDevices[0]->ActivateObject(IID_PPV_ARGS(&pSource));
    if (FAILED(hr))
    {
        goto done;
    }

    *ppSource = pSource;
    (*ppSource)->AddRef();

done:
    SafeRelease(&pAttributes);

    for (DWORD i = 0; i < count; i++)
    {
        SafeRelease(&ppDevices[i]);
    }
    CoTaskMemFree(ppDevices);
    SafeRelease(&pSource);
    return hr;
}
```



After you create media source, release the interface pointers and free the memory for the array:


```C++
    SafeRelease(&pAttributes);

    for (DWORD i = 0; i < count; i++)
    {
        SafeRelease(&ppDevices[i]);
    }
    CoTaskMemFree(ppDevices);
```



## Related topics

<dl> <dt>

[Video Capture](video-capture.md)
</dt> </dl>

 

 



