---
description: Gets or sets a value that represents the microseconds component of the datetime value.
ms.assetid: b810b781-86a3-4730-8114-44d10454f7c3
ms.tgt_platform: multiple
title: SWbemDateTime.Microseconds property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemDateTime.Microseconds
- ISWbemDateTime.Microseconds
- ISWbemDateTime.get_Microseconds
- ISWbemDateTime.put_Microseconds
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemDateTime.Microseconds property

The **Microseconds** property of the [**SWbemDateTime**](swbemdatetime.md) object gets or sets a value that represents the microseconds component of the datetime value.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read/write.

## Syntax


```VB
SWbemDateTime.Microseconds As Long
```



## Property value

## Error codes

After you get or set the **Microseconds** property, the **Err** object may contain the error code below.

<dl> <dt>

**wbemErrValueOutOfRange** - 2147749931 (0x8004102B)
</dt> <dd>

The value was not in the range of 0 through 999999.

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

[**SWbemDateTime.MicrosecondsSpecified**](swbemdatetime-microsecondsspecified.md)
</dt> <dt>

[**SWbemDateTime**](swbemdatetime.md)
</dt> <dt>

[**DATETIME**](datetime.md)
</dt> </dl>

 

 




