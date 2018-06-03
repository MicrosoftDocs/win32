---
title: Instantiating the WPD Automation Factory Interface
description: WPD Automation can be instantiated from C++/COM by CoCreating IPortableDeviceDispatchFactory and calling IPortableDeviceDispatchFactory GetDeviceDispatch, supplying a Device Plug and Play (PnP) identifier.
ms.assetid: d83db1cd-7bd2-42f1-b1f2-55090a332e9a
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Instantiating the WPD Automation Factory Interface

WPD Automation can be instantiated from C++/COM by CoCreating [**IPortableDeviceDispatchFactory**](/windows/desktop/api/PortableDeviceApi/nn-portabledeviceapi-iportabledevicedispatchfactory) and calling [**IPortableDeviceDispatchFactory::GetDeviceDispatch**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevicedispatchfactory-getdevicedispatch), supplying a Device Plug and Play (PnP) identifier. The **DevicePnPId** is a string that represents a WPD device, and is returned by the [**IPortableDeviceManager::GetDevices**](https://msdn.microsoft.com/library/windows/desktop/dd388693) method in the WPD C++/COM API.

The following example shows how to instantiate and return a WPD Automation **Device** object. The code can be wrapped in an **IDispatch** method for an ActiveX object that is accessible from JScript.


```C++
IFACEMETHODIMP CMyDeviceFactory::GetFirstDeviceObject(IDispatch** ppDeviceObject)
{
    ComPtr<IPortableDeviceManager> spDeviceManager;

    HRESULT hr = CoCreateInstance(CLSID_PortableDeviceManager, 
NULL, CLSCTX_INPROC_SERVER, IID_PPV_ARGS(&amp;spDeviceManager));

    if (SUCCEEDED(hr))
    {
        // For simplicity, the following code sample retrieves the first 
        // device, if available.

        LPWSTR pszDevicePnPID = NULL;
        DWORD cDevices = 1;
        hr = spDeviceManager->GetDevices(pszDevicePnPID, &amp;cDevices);

        if (SUCCEEDED(hr) &amp;&amp; cDevices > 0)
        {
            CComPtr<IPortableDeviceDispatchFactory> spDeviceDispatchFactory;
            hr = CoCreateInstance(CLSID_PortableDeviceDispatchFactory, NULL, CLSCTX_INPROC_SERVER, IID_PPV_ARGS(&amp;spDeviceDispatchFactory));

            if (SUCCEEDED(hr))
            {
                hr = spDeviceDispatchFactory->GetDeviceDispatch(pszDevicePnPID, ppDeviceObject);
            }
        }

        CoTaskMemFree(pszDevicePnPID);
    }

    return hr;
}
```



The following example shows how to instantiate a **Device** object from JScript by calling **CMyDeviceFactory** through **IDispatch**.


```JScript
var deviceFactory = new ActiveXObject("MyControl.MyDeviceFactory");

// Get the first device object from the device factory
var deviceObject = deviceFactory.GetFirstDeviceObject();
```



## Related topics

<dl> <dt>

[About the Device Object](about-the-device-object.md)
</dt> <dt>

[Best Practices for Writing WPD Automation Scripts](best-practices-for-writing-wpd-automation-scripts.md)
</dt> <dt>

[**IPortableDeviceDispatchFactory Interface**](/windows/desktop/api/PortableDeviceApi/nn-portabledeviceapi-iportabledevicedispatchfactory)
</dt> <dt>

[Using WPD Automation](using-wpd-automation.md)
</dt> <dt>

[Windows Portable Devices Programming Reference](https://msdn.microsoft.com/library/windows/desktop/dd375709)
</dt> </dl>

 

 




