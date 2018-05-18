---
title: FMAPI Functions
description: The following functions are used with FMAPI.
ms.assetid: 'f992b2d0-a132-487a-9e9d-fac359acc766'
---

# FMAPI Functions

The following functions are used with FMAPI.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 



| Function                                                     | Description                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CloseFileRestoreContext**](closefilerestorecontext.md)   | Closes the context that is used to restore files and unlocks the volume of the file system if it was locked.                                                                                                                                                                                                  |
| [**CreateFileRestoreContext**](createfilerestorecontext.md) | Initializes the context that is used to restore files. The context can be created for an existing recognized volume or for an unrecognized (lost) volume.                                                                                                                                                     |
| [**DetectBootSector**](detectbootsector.md)                 | Validates the correctness of the volume boot sector and provides data that is used to access the internal on-disk structures of the file system.                                                                                                                                                              |
| [**DetectEncryptedVolume**](detectencryptedvolume.md)       | Determines if the volume is encrypted with BitLocker technology and if it is encrypted, the function determines if it is unlocked.                                                                                                                                                                            |
| [**DetectEncryptedVolumeEx**](detectencryptedvolumeex.md)   | Determines whether the volume is encrypted with BitLocker technology. If the volume is encrypted, the function determines whether it is unlocked. This function is identical to the [**DetectEncryptedVolume**](detectencryptedvolume.md) function, except that it has an additional *VolumeSize* parameter. |
| [**RestoreFile**](restorefile.md)                           | Copies a removed or regular file from a volume that is defined in the file restore context to a new file on an available logical drive.                                                                                                                                                                       |
| [**ScanRestorableFiles**](scanrestorablefiles.md)           | Identifies all files that are available to be restored.                                                                                                                                                                                                                                                       |
| [**SupplyDecryptionInfo**](supplydecryptioninfo.md)         | Provides the full path for a file that contains a decryption key and provides a BitLocker information block that is stored in Active Directory.                                                                                                                                                               |



 

 

 




