---
description: When performing a VSS backup or restore, the Windows system state is defined as being a collection of several key operating system elements and their files. These elements should always be treated as a unit by backup and restore operations.
ms.assetid: 48721358-8450-462f-8f99-23e207311041
title: Backing Up and Restoring System State
ms.topic: article
ms.date: 05/31/2018
---

# Backing Up and Restoring System State

> [!Note]  
> This topic applies to Windows Vista, Windows Server 2008, and later. For information about Windows Server 2003, see [Backing Up and Restoring System State in Windows Server 2003 R2 and Windows Server 2003 SP1](backing-up-and-restoring-system-state-under-vss.md)

 

When performing a VSS backup or restore, the Windows system state is defined as being a collection of several key operating system elements and their files. These elements should always be treated as a unit by backup and restore operations.

> [!Note]  
> Microsoft does not provide developer or IT professional technical support for implementing online system state restores on Windows (all releases).

 

When backing up and recovering system state, the recommended strategy is to back up and recover the system and boot volumes in addition to the files enumerated by the system state writers. System state writers are writers that have the [**VSS\_USAGE\_TYPE**](/windows/desktop/api/VsWriter/ne-vswriter-vss_usage_type) attribute set to either VSS\_UT\_BOOTABLESYSTEMSTATE or VSS\_UT\_SYSTEMSERVICE.

> [!IMPORTANT]
> If a VSS Writer is identified by its [**VSS\_USAGE\_TYPE**](/windows/desktop/api/VsWriter/ne-vswriter-vss_usage_type) as a system state writer it must be included in a system state backup even if it is selectable.

 

In addition to the enumerated operating system and driver binary files that are enumerated by the system state writers, there are certain other files that must be backed up as part of system state.

All the components reported by a VSS system state writer are part of system state except those for which the VSS\_CF\_NOT\_SYSTEM\_STATE flag is set.

Backup programs should also set the **LastRestoreId** registry key. For more information, see [Registry Keys and Values for Backup and Restore](../backup/registry-keys-for-backup-and-restore.md).

> [!Note]  
> In Windows Vista, Windows Server 2008, and later, the names and locations of some system files have been changed as follows.

 

## System State

For Windows Server 2012 and later, in addition to the files reported by the various VSS system-state writers, only the following licensing files need to be included explicitly, and the following DRM files need to be excluded explicitly.

## Windows Media Digital Rights Management Files

In Windows Server 2008 and later, the following files, including all subdirectories under the following path, are excluded from system state and must not be backed up:

-   %ProgramData%\\Microsoft\\Windows\\DRM\\

This supersedes the information in the Windows Media Digital Rights Management section of [Working with File System and Security Features](working-with-file-system-and-security-features.md).

## Performance Counter Configuration Files

The performance counter configuration files are located in the %SystemRoot%\\System32\\ directory and have the following names:

<dl> Perf?00?.dat  
Perfc0??.dat  
Perfd0??.dat  
Perfh0??.dat  
Perfi0??.dat  
Prfc0???.dat  
Prfd0???.dat  
Prfh0???.dat  
Prfi0???.dat  
</dl>

These files are only modified during application installation and should be backed up and restored during system state backups and restores.

## IIS Configuration Files

> [!Note]  
> In Windows Vista with Service Pack 1 (SP1) and later, you should not back up these files. Instead, use the in-box IIS configuration writer. For more information about this writer, see [In-Box VSS Writers](in-box-vss-writers.md).

 

The relevant IIS configuration files and their locations are listed below:

-   The .NET FX machine.config file is located in the framework version directory.
-   The ASP.NET root web.config file is located in the framework version directory.
    > [!Note]  
    > The configuration files for both .NET FX and ASP.NET are in the framework version directory. If multiple versions of the framework are installed on the computer, this directory will contain one configuration file for each installed version.

     

-   The IIS applicationHost.config central configuration file is located in the %windir%\\system32\\inetsrv\\config directory. For the server to understand this configuration file, there are schema files that determine its grammar and structure. These files are located in the %windir%\\system32\\inetsrv\\config\\schema directory.

The framework version directory path is stored in the following registry key:

**HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\.NETFramework\\InstallRoot**

In addition, the following cryptography keys must be backed up:<dl> %ProgramData%\\Microsoft\\Crypto\\RSA\\MachineKeys\\\*  
%SystemRoot%\\System32\\Microsoft\\Protect\\\*  
</dl>

## Framework Files

All versions of the .NET framework must be backed up. The files are located in one or both of the following directories:

<dl> %windir%\\Microsoft.Net\\Framework  
%windir%\\Microsoft.Net\\Framework64  
</dl>

In addition, the assembly files must be backed up. These files are located in the following directory:<dl> %windir%\\assembly  
</dl>

## Task Scheduler Task Files

The task scheduler's task files must be backed up. The files are located in one or both of the following locations:

<dl> %windir%\\system32\\tasks and any subdirectories (recursively)  
%windir%\\tasks (no subdirectories)  
</dl>

 

 
