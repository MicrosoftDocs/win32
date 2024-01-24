---
description: The application uses the elements described in this topic to construct a null-terminated format picture string.
ms.assetid: c18868a9-6912-46fd-93f5-d8021937b049
title: Day, Month, Year, and Era Format Pictures
ms.topic: article
ms.date: 05/31/2018
---

# Day, Month, Year, and Era Format Pictures

The application uses the elements described in this topic to construct a null-terminated format picture string. If spaces are used to separate the elements in the string, these spaces will appear in the same location in the output string.

> [!Note]  
> The format types "d", "g", and "y" must be lowercase and the letter "M" must be uppercase.

 

For example, to get the date string "Wed, Aug 31 94", the application uses the picture string "ddd',' MMM dd yy".

The application uses single quotation marks to mark characters to display exactly as specified. If the application must display a single quotation mark, it should place two single quotation marks in a row. For example, 'abc''bar', is displayed as "abc'bar".

The following table defines the format types used to represent days.



| Format type | Meaning                                                                                                                                                                                                                                                                                                                                                                   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| d           | Day of the month as digits without leading zeros for single-digit days.                                                                                                                                                                                                                                                                                                   |
| dd          | Day of the month as digits with leading zeros for single-digit days.                                                                                                                                                                                                                                                                                                      |
| ddd         | Abbreviated day of the week as specified by a [LOCALE\_SABBREVDAYNAME\*](locale-sabbrev-constants.md) value, for example, "Mon" in English (United States).**Windows Vista and later:** If a short version of the day of the week is required, your application should use the [LOCALE\_SSHORTESTDAYNAME\*](locale-sshortestdayname-constants.md) constants.<br/> |
| dddd        | Day of the week as specified by a [LOCALE\_SDAYNAME\*](locale-sdayname-constants.md) value.                                                                                                                                                                                                                                                                              |



 

The following table defines the format types used to represent months.



| Format type | Meaning                                                                                                                                                                          |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| M           | Month as digits without leading zeros for single-digit months.                                                                                                                   |
| MM          | Month as digits with leading zeros for single-digit months.                                                                                                                      |
| MMM         | Abbreviated month as specified by a [LOCALE\_SABBREVMONTHNAME\*](locale-sabbrev-constants.md) value, for example, "Nov" in English (United States).                             |
| MMMM        | Month as specified by a [LOCALE\_SMONTHNAME\*](locale-smonthname-constants.md) value, for example, "November" for English (United States), and "Noviembre" for Spanish (Spain). |



 

The following table defines the format types used to represent years.



| Format type | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| y           | Year represented only by the last digit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| yy          | Year represented only by the last two digits. A leading zero is added for single-digit years.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| yyyy        | Year represented by a full four or five digits, depending on the calendar used. Thai Buddhist and Korean calendars have five-digit years. The "yyyy" pattern shows five digits for these two calendars, and four digits for all other supported calendars. Calendars that have single-digit or two-digit years, such as for the Japanese Emperor era, are represented differently. A single-digit year is represented with a leading zero, for example, "03". A two-digit year is represented with two digits, for example, "13". No additional leading zeros are displayed. |
| yyyyy       | Behaves identically to "yyyy".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |



 

The following table defines the format types used to represent a period or era.



| Format type | Meaning                                                                                                                                                                              |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| g, gg       | Period/era string formatted as specified by the CAL\_SERASTRING value. The "g" and "gg" format pictures in a date string are ignored if there is no associated era or period string. |



 

 

 




