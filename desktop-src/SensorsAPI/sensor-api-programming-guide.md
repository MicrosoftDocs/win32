---
description: This section provides information, including example code, about how to use the Sensor API features. For background information about the various programming interfaces, see About the Sensor API.
ms.assetid: 4c2ffd22-49ee-4318-bfa0-e0ce4d8c67bb
title: Sensor API Programming Guide
ms.topic: article
ms.date: 05/31/2018
---

# Sensor API Programming Guide

This section provides information, including example code, about how to use the Sensor API features. For background information about the various programming interfaces, see [About the Sensor API](about-the-sensor-api.md).

The example code in this section makes use of the following additional included headers.


```C++
#include <windows.h>
#include <initguid.h>
#include <propkeydef.h>


#include <iostream>
#include <propvarutil.h>
#include <functiondiscoverykeys.h>
#include <assert.h>
```





You must also link to these additional associated library files: Propsys.lib and PortableDeviceGuids.lib.

The example code in this section uses the following constants for sensor categories, types, and data fields. These constants are custom values that are defined by the TimeSensor driver sample in the Windows Driver Kit. Note that, though the Sensor platform enables defining and using custom types such as these, you should use platform-defined types whenever possible.


```C++
// Define an object ID.
// {0D77BEE3-7169-42bf-8379-28F9A9B59A57}
DEFINE_GUID(SAMPLE_SENSOR_TIME_ID, 
0xd77bee3, 0x7169, 0x42bf, 0x83, 0x79, 0x28, 0xf9, 0xa9, 0xb5, 0x9a, 0x57);

// Define a custom category.
// {062A5C3B-44C1-4ad1-8EFC-0F65B2E4AD48}
DEFINE_GUID(SAMPLE_SENSOR_CATEGORY_DATE_TIME, 
0x62a5c3b, 0x44c1, 0x4ad1, 0x8e, 0xfc, 0xf, 0x65, 0xb2, 0xe4, 0xad, 0x48);

// Define a custom type.
// {5F199A84-409F-4e35-B2DD-F9C79F5318A0}
DEFINE_GUID(SAMPLE_SENSOR_TYPE_TIME, 
0x5f199a84, 0x409f, 0x4e35, 0xb2, 0xdd, 0xf9, 0xc7, 0x9f, 0x53, 0x18, 0xa0);

// Time sensor fields.
// Because these are related, each field uses the same GUID, but changes the PID.
// {340946F2-9A77-42b0-8176-57D4DF00E5CA}
DEFINE_PROPERTYKEY(SAMPLE_SENSOR_DATA_TYPE_HOUR, 
0x340946f2, 0x9a77, 0x42b0, 0x81, 0x76, 0x57, 0xd4, 0xdf, 0x0, 0xe5, 0xca, PID_FIRST_USABLE); // PID = 2

DEFINE_PROPERTYKEY(SAMPLE_SENSOR_DATA_TYPE_MINUTE, 
0x340946f2, 0x9a77, 0x42b0, 0x81, 0x76, 0x57, 0xd4, 0xdf, 0x0, 0xe5, 0xca, PID_FIRST_USABLE + 1); // PID = 3

DEFINE_PROPERTYKEY(SAMPLE_SENSOR_DATA_TYPE_SECOND, 
0x340946f2, 0x9a77, 0x42b0, 0x81, 0x76, 0x57, 0xd4, 0xdf, 0x0, 0xe5, 0xca, PID_FIRST_USABLE + 2); // PID = 4
```



The example code in this section uses the following variables.


```C++
HRESULT hr = S_OK;

// Sensor interface pointers
ISensorManager* pSensorManager = NULL;    
ISensorCollection* pSensorColl = NULL;
ISensor* pSensor = NULL; 
ISensorDataReport* pReport = NULL;

// Time sensor data field variables
ULONG ulHour, ulMinute, ulSecond = 0;

```



The example code in this section uses the following function to release COM interface pointers.


```C++
template <class T> void SafeRelease(T **ppT)
{
    if (*ppT)
    {
        (*ppT)->Release();
        *ppT = NULL;
    }
}
```



## In This Section

-   [Retrieving a Sensor Object](retrieving-a-sensor.md)
-   [Requesting User Permissions](requesting-user-permissions.md)
-   [Retrieving and Setting Sensor Properties](setting-and-retrieving-sensor-properties.md)
-   [Checking for Supported Sensor Data Fields](checking-for-supported-sensor-data-fields.md)
-   [Using Sensor API Events](using-sensor-api-events.md)
-   [Retrieving Sensor Data Values](retrieving-sensor-data-fields.md)
-   [Retrieving Vector Types](retrieving-vector-types.md)
-   [Using Logical Sensors](using-logical-sensors.md)
-   [Creating Light-Aware User Interfaces](creating-light-aware-user-interfaces.md)

## Related topics

<dl> <dt>

[About the Sensor API](about-the-sensor-api.md)
</dt> </dl>

 

 



