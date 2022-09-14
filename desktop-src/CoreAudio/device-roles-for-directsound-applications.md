---
description: Device Roles for DirectSound Applications
ms.assetid: 7d82d67f-aad8-4e5b-ac65-87d75774e613
title: Device Roles for DirectSound Applications
ms.topic: article
ms.date: 05/31/2018
---

# Device Roles for DirectSound Applications

> [!Note]  
> The [MMDevice API](mmdevice-api.md) supports device roles. However, the user interface in Windows Vista does not implement support for this feature. User interface support for device roles might be implemented in a future version of Windows. For more information, see [Device Roles in Windows Vista](device-roles-in-windows-vista.md).

 

The DirectSound API does not provide a means for an application to select the [audio endpoint device](audio-endpoint-devices.md) that the user has assigned to a particular [device role](device-roles.md). However, in Windows Vista, the core audio APIs can be used in conjunction with a DirectSound application to enable device selection based on device role. With the help of the core audio APIs, the application can identify the audio endpoint device that is assigned to a particular role, get the DirectSound device GUID for the endpoint device, and call the **DirectSoundCreate** or **DirectSoundCaptureCreate** function to create an **IDirectSound** or **IDirectSoundCapture** interface instance that encapsulates the endpoint device. For more information about DirectSound, see the Windows SDK documentation.

The following code example shows how to obtain the DirectSound device GUID for the rendering or capture device that is currently assigned to a particular device role:


```C++
//-----------------------------------------------------------
// Get the DirectSound or DirectSoundCapture device GUID for
// an audio endpoint device. If flow = eRender, the function
// gets the DirectSound device GUID for the rendering device
// with the specified device role. If flow = eCapture, the
// function gets the DirectSoundCapture device GUID for the
// capture device with the specified device role.
//-----------------------------------------------------------
#define EXIT_ON_ERROR(hr)  \
              if (FAILED(hr)) { goto Exit; }
#define SAFE_RELEASE(punk)  \
              if ((punk) != NULL)  \
                { (punk)->Release(); (punk) = NULL; }

HRESULT GetDirectSoundGuid(EDataFlow flow, ERole role, GUID* pDevGuid)
{
    HRESULT hr = S_OK;
    IMMDeviceEnumerator *pEnumerator = NULL;
    IMMDevice *pDevice = NULL;
    IPropertyStore *pProps = NULL;

    PROPVARIANT var;
    PropVariantInit(&var);

    if (pDevGuid == NULL)
    {
        return E_POINTER;
    }

    // Get a device enumerator for the audio endpoint
    // devices in the system.
    hr = CoCreateInstance(__uuidof(MMDeviceEnumerator),
                          NULL, CLSCTX_INPROC_SERVER,
                          __uuidof(IMMDeviceEnumerator),
                          (void**)&pEnumerator);
    EXIT_ON_ERROR(hr)

    // Get the endpoint device with the specified dataflow
    // direction (eRender or eCapture) and device role.
    hr = pEnumerator->GetDefaultAudioEndpoint(flow, role,
                                              &pDevice);
    EXIT_ON_ERROR(hr)

    hr = pDevice->OpenPropertyStore(STGM_READ, &pProps);
    EXIT_ON_ERROR(hr)

    // Get the DirectSound or DirectSoundCapture device GUID
    // (in WCHAR string format) for the endpoint device.
    hr = pProps->GetValue(PKEY_AudioEndpoint_GUID, &var);
    EXIT_ON_ERROR(hr)

    // Convert the WCHAR string to a GUID structure.
    hr = CLSIDFromString(var.pwszVal, pDevGuid);
    EXIT_ON_ERROR(hr)

Exit:
    PropVariantClear(&var);
    SAFE_RELEASE(pEnumerator);
    SAFE_RELEASE(pDevice);
    SAFE_RELEASE(pProps);
    return hr;
}
```



In the preceding code example, the GetDirectSoundGuid function accepts a data-flow direction (eRender or eCapture) and a device role (eConsole, eMultimedia, or eCommunications) as input parameters. The third parameter is a pointer through which the function writes a device GUID that the application can supply as an input parameter to the **DirectSoundCreate** or **DirectSoundCaptureCreate** function.

The preceding code example obtains the DirectSound device GUID by:

-   Creating an [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) interface instance that represents the audio endpoint device that has the specified data-flow direction and device role.
-   Opening the property store of the audio endpoint device.
-   Getting the [**PKEY\_AudioEndpoint\_GUID**](pkey-audioendpoint-guid.md) property from the property store. The property value is a string representation of the DirectSound device GUID for the audio endpoint device.
-   Calling the [**CLSIDFromString**](https://www.bing.com/search?q=**CLSIDFromString**) function to convert the string representation of the device GUID to a GUID structure. For more information about **CLSIDFromString**, see the Windows SDK documentation.

After obtaining a device GUID from the GetDirectSoundGuid function, the application can call **DirectSoundCreate** or **DirectSoundCaptureCreate** with this GUID to create the DirectSound rendering or capture device that encapsulates the audio endpoint device. When DirectSound creates a device in this way, it always assigns the device's audio stream to the default session—the process-specific audio session that is identified by the session GUID value GUID\_NULL.

If the application requires DirectSound to assign the stream to a cross-process audio session or to a session with a non-**NULL** session GUID, it should call the [**IMMDevice::Activate**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate) method to create an **IDirectSound** or **IDirectSoundCapture** object instead of using the technique shown in the preceding code example. For a code example that shows how to use the **Activate** method to specify a cross-process audio session or a non-**NULL** session GUID for a stream, see [Device Roles for DirectShow Applications](device-roles-for-directshow-applications.md). The code example in that section shows how to create a DirectShow filter, but, with minor modifications, the code can be adapted to create a DirectSound device.

The GetDirectSoundGuid function in the preceding code example calls the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) function to create an enumerator for the audio endpoint devices in the system. Unless the calling program previously called either the [**CoInitialize**](/windows/desktop/api/objbase/nf-objbase-coinitialize) or [**CoInitializeEx**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex) function to initialize the COM library, the **CoCreateInstance** call will fail. For more information about **CoCreateInstance**, **CoInitialize**, and **CoInitializeEx**, see the Windows SDK documentation.

## Related topics

<dl> <dt>

[Interoperability with Legacy Audio APIs](interoperability-with-legacy-audio-apis.md)
</dt> </dl>

 

 
