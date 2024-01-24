---
description: Windows Portable Devices supports the following appointment properties.
ms.assetid: d7e2130b-722b-46ef-9114-17db9c95d017
title: Appointment Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Appointment
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Appointment Properties

Windows Portable Devices supports the following appointment properties.



| Property                                   | VarType        | Description                                                                          |
|--------------------------------------------|----------------|--------------------------------------------------------------------------------------|
| **WPD\_APPOINTMENT\_ACCEPTED\_ATTENDEES**  | **VT\_LPWSTR** | Semicolon-delimited list of attendees who have accepted the appointment.             |
| **WPD\_APPOINTMENT\_DECLINED\_ATTENDEES**  | **VT\_LPWSTR** | Semicolon-delimited list of attendees who have declined the appointment.             |
| **WPD\_APPOINTMENT\_LOCATION**             | VT\_LPWSTR     | A reader-friendly location of the appointment, for example, "Building 5, Room 7".    |
| **WPD\_APPOINTMENT\_OPTIONAL\_ATTENDEES**  | **VT\_LPWSTR** | Semicolon-delimited list of optional attendees for the appointment.                  |
| **WPD\_APPOINTMENT\_REQUIRED\_ATTENDEES**  | **VT\_LPWSTR** | Semicolon-delimited list of required attendees for the appointment.                  |
| **WPD\_APPOINTMENT\_RESOURCES**            | **VT\_LPWSTR** | Semicolon-delimited list of resources required for the appointment.                  |
| **WPD\_APPOINTMENT\_TENTATIVE\_ATTENDEES** | **VT\_LPWSTR** | Semicolon-delimited list of attendees who have tentatively accepted the appointment. |
| **WPD\_APPOINTMENT\_TYPE**                 | **VT\_LPWSTR** | The type of appointment, for example,"Personal", "Business", and so on.              |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




