---
description: Describes time formats supported for use in the WQL WHERE clause.
ms.assetid: d86bd2e3-f5cb-488f-9cd6-5105d82a1842
ms.tgt_platform: multiple
title: WQL-Supported Time Formats
ms.topic: article
ms.date: 05/31/2018
---

# WQL-Supported Time Formats

In addition to the WMI DATETIME format, the following date formats are supported for use in the WQL WHERE clause.



| Format                                    | Description                                                                                                                                                                                            |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| hh\[ \]{AP}M<br/>                   | Hour as shown on a twelve-hour clock, and AM or PM designation.<br/> 4 PM<br/>                                                                                                             |
| hh:mm<br/>                          | Colon-delimited hour and minutes. No AM or PM designation.<br/> 3:23<br/>                                                                                                                  |
| hh:mm\[ \]{AP}M<br/>                | Colon-delimited hour and minutes, optional space, and AM or PM designation.<br/> 3:23 AM<br/>                                                                                              |
| hh:mm:ss<br/>                       | Colon-delimited hour, minutes and seconds. No AM/PM designation.<br/> 3:23:00<br/>                                                                                                         |
| hh:mm:ss\[ \]{AP}M<br/>             | Colon-delimited hour, minutes and seconds, optional space, and AM/PM designation.<br/> 3:23:00PM<br/>                                                                                      |
| hh:mm:ss:uuu<br/>                   | Colon-delimited hour, minutes and seconds, and three-digit offset that indicates the number of minutes that the originating time zone deviates from UTC.<br/>                                    |
| hh:mm:ss:\[\[u\]u\]u<br/>           | Colon-delimited hour, minutes and seconds; and one, two, or three-digit offset that indicates the number of minutes that the originating time zone deviates from UTC.<br/>                       |
| hh:mm:ss:uuu\[ \]{AP}M<br/>         | Colon-delimited hour, minutes and seconds, three-digit offset that indicates the number of minutes that the originating time zone deviates from UTC, and AM or PM designation.<br/>              |
| hh:mm:ss:\[\[u\]u\]u\[ \]{AP}M<br/> | Colon-delimited hour, minutes and seconds; one, two, or three-digit offset that indicates the number of minutes that the originating time zone deviates from UTC; and AM or PM designation.<br/> |



 

## Related topics

<dl> <dt>

[WHERE Clause](where-clause.md)
</dt> </dl>

 

 




