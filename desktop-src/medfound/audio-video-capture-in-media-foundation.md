---
description: Microsoft Media Foundation supports audio and video capture.
ms.assetid: 8a9d96f8-1096-4b66-a2ec-8a95d754ea72
title: Audio/Video Capture in Media Foundation
ms.topic: article
ms.date: 05/31/2018
---

# Audio/Video Capture in Media Foundation

Microsoft Media Foundation supports audio and video capture. Video capture devices are supported through the UVC class driver and must be compatible with UVC 1.1. Audio capture devices are supported through Windows Audio Session API (WASAPI).

A capture device is represented in Media Foundation by a media source object, which exposes the [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource) interface. In most cases, the application will not use this interface directly, but will use a higher-level API such as the [Source Reader](source-reader.md) to control the capture device.

## Enumerate Capture Devices

To enumerate the capture devices on the system, perform the following steps:

1.  Call the [**MFCreateAttributes**](/windows/desktop/api/mfapi/nf-mfapi-mfcreateattributes) function to create an attribute store.
2.  Set the [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE](mf-devsource-attribute-source-type.md) attribute to one of the following values:

    | Value                                                    | Description                      |
    |----------------------------------------------------------|----------------------------------|
    | **MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_AUDCAP\_GUID** | Enumerate audio capture devices. |
    | **MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_GUID** | Enumerate video capture devices. |

    

     

3.  Call the [**MFEnumDeviceSources**](/windows/desktop/api/mfidl/nf-mfidl-mfenumdevicesources) function. This function allocates an array of [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) pointers. Each pointer represents an activation object for one device on the system.
4.  Call the [**IMFActivate::ActivateObject**](/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-activateobject) method to create an instance of the media source from one of the activation objects.

The following example creates a media source for the first video capture device in the enumeration list:


```C++
HRESULT CreateVideoCaptureDevice(IMFMediaSource **ppSource)
{
    *ppSource = NULL;

    UINT32 count = 0;

    IMFAttributes *pConfig = NULL;
    IMFActivate **ppDevices = NULL;

    // Create an attribute store to hold the search criteria.
    HRESULT hr = MFCreateAttributes(&pConfig, 1);

    // Request video capture devices.
    if (SUCCEEDED(hr))
    {
        hr = pConfig->SetGUID(
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE, 
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_GUID
            );
    }

    // Enumerate the devices,
    if (SUCCEEDED(hr))
    {
        hr = MFEnumDeviceSources(pConfig, &ppDevices, &count);
    }

    // Create a media source for the first device in the list.
    if (SUCCEEDED(hr))
    {
        if (count > 0)
        {
            hr = ppDevices[0]->ActivateObject(IID_PPV_ARGS(ppSource));
        }
        else
        {
            hr = MF_E_NOT_FOUND;
        }
    }

    for (DWORD i = 0; i < count; i++)
    {
        ppDevices[i]->Release();
    }
    CoTaskMemFree(ppDevices);
    return hr;
}
```



You can query the activation objects for various attributes, including the following:

-   The [MF\_DEVSOURCE\_ATTRIBUTE\_FRIENDLY\_NAME](mf-devsource-attribute-friendly-name.md) attribute contains the display name of the device. The display name is suitable for showing to the user, but might not be unique.
-   For video devices, the [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_SYMBOLIC\_LINK](mf-devsource-attribute-source-type-vidcap-symbolic-link.md) attribute contains the symbolic link to the device. The symbolic link uniquely identifies the device on the system, but is not a readable string.
-   For audio devices, the [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_AUDCAP\_ENDPOINT\_ID](mf-devsource-attribute-source-type-audcap-endpoint-id.md) attribute contains the audio endpoint ID of the device. The audio endpoint ID is similar to a symbolic link. It uniquely identifies the device on the system, but is not a readable string.

The following example takes an array of [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) pointers and prints the display name of each device to the debug window:


```C++
void DebugShowDeviceNames(IMFActivate **ppDevices, UINT count)
{
    for (DWORD i = 0; i < count; i++)
    {
        HRESULT hr = S_OK;
        WCHAR *szFriendlyName = NULL;
    
        // Try to get the display name.
        UINT32 cchName;
        hr = ppDevices[i]->GetAllocatedString(
            MF_DEVSOURCE_ATTRIBUTE_FRIENDLY_NAME,
            &szFriendlyName, &cchName);

        if (SUCCEEDED(hr))
        {
            OutputDebugString(szFriendlyName);
            OutputDebugString(L"\n");
        }
        CoTaskMemFree(szFriendlyName);
    }
}
```



If you already know the symbolic link for a video device, there is another way to create the media source for the device:

