---
title: Srdelayed.exe
description: Applications that perform system state restore operations early in the startup of the operating system may be unable to use the file management functions to move, delete, or set the short name of certain system files.
ms.assetid: cedeb48e-bc1d-48d1-9bee-0b8b0132c3e5
keywords:
- Srdelayed.exe Backup
- system state recovery Backup
ms.topic: article
ms.date: 05/31/2018
---

# Srdelayed.exe

Applications that perform system state restore operations early in the startup of the operating system may be unable to use the file management functions to move, delete, or set the short name of certain system files. Srdelayed.exe is an executable file, provided with the Windows Server Backup (WSB) feature in Windows Server 2008, that can enable system state recovery applications to move, delete, and set the short name of system files.

The Srdelayed tool is intended for system state recovery applications; it does not replace the file management functions. This tool should be used only when the application is unable to move, delete, or set the short name of a system file using the [**MoveFileEx**](/windows/desktop/api/winbase/nf-winbase-movefileexa), [**DeleteFile**](/windows/desktop/api/fileapi/nf-fileapi-deletefilea), and [**SetFileShortName**](/windows/desktop/api/winbase/nf-winbase-setfileshortnamea) functions. During a system state restore and restart, Srdelayed.exe is used by System Restore and the wbadmin.exe command-line tool to move, delete, and set the short name on certain system files. Srdelayed may therefore be useful to developers that require the capability to restore these system files in their own system state recovery applications.

Srdelayed can perform the following operations:

-   A move file operation similar to the [**MoveFileEx**](/windows/desktop/api/winbase/nf-winbase-movefileexa) function with the **MOVEFILE\_DELAY\_UNTIL\_REBOOT** flag
-   A delete file operation similar to the [**DeleteFile**](/windows/desktop/api/fileapi/nf-fileapi-deletefilea) function
-   A set short-name operation similar to the [**SetFileShortName**](/windows/desktop/api/winbase/nf-winbase-setfileshortnamea) function

To use Srdelayed, your application requires the full path to the location of the Srdelayed.exe file and the full path to a Unicode text file that you have authored to contain the information the tool needs to perform all the file management operations being requested. Your application is responsible for ensuring that this text file does not contain redundant requests for an operation and that it handles any required ordering of the file management operations. For example, because a folder must be empty to be deleted, your application needs to ensure that the text file specifies the removal of all files inside the folder before requesting the folder be deleted.

If the **SetupExecute** entry does not already exist in the registry, your application needs to create a **REG\_MULTI\_SZ** type entry named **SetupExecute** under the following registry key: **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**Session Manager**.

Your application should use the following format to set the value of **SetupExecute** to the full path to the location of the Srdelayed.exe file and the full path to the location of the text file. Prefix "\\\\??\\" to the path of the text file, as follows:

*Full Path to Srdelayed.exe* \\\\??\\*Full Path to Text file*  


For example, the following value for **SetupExecute** indicates that the Srdelayed.exe is located in the System32 folder and the text file is named DelayedOperations:

C:\\Windows\\System32\\srdelayed.exe \\\\??\\C:\\temp\\DelayedOperations  


Spaces in the path and name should be hexadecimal encoded. For example, for *Program Files*, encode the path as "\\\\??\\C:Program%20Files\\a.dll".

When the registry or system is being restored upon restart, your application needs to ensure that **SetupExecute** gets written in the correct registry hive. Recovery of the registry is performed before Srdelayed.exe is run. The application needs to write **SetupExecute** into the recovered version of the registry because this is the version that is read.

## Format for the Srdelayed Input File

All the information Srdelayed needs to perform file management operations is specified as a string of Unicode characters in a Unicode text file. The string of Unicode characters is partitioned into records that are themselves each partitioned into four fields. Each record specifies a single move file, delete file, or set short-name operation. The four fields of each record contain the parameters for the operation. Srdelayed.exe performs each operation in the order that their records occur in the string. Your application should check for any duplicate records in this file and remove the duplicates.

The following string illustrates the format for a file requesting two operations and consisting of two records. Each parameter field ends with a single L'\\0' character. A record is composed of four consecutive fields. An additional single L'\\0' character is appended to the end of all records.

`<ParamA1>L'\0'<ParamA2>L'\0'<ParamA3>L'\0'<ParamA4>L'\0'<ParamB1>L'\0'<ParamB2>L'\0'<ParamB3>L'\0'<ParamB4>L'\0'L'\0'`  
`|-----------------------RecordA------------------------|------------------------RecordB------------------------|`  


The meaning of the first, second, third, and fourth parameter fields depends on whether the record describes a move, delete, or set short-name operation.

## Format for a Move File Record

Field 1 identifies this as a request to move a file. The value in this field is always L"MoveFile" and is case sensitive.

