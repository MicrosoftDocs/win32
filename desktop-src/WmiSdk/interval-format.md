---
description: Defines date-time intervals with a format similar to the date and time syntax by breaking the string into the fields for days, hours, minutes, seconds, and microseconds.
ms.assetid: 13a3ca74-e3e9-44d7-9254-e288eb70ae4c
ms.tgt_platform: multiple
title: Interval Format
ms.topic: article
ms.date: 05/31/2018
---

# Interval Format

WMI defines date-time intervals with a format similar to the date and time syntax by breaking the string into the fields for days, hours, minutes, seconds, and microseconds.

The following example shows the format of a date-time interval.

``` syntax
ddddddddHHMMSS.mmmmmm:000
```

The following table lists the fields of the date-time interval.



| Field    | Description                                                                                                                                                                                                                                  |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dddddddd | Eight digits that represent a number of days (00000000 through 99999999).                                                                                                                                                                    |
| HH       | Two-digit hour of the day that uses the 24-hour clock (00 through 23).                                                                                                                                                                       |
| MM       | Two-digit minute in the hour (00 through 59).                                                                                                                                                                                                |
| SS       | Two-digit number of seconds in the minute (00 through 59).                                                                                                                                                                                   |
| mmmmmm   | Six-digit number of microseconds in the second (000000 through 999999). Your implementation is not required to support evaluation using this field, but this field must always be present to preserve the fixed-length nature of the string. |



 

Intervals always have a trailing ":000" as the last four characters. Further, unlike the date and time, you cannot use asterisks to indicate unused fields. In addition, all properties of type [CIM\_DATETIME](cim-datetime.md) that represent intervals must be marked with the [SubType](standard-wmi-qualifiers.md) standard qualifier, with the qualifier set to "interval".

The following string represents an interval of 1 day, 12 hours, 0 minutes, and 32 seconds.

``` syntax
00000001120032.000000:000
```

## Related topics

<dl> <dt>

[Date and Time Format](date-and-time-format.md)
</dt> <dt>

[About WMI](about-wmi.md)
</dt> <dt>

[CIM\_DATETIME](cim-datetime.md)
</dt> </dl>

 

 



