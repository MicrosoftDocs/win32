---
title: Tape Input and Output
description: There are several functions that applications can use to perform input and output (I/O) on a tape drive. Tape I/O is similar to I/O performed on a communications device.
ms.assetid: 1862c267-0070-4fe8-bb77-40167913978a
keywords:
- tape input and output Backup
ms.topic: article
ms.date: 05/31/2018
---

# Tape Input and Output

There are several functions that applications can use to perform input and output (I/O) on a tape drive. Tape I/O is similar to I/O performed on a communications device.

When performing tape I/O, some tape drives store tape firmware information in the first few blocks on a tape, typically using some portion of the first 100 blocks. Applications should not use those blocks. More specific information on this subject is available from individual tape system manufacturers. In general, an application that skips the first 100 blocks on a tape will avoid tape drive idiosyncrasies.

The [**GetTapePosition**](/windows/desktop/api/Winbase/nf-winbase-gettapeposition) and [**SetTapePosition**](/windows/desktop/api/Winbase/nf-winbase-settapeposition) functions retrieve and move the current tape position. The [**WriteTapemark**](/windows/desktop/api/Winbase/nf-winbase-writetapemark) function writes a specified number of setmarks, filemarks, short filemarks, and long filemarks. The [**EraseTape**](/windows/desktop/api/Winbase/nf-winbase-erasetape) function erases all or part of a tape.

The [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) and [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile) functions read and write file data from and to the tape. The data is read and written in complete blocks. If the tape's block size is 512 bytes, all read and write operations must use buffers that are simple integer multiples of that block size: 512, 1024, 1536, 2048, and so on. Most, if not all, drives only allow a write operation after the tape is rewound or after a read operation produces an end-of-data error message.

To read or write file data to or from a tape in variable-length block mode, perform the following steps:

1.  Determine whether the tape drive supports variable-length block mode by calling the [**GetTapeParameters**](/windows/desktop/api/Winbase/nf-winbase-gettapeparameters) function and checking the TAPE\_DRIVE\_VARIABLE\_BLOCK bit of the **FeaturesLow** member of the returned [**TAPE\_GET\_DRIVE\_PARAMETERS**](/windows/desktop/api/Winnt/ns-winnt-tape_get_drive_parameters) structure.
2.  Specify the variable block size mode by calling the [**SetTapeParameters**](/windows/desktop/api/Winbase/nf-winbase-settapeparameters) function, setting the **BlockSize** member of the [**TAPE\_SET\_MEDIA\_PARAMETERS**](/windows/desktop/api/Winnt/ns-winnt-tape_set_media_parameters) structure to zero. Then, use [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) or [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile) to read or write the file data.

If [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) encounters a filemark, the data up to the filemark is read and the function fails. (The [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function returns an error code indicating the type of filemark that was encountered.) The operating system moves the tape past the filemark, and an application can call **ReadFile** again to continue reading.

[**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) and [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile) read and write only the data stream. The [**BackupRead**](/windows/desktop/api/Winbase/nf-winbase-backupread) and [**BackupWrite**](/windows/desktop/api/Winbase/nf-winbase-backupwrite) functions read and write all the streams associated with a file. These include data, extended attributes, security, and alternative data streams. The security and alternate data streams are relevant only on the NTFS file system partition.

The [**BackupSeek**](/windows/desktop/api/Winbase/nf-winbase-backupseek) function seeks forward in a file initially accessed by [**BackupRead**](/windows/desktop/api/Winbase/nf-winbase-backupread) or [**BackupWrite**](/windows/desktop/api/Winbase/nf-winbase-backupwrite). This function enables an application to skip information that causes access errors.

If an application needs to access only the file data, it should use [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) and [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile). These functions can also read alternative data streams if the streams were created by using the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function.

A tape-backup application must use [**BackupRead**](/windows/desktop/api/Winbase/nf-winbase-backupread) and [**BackupWrite**](/windows/desktop/api/Winbase/nf-winbase-backupwrite) to copy all information pertaining to a file. However, these functions do not read or write file characteristics such as attributes, file creation time, and so on. Applications must use the file input and output functions, such as [**GetFileAttributes**](/windows/desktop/api/fileapi/nf-fileapi-getfileattributesa) and [**SetFileAttributes**](/windows/desktop/api/fileapi/nf-fileapi-setfileattributesa), to retrieve and set those values.

 

 