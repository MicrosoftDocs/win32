---
description: Gets or sets the raw CIM date in the DMTF (Distributed Management Task Force) format.
ms.assetid: 426a60d5-c364-406e-8346-049a13d59c7f
ms.tgt_platform: multiple
title: SWbemDateTime.Value property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemDateTime.Value
- ISWbemDateTime.Value
- ISWbemDateTime.get_Value
- ISWbemDateTime.put_Value
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemDateTime.Value property

The **Value** property of the [**SWbemDateTime**](swbemdatetime.md) object gets or sets the raw CIM date in the DMTF (Distributed Management Task Force) format. The DMTF format is a string representation of the [**DATETIME**](datetime.md) value. This property is the default property for **SWbemDateTime** objects. The **Value** property has a default value of 00000101000000.000000+000.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read/write.

## Syntax


```VB
SWbemDateTime.Value As String
```



## Property value

## Error codes

After you get or set the **Value** property, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain the error code below.

<dl> <dt>

**wbemErrInvalidSyntax** - 2147749921 (0x80041021)
</dt> <dd>

The format of *strValue* is not valid.

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

[**SWbemDateTime**](swbemdatetime.md)
</dt> <dt>

[**DATETIME**](datetime.md)
</dt> </dl>

 

