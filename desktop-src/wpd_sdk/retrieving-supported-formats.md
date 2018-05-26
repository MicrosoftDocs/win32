---
Description: Retrieving Supported Service Formats
ms.assetid: b54dfeda-c2a3-42ec-895f-9abbbd4dd2ec
title: Retrieving Supported Service Formats
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving Supported Service Formats

The WpdServicesApiSample application includes code that demonstrates how an application can retrieve the formats supported by a given Contacts service by calling methods of the interfaces in the following table.



|                                                                                      |                                                                                                       |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Interface                                                                            | Description                                                                                           |
| [**IPortableDeviceService**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservice?branch=master)                             | Used to retrieve the **IPortableDeviceServiceCapabilities** interface to access the supported events. |
| [**IPortableDeviceServiceCapabilities**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicecapabilities?branch=master)     | Provides access to the supported events and event attributes.                                         |
| [**IPortableDevicePropVariantCollection**](iportabledevicepropvariantcollection.md) | Contains the list of supported formats.                                                               |
| [**IPortableDeviceValues**](iportabledevicevalues.md)                               | Contains the attributes for a given format.                                                           |



 

When the user chooses option "3" at the command line, the application invokes the **ListSupportedFormats** method that is found in the ServiceCapabilities.cpp module.

Note that prior to retrieving the list of events, the sample application opens a Contacts service on a connected device.

In WPD, a format is described by attributes that specify the name and (optionally) the MIME type of a given format. These attributes are defined in thePortableDevice.h header file. For a description of supported attributes, refer to the [Attributes](attributes.md) topic.

In the case of the sample application, if the WpdServiceSampleDriver is the only installed device, the driver returns two supported formats for its Contact service: "AbstractContactFormat" and "VCard2Format". These formats correspond to the **WPD\_OBJECT\_FORMAT\_ABSTRACT\_CONTACT** and the **WPD\_OBJECT\_FORMAT\_VCARD2** attributes found in PortableDevice.h.

Two methods in the ServiceCapabilities.cpp module support the retrieval of supported formats for the Contacts service: **ListSupportedFormats** and **DisplayFormat**. The former retrieves the GUID identifier for each supported format. The latter converts this GUID into a user-friendly string.

The **ListSupportedFormats** method invokes the [**IPortableDeviceService::Capabilities**](/windows/win32/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservice-capabilities?branch=master) method to retrieve an [**IPortableDeviceServiceCapabilities**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicecapabilities?branch=master) interface. Using this interface, it retrieves the supported formats by calling the [**IPortableDeviceServiceCapabilities::GetSupportedFormats**](/windows/win32/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicecapabilities-getsupportedformats?branch=master) method. The **GetSupportedFormats** method retrieves the GUID for each format supported by the service and copies that GUID into an [**IPortableDevicePropVariantCollection**](iportabledevicepropvariantcollection.md) object.

The following code uses the **ListSupportedFormats** method.


```C++
// List all supported formats on the service
void ListSupportedFormats(
    IPortableDeviceService* pService)
{
    HRESULT hr              = S_OK;
    DWORD   dwNumFormats    = 0;
    CComPtr<IPortableDeviceServiceCapabilities>     pCapabilities;
    CComPtr<IPortableDevicePropVariantCollection>   pFormats;

    if (pService == NULL)
    {
        printf("! A NULL IPortableDeviceService interface pointer was received\n");
        return;
    }

    // Get an IPortableDeviceServiceCapabilities interface from the IPortableDeviceService interface to
    // access the service capabilities-specific methods.
    hr = pService->Capabilities(&amp;pCapabilities);
    if (FAILED(hr))
    {
        printf("! Failed to get IPortableDeviceServiceCapabilities from IPortableDeviceService, hr = 0x%lx\n",hr);
    }

    // Get all formats supported by the service.
    if (SUCCEEDED(hr))
    {
        hr = pCapabilities->GetSupportedFormats(&amp;pFormats);
        if (FAILED(hr))
        {
            printf("! Failed to get supported formats from the service, hr = 0x%lx\n",hr);
        }
    }

    // Get the number of supported formats found on the service.
    if (SUCCEEDED(hr))
    {
        hr = pFormats->GetCount(&amp;dwNumFormats);
        if (FAILED(hr))
        {
            printf("! Failed to get number of supported formats, hr = 0x%lx\n",hr);
        }
    }

    printf("\n%d Supported Formats Found on the service\n\n", dwNumFormats);

    // Loop through each format and display it
    if (SUCCEEDED(hr))
    {
        for (DWORD dwIndex = 0; dwIndex < dwNumFormats; dwIndex++)
        {
            PROPVARIANT pv = {0};
            PropVariantInit(&amp;pv);
            hr = pFormats->GetAt(dwIndex, &amp;pv);

            if (SUCCEEDED(hr))
            {
                // We have a format.  It is assumed that
                // formats are returned as VT_CLSID VarTypes.
                if (pv.puuid != NULL)
                {
                    DisplayFormat(pCapabilities, *pv.puuid);
                    printf("\n");
                }
            }

            PropVariantClear(&amp;pv);
        }
    }
}
```



After the **ListSupportedFormats** method retrieves the GUID for each format supported by the given service, it invokes the **DisplayFormat** method to display the script friendly name for each format; for example, "VCard2".

The **DisplayFormat** method invokes the [**IPortableDeviceServiceCapabilities::GetFormatAttributes**](/windows/win32/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicecapabilities-getformatattributes?branch=master) method retrieve a collection of attributes for the given format GUID. It then calls the [**IPortableDeviceValues::GetStringValue**](iportabledevicevalues-getstringvalue.md) method and requests that the driver return a script-friendly name for the given format.

The following code uses the **DisplayFormat** method.


```C++
// Display basic information about a format
void DisplayFormat(
    IPortableDeviceServiceCapabilities* pCapabilities,
    REFGUID                             Format)
{
    CComPtr<IPortableDeviceValues> pAttributes;

    HRESULT hr = pCapabilities->GetFormatAttributes(Format, &amp;pAttributes);

    if (SUCCEEDED(hr))
    {
        PWSTR pszFormatName = NULL;
        hr = pAttributes->GetStringValue(WPD_FORMAT_ATTRIBUTE_NAME, &amp;pszFormatName);

        // Display the name of the format if it is available, otherwise fall back to displaying the GUID.
        if (SUCCEEDED(hr))
        {
            printf("%ws", pszFormatName);
        }
        else
        {
            printf("%ws", (PWSTR)CGuidToString(Format));
        }       

        CoTaskMemFree(pszFormatName);
        pszFormatName = NULL;
    }
}
```



## Related topics

<dl> <dt>

[**IPortableDeviceService**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservice?branch=master)
</dt> <dt>

[**IPortableDeviceServiceCapabilities**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicecapabilities?branch=master)
</dt> <dt>

[**IPortableDeviceValues**](iportabledevicevalues.md)
</dt> <dt>

[WpdServicesApiSample](wpdapisample-sample-service-application.md)
</dt> </dl>

 

 



