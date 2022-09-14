---
description: You can access all Common Information Model (CIM) dates and times in WMI by using one of two fixed-length formats specific to WMI and CIM. In scripting, use the SWbemDateTime object to convert these to regular dates and times.
ms.assetid: 15126802-82f9-4ab4-98d8-0a15184302e9
ms.tgt_platform: multiple
title: CIM_DATETIME
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# CIM\_DATETIME

You can access all [*Common Information Model (CIM)*](gloss-c.md) dates and times in WMI by using one of two fixed-length formats specific to WMI and CIM. In scripting, use the [**SWbemDateTime**](swbemdatetime.md) object to convert these to regular dates and times.

The following sections describe how to use the WMI date and time formats.

## Format

The following table lists the two date and time formats used by WMI.



| Format                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DATETIME](datetime.md)<br/> *yyyymmddHHMMSS.mmmmmmsUUU*<br/>                             | Format in which CIM [**DATETIME**](datetime.md) values are stored. This format is locale-independent so you can write a script that runs on any machine. You must use this format to define a date and time in [*Managed Object Format (MOF)*](gloss-m.md), or when writing to an instance using the [COM API for WMI](com-api-for-wmi.md) or the [Scripting API for WMI](scripting-api-for-wmi.md). For more information, see [Modifying an Instance Property](modifying-an-instance-property.md). |
| Format valid only in WMI Query Language (WQL) queries.<br/> *yyyy-mm-dd HH:MM:SS:mmm*<br/> | This format can be used in scripts that use the [**SWbemDateTime**](swbemdatetime.md) methods. For more information, see [Querying WMI](querying-wmi.md) or [Querying with WQL](querying-with-wql.md). This format is not independent of locale. The order of year, month, and day depends on the regional and language format setting of the user session. For example, while the default for United States English is "mm-dd-yyyy hh:mm:ss:mmm", the format for most other countries or regions is "yyyy-mm-dd hh:mm:ss:mmm".       |



 

The following table lists the fields in the formats.



| Field    | Description                                                                                                                                                                                                                                     |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *yyyy*   | Four-digit year (0000 through 9999). Your implementation can restrict the supported range. For example, an implementation can support only the years 1980 through 2099.                                                                         |
| *mm*     | Two-digit month (01 through 12).                                                                                                                                                                                                                |
| *dd*     | Two-digit day of the month (01 through 31). This value must be appropriate for the month. For example, February 31 is not valid. However, your implementation does not have to check for valid data.                                            |
| *HH*     | Two-digit hour of the day using the 24-hour clock (00 through 23).                                                                                                                                                                              |
| *MM*     | Two-digit minute in the hour (00 through 59).                                                                                                                                                                                                   |
| *SS*     | Two-digit number of seconds in the minute (00 through 59).                                                                                                                                                                                      |
| *mmmmmm* | Six-digit number of microseconds in the second (000000 through 999999). Your implementation does not have to support evaluation using this field. However, this field must always be present to preserve the fixed-length nature of the string. |
| *mmm*    | Three-digit number of milliseconds in the minute (000 through 999).                                                                                                                                                                             |
| *s*      | Plus sign (+) or minus sign (-) to indicate a positive or negative offset from Coordinated Universal Times (UTC).                                                                                                                               |
| *UUU*    | Three-digit offset indicating the number of minutes that the originating time zone deviates from UTC. For WMI, it is encouraged, but not required, to convert times to GMT (a UTC offset of zero).                                              |



 

You must enter all fields with the indicated length, using leading zeros as appropriate for the type. However, use asterisks to indicate unused fields or as a wildcard value. You can use an asterisk (\*) everywhere except the **WHERE** clause of a query. For example, a date and time with an unspecified year can occur in any year. If you wish to leave a field unspecified, you must replace the entire field with asterisks.

The following examples describe valid and invalid uses of asterisks:

