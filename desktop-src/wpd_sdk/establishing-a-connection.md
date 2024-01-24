---
description: Establishing a Connection
ms.assetid: 16286da5-5979-413b-a4db-ca157b10a571
title: Establishing a Connection
ms.topic: article
ms.date: 05/31/2018
---

# Establishing a Connection

Once the user selects a device, the ChooseDevice function, in turn, calls the [**IPortableDevice::Open**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-open) method to establish a connection between the application and the device. The IPortableDevice::Open method takes two arguments:

-   A pointer to a null-terminated string that specifies the Plug and Play name of the device. (This string is retrieved by calling the [**IPortableDeviceManager::GetDevices**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevicemanager-getdevices) method.)
-   A pointer to an [**IPortableDeviceValues interface**](iportabledevicevalues.md) that specifies client information for the application.


```C++
// CoCreate the IPortableDevice interface and call Open() with
// the chosen PnPDeviceID string.
hr = CoCreateInstance(CLSID_PortableDeviceFTM,
                      NULL,
                      CLSCTX_INPROC_SERVER,
                      IID_PPV_ARGS(ppDevice));
if (SUCCEEDED(hr))
{
    hr = (*ppDevice)->Open(pPnpDeviceIDs[uiCurrentDevice], pClientInformation);
    if (FAILED(hr))
    {
        if (hr == E_ACCESSDENIED)
        {
            printf("Failed to Open the device for Read Write access, will open it for Read-only access instead\n");
            pClientInformation->SetUnsignedIntegerValue(WPD_CLIENT_DESIRED_ACCESS, GENERIC_READ);
            hr = (*ppDevice)->Open(pPnpDeviceIDs[uiCurrentDevice], pClientInformation);
            if (FAILED(hr))
            {
                printf("! Failed to Open the device, hr = 0x%lx\n",hr);
                // Release the IPortableDevice interface, because we cannot proceed
                // with an unopen device.
                (*ppDevice)->Release();
                *ppDevice = NULL;
            }
        }
        else
        {
            printf("! Failed to Open the device, hr = 0x%lx\n",hr);
            // Release the IPortableDevice interface, because we cannot proceed
            // with an unopen device.
            (*ppDevice)->Release();
            *ppDevice = NULL;
        }
    }
}
else
{
    printf("! Failed to CoCreateInstance CLSID_PortableDeviceFTM, hr = 0x%lx\n",hr);
}
```



For Windows 7, [**IPortableDevice**](/windows/desktop/api/PortableDeviceApi/nn-portabledeviceapi-iportabledevice) supports two CLSIDs for **CoCreateInstance**. **CLSID\_PortableDevice** returns an **IPortableDevice** pointer that does not aggregate the free-threaded marshaler; **CLSID\_PortableDeviceFTM** is a new CLSID that returns an **IPortableDevice** pointer that aggregates the free-threaded marshaler. Both pointers support the same functionality otherwise.

Applications that live in Single Threaded Apartments should use **CLSID\_PortableDeviceFTM** as this eliminates the overhead of interface pointer marshaling. **CLSID\_PortableDevice** is still supported for legacy applications.

## Related topics

<dl> <dt>

[**Selecting a Device**](selecting-a-device.md)
</dt> </dl>

 

 



