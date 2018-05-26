---
Description: Retrieving the Events Supported by a Device
ms.assetid: 951b300f-03de-4a3d-9356-e3a7b5b17fdb
title: Retrieving the Events Supported by a Device
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving the Events Supported by a Device

Some WPD drivers support event notification. This means that an application can register with the driver to receive a notification when a specific action occurs. For example, an application can register to receive a notification when an object is added or removed.

There are ten predefined events that an application can monitor. They are described in the following table.



| Event                       | Description                                                                                                                            |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Device capabilities updated | Occurs when the device capabilities have changed.                                                                                      |
| Device removed              | Occurs when the device is unplugged.                                                                                                   |
| Device reset                | Occurs when the device has been reset.                                                                                                 |
| Object added                | Occurs after a new object becomes available on the device.                                                                             |
| Object removed              | Occurs after an object has been removed from the device.                                                                               |
| Object transfer requested   | Indicates that a request has been made to transfer an object.                                                                          |
| Object updated              | Occurs after either an object or its children has been updated. (Connected clients should then update their view of the given object.) |
| Storage format in progress  | Occurs when the device storage is being formatted.                                                                                     |



 

For a list of the constants associated with these events, see the [Event Constants](event-constants.md) topic.

The ListSupportedEvents function in the DeviceCapabilities.cpp module demonstrates the retrieval of events supported by a given device.

Your application can retrieve the identifiers for events supported by a device using the interfaces described in the following table.



| Interface                                                                                      | Description                                               |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [**IPortableDeviceCapabilities Interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledevicecapabilities?branch=master)                   | Provides access to the supported-event retrieval methods. |
| [**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md) | Used to enumerate and store functional-category data.     |



 

The first task accomplished by the sample application is the retrieval of an [**IPortableDeviceCapabilities**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledevicecapabilities?branch=master) object, which is used to retrieve the events supported by the given device.


```C++
HRESULT hr = S_OK;
CComPtr<IPortableDeviceCapabilities>            pCapabilities;
CComPtr<IPortableDevicePropVariantCollection>   pEvents;
DWORD dwNumEvents = 0;

if (pDevice == NULL)
{
    printf("! A NULL IPortableDevice interface pointer was received\n");
    return;
}


// Get an IPortableDeviceCapabilities interface from the IPortableDevice interface to
// access the device capabilities-specific methods.
hr = pDevice->Capabilities(&amp;pCapabilities);
if (FAILED(hr))
{
    printf("! Failed to get IPortableDeviceCapabilities from IPortableDevice, hr = 0x%lx\n",hr);
}
```



The supported events are retrieved by calling the [**IPortableDeviceCapabilities::GetSupportedEvents**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-iportabledevicecapabilities-getsupportedevents?branch=master) method. This method retrieves a collection of event identifiers for the given device and stores them in an [**IPortableDevicePropVariantCollection**](iportabledevicepropvariantcollection.md) object pointed to by the pEvents argument.


```C++
if (SUCCEEDED(hr))
{
    hr = pCapabilities->GetSupportedEvents(&amp;pEvents);
    if (FAILED(hr))
    {
        printf("! Failed to get supported events from the device, hr = 0x%lx\n",hr);
    }
}
```



The next step is to retrieve the count of supported events so that the application can iterate through the [**IPortableDevicePropVariantCollection**](iportabledevicepropvariantcollection.md) object and retrieve the identifier for each.


```C++
if (SUCCEEDED(hr))
{
    hr = pEvents->GetCount(&amp;dwNumEvents);
    if (FAILED(hr))
    {
        printf("! Failed to get number of supported events, hr = 0x%lx\n",hr);
    }
}

printf("\n%d Supported Events Found on the device\n\n", dwNumEvents);

// Loop through each event and display its name
if (SUCCEEDED(hr))
{
    for (DWORD dwIndex = 0; dwIndex < dwNumEvents; dwIndex++)
    {
        PROPVARIANT pv = {0};
        PropVariantInit(&amp;pv);
        hr = pEvents->GetAt(dwIndex, &amp;pv);
        if (SUCCEEDED(hr))
        {
            // We have an event.  It is assumed that
            // events are returned as VT_CLSID VarTypes.

            if (pv.puuid != NULL)
            {
                // Display the event name
                DisplayEvent(*pv.puuid);
                printf("\n");
                // Display the event options
                DisplayEventOptions(pCapabilities, *pv.puuid);
                printf("\n");
            }
        }

        PropVariantClear(&amp;pv);
    }
}
```



## Related topics

<dl> <dt>

[**Event Constants**](event-constants.md)
</dt> <dt>

[**IPortableDevice Interface**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevice?branch=master)
</dt> <dt>

[**IPortableDeviceCapabilities Interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledevicecapabilities?branch=master)
</dt> <dt>

[**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md)
</dt> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 



