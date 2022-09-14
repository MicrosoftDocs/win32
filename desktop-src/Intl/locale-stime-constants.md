---
description: LOCALE\_STIME\* Constants
ms.assetid: d16e7e0c-93f1-4f08-a319-02b717b7d33b
title: LOCALE_STIME* Constants
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_STIME\* Constants

This topic defines the LOCALE\_STIME\* constants used by NLS.



| Value               | Meaning                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOCALE\_STIME       | Character(s) for the time separator. The maximum number of characters allowed for this string is four, including a terminating null character. <br/> **Windows Vista and later:** This constant is deprecated. Use LOCALE\_STIMEFORMAT instead. A custom locale might not have a single, uniform separator character. For example, a format such as "03:56'23" is valid.<br/> |
| LOCALE\_STIMEFORMAT | Time formatting strings for the locale. The maximum number of characters allowed for this string is 80, including a terminating null character. The string can consist of a combination of [hour, minute, and second format pictures](hour--minute--and-second-format-pictures.md).                                                                                                      |



 

 

 




