---
description: LOCALE\_SMON\* Constants
ms.assetid: df7f026b-2f2d-420f-8a14-656734409835
title: LOCALE_SMON* Constants
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_SMON\* Constants

This topic defines the LOCALE\_SMON\* constants used by NLS in representing monetary values.



| Value                   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOCALE\_SMONDECIMALSEP  | Character(s) used as the monetary decimal separator. The maximum number of characters allowed for this string is four, including a terminating null character. For example, if a monetary amount is displayed as "$3.40", just as "three dollars and forty cents" is displayed in the United States, then the monetary decimal separator is ".".                                                                                                                                             |
| LOCALE\_SMONGROUPING    | Sizes for each group of monetary digits to the left of the decimal. The maximum number of characters allowed for this string is ten, including a terminating null character. An explicit size is needed for each group, and sizes are separated by semicolons. If the last value is 0, the preceding value is repeated. For example, to group thousands, specify 3;0. Indic languages group the first thousand and then group by hundreds. For example 12,34,56,789 is represented by 3;2;0. |
| LOCALE\_SMONTHOUSANDSEP | Character(s) used as the monetary separator between groups of digits to the left of the decimal. The maximum number of characters allowed for this string is four, including a terminating null character. Typically, the groups represent thousands. However, depending on the value specified for LOCALE\_SMONGROUPING, they can represent something else.                                                                                                                                 |



 

 

 



