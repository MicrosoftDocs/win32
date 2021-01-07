---
description: The following are hints for interoperating correctly with various file system and security features that were introduced in Windows Vista and Windows Server 2008.
ms.assetid: 3e8a1fd2-59e5-4f18-aafc-0ce5ac1e1cfa
title: Working with File System and Security Features
ms.topic: article
ms.date: 05/31/2018
---

# Working with File System and Security Features

The following are hints for interoperating correctly with various file system and security features that were introduced in Windows Vista and Windows Server 2008.

## Interoperability with Transactions

To support transactions, VSS ensures that both the Kernel Transaction Manager (KTM) and the Distributed Transaction Coordinator (DTC) are frozen prior to the creation of volume shadow copies. If the system fails to freeze or thaw KTM or DTC, the following timeout errors may be returned by the [**IVssBackupComponents::DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset) method:

<dl> VSS\_E\_TRANSACTION\_FREEZE\_TIMEOUT  
VSS\_E\_TRANSACTION\_THAW\_TIMEOUT  
</dl>

If the requester receives one of these error codes, it must retry the shadow copy creation.

Registry and file system operations can also be transacted. In the case of the registry, the registry writer is responsible for ensuring transactional consistency. In the case of Transactional NTFS (TxF) file system operations, the system provider is responsible for ensuring transactional consistency. This is accomplished by mounting the shadow copy as read/write after it is created to allow for auto-recovery. During the auto-recovery phase, KTM rolls back any incomplete transactions.

## Identifying and Creating Hard Links

When backing up files, a backup application must identify all hard links to each file to avoid backing up the same file more than once. Two new functions are available for enumerating hard links: [**FindFirstFileNameW**](/windows/win32/api/fileapi/nf-fileapi-findfirstfilenamew) and [**FindNextFileNameW**](/windows/win32/api/fileapi/nf-fileapi-findnextfilenamew).

Similarly, when restoring files, the backup application must restore hard links using the [**CreateHardLink**](/windows/win32/api/winbase/nf-winbase-createhardlinka) function.

Backup applications must also assert the SE\_BACKUP\_NAME privilege during the backup phase and the SE\_RESTORE\_NAME during the restore phase.

## Permissions and Privileges Required by Backup Applications

Backup applications that restore system files require the following privileges:

<dl> SE\_BACKUP\_NAME  
SE\_RESTORE\_NAME  
SE\_SECURITY\_NAME  
SE\_TAKE\_OWNERSHIP\_NAME  
</dl>

Backup applications must also request WRITE\_OWNER access rights during the restore phase.

## Windows Media Digital Rights Management

Windows Media Digital Rights Management (DRM) client maintains a directory of sensitive state and license files in the %ProgramData%\\Microsoft\\Windows\\DRM directory. The files in this directory should be purged at the same time as temporary and cache files. To ensure that the Windows DRM client remains in a consistent state, you must avoid backing up or restoring these files. This directory is listed in the FilesNotToBackup registry key. For more information about the FilesNotToBackup key, see [Generating a Backup Set](generating-a-backup-set.md).

## User Account Control

The introduction of User Account Control (UAC) in Windows Vista means that unless specified otherwise, applications must run under a standard user account. Additionally, the file and registry virtualization feature of UAC alters the locations where user data is stored. For more information about how to work with UAC and file and registry virtualization, see the following references:

<dl>

[The Windows Vista and Windows Server 2008 Developer Story: Windows Vista Application Development Requirements for User Account Control (UAC)](/previous-versions/aa905330(v=msdn.10))  
[Windows Vista Application Development Requirements for User Account Control Compatibility](/previous-versions/dotnet/articles/bb530410(v=msdn.10))  
[User Account Control (UAC) Patching](../msi/user-account-control--uac--patching.md)  
</dl>

## BitLocker Drive Encryption

BitLocker Drive Encryption is a new feature in Windows Vista Enterprise, Windows Vista Ultimate, and Windows Server 2008 that offers secure startup and full volume encryption. Understanding this feature is important for developers of backup applications that perform offline restores where data may need to be restored onto an encrypted drive.

To restore data onto an encrypted drive, perform the following steps:

1.  Unlock the drive.
2.  Turn off BitLocker Drive Encryption.
3.  Perform the restore.
4.  Boot into the restored operating system and turn on BitLocker Drive Encryption.

For detailed information about BitLocker Drive Encryption, including a step-by-step guide, see [BitLocker Drive Encryption](https://www.microsoft.com/technet/windowsvista/security/bitlockr.mspx) on the Microsoft TechNet Windows Vista website. For information about the BitLocker Drive Encryption WMI provider, see [BitLocker Drive Encryption Provider](../secprov/bitlocker-drive-encryption-provider.md).

 

 
