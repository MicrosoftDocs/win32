---
Description: 'Once an application has the device ID of a given device, it can call the IWiaDevMgr::CreateDevice or IWiaDevMgr2::CreateDevicemethod, which creates a hierarchical tree of IWiaItem or IWiaItem2 objects that represent an imaging device and the image scanning beds, and folders contained on that device.'
ms.assetid: '807695c2-4c42-4318-9a5d-d34ac9014f0f'
title: Creating a Device
---

# Creating a Device

Once an application has the device ID of a given device, it can call the [**IWiaDevMgr::CreateDevice**](-wia-iwiadevmgr-createdevice.md) or [**IWiaDevMgr2::CreateDevice**](-wia-iwiadevmgr2-createdevice.md)method, which creates a hierarchical tree of [**IWiaItem**](-wia-iwiaitem.md) or [**IWiaItem2**](-wia-iwiaitem2.md) objects that represent an imaging device and the image scanning beds, and folders contained on that device.

The following example from the sample application WiaSSamp implements a function that takes a device ID as a parameter. For information about how to obtain a device ID for a particular device, see [Reading Device Properties](-wia-reading-device-properties.md).


```
    //XP or earlier:
    HRESULT CreateWiaDevice( IWiaDevMgr *pWiaDevMgr, BSTR bstrDeviceID, IWiaItem **ppWiaDevice ) 
    //Vista or later:
    HRESULT CreateWiaDevice( IWiaDevMgr2 *pWiaDevMgr, BSTR bstrDeviceID, IWiaItem2 **ppWiaDevice ) 
    {
        //
        // Validate arguments
        //
        if (NULL == pWiaDevMgr || NULL == bstrDeviceID || NULL == ppWiaDevice)
        {
            return E_INVALIDARG;
        }

        //
        // Initialize out variables
        //
        *ppWiaDevice = NULL;

        //
        // Create the WIA Device
        //
        HRESULT hr = pWiaDevMgr->CreateDevice( bstrDeviceID, ppWiaDevice );

        //
        // Return the result of creating the device
        //
        return hr;
    }
```



In this example, **pWiaDevMgr** is a pointer to the [**IWiaDevMgr**](-wia-iwiadevmgr.md) or [**IWiaDevMgr2**](-wia-iwiadevmgr2.md) interface, and **ppWiaDevice** is a variable that, after the call to [**IWiaDevMgr::CreateDevice**](-wia-iwiadevmgr-createdevice.md) (or to [**IWiaDevMgr2::CreateDevice**](-wia-iwiadevmgr2-createdevice.md)), contains the address of a pointer to the root item of the tree that represents the newly created device.

 

 