Field 2 specifies the source location of the file. The Srdelayed move file operation does not support moving a folder. A file must be specified in this field. The value for this field is the full path of the file appended to "\\\\??\\" unless the path includes a globally unique identifier (GUID), which uses "\\\\?\\" as a prefix. Remove "\\\\?\\" before appending to "\\\\??\\".

Field 3 specifies the destination of the file. The move file operation works only within a volume. The source and destination must be on the same volume. The value for this field is the full path of the file appended to "\\\\??\\" unless the path includes a globally unique identifier (GUID), which uses "\\\\?\\" as a prefix. Remove "\\\\?\\" before appending to "\\\\??\\".

Field 4 receives status information from Srdelayed. The value in this field should be set to L"NotExecuted" for a new record.

The following example references the file by drive path. If the path and name of the source is C:\\Stage\\a.dll, this record requests that Srdelayed move it to C:\\temp\\a.dll.

MoveFile \\\\??\\C:\\Stage\\a.dll \\\\??\\C:\\temp\\a.dll NotExecuted  


The following example references the file by volume GUID path. If the path and name of the source is \\\\?\\Volume{26a21bda-a627-11d7-9931-806e6f6e6963}\\Stage\\a.dll, this record requests that Srdelayed move it to \\\\?\\Volume{26a21bda-a627-11d7-9931-806e6f6e6963}\\temp\\a.dll

 MoveFile \\\\??\\Volume{26a21bda-a627-11d7-9931-806e6f6e6963}\\Stage\\a.dll \\\\??\\Volume{26a21bda-a627-11d7-9931-806e6f6e6963}\\temp\\a.dll NotExecuted  


## Format for a Delete File Record

Field 1 identifies this as a request to delete a file. The value in this field is always L"DeleteFile" and is case sensitive.

Field 2 is unused. The value in this field should be set to L"Unused".

Field 3 specifies the file to be removed. A folder must be empty to be removed. Use delete file operations to remove all files in the folder before removing the folder. The value for this field is the full path of the file appended to "\\\\??\\" unless the path includes a globally unique identifier (GUID), which uses "\\\\?\\" as a prefix. Remove "\\\\?\\" before appending to "\\\\??\\".

Field 4 receives status information from Srdelayed. The value in this field should be set to L"NotExecuted" for a new record.

The following example references the file by drive path. If the path and name is C:\\temp\\b.dll, this record requests that Srdelayed delete the file.

DeleteFile Unused \\\\??\\C:\\temp\\b.dll NotExecuted  


The following example references the file by volume GUID. If the path and name is \\\\?\\Volume{26a21bda-a627-11d7-9931-806e6f6e6963}\\temp\\b.dll, this record requests that Srdelayed remove the file.

DeleteFile Unused \\\\??\\Volume{26a21bda-a627-11d7-9931-806e6f6e6963}\\temp\\b.dll\\ NotExecuted  


## Format for Set Short-Name Record

Field 1 identifies this as a request to set a file's short name. The value in this field is always L"SetFileShortName" and is case sensitive.

Field 2 specifies the short name.

Field 3 field specifies the path and long name to receive the short name. The value for this field is the path and long name of the file appended to "\\\\??\\" unless the path includes a globally unique identifier (GUID), which uses "\\\\?\\" as a prefix. Remove "\\\\?\\" before appending to "\\\\??\\".

Field 4 receives status information from Srdelayed. The value in this field should be set to L"NotExecuted" for a new record.

The following example references the file by drive path. If the path and name of the file is C:\\temp\\ShortFileName.dll, this record requests that the file receive a short name, ShortN~1.dll.

SetFileShortName ShortN~1.dll \\\\??\\C:\\temp\\ShortFileName.dll NotExecuted  


The following example references the file by volume GUID. If the path and name of the file is \\\\?\\Volume{26a21bda-a627-11d7-9931-806e6f6e6963}\\temp\\ShortFileName.dll\\, this record requests that the file receive a short name, ShortN~1.dll.

SetFileShortName ShortN~1.dll \\\\??\\Volume{26a21bda-a627-11d7-9931-806e6f6e6963}\\temp\\ShortFileName.dll\\ NotExecuted  


## Srdelayed Operations Status

Srdelayed writes the string L"SC=*xxxxxxx*" into the fourth field of each record of the text file, where *xxxxxxx* is a hexadecimal that indicates the status of the requested operation. A value of zero indicates the operation succeeded.

Srdelayed creates a registry key named **SystemRestore** under **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows NT**\\**CurrentVersion** to log the outcome of the entire restore operation. If Srdelayed performs all the requested operations with success, the name RestoreStatusResult is written under this key with a zero value. If Srdelayed is unable to perform any of the requested operations, the names RestoreStatusResult and RestoreStatusDetails are written under this key with nonzero values. The name RestoreStatusDetails is written under this key only if Srdelayed is unable to perform any requested operations. If an operation to set the short name of a file is unsuccessful, Srdelayed continues to the next operation. Srdelayed considers the move file and delete file operations to be critical and does not continue if a move or delete operation is unsuccessful.

 

 