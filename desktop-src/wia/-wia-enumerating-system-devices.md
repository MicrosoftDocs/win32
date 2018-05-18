---
Description: 'Use the IWiaDevMgr::EnumDeviceInfo (or IWiaDevMgr2::EnumDeviceInfo) method to enumerate the Windows Image Acquisition (WIA) devices installed on a system.'
ms.assetid: '6465a33e-1b3b-4142-a58f-b27e9c95cd3e'
title: Enumerating System Devices
---

# Enumerating System Devices

Use the [**IWiaDevMgr::EnumDeviceInfo**](-wia-iwiadevmgr-enumdeviceinfo.md) (or [**IWiaDevMgr2::EnumDeviceInfo**](-wia-iwiadevmgr2-enumdeviceinfo.md)) method to enumerate the Windows Image Acquisition (WIA) devices installed on a system. This method creates an enumeration object for the properties of the devices, and returns a pointer to the [**IEnumWIA\_DEV\_INFO**](-wia-ienumwia-dev-info.md) interface that the enumeration object supports.

You can then use the methods of the [**IEnumWIA\_DEV\_INFO**](-wia-ienumwia-dev-info.md) interface to obtain an [**IWiaPropertyStorage**](-wia-iwiapropertystorage.md) interface pointer for each device installed on the system.

The following code from the WiaSSamp sample application demonstrates how to create an enumeration object for the devices on a system and iterate through those devices:


```
    HRESULT EnumerateWiaDevices( IWiaDevMgr *pWiaDevMgr ) //XP or earlier
    HRESULT EnumerateWiaDevices( IWiaDevMgr2 *pWiaDevMgr ) //Vista or later
    
    {
        //
        // Validate arguments
        //
        if (NULL == pWiaDevMgr)
        {
            return E_INVALIDARG;
        }

        //
        // Get a device enumerator interface
        //
        IEnumWIA_DEV_INFO *pWiaEnumDevInfo = NULL;
        HRESULT hr = pWiaDevMgr->EnumDeviceInfo( WIA_DEVINFO_ENUM_LOCAL, &amp;pWiaEnumDevInfo );
        if (SUCCEEDED(hr))
        {
            //
            // Loop until you get an error or pWiaEnumDevInfo->Next returns
            // S_FALSE to signal the end of the list.
            //
            while (S_OK == hr)
            {
                //
                // Get the next device's property storage interface pointer
                //
                IWiaPropertyStorage *pWiaPropertyStorage = NULL;
                hr = pWiaEnumDevInfo->Next( 1, &amp;pWiaPropertyStorage, NULL );

                //
                // pWiaEnumDevInfo->Next will return S_FALSE when the list is
                // exhausted, so check for S_OK before using the returned
                // value.
                //
                if (hr == S_OK)
                {
                    //
                    // Do something with the device's IWiaPropertyStorage*
                    //

                    //
                    // Release the device's IWiaPropertyStorage*
                    //
                    pWiaPropertyStorage->Release();
                    pWiaPropertyStorage = NULL;
                }
            }

            //
            // If the result of the enumeration is S_FALSE (which
            // is normal), change it to S_OK.
            //
            if (S_FALSE == hr)
            {
                hr = S_OK;
            }

            //
            // Release the enumerator
            //
            pWiaEnumDevInfo->Release();
            pWiaEnumDevInfo = NULL;
        }

        //
        // Return the result of the enumeration
        //
        return hr;
    }
```



WIA\_DEVINFO\_ENUM\_LOCAL is a WIA constant that represents the only valid value for this parameter.

In the example, the parameter **pWiaDevMgr** points to an instance of the [**IWiaDevMgr**](-wia-iwiadevmgr.md) (or [**IWiaDevMgr2**](-wia-iwiadevmgr2.md)) interface after a previous call to [CoCreateInstance](com.cocreateinstance).

The application calls the [**IWiaDevMgr::EnumDeviceInfo**](-wia-iwiadevmgr-enumdeviceinfo.md) (or [**IWiaDevMgr2::EnumDeviceInfo**](-wia-iwiadevmgr2-enumdeviceinfo.md)) method of the [**IWiaDevMgr**](-wia-iwiadevmgr.md) (or [**IWiaDevMgr2**](-wia-iwiadevmgr2.md)) pointer **pWiaDevMgr** that fills **pWiaEnumDevInfo** with the address of a pointer to the [**IEnumWIA\_DEV\_INFO**](-wia-ienumwia-dev-info.md) interface.

If the call succeeds, the application then calls the [**IEnumWIA\_DEV\_INFO::Reset**](-wia-ienumwia-dev-info-reset.md) method of the [**IEnumWIA\_DEV\_INFO**](-wia-ienumwia-dev-info.md) pointer. The **pWiaEnumDevInfo** variable ensures that the enumeration starts at the beginning.

If this call succeeds, the application iterates through the devices on the system by repeatedly calling the [**IEnumWIA\_DEV\_INFO::Next**](-wia-ienumwia-dev-info-next.md) method of the [**IEnumWIA\_DEV\_INFO**](-wia-ienumwia-dev-info.md) pointer **pWiaEnumDevInfo** until the method no longer returns S\_OK, indicating that the enumeration is complete.

Each call to **pWiaEnumDevInfo-&gt;Next** fills **pWiaPropertyStorage** with a pointer to the [**IWiaPropertyStorage**](-wia-iwiapropertystorage.md) interface that contains property information for a specific device.

 

 



