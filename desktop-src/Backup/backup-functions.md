---
title: Backup Functions
description: The following functions are used with tape backup.
ms.assetid: '8c5f92f7-4918-475c-bc86-2b02291488d5'
---

# Backup Functions

The following functions are used with [tape backup](tape-backup.md).



| Function                                           | Description                                                                                            |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**BackupRead**](backupread.md)                   | Reads data associated with a specified file or directory into a buffer.                                |
| [**BackupSeek**](backupseek.md)                   | Seeks forward in a data stream.                                                                        |
| [**BackupWrite**](backupwrite.md)                 | Writes a stream of data from a buffer to a specified file or directory.                                |
| [**CreateTapePartition**](createtapepartition.md) | Reformats a tape.                                                                                      |
| [**EraseTape**](erasetape.md)                     | Erases all or part of a tape.                                                                          |
| [**GetTapeParameters**](gettapeparameters.md)     | Retrieves information that describes the tape or the tape drive.                                       |
| [**GetTapePosition**](gettapeposition.md)         | Retrieves the current address of the tape.                                                             |
| [**GetTapeStatus**](gettapestatus.md)             | Determines whether the tape device is ready to process tape commands.                                  |
| [**PrepareTape**](preparetape.md)                 | Prepares the tape to be accessed or removed.                                                           |
| [**SetTapeParameters**](settapeparameters.md)     | Specifies the block size of a tape or configures the tape device.                                      |
| [**SetTapePosition**](settapeposition.md)         | Sets the tape position on the specified device.                                                        |
| [**WriteTapemark**](writetapemark.md)             | Writes a specified number of filemarks, setmarks, short filemarks, or long filemarks to a tape device. |



 

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



 

The following functions are provided for working with [backup and restore of encrypted files](https://msdn.microsoft.com/library/windows/desktop/aa363783).



| Function                                                | Description                                                                                |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**CloseEncryptedFileRaw**](https://msdn.microsoft.com/library/windows/desktop/aa363839) | Close an encrypted file opened with [**OpenEncryptedFileRaw**](https://msdn.microsoft.com/library/windows/desktop/aa365429). |
| [**OpenEncryptedFileRaw**](https://msdn.microsoft.com/library/windows/desktop/aa365429)   | Open an encrypted file with access to data in encrypted format.                            |
| [**ReadEncryptedFileRaw**](https://msdn.microsoft.com/library/windows/desktop/aa365466)   | Read an encrypted file leaving its data in encrypted format.                               |
| [**WriteEncryptedFileRaw**](https://msdn.microsoft.com/library/windows/desktop/aa365746) | Write an encrypted file leaving its data in encrypted format.                              |



 

 

 




