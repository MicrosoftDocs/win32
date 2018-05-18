---
title: Enumerating Devices
description: Enumerating Devices
ms.assetid: '0236a629-c09a-4687-a8ba-fa05107fab33'
keywords: ["Windows Media Player,portable devices", "Windows Media Player object model,portable devices", "object model,portable devices", "Windows Media Player ActiveX control,portable devices", "ActiveX control,portable devices", "Windows Media Player Mobile ActiveX control,portable devices", "Windows Media Player Mobile,portable devices", "portable devices,enumerating", "enumerations,portable devices"]
---

# Enumerating Devices

Windows Media Player represents portable devices by using the **IWMPSyncDevice** interface. The following example code shows a function that creates an array of pointers to **IWMPSyncDevice**. Each pointer in the array represents a device for which Windows Media Player has stored information. A device is not required to be connected to the computer, nor is it required to have a partnership with the current Windows Media Player instance.

You should enumerate devices whenever you receive the **DeviceConnect** event or the **DeviceDisconnect** event.

The following function enumerates devices. The *bConnectedOnly* parameter specifies whether to enumerate only devices currently connected to the user's computer.


```C++
STDMETHODIMP CMainDlg::EnumDevices(BOOL bConnectedOnly)
{
    HRESULT hr = S_OK;
    CComPtr<IWMPSyncServices>  spSyncServices;
    long cDeviceArray = 0;  // Size to make the array
    long cAllDevices = 0;  // Count of all devices
    long cDeviceIndex = 0; // Index for adding devices to array.
    CComPtr<IWMPSyncDevice> spTempDevice;
    VARIANT_BOOL vbIsConnected = VARIANT_FALSE;

    // Delete any existing array.
    FreeDeviceArray();

    // Retrieve a pointer to IWMPSyncServices.
    hr = m_spPlayer->QueryInterface(&amp;spSyncServices);

    if(SUCCEEDED(hr) &amp;&amp; spSyncServices.p)
    {  
        hr = spSyncServices->get_deviceCount(&amp;cAllDevices);
    }

    if(SUCCEEDED(hr) &amp;&amp; cAllDevices > 0)
    {
        if(bConnectedOnly)
        {
            // Count the number of connected devices.
            for(long i = 0; i < cAllDevices; i++)
            {     
                spTempDevice.Release();
                hr = spSyncServices->getDevice(i, &amp;spTempDevice);

                if(SUCCEEDED(hr) &amp;&amp; spTempDevice.p)
                {
                    spTempDevice->get_connected(&amp;vbIsConnected);

                    if(vbIsConnected == VARIANT_TRUE)
                    {
                        // Count only the connected devices.
                        cDeviceArray++;
                    }
                }
            }
        }
        else
        {
            cDeviceArray = cAllDevices;
        }

        if(cDeviceArray == 0)
        {
            return hr;
        }

        // Cache the device count.
        m_cDevices = cDeviceArray;

        // Create a new device array.
        m_ppWMPDevices = new IWMPSyncDevice*[cDeviceArray];
        if(!m_ppWMPDevices)
        {
            return E_OUTOFMEMORY;
        }
        
        ZeroMemory(m_ppWMPDevices, sizeof (IWMPSyncDevice*) * cDeviceArray);

        // Fill the array.
        for(long i = 0; i < cAllDevices; i++)
        {
            spTempDevice.Release();
            hr = spSyncServices->getDevice(i, &amp;spTempDevice);
            if(SUCCEEDED(hr) &amp;&amp; spTempDevice.p)
            {
                spTempDevice->get_connected(&amp;vbIsConnected);

                if( (bConnectedOnly &amp;&amp; vbIsConnected == VARIANT_TRUE) ||
                     !bConnectedOnly )
                {
                    // Add the device to the custom array.
                    spTempDevice.CopyTo(&amp;m_ppWMPDevices[cDeviceIndex++]);
                }
            }
        }
    }

    return hr;
}
```



You might use similar code to retrieve other such device lists. For example, you could use [IWMPSyncDevice::get\_status](iwmpsyncdevice-get-status.md) to create an array of devices for which a partnership exists.

## Related topics

<dl> <dt>

[**IWMPEvents2::DeviceConnect**](iwmpevents2-iwmpevents2--deviceconnect.md)
</dt> <dt>

[**IWMPEvents2::DeviceDisconnect**](iwmpevents2-iwmpevents2--devicedisconnect.md)
</dt> <dt>

[**IWMPSyncDevice Interface**](iwmpsyncdevice.md)
</dt> <dt>

[**IWMPSyncDevice::get\_connected**](iwmpsyncdevice-get-connected.md)
</dt> <dt>

[**IWMPSyncServices Interface**](iwmpsyncservices.md)
</dt> <dt>

[**Working with Portable Devices**](working-with-portable-devices.md)
</dt> </dl>

 

 




