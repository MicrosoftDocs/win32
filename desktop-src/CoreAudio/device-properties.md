---
description: Device Properties
ms.assetid: ad8753ba-ad20-4122-b0f2-eb165f98db67
title: Device Properties (Core Audio APIs)
ms.topic: article
ms.date: 05/31/2018
---

# Device Properties (Core Audio APIs)

During the process of enumerating [audio endpoint devices](audio-endpoint-devices.md), a client application can interrogate the endpoint objects for their device properties. The device properties are exposed in MMDevice API's implementation of the **IPropertyStore** interface. Given a reference to the [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) interface of an endpoint object, a client can obtain a reference to the endpoint object's property store by calling the [**IMMDevice::OpenPropertyStore**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-openpropertystore) method.

The property-store object exposes an **IPropertyStore** interface. The two primary methods in this interface are **IPropertyStore::GetValue**, which gets a device property value, and **IPropertyStore::SetValue**, which sets a device property value. For more information about **IPropertyStore**, see the Windows SDK documentation.

The MMDevice API's implementation of the property store is different from the standard shell property store object. To change a property value, the client application must call the **IPropertyStore::SetValue** method. During this call, the new values are set and written in the registry. Therefore, the application does not need to call the **IPropertyStore::Commit** method after the **SetValue** call. The handle to the registry is closed only when the client releases the interface pointer.

Typically, third-party client applications call the **GetValue** method but not the **SetValue** method. The endpoint manager sets the basic device properties for endpoints. The endpoint manager is the Windows Vista component that is responsible for detecting the presence of audio endpoint devices.

Each PKEY\_Xxx property identifier in the following list is a constant of type **PROPERTYKEY** that is defined in header file Functiondiscoverykeys\_devpkey.h. All audio endpoint devices have these three device properties.



| Property                                                                         | Description                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PKEY\_DeviceInterface\_FriendlyName**](pkey-deviceinterface-friendlyname.md) | The friendly name of the audio adapter to which the endpoint device is attached (for example, "XYZ Audio Adapter"). **PROPVARIANT** member **vt** is set to VT\_LPWSTR and member **pwszVal** points to a null-terminated, wide-character string that contains the friendly name. |
| [**PKEY\_Device\_DeviceDesc**](pkey-device-devicedesc.md)                       | The device description of the endpoint device (for example, "Speakers"). **PROPVARIANT** member **vt** is set to VT\_LPWSTR and member **pwszVal** points to a null-terminated, wide-character string that contains the device description.                                       |
| [**PKEY\_Device\_FriendlyName**](pkey-device-friendlyname.md)                   | The friendly name of the endpoint device (for example, "Speakers (XYZ Audio Adapter)"). **PROPVARIANT** member **vt** is set to VT\_LPWSTR and member **pwszVal** points to a null-terminated, wide-character string that contains the friendly name.                             |



 

Some audio endpoint devices might have additional properties that do not appear in the preceding list. For more information about additional properties, see [Audio Endpoint Properties](audio-endpoint-properties.md). For more information about **PROPERTYKEY**, see the Windows SDK documentation.

The following code example prints the display names of all audio-rendering endpoint devices in the system:


