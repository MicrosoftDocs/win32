---
description: Windows Portable Devices supports the following task properties.
ms.assetid: 9bd6c2e1-740a-453d-b390-120700af7c93
title: Task Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Task
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Task Properties

Windows Portable Devices supports the following task properties.



| Property                         | VarType        | Description                                                                                 |
|----------------------------------|----------------|---------------------------------------------------------------------------------------------|
| **WPD\_TASK\_OWNER**             | **VT\_LPWSTR** | The owner of the task.                                                                      |
| **WPD\_TASK\_PERCENT\_COMPLETE** | **VT\_UI4**    | A number between 0 and 100 that specifies how complete the task is.                         |
| **WPD\_TASK\_REMINDER\_DATE**    | **VT\_DATE**   | A value that specifies when a reminder should be sent to perform the task, if not complete. |
| **WPD\_TASK\_STATUS**            | **VT\_LPWSTR** | A string description of the status of the task, for example, "In Progress".                 |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




