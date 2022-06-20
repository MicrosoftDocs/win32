---
description: Device Properties
ms.assetid: ad8753ba-ad20-4122-b0f2-eb165f98db67
title: Device Properties (Core Audio APIs)
ms.topic: article
ms.date: 05/31/2018
---

# Device Properties (Core Audio APIs)

During the process of enumerating [audio endpoint devices](audio-endpoint-devices.md), a client application can interrogate the endpoint objects for their device properties. The device properties are exposed in MMDevice API's implementation of the [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) interface. Given a reference to the [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) interface of an endpoint object, a client can obtain a reference to the endpoint object's property store by calling the [**IMMDevice::OpenPropertyStore**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-openpropertystore) method.

Clients can read these properties, but should not set them. Property values are stored as **PROPVARIANT** structures.

The endpoint manager sets the basic device properties for endpoints. The endpoint manager is the Windows component that is responsible for detecting the presence of audio endpoint devices.

Each **PKEY\_Xxx** property identifier in the following list is a constant of type **PROPERTYKEY** that is defined in header file **Functiondiscoverykeys\_devpkey.h**. All audio endpoint devices have these device properties.

| Property | Description |
|----------|-------------|
| [**PKEY\_DeviceInterface\_FriendlyName**](pkey-deviceinterface-friendlyname.md) | The friendly name of the audio adapter to which the endpoint device is attached (for example, "XYZ Audio Adapter"). |
| [**PKEY\_Device\_DeviceDesc**](pkey-device-devicedesc.md) | The device description of the endpoint device (for example, "Speakers"). |
| [**PKEY\_Device\_FriendlyName**](pkey-device-friendlyname.md) | The friendly name of the endpoint device (for example, "Speakers (XYZ Audio Adapter)"). |
| **PKEY\_Device\_InstanceId** | Stores the audio endpoint [device instance identifier](/windows-hardware/drivers/install/device-instance-ids). The value can also be aquired via [**IMMDevice::GetId**](nf-mmdeviceapi-immdevice-getid.md) method. For more information about this property, see [Endpoint ID Strings](endpoint-id-strings.md) and [DEVPKEY_Device_InstanceId](/windows-hardware/drivers/install/devpkey-device-instanceid). |
| **PKEY\_Device\_ContainerId** | Stores the [container identifier](/windows-hardware/drivers/install/container-ids) of the PnP device that implements the audio endpoint. For more information about this property, see [DEVPKEY_Device_ContainerId](/windows-hardware/drivers/install/devpkey-device-containerid). |

Some audio endpoint devices might have additional properties that do not appear in the preceding list. For more information about additional properties, see [Audio Endpoint Properties](audio-endpoint-properties.md).

For more information about **PROPERTYKEY**, see the [Windows Property System documentation](/windows/win32/api/wtypes/ns-wtypes-propertykey).

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

 

 



