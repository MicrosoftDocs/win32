---
description: Opening a Service
ms.assetid: 722d657d-332a-40df-ac30-bc2050deda74
title: Opening a Service
ms.topic: article
ms.date: 05/31/2018
---

# Opening a Service

Before your application can perform operations on a service, for example, enumerating content or retrieving descriptions of supported events or methods, it must open the service. In the WpdServicesApiSample application, this task is demonstrated in the ServiceEnumeration.cpp module using the interfaces described in the following table.



| Interface                                                              | Description                                        |
|------------------------------------------------------------------------|----------------------------------------------------|
| [**IPortableDeviceServiceManager**](/windows/desktop/api/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicemanager) | Used to enumerate the services on a device.        |
| [**IPortableDeviceService**](/windows/desktop/api/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservice)               | Used to open a connection to a device service.     |
| [**IPortableDeviceValues**](iportabledevicevalues.md)                 | Used to hold the application's client information. |



 

The method that opens a service is [**IPortableDeviceService::Open**](/windows/desktop/api/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservice-open). This method takes two arguments: a Plug-and-Play (PnP) identifier for the service and an [**IPortableDeviceValues**](iportabledevicevalues.md) object that contains the application's client information.

To obtain a PnP identifier for a given service, your application calls the [**IPortableDeviceServiceManager::GetDeviceServices**](/windows/desktop/api/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicemanager-getdeviceservices) method. This method retrieves an array of PnP identifiers for services of a service category GUID (for example SERVICE Contacts).

The sample Service application retrieves a PnP identifier for Contacts services within the **EnumerateContactsServices** method in the ServiceEnumeration.cpp module. The following code sample is taken from this method.


```C++
// For each device found, find the contacts service
for (dwIndex = 0; dwIndex < cPnpDeviceIDs; dwIndex++)
{
    DWORD   cPnpServiceIDs = 0;
    PWSTR   pPnpServiceID  = NULL;

    // First, pass NULL as the PWSTR array pointer to get the total number
    // of contacts services (SERVICE_Contacts) found on the device.
    // To find the total number of all services on the device, use GUID_DEVINTERFACE_WPD_SERVICE.
    hr = pServiceManager->GetDeviceServices(pPnpDeviceIDs[dwIndex], SERVICE_Contacts, NULL, &cPnpServiceIDs);
    
    if (SUCCEEDED(hr) && (cPnpServiceIDs > 0))
    {                               
        // For simplicity, we are only using the first contacts service on each device
        cPnpServiceIDs = 1;
        hr = pServiceManager->GetDeviceServices(pPnpDeviceIDs[dwIndex], SERVICE_Contacts, &pPnpServiceID, &cPnpServiceIDs);

        if (SUCCEEDED(hr))
        {
            // We've found the service, display it and save its PnP Identifier
            ContactsServicePnpIDs.Add(pPnpServiceID);

            printf("[%d] ", static_cast<DWORD>(ContactsServicePnpIDs.GetCount()-1));

            // Display information about the device that contains this service.
            DisplayDeviceInformation(pServiceManager, pPnpServiceID);

            // ContactsServicePnpIDs now owns the memory for this string
            pPnpServiceID = NULL;
        }
        else
        {
            printf("! Failed to get the first contacts service from '%ws, hr = 0x%lx\n",pPnpDeviceIDs[dwIndex],hr);
        }
    }
}
```



After your application retrieves the PnP identifier for the service, it can set up the client information and call [**IPortableDeviceService::Open**](/windows/desktop/api/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservice-open).

In the sample application, this method is called within **ChooseDeviceService** in the ServiceEnumeration.cpp module.

[**IPortableDeviceService**](/windows/desktop/api/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservice) supports two CLSIDs for **CoCreateInstance**. **CLSID\_PortableDeviceService** returns an **IPortableDeviceService** pointer that does not aggregate the free-threaded marshaler; **CLSID\_PortableDeviceServiceFTM** is a new CLSID that returns an **IPortableDeviceService** pointer that aggregates the free-threaded marshaler. Both pointers support the same functionality otherwise.

Applications that live in Single Threaded Apartments should use **CLSID\_PortableDeviceServiceFTM** as this eliminates the overhead of interface pointer marshaling. **CLSID\_PortableDeviceService** is still supported for legacy applications.


```C++
hr = CoCreateInstance(CLSID_PortableDeviceServiceFTM,
                      NULL,
                      CLSCTX_INPROC_SERVER,
                      IID_PPV_ARGS(&pService));
if (SUCCEEDED(hr))
{
    hr = pService->Open(ContactsServicesArray[uiCurrentService], pClientInformation);
    if (FAILED(hr))
    {
        if (hr == E_ACCESSDENIED)
        {
            printf("Failed to Open the service for Read Write access, will open it for Read-only access instead\n");

            pClientInformation->SetUnsignedIntegerValue(WPD_CLIENT_DESIRED_ACCESS, GENERIC_READ);

            hr = pService->Open(ContactsServicesArray[uiCurrentService], pClientInformation);

            if (FAILED(hr))
            {
                printf("! Failed to Open the service for Read access, hr = 0x%lx\n",hr);
            }
        }
        else
        {
            printf("! Failed to Open the service, hr = 0x%lx\n",hr);
        }
    }
```



## Related topics

<dl> <dt>

[**IPortableDeviceService Interface**](/windows/desktop/api/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservice)
</dt> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceServiceManager Interface**](/windows/desktop/api/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicemanager)
</dt> <dt>

[WpdServicesApiSample](wpdapisample-sample-service-application.md)
</dt> </dl>

 

 