1.  Call [**MFCreateAttributes**](/windows/desktop/api/mfapi/nf-mfapi-mfcreateattributes) to create an attribute store.
2.  Set the [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE](mf-devsource-attribute-source-type.md) attribute to **MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_GUID**.
3.  Set the [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_SYMBOLIC\_LINK](mf-devsource-attribute-source-type-vidcap-symbolic-link.md) attribute to the symbolic link.
4.  Call either the [**MFCreateDeviceSource**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatedevicesource) or [**MFCreateDeviceSourceActivate**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatedevicesourceactivate) function. The former returns an [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource) pointer. The latter returns an [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) pointer to an activation object. You can use the activation object to create the source. (An activation object can be marshaled to another process, so it is useful if you want to create the source in another process. For more information, see [Activation Objects](activation-objects.md).)

The following example takes the symbolic link of a video device and creates a media source.


```C++
HRESULT CreateVideoCaptureDevice(PCWSTR *pszSymbolicLink, IMFMediaSource **ppSource)
{
    *ppSource = NULL;
    
    IMFAttributes *pAttributes = NULL;
    IMFMediaSource *pSource = NULL;

    HRESULT hr = MFCreateAttributes(&pAttributes, 2);

    // Set the device type to video.
    if (SUCCEEDED(hr))
    {
        hr = pAttributes->SetGUID(
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE,
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_GUID
            );
    }


    // Set the symbolic link.
    if (SUCCEEDED(hr))
    {
        hr = pAttributes->SetString(
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_SYMBOLIC_LINK,
            (LPCWSTR)pszSymbolicLink
            );            
    }

    if (SUCCEEDED(hr))
    {
        hr = MFCreateDeviceSource(pAttributes, ppSource);
    }

    SafeRelease(&pAttributes);
    return hr;    
}
```



There is an equivalent way to create an audio device from the audio endpoint ID:

1.  Call [**MFCreateAttributes**](/windows/desktop/api/mfapi/nf-mfapi-mfcreateattributes) to create an attribute store.
2.  Set the [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE](mf-devsource-attribute-source-type.md) attribute to **MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_AUDCAP\_GUID**.
3.  Set the [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_AUDCAP\_ENDPOINT\_ID](mf-devsource-attribute-source-type-audcap-endpoint-id.md) attribute to the endpoint ID.
4.  Call either the [**MFCreateDeviceSource**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatedevicesource) or [**MFCreateDeviceSourceActivate**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatedevicesourceactivate) function.

The following example takes an audio endpoint ID and creates a media source.


```C++
HRESULT CreateAudioCaptureDevice(PCWSTR *pszEndPointID, IMFMediaSource **ppSource)
{
    *ppSource = NULL;
    
    IMFAttributes *pAttributes = NULL;
    IMFMediaSource *pSource = NULL;

    HRESULT hr = MFCreateAttributes(&pAttributes, 2);

    // Set the device type to audio.
    if (SUCCEEDED(hr))
    {
        hr = pAttributes->SetGUID(
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE,
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_AUDCAP_GUID
            );
    }

    // Set the endpoint ID.
    if (SUCCEEDED(hr))
    {
        hr = pAttributes->SetString(
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_AUDCAP_ENDPOINT_ID,
            (LPCWSTR)pszEndPointID
            ); 
    }

    if (SUCCEEDED(hr))
    {
        hr = MFCreateDeviceSource(pAttributes, ppSource);
    }

    SafeRelease(&pAttributes);
    return hr;    
}
```



## Use a capture device

After you create the media source for a capture device, use the [Source Reader](source-reader.md) to get data from the device. The Source Reader delivers media samples that contain the capture audio data or video frames. The next step depends on your application scenario:

-   Video preview: Use Microsoft Direct3D or Direct2D to display the video.
-   File capture: Use the [Sink Writer](sink-writer.md) to encode the file.
-   Audio preview: Use [WASAPI](/windows/desktop/CoreAudio/wasapi).

If you want to combine audio capture with video capture, use the *aggregate media source*. The aggregate media source contains a collection of media sources and combines all of their streams into a single media source object. To create an instance of the aggregate media source, call the [**MFCreateAggregateSource**](/windows/desktop/api/mfidl/nf-mfidl-mfcreateaggregatesource) function.

## Shut down the capture device

When the capture device is no longer needed, you must shut down the device by calling [**Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-shutdown) on the [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource) object you obtained by calling [**MFCreateDeviceSource**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatedevicesource) or [**IMFActivate::ActivateObject**](/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-activateobject). Failure to call **Shutdown** can result in memory links because the system may keep a reference to **IMFMediaSource** resources until **Shutdown** is called.


```C++
if (g_pSource)
{
    g_pSource->Shutdown();
    g_pSource->Release();
    g_pSource = NULL;
}
```



If you allocated a string containing the symbolic link to a capture device, you should release this object as well.


```C++
    CoTaskMemFree(g_pwszSymbolicLink);
    g_pwszSymbolicLink = NULL;

    g_cchSymbolicLink = 0;
```



## Related topics

<dl> <dt>

[Audio/Video Capture](audio-video-capture.md)
</dt> </dl>

 

 
