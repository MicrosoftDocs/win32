---
title: Device Collections Returned By Synchronous Searches
description: Device collections are objects that contain one or more Device objects. A Device collection exposes the IUPnPDevices interface that provides methods and properties for traversing the collection and extracting individual device objects.
ms.assetid: '45455c3f-7281-4f96-a609-2efd2cf36aa2'
---

# Device Collections Returned By Synchronous Searches

Device collections are objects that contain one or more Device objects. A Device collection exposes the [**IUPnPDevices**](iupnpdevices.md) interface that provides methods and properties for traversing the collection and extracting individual device objects.

## VBScript Example

VBScript applications can access the objects in the collection in two ways. First, they can traverse the elements sequentially using a for … each ... next loop as shown in the following example:


```VB
for each deviceObj in devices
    MsgBox(deviceObj.FriendlyName)
next
```



In this example, the devices variable is assumed to have been initialized with the result of a prior search. The loop steps through the Device objects in the collection, assigning the variable deviceObj the value of each Device object in turn. The body of the loop can contain code that processes the Device object.

## C++ Example

The following example shows the C++ code required to access the objects in a collection of device objects. The function shown, **TraverseCollection**, receives a pointer to the [**IUPnPDevices**](iupnpdevices.md) interface as an input parameter. This interface pointer could be returned by the [**FindByType**](iupnpdevicefinder-findbytype.md) method, or other **Find** methods, of the Device Finder object.


```C++
#include <windows.h>
#include <upnp.h>

#pragma comment(lib, "oleaut32.lib")

HRESULT TraverseCollection(IUPnPDevices * pDevices)
{
    IUnknown * pUnk = NULL;
    HRESULT hr = pDevices->get__NewEnum(&amp;pUnk);
    if (SUCCEEDED(hr))
    {
        IEnumVARIANT * pEnumVar = NULL;
        hr = pUnk->QueryInterface(IID_IEnumVARIANT, (void **) &amp;pEnumVar);
        if (SUCCEEDED(hr))
        {
            VARIANT varCurDevice;
            VariantInit(&amp;varCurDevice);
            pEnumVar->Reset();
            // Loop through each device in the collection
            while (S_OK == pEnumVar->Next(1, &amp;varCurDevice, NULL))
            {
                IUPnPDevice * pDevice = NULL;
                IDispatch * pdispDevice = V_DISPATCH(&amp;varCurDevice);
                if (SUCCEEDED(pdispDevice->QueryInterface(IID_IUPnPDevice, (void **) &amp;pDevice)))
                {
                    // Do something interesting with pDevice
                    BSTR bstrName = NULL;
                    if (SUCCEEDED(pDevice->get_FriendlyName(&amp;bstrName)))
                    {
                        OutputDebugStringW(bstrName);
                        SysFreeString(bstrName);
                    }
                }
                VariantClear(&amp;varCurDevice);
                pDevice->Release();
            }
            pEnumVar->Release();
        }
        pUnk->Release();
    }
    return hr;
}
```



The first step is to request a new enumerator for the collection using the [**\_NewEnum**](iupnpdevices--newenum.md) property. This returns an enumerator as the [**IUnknown**](_com_iunknown) interface. The sample code invokes [**IUnknown::QueryInterface**](_com_iunknown_queryinterface) to obtain the [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface. The sample code then sets the enumerator to the beginning of the collection by invoking the [**IEnumVARIANT::Reset**](0c3f0cd7-6bad-4cb7-8b84-d8a212dbadbd) method. Finally, the sample code invokes the [**IEnumVARIANT::Next**](691c1624-8d01-41e0-890e-a4782eba1f59) method to traverse the collection. The device objects in the collection are contained within **VARIANT** structures. These structures contain pointers to [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interfaces on the device objects. To obtain the [**IUPnPDevice**](iupnpdevice.md) interface, the sample code invokes **QueryInterface** on the **IDispatch** interface.

 

 




