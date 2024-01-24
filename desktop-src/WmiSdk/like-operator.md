---
description: The LIKE operator determines whether or not a character string matches a specified pattern.
ms.assetid: 6cafe696-891d-4b17-8802-4b872f76fc78
ms.tgt_platform: multiple
title: LIKE Operator
ms.topic: article
ms.date: 05/31/2018
---

# LIKE Operator

The LIKE operator determines whether or not a character string matches a specified pattern. The specified pattern can contain exactly the characters to match, or it can contain meta characters. In effect, the LIKE operator matches substrings using the wildcard characters in the following table.



| Character       | Description                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \[ \]           | Any one character within the specified range (\[a-f\]) or set (\[abcdef\]).                                                                                                                 |
| ^               | Any one character not within the range (\[^a-f\]) or set (\[^abcdef\].)                                                                                                                     |
| %               | Any string of 0 (zero) or more characters. The following example finds all instances where "Win" is found anywhere in the class name: `SELECT * FROM meta_class WHERE __Class LIKE "%Win%"` |
| \_ (underscore) | Any one character. Any literal underscore used in the query string must be escaped by placing it inside \[\] (square brackets).                                                             |



 

For example, the following Power shell code retrieves all instances of the **Win32\_operatingSystem** class whose **Name** property begins with **FirstName**:

`Get-WmiObject win32_computerSystem -filter "Name LIKE 'FirstName%'"`

Because the underscore is a meta character, if the query target has an underscore, the "\[\]" escape characters must surround it. For example, you can query for all the classes that have a double underscore in the name.

To locate all classes with a double underscore in the name, you must escape both underscores with \[\] (square brackets), for example:

`SELECT * FROM meta_class WHERE __CLASS LIKE "%[_][_]%"`

You can negate a LIKE statement using NOT; to do so, be sure to place the NOT directly in front of the field name. For example:

`  Get-WmiObject -computerName "." -query 'Select * FROM Win32_Printer WHERE Local="TRUE"      AND Network ="False" AND DriverName LIKE "%HP%"      AND NOT PortName LIKE "%10.%" AND NOT PortName LIKE "%\\%"'`

## Related topics

<dl> <dt>

[WQL Operators](wql-operators.md)
</dt> </dl>

 

 



