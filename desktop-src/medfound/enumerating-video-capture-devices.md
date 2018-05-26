---
Description: This topic describes how to enumerate the video capture devices on the users system, and how create an instance of a device.
ms.assetid: b1267478-329b-4e46-a2ed-1ec11d2e2e6d
title: Enumerating Video Capture Devices
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating Video Capture Devices

This topic describes how to enumerate the video capture devices on the user's system, and how create an instance of a device.

To enumerate the video capture devices on the system, do the following:

1.  Call [**MFCreateAttributes**](/windows/win32/mfapi/nf-mfapi-mfcreateattributes?branch=master) to create an attribute store. This function receives an [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) pointer.
2.  Call [**IMFAttributes::SetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setguid?branch=master) to set the [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE](mf-devsource-attribute-source-type.md) attribute. Set the attribute value to **MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_GUID**.
3.  Call [**MFEnumDeviceSources**](/windows/win32/mfidl/nf-mfidl-mfenumdevicesources?branch=master). This function receives an array of [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) pointers and the array size. Each pointer represents a distinct video capture device.

To create an instance of a capture device:

-   Call [**IMFActivate::ActivateObject**](/windows/win32/mfobjects/nf-mfobjects-imfactivate-activateobject?branch=master) to get a pointer to the [**IMFMediaSource**](/windows/win32/mfidl/nn-mfidl-imfmediasource?branch=master) interface.

The following code shows these steps:


```C++
HRESULT CreateVideoDeviceSource(IMFMediaSource **ppSource)
{
    *ppSource = NULL;

    IMFMediaSource *pSource = NULL;
    IMFAttributes *pAttributes = NULL;
    IMFActivate **ppDevices = NULL;

    // Create an attribute store to specify the enumeration parameters.
    HRESULT hr = MFCreateAttributes(&amp;pAttributes, 1);
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
    hr = MFEnumDeviceSources(pAttributes, &amp;ppDevices, &amp;count);
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
    hr = ppDevices[0]->ActivateObject(IID_PPV_ARGS(&amp;pSource));
    if (FAILED(hr))
    {
        goto done;
    }

    *ppSource = pSource;
    (*ppSource)->AddRef();

done:
    SafeRelease(&amp;pAttributes);

    for (DWORD i = 0; i < count; i++)
    {
        SafeRelease(&amp;ppDevices[i]);
    }
    CoTaskMemFree(ppDevices);
    SafeRelease(&amp;pSource);
    return hr;
}
```



After you create media source, release the interface pointers and free the memory for the array:


```C++
    SafeRelease(&amp;pAttributes);

    for (DWORD i = 0; i < count; i++)
    {
        SafeRelease(&amp;ppDevices[i]);
    }
    CoTaskMemFree(ppDevices);
```



## Related topics

<dl> <dt>

[Video Capture](video-capture.md)
</dt> </dl>

 

 



