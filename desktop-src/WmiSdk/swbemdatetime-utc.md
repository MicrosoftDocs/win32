---
description: Gets or sets the Coordinated Universal Times (UTC) representation of the datetime value.
ms.assetid: 43d9d0c8-5521-410f-825b-6b00c3dd0039
ms.tgt_platform: multiple
title: SWbemDateTime.UTC property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemDateTime.UTC
- ISWbemDateTime.UTC
- ISWbemDateTime.get_UTC
- ISWbemDateTime.put_UTC
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemDateTime.UTC property

The **UTC** property of the [**SWbemDateTime**](swbemdatetime.md) object gets or sets the Coordinated Universal Times (UTC) representation of the **datetime** value. UTC is the time as set by the World Time Standard. UTC has replaced Greenwich Mean Time (GMT). A UTC value with a zero offset is the same as GMT with a zero offset. The signed number must be in the range of -720 through 720 or the error **wbemErrValueOutOfRange** is returned.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read/write.

## Syntax


```VB
SWbemDateTime.UTC As Long
```



## Property value

## Error codes

After you get or set the **UTC** property, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain the error code below.

<dl> <dt>

**wbemErrValueOutOfRange** - 2147749931 (0x8004102B)
</dt> <dd>

The value was not in the range of -720 through 720.

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

[**SWbemDateTime.UTCSpecified**](swbemdatetime-utcspecified.md)
</dt> <dt>

[**SWbemDateTime**](swbemdatetime.md)
</dt> <dt>

[**DATETIME**](datetime.md)
</dt> </dl>

 

