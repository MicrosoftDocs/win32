---
Description: Invoking Service Methods Asynchronously
ms.assetid: d3072e34-65f2-4eeb-bcfa-e2db2d34e680
title: Invoking Service Methods Asynchronously
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Invoking Service Methods Asynchronously

The WpdServiceApiSample application includes code that demonstrates how an application can invoke the service methods asynchronously. This sample uses the following interfaces.



|                                                                                         |                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interface                                                                               | Description                                                                                                                                                             |
| [**IPortableDeviceService**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservice?branch=master)                                | Used to retrieve the **IPortableDeviceServiceMethods** interface to invoke methods on a given service.                                                                  |
| [**IPortableDeviceServiceMethods**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicemethods?branch=master)                  | Used to invoke a service method.                                                                                                                                        |
| [**IPortableDeviceValues**](iportabledevicevalues.md)                                  | Used to hold the outgoing method parameters, and the incoming method results. This can be **NULL** if the method does not require any parameters or return any results. |
| [**IPortableDeviceServiceMethodCallback**](https://msdn.microsoft.com/library/windows/desktop/dd319411) | Implemented by the application to receive the method results when a method has completed.                                                                               |



 

When the user chooses option "10" at the command line, the application invokes the **InvokeMethodsAsync** method that is found in the ServiceMethods.cpp module. Note that prior to invoking the methods, the sample application opens a Contacts service on a connected device.

Service methods encapsulate functionality that each service defines and implements. They are unique to each type of service and are represented by a GUID. For example, the Contacts service defines a **BeginSync** method that applications call to prepare the device for synchronizing Contact objects, and an **EndSync** method to notify the device that synchronization has completed. Applications execute a portable device service method by calling [**IPortableDeviceServiceMethods::Invoke**](/windows/win32/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicemethods-invoke?branch=master).

Service methods should not be confused with WPD commands. WPD commands are part of the standard WPD Device Driver Interface (DDI), and are the mechanism for communication between a WPD application and the driver. Commands are predefined, grouped by categories (for example, **WPD\_CATEGORY\_COMMON**), and are represented by a **PROPERTYKEY** structure. An application sends commands to the device driver by calling [**IPortableDeviceService::SendCommand**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-sendcommand?branch=master). For more information, see the Commands topic.

The **InvokeMethodsAsync** method invokes [**IPortableDeviceService::Methods**](/windows/win32/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservice-capabilities?branch=master) to retrieve an [**IPortableDeviceServiceMethods**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicecapabilities?branch=master) interface. Using this interface, it invokes the **InvokeMethodAsync** helper function twice; once for the **BeginSync** method and once for the **EndSync** method. In this example, , **InvokeMethodAsync** waits indefinitely for a global event to be signaled when [**IPortableDeviceServiceMethodCallback::OnComplete**](/windows/win32/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicemethodcallback-oncomplete?branch=master) is called.

The following code uses the **InvokeMethodsAsync** method.


```C++
// Invoke methods on the Contacts Service asynchornously.
// BeginSync and EndSync are methods defined by the FullEnumerationSync Device Service.
void InvokeMethodsAsync(IPortableDeviceService* pService)
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

    // Invoke the BeginSync method asynchronously
    if (SUCCEEDED(hr))
    {
        printf("Invoking %ws asynchronously...\n",NAME_FullEnumSyncSvc_BeginSync);

        // This method does not take any parameters, so we pass in NULL
        hr = InvokeMethodAsync(pMethods, METHOD_FullEnumSyncSvc_BeginSync, NULL);
        if (FAILED(hr))
        {
            printf("! Failed to invoke %ws asynchronously, hr = 0x%lx\n",NAME_FullEnumSyncSvc_BeginSync, hr);
        }
    }

    // Invoke the EndSync method asynchronously
    if (SUCCEEDED(hr))
    {
        printf("Invoking %ws asynchronously...\n",NAME_FullEnumSyncSvc_EndSync);

        hr = InvokeMethodAsync(pMethods, METHOD_FullEnumSyncSvc_EndSync, NULL);
        if (FAILED(hr))
        {
            printf("! Failed to invoke %ws asynchronously, hr = 0x%lx\n",NAME_FullEnumSyncSvc_EndSync, hr);
        }
    }
}
```



The **InvokeMethodAsync** helper function does the following for each method that it invokes:

-   Creates a global event handle that it monitors to determine method completion.
-   Creates a **CMethodCallback** object that is supplied as an argument to [**IPortableDeviceServiceMethods:InvokeAsync**](/windows/win32/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicemethods-invokeasync?branch=master).
-   Calls the **IPortableDeviceServiceMethods::InvokeAsync** method to invoke the given method.
-   Monitors the global event handle for completion.
-   Performs cleanup.

The **CMethodCallback** class demonstrates how an application can implement [**IPortableDeviceServiceMethodCallback**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicemethodcallback?branch=master). The implementation of **OnComplete** in this class signals an event to notify the application that the service method has completed. In addition to the **OnComplete** method, this class implements **AddRef**, **QueryInterface**, and **Release**, which are used to maintain the object's reference count and the interfaces that it implements.


```C++
class CMethodCallback : public IPortableDeviceServiceMethodCallback
{
public:
   CMethodCallback () : m_cRef(1)
   {
   }

   ~CMethodCallback ()
   {
   }

public:
    // IPortableDeviceServiceMethodCallback::QueryInterface
    virtual HRESULT STDMETHODCALLTYPE OnComplete(
        HRESULT                 hrStatus,
        IPortableDeviceValues*  /*pResults*/) // We are ignoring results as our methods will not return any results
    {
        printf("** Method completed, status HRESULT = 0x%lx **\n", hrStatus);

        if (g_hMethodCompleteEvent != NULL)
        {
            SetEvent(g_hMethodCompleteEvent);
        }          
        return S_OK;
    }

    // IUnknown::AddRef
    virtual ULONG STDMETHODCALLTYPE AddRef(void)
    {
        InterlockedIncrement((long*) &amp;m_cRef);
        return m_cRef;
    }

    // IUnknown::QueryInterface
    virtual HRESULT STDMETHODCALLTYPE QueryInterface(
        REFIID  riid,
        LPVOID* ppvObj)
    {
        HRESULT hr = S_OK;
        if (ppvObj == NULL)
        {
            hr = E_INVALIDARG;
            return hr;
        }

        if ((riid == IID_IUnknown) ||
            (riid == IID_IPortableDeviceServiceMethodCallback))
        {
            AddRef();
            *ppvObj = this;
        }
        else
        {
            *ppvObj = NULL;
            hr = E_NOINTERFACE;
        }
        return hr;
    }

    // IUnknown::Release
    virtual ULONG STDMETHODCALLTYPE Release(void)
    {
        ULONG ulRefCount = m_cRef - 1;

        if (InterlockedDecrement((long*) &amp;m_cRef) == 0)
        {
            delete this;
            return 0;
        }
        return ulRefCount;
    }

private:
    DWORD   m_cRef;
};
```



## Related topics

<dl> <dt>

[**IPortableDeviceService**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservice?branch=master)
</dt> <dt>

[**IPortableDeviceServiceMethodCallback**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicemethodcallback?branch=master)
</dt> <dt>

[**IPortableDeviceServiceMethods**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicemethods?branch=master)
</dt> <dt>

[WpdServicesApiSample](wpdapisample-sample-service-application.md)
</dt> </dl>

 

 



