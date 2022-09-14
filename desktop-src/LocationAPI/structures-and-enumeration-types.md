---
description: The Location API defines the following enumeration types.
ms.assetid: a1d9d274-2861-4818-8fa1-d8d66edf27b3
title: Structures and Enumeration Types (Location API)
ms.topic: article
ms.date: 05/31/2018
---

# Structures and Enumeration Types (Location API)

\[The Win32 Location API is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use the [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API. \]

The Location API defines the following enumeration types.



| Enumeration                                                                       | Description                                                          |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [**LOCATION\_DESIRED\_ACCURACY**](/previous-versions/windows/desktop/legacy/dd756639(v=vs.85))                  | Defines the possible desired accuracy types.                         |
| [**LOCATION\_REPORT\_STATUS**](/windows/win32/api/locationapi/ne-locationapi-location_report_status) | Defines possible status for new reports of a particular report type. |



 

## Location Constants from the Sensor API

The Sensor API also defines location-related property keys and constants. The property keys defined in sensors.h can be used to retrieve location data from a report by calling [**ILocationReport::GetValue**](/windows/win32/api/locationapi/nf-locationapi-ilocationreport-getvalue).

 

 
