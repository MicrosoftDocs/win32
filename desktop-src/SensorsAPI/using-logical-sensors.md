---
Description: Using Logical Sensors
ms.assetid: 97f4c44e-27dd-4f2a-b987-060bb2d9bc00
title: Using Logical Sensors
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Logical Sensors

To instantiate a device node for a logical sensor, or to reconnect to an existing logical sensor device node, an application or service must call [**ILogicalSensorManager::Connect**](https://msdn.microsoft.com/en-us/library/Dd374029(v=VS.85).aspx). The *pPropertyStore* parameter for this method requires a pointer to an [IPropertyStore](http://go.microsoft.com/fwlink/p/?linkid=134680) interface that contains the IDs for the sensor drivers to connect to. This means that you must create a property store and add this data to the store before calling this method.

### Connecting to the Logical Sensor

To connect to a logical sensor, you must provide, at a minimum, a hardware ID, as defined in the sensor driver's .inf file, and a logical **GUID** that identifies the sensor. The platform uses this **GUID** to identify the sensor when you choose to disconnect from, or uninstall, the sensor device node.

The following example code creates a helper method that connects to a specified logical sensor. The method parameters receive the sensor hardware ID and a unique **GUID** to identify the sensor.


```C++
HRESULT ConnectToLogicalSensor(PCWSTR* wszHardwareID, GUID guidLogicalID)
{
    HRESULT hr = S_OK;
    
    ILogicalSensorManager* pLSM = NULL;
    IPropertyStore* pStore = NULL;
    PROPVARIANT pv = {};

    // Create the property store.
    hr = PSCreateMemoryPropertyStore(IID_PPV_ARGS(&amp;pStore));

    if(SUCCEEDED(hr))
    {
        // Create the logical sensor manager.
        hr = CoCreateInstance(CLSID_LogicalSensorManager, 
                                NULL, 
                                CLSCTX_INPROC_SERVER, 
                                IID_PPV_ARGS(&amp;pLSM));
    }

    // Fill in the values.
    if(SUCCEEDED(hr))
    {
        hr = InitPropVariantFromStringVector(wszHardwareID, 1, &amp;pv);
    }

    if(SUCCEEDED(hr))
    {
        hr = pStore->SetValue(PKEY_Device_HardwareIds, pv);
    }

    if(SUCCEEDED(hr))
    {
        hr = pStore->SetValue(PKEY_Device_CompatibleIds, pv);
    }

    if(SUCCEEDED(hr))
    {
        // Connect to the logical sensor.
        hr = pLSM->Connect(guidLogicalID, pStore);
    }

    SafeRelease(&amp;pStore);
    SafeRelease(&amp;pLSM);

    return hr;
}
```



### Disconnecting from a Logical Sensor

To disconnect from a logical sensor, you must provide the same logical ID that you used when you called [**Connect**](https://msdn.microsoft.com/en-us/library/Dd374029(v=VS.85).aspx).

The following example code creates a helper function that disconnects from a logical sensor.


```C++
HRESULT DisconnectFromLogicalSensor(GUID guidLogicalID)
{
    HRESULT hr = S_OK;

    ILogicalSensorManager* pLSM = NULL;
 
    if(SUCCEEDED(hr))
    {
        // Create the logical sensor manager.
        hr = CoCreateInstance(CLSID_LogicalSensorManager, 
                                NULL, 
                                CLSCTX_INPROC_SERVER, 
                                IID_PPV_ARGS(&amp;pLSM));
    }

    if(SUCCEEDED(hr))
    {
        hr = pLSM->Disconnect(guidLogicalID);
    }

    SafeRelease(&amp;pLSM);

    return hr;
}
```



### Uninstalling a Logical Sensor

To uninstall a logical sensor, you must provide the same logical ID that you used when you called [**Connect**](https://msdn.microsoft.com/en-us/library/Dd374029(v=VS.85).aspx).

The following example code creates a helper function that uninstalls a logical sensor.


```C++
HRESULT UninstallLogicalSensor(REFGUID guidLogicalID)
{
    HRESULT hr = S_OK;

    ILogicalSensorManager* pLSM;
 
    // Create the logical sensor manager.
    hr = CoCreateInstance(CLSID_LogicalSensorManager, 
                            NULL, 
                            CLSCTX_INPROC_SERVER, 
                            IID_PPV_ARGS(&amp;pLSM));
 
    if(SUCCEEDED(hr))
    {
        hr = pLSM->Uninstall(guidLogicalID);
    }

    SafeRelease(&amp;pLSM);

    return hr;
}
```



## Related topics

<dl> <dt>

[About Logical Sensors](about-logical-sensors.md)
</dt> </dl>

 

 



