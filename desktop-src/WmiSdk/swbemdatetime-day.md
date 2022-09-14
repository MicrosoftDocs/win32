---
description: Gets or sets a value that represents the day component of the datetime value.
ms.assetid: 60da99bc-560c-45bc-b787-f4bef8e5a509
ms.tgt_platform: multiple
title: SWbemDateTime.Day property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemDateTime.Day
- ISWbemDateTime.Day
- ISWbemDateTime.get_Day
- ISWbemDateTime.put_Day
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemDateTime.Day property

The **Day** property of the [**SWbemDateTime**](swbemdatetime.md) object gets or sets a value that represents the day component of the datetime value. The value must be in the range of 1 through 31 if [**IsInterval**](swbemdatetime-isinterval.md) is **FALSE**. However, error checking is not sensitive to the month value. Thus, the in-range value of 31 will not return an error in the cases where the [**SWbemDateTime.Month**](swbemdatetime-month.md) value is for a month of fewer than 31 days (February, April, June, September, November).

The default value for **Day** is 01.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read/write.

## Syntax


```VB
SWbemDateTime.Day As Long
```



## Property value

## Error codes

After you get or set the **Day** property, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain the error code below.

<dl> <dt>

**wbemErrValueOutOfRange** - 2147749931 (0x8004102B)
</dt> <dd>

If [**IsInterval**](swbemdatetime-isinterval.md) is **TRUE** and the range of correct values exceeds 0 through 99999999.

</dd> </dl>

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

[**SWbemDateTime.DaySpecified**](swbemdatetime-dayspecified.md)
</dt> <dt>

[**SWbemDateTime**](swbemdatetime.md)
</dt> <dt>

[DATETIME](datetime.md)
</dt> </dl>

 

