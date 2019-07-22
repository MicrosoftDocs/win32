---
Description: The Location API defines the following enumeration types.
ms.assetid: a1d9d274-2861-4818-8fa1-d8d66edf27b3
title: Structures and Enumeration Types
ms.topic: article
ms.date: 05/31/2018
---

# Structures and Enumeration Types

\[The Win32 Location API is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use the [**Windows.Devices.Geolocation**](https://docs.microsoft.com/uwp/api/Windows.Devices.Geolocation) API. \]

The Location API defines the following enumeration types.



| Enumeration                                                                       | Description                                                          |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [**LOCATION\_DESIRED\_ACCURACY**](https://msdn.microsoft.com/en-us/library/Dd756639(v=VS.85).aspx)                  | Defines the possible desired accuracy types.                         |
| [**LOCATION\_REPORT\_STATUS**](https://msdn.microsoft.com/en-us/library/Dd317641(v=VS.85).aspx) | Defines possible status for new reports of a particular report type. |



 

## Location Constants from the Sensor API

The Sensor API also defines location-related property keys and constants. The property keys defined in sensors.h can be used to retrieve location data from a report by calling [**ILocationReport::GetValue**](https://msdn.microsoft.com/en-us/library/Dd317624(v=VS.85).aspx).

 

 



