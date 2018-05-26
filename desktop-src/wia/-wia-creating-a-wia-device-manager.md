---
Description: The first step in using Windows Image Acquisition (WIA) services is to obtain an IWiaDevMgr interface pointer (if you are programming for Windows XP or earlier) or an IWiaDevMgr2 interface pointer (if you are programming for Windows Vista or later).
ms.assetid: 8f20c64a-db79-4c3c-a544-685ed82143bb
title: Creating a WIA Device Manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating a WIA Device Manager

The first step in using Windows Image Acquisition (WIA) services is to obtain an [**IWiaDevMgr**](/windows/win32/wia_xp/nn-wia_xp-iwiadevmgr?branch=master) interface pointer (if you are programming for Windows XP or earlier) or an [**IWiaDevMgr2**](-wia-iwiadevmgr2.md) interface pointer (if you are programming for Windows Vista or later). To do this, call [CoCreateInstance](com.cocreateinstance) with the appropriate parameters. The sample application WiaSSamp creates a device manager within a global function implemented by the following code:


```
    HRESULT CreateWiaDeviceManager( IWiaDevMgr **ppWiaDevMgr ) //XP or earlier
    HRESULT CreateWiaDeviceManager( IWiaDevMgr2 **ppWiaDevMgr ) //Vista or later
    {
        //
        // Validate arguments
        //
        if (NULL == ppWiaDevMgr)
        {
            return E_INVALIDARG;
        }

        //
        // Initialize out variables
        //
        *ppWiaDevMgr = NULL;

        //
        // Create an instance of the device manager
        //
        
        //XP or earlier:
        HRESULT hr = CoCreateInstance( CLSID_WiaDevMgr, NULL, CLSCTX_LOCAL_SERVER, IID_IWiaDevMgr, (void**)ppWiaDevMgr );

        //Vista or later:
        HRESULT hr = CoCreateInstance( CLSID_WiaDevMgr2, NULL, CLSCTX_LOCAL_SERVER, IID_IWiaDevMgr2, (void**)ppWiaDevMgr ); 

        //
        // Return the result of creating the device manager
        //
        return hr;
    }
```



In this example, CLSID\_WiaDevMgr and IID\_IWiaDevMgr are WIA constants that represent the class ID and the interface ID of [**IWiaDevMgr**](/windows/win32/wia_xp/nn-wia_xp-iwiadevmgr?branch=master), respectively. CLSID\_WiaDevMgr2 and IID\_IWiaDevMgr2 are WIA constants that represent the class ID and the interface ID of [**IWiaDevMgr2**](-wia-iwiadevmgr2.md), respectively.

The value for the *dwClsContext* argument of the [CoCreateInstance](_com_cocreateinstance) call must be CLSCTX\_LOCAL\_SERVER. No other server type is supported, and Component Object Model (COM) rejects any other value for this parameter.

 

 



