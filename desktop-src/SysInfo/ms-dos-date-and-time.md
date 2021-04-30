---
description: MS-DOS date and MS-DOS time are packed 16-bit values that specify the month, day, year, and time of day an MS-DOS file was last written to.
ms.assetid: 948e6d77-dd01-4c90-9ef0-af143972c3fa
title: MS-DOS Date and Time
ms.topic: article
ms.date: 05/31/2018
---

# MS-DOS Date and Time

**MS-DOS date** and **MS-DOS time** are packed 16-bit values that specify the month, day, year, and time of day an MS-DOS file was last written to. MS-DOS records the date and time whenever an MS-DOS application creates or writes to a file. MS-DOS applications retrieve this date and time using MS-DOS functions. When you use the [**GetFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-getfiletime) function to retrieve the file times for files that were created by MS-DOS, **GetFileTime** automatically converts MS-DOS dates and times to UTC-based times.

If you encounter an MS-DOS date and time that has not been converted, you can convert it to a UTC-based time by using the [**DosDateTimeToFileTime**](/windows/desktop/api/Winbase/nf-winbase-dosdatetimetofiletime) function. This function copies the converted date and time to a [**FILETIME**](/windows/win32/api/minwinbase/ns-minwinbase-filetime) structure. You can convert the value back to an MS-DOS date and time by using the [**FileTimeToDosDateTime**](/windows/desktop/api/Winbase/nf-winbase-filetimetodosdatetime) function.

 

 
