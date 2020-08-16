---
title: Backup Functions
description: The following functions are used with tape backup.
ms.assetid: 8c5f92f7-4918-475c-bc86-2b02291488d5
ms.topic: article
ms.date: 05/31/2018
---

# Backup Functions

The following functions are used with [tape backup](tape-backup.md).



| Function                                           | Description                                                                                            |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**BackupRead**](/windows/desktop/api/Winbase/nf-winbase-backupread)                   | Reads data associated with a specified file or directory into a buffer.                                |
| [**BackupSeek**](/windows/desktop/api/Winbase/nf-winbase-backupseek)                   | Seeks forward in a data stream.                                                                        |
| [**BackupWrite**](/windows/desktop/api/Winbase/nf-winbase-backupwrite)                 | Writes a stream of data from a buffer to a specified file or directory.                                |
| [**CreateTapePartition**](/windows/desktop/api/Winbase/nf-winbase-createtapepartition) | Reformats a tape.                                                                                      |
| [**EraseTape**](/windows/desktop/api/Winbase/nf-winbase-erasetape)                     | Erases all or part of a tape.                                                                          |
| [**GetTapeParameters**](/windows/desktop/api/Winbase/nf-winbase-gettapeparameters)     | Retrieves information that describes the tape or the tape drive.                                       |
| [**GetTapePosition**](/windows/desktop/api/Winbase/nf-winbase-gettapeposition)         | Retrieves the current address of the tape.                                                             |
| [**GetTapeStatus**](/windows/desktop/api/Winbase/nf-winbase-gettapestatus)             | Determines whether the tape device is ready to process tape commands.                                  |
| [**PrepareTape**](/windows/desktop/api/Winbase/nf-winbase-preparetape)                 | Prepares the tape to be accessed or removed.                                                           |
| [**SetTapeParameters**](/windows/desktop/api/Winbase/nf-winbase-settapeparameters)     | Specifies the block size of a tape or configures the tape device.                                      |
| [**SetTapePosition**](/windows/desktop/api/Winbase/nf-winbase-settapeposition)         | Sets the tape position on the specified device.                                                        |
| [**WriteTapemark**](/windows/desktop/api/Winbase/nf-winbase-writetapemark)             | Writes a specified number of filemarks, setmarks, short filemarks, or long filemarks to a tape device. |



 

The following functions are provided for working with [single-instance store and SIS backup](single-instance-store-and-sis-backup.md).



| Function                                                          | Description                                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [**SisCreateBackupStructure**](siscreatebackupstructure.md)      | Creates the specified SIS backup structure based on the supplied information.                      |
| [**SisCreateRestoreStructure**](siscreaterestorestructure.md)    | Creates the specified SIS restore structure based on the supplied information.                     |
| [**SisCSFilesToBackupForLink**](siscsfilestobackupforlink.md)    | Returns information describing the common-store files the specified SIS link points to.            |
| [**SisFreeAllocatedMemory**](sisfreeallocatedmemory.md)          | Frees memory allocated by SIS API functions.                                                       |
| [**SisFreeBackupStructure**](sisfreebackupstructure.md)          | Frees the specified SIS backup structure.                                                          |
| [**SisFreeRestoreStructure**](sisfreerestorestructure.md)        | Frees the specified SIS restore structure.                                                         |
| [**SisRestoredCommon StoreFile**](sisrestoredcommonstorefile.md) | Reports to the SIS architecture that a common-store file has been written.                         |
| [**SisRestoredLink**](sisrestoredlink.md)                        | Returns the names of the common-store file or files pointed to by the specified restored SIS link. |



 

The following functions are provided for working with [backup and restore of encrypted files](/windows/desktop/FileIO/backup-and-restore-of-encrypted-files).



| Function                                                | Description                                                                                |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**CloseEncryptedFileRaw**](/windows/desktop/api/winbase/nf-winbase-closeencryptedfileraw) | Close an encrypted file opened with [**OpenEncryptedFileRaw**](/windows/desktop/api/winbase/nf-winbase-openencryptedfilerawa). |
| [**OpenEncryptedFileRaw**](/windows/desktop/api/winbase/nf-winbase-openencryptedfilerawa)   | Open an encrypted file with access to data in encrypted format.                            |
| [**ReadEncryptedFileRaw**](/windows/desktop/api/winbase/nf-winbase-readencryptedfileraw)   | Read an encrypted file leaving its data in encrypted format.                               |
| [**WriteEncryptedFileRaw**](/windows/desktop/api/winbase/nf-winbase-writeencryptedfileraw) | Write an encrypted file leaving its data in encrypted format.                              |



 

 

 