```C++
//-----------------------------------------------------------
// This function enumerates all active (plugged in) audio
// rendering endpoint devices. It prints the friendly name
// and endpoint ID string of each endpoint device.
//-----------------------------------------------------------
#define EXIT_ON_ERROR(hres)  \
              if (FAILED(hres)) { goto Exit; }
#define SAFE_RELEASE(punk)  \
              if ((punk) != NULL)  \
                { (punk)->Release(); (punk) = NULL; }

const CLSID CLSID_MMDeviceEnumerator = __uuidof(MMDeviceEnumerator);
const IID IID_IMMDeviceEnumerator = __uuidof(IMMDeviceEnumerator);

void PrintEndpointNames()
{
    HRESULT hr = S_OK;
    IMMDeviceEnumerator *pEnumerator = NULL;
    IMMDeviceCollection *pCollection = NULL;
    IMMDevice *pEndpoint = NULL;
    IPropertyStore *pProps = NULL;
    LPWSTR pwszID = NULL;

    hr = CoCreateInstance(
           CLSID_MMDeviceEnumerator, NULL,
           CLSCTX_ALL, IID_IMMDeviceEnumerator,
           (void**)&pEnumerator);
    EXIT_ON_ERROR(hr)

    hr = pEnumerator->EnumAudioEndpoints(
                        eRender, DEVICE_STATE_ACTIVE,
                        &pCollection);
    EXIT_ON_ERROR(hr)

    UINT  count;
    hr = pCollection->GetCount(&count);
    EXIT_ON_ERROR(hr)

    if (count == 0)
    {
        printf("No endpoints found.\n");
    }

    // Each loop prints the name of an endpoint device.
    for (ULONG i = 0; i < count; i++)
    {
        // Get pointer to endpoint number i.
        hr = pCollection->Item(i, &pEndpoint);
        EXIT_ON_ERROR(hr)

        // Get the endpoint ID string.
        hr = pEndpoint->GetId(&pwszID);
        EXIT_ON_ERROR(hr)
        
        hr = pEndpoint->OpenPropertyStore(
                          STGM_READ, &pProps);
        EXIT_ON_ERROR(hr)

        PROPVARIANT varName;
        // Initialize container for property value.
        PropVariantInit(&varName);

        // Get the endpoint's friendly-name property.
        hr = pProps->GetValue(
                       PKEY_Device_FriendlyName, &varName);
        EXIT_ON_ERROR(hr)

        // Print endpoint friendly name and endpoint ID.
        printf("Endpoint %d: \"%S\" (%S)\n",
               i, varName.pwszVal, pwszID);

        CoTaskMemFree(pwszID);
        pwszID = NULL;
        PropVariantClear(&varName);
        SAFE_RELEASE(pProps)
        SAFE_RELEASE(pEndpoint)
    }
    SAFE_RELEASE(pEnumerator)
    SAFE_RELEASE(pCollection)
    return;

Exit:
    printf("Error!\n");
    CoTaskMemFree(pwszID);
    SAFE_RELEASE(pEnumerator)
    SAFE_RELEASE(pCollection)
    SAFE_RELEASE(pEndpoint)
    SAFE_RELEASE(pProps)
}
```



The FAILED macro in the preceding code example is defined in header file Winerror.h.

In the preceding code example, the **for**-loop body in the PrintEndpointNames function calls the [**IMMDevice::GetId**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-getid) method to obtain the [endpoint ID string](endpoint-id-strings.md) for the audio endpoint device that is represented by the **IMMDevice** interface instance. The string uniquely identifies the device with respect to all of the other audio endpoint devices in the system. A client can use the endpoint ID string to create an instance of the audio endpoint device at a later time or in a different process by calling the [**IMMDeviceEnumerator::GetDevice**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdevice) method. Clients should treat the contents of the endpoint ID string as opaque. That is, clients should not attempt to parse the contents of the string to obtain information about the device. The reason is that the string format is undefined and might change from one implementation of the MMDevice API to the next.

The friendly device names and endpoint ID strings that are obtained by the PrintEndpointNames function in the preceding code example are identical to the friendly device names and endpoint ID strings that are provided by DirectSound during device enumeration. For more information, see [Audio Events for Legacy Audio Applications](audio-events-for-legacy-audio-applications.md).

In the preceding code example, the PrintEndpointNames function calls the **CoCreateInstance** function to create an enumerator for the audio endpoint devices in the system. Unless the calling program previously called either the **CoInitialize** or **CoInitializeEx** function to initialize the COM library, the **CoCreateInstance** call will fail. For more information about **CoCreateInstance**, **CoInitialize**, and **CoInitializeEx**, see the Windows SDK documentation.

For more information about the **IMMDeviceEnumerator**, **IMMDeviceCollection**, and **IMMDevice** interfaces, see [MMDevice API](mmdevice-api.md).

## Related topics

<dl> <dt>

[Audio Endpoint Devices](audio-endpoint-devices.md)
</dt> </dl>

 

 



