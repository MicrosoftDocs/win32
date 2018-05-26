---
title: Searching Asynchronously in C++
description: The following code can be used as a basis for a C++ application that searches for devices asynchronously. The code implements the IUPnPDeviceFinderCallback interface by creating a class that inherits from it.
ms.assetid: bb874e60-6a93-4d94-be67-ba03ba92eff5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Searching Asynchronously in C++

The following code can be used as a basis for a C++ application that searches for devices asynchronously. The code implements the [**IUPnPDeviceFinderCallback**](/windows/win32/Upnp/nn-upnp-iupnpdevicefindercallback?branch=master) interface by creating a class that inherits from it.

To implement both [**IUPnPDeviceFinderCallback**](/windows/win32/Upnp/nn-upnp-iupnpdevicefindercallback?branch=master) and [**IUPnPDeviceFinderAddCallbackWithInterface**](/windows/win32/Upnp/nn-upnp-iupnpdevicefinderaddcallbackwithinterface?branch=master), the class must inherit from both interfaces. Implementation of **IUPnPDeviceFinderAddCallbackWithInterface** is optional, but if you choose to implement it, you must also implement **IUPnPDeviceFinderCallback**.


```C++
#include <windows.h>
#include <upnp.h>
#include <stdio.h>

#pragma comment(lib, "ole32.lib")
#pragma comment(lib, "oleaut32.lib")
#pragma comment(lib, "user32.lib")

class CUPnPDeviceFinderCallback : public IUPnPDeviceFinderCallback
{
public:
    CUPnPDeviceFinderCallback()
    {
        m_lRefCount = 0;
    };
    
    STDMETHODIMP QueryInterface(REFIID iid, LPVOID* ppvObject)
    {
        HRESULT hr = S_OK;
        
        if(NULL == ppvObject)
        {
            hr = E_POINTER;
        }
        else
        {
            *ppvObject = NULL;
        }
        
        if(SUCCEEDED(hr))
        {
            if(IsEqualIID(iid, IID_IUnknown) || IsEqualIID(iid, IID_IUPnPDeviceFinderCallback))
            {
                *ppvObject = static_cast<IUPnPDeviceFinderCallback*>(this);
                AddRef();
            }
            else
            {
                hr = E_NOINTERFACE;
            }
        }
        
        return hr;
    };
    
    STDMETHODIMP_(ULONG) AddRef()
    {
        return ::InterlockedIncrement(&amp;m_lRefCount);
    };
    
    STDMETHODIMP_(ULONG) Release()
    {
        LONG lRefCount = ::InterlockedDecrement(&amp;m_lRefCount);
        if(0 == lRefCount)
        {
            delete this;
        }
        
        return lRefCount;
    };
    
    STDMETHODIMP DeviceAdded(LONG lFindData, IUPnPDevice* pDevice)
    {
        HRESULT hr = S_OK;

        //You should save pDevice so that it is accessible outside the scope of this method.

        BSTR UniqueDeviceName;
        hr = pDevice->get_UniqueDeviceName(&amp;UniqueDeviceName);
        if (SUCCEEDED(hr))
        {
            BSTR FriendlyName;
            hr = pDevice->get_FriendlyName(&amp;FriendlyName);
            if (SUCCEEDED(hr))
            {
                printf("Device Added: udn: %S, name: %S\n", FriendlyName, UniqueDeviceName);
                ::SysFreeString(FriendlyName);
            }
            ::SysFreeString(UniqueDeviceName);
        }
        return hr;
        
    };
    
    STDMETHODIMP DeviceRemoved(LONG lFindData, BSTR bstrUDN)
    {
        printf("Device Removed: udn: %S", bstrUDN);
        return S_OK;
    };
    
    STDMETHODIMP SearchComplete(LONG lFindData)
    {
        return S_OK;
    };
    
    
    
private:
    LONG m_lRefCount;
    
};

HRESULT FindUPnPDevice(BSTR TypeURI)
{
    HRESULT hr = S_OK;
    
    IUPnPDeviceFinderCallback* pUPnPDeviceFinderCallback = new CUPnPDeviceFinderCallback();
    if(NULL != pUPnPDeviceFinderCallback)
    {
        pUPnPDeviceFinderCallback->AddRef();
        IUPnPDeviceFinder* pUPnPDeviceFinder;
        hr = CoCreateInstance(CLSID_UPnPDeviceFinder, NULL, CLSCTX_INPROC_SERVER, 
            IID_IUPnPDeviceFinder, reinterpret_cast<void**>(&amp;pUPnPDeviceFinder));
        if(SUCCEEDED(hr))
        {
            LONG lFindData;
            hr = pUPnPDeviceFinder->CreateAsyncFind(TypeURI, 0, pUPnPDeviceFinderCallback, &amp;lFindData);
            if(SUCCEEDED(hr))
            {
                hr = pUPnPDeviceFinder->StartAsyncFind(lFindData);
                if(SUCCEEDED(hr))
                {
                    // STA threads must pump messages
                    MSG Message;
                    BOOL bGetMessage;
                    while(bGetMessage = GetMessage(&amp;Message, NULL, 0, 0) &amp;&amp; -1 != bGetMessage)
                    {
                        DispatchMessage(&amp;Message);      
                    }
                }
                pUPnPDeviceFinder->CancelAsyncFind(lFindData);
            }
            pUPnPDeviceFinder->Release();
        }
        pUPnPDeviceFinderCallback->Release();
    }
    else
    {
        hr = E_OUTOFMEMORY;
    }
   
    return hr;
}
```



 

 




