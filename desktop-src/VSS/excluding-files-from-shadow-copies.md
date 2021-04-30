---
description: In Windows Vista and Windows Server 2008 and later, the developer of a VSS writer or application may choose to exclude certain files from shadow copies.
ms.assetid: 4fe1ae94-7b2f-421a-9009-3a7e88822458
title: Excluding Files from Shadow Copies
ms.topic: article
ms.date: 05/31/2018
---

# Excluding Files from Shadow Copies

In Windows Vista and Windows Server 2008 and later, the developer of a VSS writer or application may choose to exclude certain files from shadow copies.

The performance impact and shadow copy storage area (also called "diff area") usage of a file in a shadow copy are directly related to the amount of change in the file's contents after the shadow copy is created. In addition, excluding files from shadow copies may slow down shadow copy creation.

For these reasons, a file should be excluded from shadow copies only if it is large, undergoes significant change between one shadow copy and the next, and does not need to be backed up.

You should only exclude files that belong to your application.

If the VSS\_VOLSNAP\_ATTR\_NO\_AUTORECOVERY flag is set in the shadow copy context, this means that auto-recovery is disabled, and no files can be excluded from the shadow copy. For more information, see the [**\_VSS\_VOLUME\_SNAPSHOT\_ATTRIBUTES**](/windows/desktop/api/Vss/ne-vss-vss_volume_snapshot_attributes) enumeration.

## Using the AddExcludeFilesFromSnapshot Method

A VSS writer can exclude files from a shadow copy as follows:

1.  Call the [**IVssCreateWriterMetadataEx::AddExcludeFilesFromSnapshot**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadataex-addexcludefilesfromsnapshot) method to report the files to be excluded.
2.  In the writer's [**CVssWriter::OnPostSnapshot**](/windows/desktop/api/VsWriter/nf-vswriter-cvsswriter-onpostsnapshot) method, delete the files from the shadow copy.

## Using the FilesNotToSnapshot Registry Key

> [!Note]  
> The **FilesNotToSnapshot** registry key is intended to be used only by applications. Users who attempt to use it will encounter limitations such as the following:
>
> -   It cannot delete files from a shadow copy that was created on a Windows Server by using the Previous Versions feature.
> -   It cannot delete files from shadow copies for shared folders.
> -   It can delete files from a shadow copy that was created by using the [DiskShadow](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc772172(v=ws.11)) utility, but it cannot delete files from a shadow copy that was created by using the [Vssadmin](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc754968(v=ws.11)) utility.
> -   Files are deleted from a shadow copy on a best-effort basis. This means that they are not guaranteed to be deleted.

 

A VSS application can delete files from a shadow copy during shadow copy creation by using the following registry key:

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\BackupRestore\\FilesNotToSnapshot**

This registry key has REG\_MULTI\_SZ values for each application whose files can be excluded. The files are specified by fully qualified paths, which can contain the \* wildcard.

In all cases, the entry is ignored if there are no files that match the path string.

After a file is added to the appropriate registry key value, it is deleted from the shadow copy during creation by the shadow copy optimization writer on a best-effort basis.

If a fully qualified path cannot be specified, then a path can also be implied by using the $UserProfile$ or $AllVolumes$ variable. For example:

-   $UserProfile$\\Directory\\Subdirectory\\FileName.\*
-   $AllVolumes$\\TemporaryFiles\\\*.\*

To make the path recursive, append " /s" to the end. For example:

-   $UserProfile$\\Directory\\Subdirectory\\FileName.\* /s
-   $AllVolumes$\\TemporaryFiles\\\*.\* /s

The $UserProfile$ variable causes the path string to be applied to all user profiles on the computer. The user profiles are enumerated by examining the following registry key:

**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList**

The $AllVolumes$ variable causes the path string to be applied to all shadow copies on the computer. For example, suppose the path is "$AllVolumes$\\TemporaryFiles\\\*.\* /s", and the computer has three volumes: C:, D:, and E:. If C: and E: contain the path "\\TemporaryFiles\\", and volume D: contains only the path D:\\Data\\, the directory tree C:\\TemporaryFiles\\ is deleted from shadow copies of C:, and the directory tree E:\\TemporaryFiles\\ is deleted from shadow copies of E:.

Administrators can disable expansion of the $UserProfile$ variable by using the following registry key:

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\Vss\\Settings**

Under this registry key, specify DisableUserProfileExpansion for the value name, REG\_DWORD for the value type, and a nonzero value for the value data.

## About the FilesNotToBackup Registry Key

The **FilesNotToBackup** registry key can be used to specify the names of the files and directories that backup applications should not backup or restore. However, it does not exclude those files from shadow copies. For more information about this registry key, see [Registry Keys and Values for Backup and Restore](../backup/registry-keys-for-backup-and-restore.md).

 

 
