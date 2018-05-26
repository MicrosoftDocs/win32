---
Description: Invoking Service Methods
ms.assetid: 3a2796c8-1a39-49eb-98e1-c9e06c61f397
title: Invoking Service Methods
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Invoking Service Methods

The WpdServicesApiSample application includes code that demonstrates how an application can invoke the methods supported by a given Contacts service synchronously.. This sample uses the following interfaces



|                                                                        |                                                                                                                                                                         |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interface                                                              | Description                                                                                                                                                             |
| [**IPortableDeviceService**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservice?branch=master)               | Used to retrieve the **IPortableDeviceServiceMethods** interface to invoke methods on a given service.                                                                  |
| [**IPortableDeviceServiceMethods**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicemethods?branch=master) | Used to invoke a service method.                                                                                                                                        |
| [**IPortableDeviceValues**](iportabledevicevalues.md)                 | Used to hold the outgoing method parameters, and the incoming method results. This can be **NULL** if the method does not require any parameters or return any results. |



 

When the user chooses option "9" at the command line, the application invokes the **InvokeMethods** method that is found in the ServiceMethods.cpp module. Note that prior to invoking the methods, the sample application opens a Contacts service on a connected device.

Service methods encapsulate functionality that each service defines and implements. They are unique to each type of service and are represented by a GUID. For example, the Contacts service defines a **BeginSync** method that applications call to prepare the device for synchronizing Contact objects, and an **EndSync** method to notify the device that synchronization has completed. Applications execute a method by calling [**IPortableDeviceServiceMethods::Invoke**](/windows/win32/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicemethods-invoke?branch=master).

Service methods should not be confused with WPD commands. WPD commands are part of the standard WPD Device Driver Interface (DDI), and are the mechanism for communication between a WPD application and the driver. Commands are predefined, grouped by categories, for example, **WPD\_CATEGORY\_COMMON**, and are represented by a **PROPERTYKEY** structure. An application sends commands to the device driver by calling [**IPortableDeviceService::SendCommand**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-sendcommand?branch=master). For more information, see the Commands topic.

The **InvokeMethods** method invokes the [**IPortableDeviceService::Methods**](/windows/win32/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservice-capabilities?branch=master) method to retrieve an [**IPortableDeviceServiceMethods**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicecapabilities?branch=master) interface. Using this interface, it invokes the **BeginSync** and **EndSync** methods by calling the [**IPortableDeviceServiceMethods::Invoke**](/windows/win32/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicecapabilities-getsupportedmethods?branch=master) method. Each time it calls **Invoke**, the application supplies the REFGUID for the method that is invoked.

The following code uses the **InvokeMethods** method.


```C++
// Invoke methods on the Contacts Service.
// BeginSync and EndSync are methods defined by the FullEnumerationSync Device Service.
void InvokeMethods(IPortableDeviceService* pService)
{
    HRESULT hr = S_OK;
    CComPtr<IPortableDeviceServiceMethods> pMethods;

    if (pService == NULL)
    {
        printf("! A NULL IPortableDeviceService interface pointer was received\n");
        return;
    }

    // Get an IPortableDeviceServiceMethods interface from the IPortableDeviceService interface to
    // invoke methods.
    hr = pService->Methods(&amp;pMethods);
    if (FAILED(hr))
    {
        printf("! Failed to get IPortableDeviceServiceMethods from IPortableDeviceService, hr = 0x%lx\n",hr);
    }

    // Invoke() the BeginSync method
    if (SUCCEEDED(hr))
    {
        // This method does not take any parameters or results, so we pass in NULL
        hr = pMethods->Invoke(METHOD_FullEnumSyncSvc_BeginSync, NULL, NULL);
        if (SUCCEEDED(hr))
        {
            printf("%ws called, hr = 0x%lx\n",NAME_FullEnumSyncSvc_BeginSync, hr);
        }
        else
        {
            printf("! Failed to invoke %ws, hr = 0x%lx\n",NAME_FullEnumSyncSvc_BeginSync, hr);
        }
    }

    // Invoke the EndSync method asynchronously
    if (SUCCEEDED(hr))
    {
        // This method does not take any parameters or results, so we pass in NULL
        hr = pMethods->Invoke(METHOD_FullEnumSyncSvc_EndSync, NULL, NULL);
        if (SUCCEEDED(hr))
        {
            printf("%ws called, hr = 0x%lx\n",NAME_FullEnumSyncSvc_EndSync, hr);
        }
        else
        {
            printf("! Failed to invoke %ws, hr = 0x%lx\n",NAME_FullEnumSyncSvc_EndSync, hr);
        } 
    }
}
```



## Related topics

<dl> <dt>

[**IPortableDeviceService**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservice?branch=master)
</dt> <dt>

[**IPortableDeviceServiceMethods**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicemethods?branch=master)
</dt> <dt>

[WpdServicesApiSample](wpdapisample-sample-service-application.md)
</dt> </dl>

 

 



