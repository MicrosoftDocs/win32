---
description: This topic describes how to request permissions from the user to use sensors. For background information about permissions in the Sensor API, see Managing User Permissions.
ms.assetid: e43ad497-86f1-4804-a67a-0aeb56b80d7f
title: Requesting User Permissions
ms.topic: article
ms.date: 05/31/2018
---

# Requesting User Permissions

This topic describes how to request permissions from the user to use sensors. For background information about permissions in the Sensor API, see [Managing User Permissions](managing-user-permissions.md).

The following examples illustrate some of the common scenarious where you can choose to request user permissions.

The following example code simply requests permissions for all sensors retrieved from the sensor manager, by type, using an asynchronous method call. The platform will open a dialog box to prompt the user only to enable sensors that are not already enabled. To determine whether the user enabled any sensors in this case, you must handle the [**ISensorEvents::OnStateChanged**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensorevents-onstatechanged) event.


```C++
// Get the sensor collection.
hr = pSensorManager->GetSensorsByType(SAMPLE_SENSOR_TYPE_TIME, &pSensorColl);

if(SUCCEEDED(hr))
{
    // Request permissions for all sensors
    // in the collection.
    hr = pSensorManager->RequestPermissions(0, pSensorColl, FALSE);
}

```



You can choose to test the sensor state synchronously before attempting to retrieve data. The following example code demonstrates this technique.


```C++
if(SUCCEEDED(hr))
{
   // Check the current sensor state.
   SensorState state = SENSOR_STATE_NOT_AVAILABLE;

   hr = pSensor->GetState(&state);

   if(SUCCEEDED(hr))
   {
       if(state == SENSOR_STATE_ACCESS_DENIED)
       {
           wprintf_s(L"\nSensor not enabled, requesting permissions...\n");
           hr = pSensorManager->RequestPermissions(0, pSensorColl, TRUE);

           if(hr == HRESULT_FROM_WIN32(ERROR_ACCESS_DENIED) ||
              hr == HRESULT_FROM_WIN32(ERROR_CANCELLED)) 
           {
               wprintf_s(L"\nYou have previously denied access to this sensor.\n");
               wprintf_s(L"Please use the Location and Other Sensors control panel\n");
               wprintf_s(L"to enable the WDK Time Sensor and run this program again.\n");
           }
       }
   }
}

if(SUCCEEDED(hr))
{
    // Get the data report.
    hr = pSensor->GetData(&pReport);
}
```



The following example code prompts the user for sensor permissions if an attempt to retrieve a data report from a particular sensor fails.


```C++
if(SUCCEEDED(hr))
{
    // Get the data report.
    hr = pSensor->GetData(&pReport);

    if(E_ACCESSDENIED == hr)
    {
       wprintf_s(L"\nSensor not enabled, requesting permissions...\n");
       hr = pSensorManager->RequestPermissions(0, pSensorColl, TRUE);

       if(hr == HRESULT_FROM_WIN32(ERROR_ACCESS_DENIED) ||
          hr == HRESULT_FROM_WIN32(ERROR_CANCELLED)) 
       {
           wprintf_s(L"\nYou have previously denied access to this sensor.\n");
           wprintf_s(L"Please use the Location and Other Sensors control panel\n");
           wprintf_s(L"to enable the WDK Time Sensor and run this program again.\n");
       }
    }
}
```



## Related topics

<dl> <dt>

[**ISensorManager**](/windows/desktop/api/sensorsapi/nn-sensorsapi-isensormanager)
</dt> <dt>

[Managing User Permissions](managing-user-permissions.md)
</dt> </dl>

 

 