-   19980416\*\*\*\*\*\*.000000+\*\*\* (Legal)
-   1998-04-16 \*\*\*\*\*\*:\*\*\* (Illegal)
-   199\*0416\*\*\*\*\*\*.000000+\*\*\* (Illegal)
-   199\*-04-16 \*\*\*\*\*\*:\*\*\* (Illegal)

If a datetime is used to represent a specific point in time, all of its fields should include data. If it is used to represent a range of time, only the fields necessary to convey the duration should include data.

The following example describes "April first": a date relative to some unspecified year but still a defined point if the level of measurement detail is one day.

-   \*\*\*\*0401\*\*\*\*\*\*.000000+\*\*\*
-   \*\*\*\*-04-01 \*\*\*\*\*\*:\*\*\* (Illegal)

## Setting UTC Offset and GMT

The following examples describe how you can define a time with no time zone by placing asterisks in the UUU field after either the plus or minus sign:

-   19980401135809.000000+\*\*\*
-   19980401135809.000000-\*\*\*
-   1998-04-01 13:58:09:\*\*\* (Illegal)

An application interprets an unzoned date and time reference to a local, abstract chronometer within the executing operating system. For example, portable computers can have internal clocks whose settings may or may not correspond to the geographical time zone. You can interpret unzoned time by substituting the time zone of the current abstract time source rather than the local time zone.

You should give special consideration to the meaning of the UTC offset with dates and times in queries. In general, equivalence, greater-than, or less-than comparisons work between two dates and times if the dates and times use the same UTC offset. When dealing with dates and times that occur with different time zone offsets, you should first convert the dates and times to GMT.

Queries that involve relative dates and times with asterisks in one or more subfields are only meaningful to WMI when compared for equivalence. Further, WMI does not allow using asterisks as wildcards. Instead, WMI compares relative dates and times on a character-for-character basis.

The following examples describe two dates that a WMI query does not consider equal:

-   19980401135809.000000+\*\*\*
-   19980401135809.000000+000

## Converting to FILETIME or VT\_DATE format

The CIM [**DATETIME**](datetime.md) format is used only within WMI. You can convert to and from the WMI format and either the FILETIME or VT\_DATE format by calling the methods of the [**SWbemDateTime**](swbemdatetime.md) scripting object. A [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime) **datetime** structure is a 64-bit value that the 32-bit Windows operating systems use. VT\_DATE format is an automation variant datetime value used by Visual Basic and ActiveX. The following table lists the conversion methods.



| Method                                                         | Description                                                                                           |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**SWbemDateTime.GetFileTime**](swbemdatetime-getfiletime.md) | Gets a [**DATETIME**](datetime.md) value in [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime) format.                |
| [**SWbemDateTime.GetVarDate**](swbemdatetime-getvardate.md)   | Gets a [**DATETIME**](datetime.md) value in VT\_DATE format.                                         |
| [**SWbemDateTime.SetFileTime**](swbemdatetime-setvardate.md)  | Sets a [**DATETIME**](datetime.md) property using a [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime) date as input. |
| [**SWbemDateTime.SetVarDate**](swbemdatetime-setvardate.md)   | Sets a [**DATETIME**](datetime.md) property using a VT\_DATE date as input.                          |



 

## Related topics

<dl> <dt>

[Date and Time Format](date-and-time-format.md)
</dt> <dt>

[About WMI](about-wmi.md)
</dt> <dt>

[WMI Tasks: Dates and Times](wmi-tasks--dates-and-times.md)
</dt> <dt>

[Interval Format](interval-format.md)
</dt> <dt>

[**SWbemObject.Put\_**](swbemobject-put-.md)
</dt> <dt>

[**SWbemServicesEx.Put**](swbemservicesex-put.md)
</dt> <dt>

[**SWbemDateTime**](swbemdatetime.md)
</dt> <dt>

[**IWbemClassObject::Put**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-put)
</dt> <dt>

[**IWbemServices::PutClass**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putclass)
</dt> </dl>

 

