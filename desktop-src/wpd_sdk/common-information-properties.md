---
description: Windows Portable Devices supports the following common information properties.
ms.assetid: eaae7431-d53d-42a1-9286-001c6f5b1641
title: Common Information Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Common
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Common Information Properties

Windows Portable Devices supports the following common information properties.



| Property                                      | VarType        | Description                                                                                              |
|-----------------------------------------------|----------------|----------------------------------------------------------------------------------------------------------|
| **WPD\_COMMON\_INFORMATION\_NOTES**           | **VT\_LPWSTR** | For appointments, tasks, and similar objects, this property contains any notes for the given object.     |
| **WPD\_COMMON\_INFORMATION\_SUBJECT**         | **VT\_LPWSTR** | A value that specifies the subject field of this object.                                                 |
| **WPD\_COMMON\_INFORMATION\_BODY\_TEXT**      | **VT\_LPWSTR** | This property contains the body text of an object, in plaintext or HTML format.                          |
| **WPD\_COMMON\_INFORMATION\_PRIORITY**        | **VT\_UI4**    | A value that specifies the priority of this object. 0 indicates the highest priority.                    |
| **WPD\_COMMON\_INFORMATION\_START\_DATETIME** | **VT\_DATE**   | A value that specifies the date/time that an appointment, task, or similar object is scheduled to start. |
| **WPD\_COMMON\_INFORMATION\_END\_DATETIME**   | **VT\_DATE**   | A value that specifies the date/time that an appointment, task, or similar object is scheduled to end.   |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




