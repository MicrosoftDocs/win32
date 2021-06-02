---
description: A file time is a 64-bit value that represents the number of 100-nanosecond intervals that have elapsed since 12:00 A.M. January 1, 1601 Coordinated Universal Time (UTC). The system records file times when applications create, access, and write to files.
ms.assetid: 52d80b82-9ab0-4631-9e70-85df21da4946
title: File Times
ms.topic: article
ms.date: 05/31/2018
---

# File Times

A *file time* is a 64-bit value that represents the number of 100-nanosecond intervals that have elapsed since 12:00 A.M. January 1, 1601 Coordinated Universal Time (UTC). The system records file times when applications create, access, and write to files.

The NTFS file system stores time values in UTC format, so they are not affected by changes in time zone or daylight saving time. The FAT file system stores time values based on the local time of the computer. For example, a file that is saved at 3:00pm PST in Washington is seen as 6:00pm EST in New York on an NTFS volume, but it is seen as 3:00pm EST in New York on a FAT volume.

Time stamps are updated at various times and for various reasons. The only guarantee about a file time stamp is that the file time is correctly reflected when the handle that makes the change is closed.

Not all file systems can record creation and last access times, and not all file systems record them in the same manner. For example, the resolution of create time on FAT is 10 milliseconds, while write time has a resolution of 2 seconds and access time has a resolution of 1 day, so it is really the access date. The NTFS file system delays updates to the last access time for a file by up to 1 hour after the last access.

To retrieve the file times for a specified file, use the [**GetFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-getfiletime) function. **GetFileTime** copies the creation, last access, and last write times to individual [**FILETIME**](/windows/win32/api/minwinbase/ns-minwinbase-filetime) structures. You can also retrieve file times using the [**FindFirstFile**](/windows/desktop/api/fileapi/nf-fileapi-findfirstfilea) and [**FindNextFile**](/windows/desktop/api/fileapi/nf-fileapi-findnextfilea) functions. These functions copy the file times to **FILETIME** structures in a [**WIN32\_FIND\_DATA**](/windows/desktop/api/minwinbase/ns-minwinbase-win32_find_dataa) structure. When writing to a file, the last write time is not fully updated until all handles that are used for writing are closed.

To set the file times for a file, use the [**SetFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-setfiletime) function. This function lets you modify creation, last access, and last write times without changing the content of the file. You can compare the times of different files by using the [**CompareFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-comparefiletime) function. The function compares two file times and returns a value that indicates which time is later or returns 0 (zero) if the times are equal.

If you plan to modify file times for specified files, you can convert a date and time of day to a file time by using the [**SystemTimeToFileTime**](/windows/win32/api/timezoneapi/nf-timezoneapi-systemtimetofiletime) function. You can also obtain the system time in a [**FILETIME**](/windows/win32/api/minwinbase/ns-minwinbase-filetime) structure by calling the [**GetSystemTimeAsFileTime**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemtimeasfiletime) function.

To make a file time easy to display to a user, use the [**FileTimeToSystemTime**](/windows/win32/api/timezoneapi/nf-timezoneapi-filetimetosystemtime) function. **FileTimeToSystemTime** converts the file time and copies the month, day, year, and time of day from the file time to a [**SYSTEMTIME**](/windows/win32/api/minwinbase/ns-minwinbase-systemtime) structure.

## File Times and Daylight Saving Time

You must take care when using file times if the user has set the system to automatically adjust for daylight saving time.

To convert a file time to local time, use the [**FileTimeToLocalFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-filetimetolocalfiletime) function. However, **FileTimeToLocalFileTime** uses the current settings for the time zone and daylight saving time. Therefore, if it is daylight saving time, it takes daylight saving time into account, even if the file time you are converting is in standard time.

The FAT file system records times on disk in local time. [**GetFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-getfiletime) retrieves cached UTC times from the FAT file system. When it becomes daylight saving time, the time retrieved by **GetFileTime** is off an hour, because the cache is not updated. When you restart the computer, the cached time that **GetFileTime** retrieves is correct. [**FindFirstFile**](/windows/desktop/api/fileapi/nf-fileapi-findfirstfilea) retrieves the local time from the FAT file system and converts it to UTC by using the current settings for the time zone and daylight saving time. Therefore, if it is daylight saving time, **FindFirstFile** takes daylight saving time into account, even if the file time you are converting is in standard time.

The NTFS file system records times on disk in UTC. To account for daylight saving time when converting a file time to a local time, use the following sequence of functions instead of using [**FileTimeToLocalFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-filetimetolocalfiletime):

-   [**FileTimeToSystemTime**](/windows/win32/api/timezoneapi/nf-timezoneapi-filetimetosystemtime)
-   [**SystemTimeToTzSpecificLocalTime**](/windows/win32/api/timezoneapi/nf-timezoneapi-systemtimetotzspecificlocaltime)
-   [**SystemTimeToFileTime**](/windows/win32/api/timezoneapi/nf-timezoneapi-systemtimetofiletime)

## File Times and CDFS

The date and time stamps of files that are located on or originate from media using Compact Disc File System (CDFS) are adjusted for the local time zone. ISO 9660 states that CDFS is to display the date information correctly for the local time zone. This is done so that dates for files on CDFS are displayed the same as those on Universal Disk Format (UDF). UDF is the newer standard for distribution media. If your code depends on the unmodified date information for a file that resides on or originates from media using CDFS, it may not function correctly.

 

 
