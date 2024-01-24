---
description: The HoursSpecified property of the SWbemDateTime object is a Boolean value that indicates whether the hours component in the CIM datetime value contains an interval or a wildcard value.
ms.assetid: 55211da6-cbd5-4e61-ab7d-ee20363e9d81
ms.tgt_platform: multiple
title: SWbemDateTime.HoursSpecified property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemDateTime.HoursSpecified
- ISWbemDateTime.HoursSpecified
- ISWbemDateTime.get_HoursSpecified
- ISWbemDateTime.put_HoursSpecified
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemDateTime.HoursSpecified property

The **HoursSpecified** property of the [**SWbemDateTime**](swbemdatetime.md) object is a Boolean value that indicates whether the hours component in the CIM datetime value contains an interval or a wildcard value. If **HoursSpecified** is **TRUE** and [**IsInterval**](swbemdatetime-isinterval.md) is **FALSE**, then [**SWbemDateTime.Hours**](swbemdatetime-hours.md) contains a datetime value. A datetime value that contains an interval cannot be converted into either the **VT\_DATE** format or the **FILETIME** format. If **HoursSpecified** is **FALSE** and **IsInterval** is **TRUE**, then **SWbemDateTime.Hours** contains an interval.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read/write.

## Syntax


```VB
SWbemDateTime.HoursSpecified As Boolean
```



## Property value

## Examples

For examples of using the [**SWbemDateTime**](swbemdatetime.md) object to convert CIM [**DATETIME**](datetime.md) values to and from either the **FILETIME** format or the **VT\_DATE** format, see [WMI Tasks: Dates and Times](wmi-tasks--dates-and-times.md). For a description of the CIM **DATETIME** format, see [Date and Time Format](date-and-time-format.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemDateTime<br/>                                                         |
| IID<br/>                      | IID\_ISWbemDateTime<br/>                                                          |



## See also

<dl> <dt>

[**SWbemDateTime.Hours**](swbemdatetime-hours.md)
</dt> <dt>

[**SWbemDateTime**](swbemdatetime.md)
</dt> <dt>

[DATETIME](datetime.md)
</dt> </dl>

 

 




