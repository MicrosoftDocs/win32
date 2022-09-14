---
description: Using Light Sensor Data
ms.assetid: 98272df5-08c0-4392-a74b-2919bbdcb022
title: Using Light Sensor Data
ms.topic: article
ms.date: 05/31/2018
---

# Using Light Sensor Data

There are two recommended ways of interpreting and using lux data that comes from ambient light sensors.

-   Apply a transform to the data so that the normalized light level can be used in direct proportion to program behaviors or interactions. An example would be to vary the size of a button in your program in direct proportion to the normalized data (or a range of the normalized data, corresponding to outdoors, for example). This approach gives the optimal implementation.
-   Deal with ranges of lux data, and map program behaviors and reactions to the upper and lower thresholds of these ranges of lux data. This is a simple way to respond to lighting conditions and may not yield the optimal user experience. However, this approach works fine if smooth transitions are not feasible.

## Handling Data from Multiple Light Sensors

To produce the most accurate approximation of the current lighting conditions, you can use data from multiple ambient light sensors. Because ambient light sensors can be partly or fully obscured by shadows or objects that cover the sensor, multiple sensors placed some distance apart can provide a much better approximation of the current lighting conditions than a single sensor.

To keep track of the data coming from multiple sensors, you can use the following two techniques:

-   The most recent data value for each ambient light sensor can be retained, along with the time stamp from the sensor data report for each of these readings. The last [**ISensorDataReport**](/windows/desktop/api/sensorsapi/nn-sensorsapi-isensordatareport) received for each sensor reading could be retained and could provide both values for later reference. By referring to the time stamp for each sensor data report, the data can be managed based on its age. For example, if the data is more than 2 seconds old, it could be omitted. Based on the newer sensor data values, the highest reading could be used because the corresponding sensor would be presumed not to be obscured.
-   You can use the last ambient light sensor value reported. This implementation would not be optimal because the values from multiple sensors are not compared to one another to obtain the most accurate result. We do not recommend this method.

## Example Code

The following example code shows an implementation for the [**OnDataUpdated**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensorevents-ondataupdated) event. The event handler calls a helper function, named **UpdateUI**, that changes the user interface based on the lux value. Writing the implementation of UpdateUI is up to you.


```C++
// Override of ISensorEvents::OnDataUpdated
// Part of an event sink implementation for ISensorEvents
STDMETHODIMP CALSEventSink::OnDataUpdated(
    ISensor* pSensor, 
    ISensorDataReport* pNewData)
{
    HRESULT hr = S_OK;
   
    if(pSensor == NULL ||
       pNewData == NULL)
    {
         return E_POINTER;
    }

    // Declare and initialize the PROPVARIANT
    PROPVARIANT lightLevel;
    PropVariantInit(&lightLevel);

    // Get the sensor reading from the ISensorDataReport object
    hr = pNewData->GetSensorValue(
        SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX, 
        &lightLevel);

    if(SUCCEEDED(hr))
    {
        if(lightlevel.vt == VT_R4)
        {
            // Extract the float value from the PROPVARIANT object
            float luxValue = lightLevel.fltVal;

            // Normalize the light sensor data
            double lightNormalized = ::log10(luxValue) / 5.0;

            // Handle UI changes based on the normalized LUX data
            // which ranges from 0.0 - 1.0 for a lux range of 
            // 0 lux to 100,000 lux. 
            UpdateUI(lightNormalized);
        }
    }

    // Release the variant.     
    PropVariantClear(&lightLevel);

    return hr;
}
```



 

 
