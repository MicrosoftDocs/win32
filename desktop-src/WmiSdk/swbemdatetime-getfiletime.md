---
description: Converts a date and time value in the CIM DATETIME format to the FILETIME format.
ms.assetid: 08e0761d-e735-454a-8429-2bd1eb331123
ms.tgt_platform: multiple
title: SWbemDateTime.GetFileTime method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemDateTime.GetFileTime
- ISWbemDateTime.GetFileTime
- ISWbemDateTime.GetFileTime
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemDateTime.GetFileTime method

The **GetFileTime** method of the [**SWbemDateTime**](swbemdatetime.md) object converts a date and time value in the CIM [DATETIME](datetime.md) format to the FILETIME format.

If the parameter is set to **TRUE**, then the return value represents a local time for the client. Otherwise, the return value is a Coordinated Universal Time (UTC) time. A **FILETIME** [DATETIME](datetime.md) structure is a 64-bit value that represents the number of 100-nanosecond units since the beginning of January 1, 1601. Windows Management Instrumentation (WMI) treats **FILETIME** values as string representations of unsigned 64-bit numbers.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
vDate = .GetFileTime( _
  [ ByVal bIsLocaL ] _
)
```



## Parameters

<dl> <dt>

*bIsLocaL* \[in, optional\]
</dt> <dd>

Indicates whether the returned value is interpreted as local time. The UTC property then contains the local time converted to the correct Coordinated Universal Times (UTC) offset. If the value is **FALSE**, then the value is interpreted as UTC with a zero (0) offset.

</dd> </dl>

## Return value

The date and time in the **FILETIME** format.

## Error codes

After completing the **GetFileTime** method, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain the error code in the following list.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

The call failed.

</dd> </dl>

## Remarks

**VT\_DATE** and **FILETIME** values cannot contain wildcard fields.

The **GetFileTime** method fails (wbemErrFailed) if any of the following properties are **FALSE**:

-   [**YearSpecified**](swbemdatetime-yearspecified.md)
-   [**MonthSpecified**](swbemdatetime-monthspecified.md)
-   [**DaySpecified**](swbemdatetime-dayspecified.md)
-   [**HoursSpecified**](swbemdatetime-hoursspecified.md)
-   [**MinutesSpecified**](swbemdatetime-minutesspecified.md)
-   [**SecondsSpecified**](swbemdatetime-secondsspecified.md)
-   [**MicrosecondsSpecified**](swbemdatetime-microsecondsspecified.md)
-   [**UTCSpecified**](swbemdatetime-utcspecified.md)

On a successful return from [**SetFileTime**](swbemdatetime-setfiletime.md), all of these properties are set to **TRUE**.

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

[**SWbemDateTime.GetVarDate**](swbemdatetime-getvardate.md)
</dt> <dt>

[**SWbemDateTime**](swbemdatetime.md)
</dt> <dt>

[**DATETIME**](datetime.md)
</dt> </dl>

 

