---
description: Note  This topic only applies to Windows Server 2003 R2 and Windows Server 2003 with Service Pack 1 (SP1).
ms.assetid: a192d9a7-1c65-4251-acb1-4df03ebfe910
title: Backing Up and Restoring System State in Windows Server 2003 R2 and Windows Server 2003 SP1
ms.topic: article
ms.date: 05/31/2018
---

# Backing Up and Restoring System State in Windows Server 2003 R2 and Windows Server 2003 SP1

> [!Note]  
> This topic only applies to Windows Server 2003 R2 and Windows Server 2003 with Service Pack 1 (SP1). For information about other operating system versions, see [Backing Up and Restoring System State](locating-additional-system-files.md).

 

> [!Note]  
> Microsoft does not provide developer or IT professional technical support for implementing online system state restores on Windows (all releases). For information about using Microsoft-provided APIs and procedures to implement online system state restores, see the community resources available at the [MSDN Community Center](https://msdn.microsoft.com/community/default.aspx).

 

When performing a VSS backup or restore, the Windows system state is defined as being a collection of several key operating system elements and their files. These elements should always be treated by backup and restore operations as a unit.

In Windows Server 2003 R2 and Windows Server 2003 with SP1, there is no Windows API designed to treat these objects as one, so it is recommended that requesters have their own system state object so that they can process these components in a consistent manner.

Because VSS runs on versions of Windows where [*System File Protection*](vssgloss-s.md) (WFP) protects system state files from corruption, special steps are needed to back up and restore system state.

System state consists of the following:

-   All files protected by WFP, boot files including ntldr, ntdetect, and performance counter configurations
-   The Active Directory (ADSI) (on systems that are domain controllers)
-   The System Volume Folder (SYSVOL) that is replicated by the File Replication Service (FRS) (on systems that are domain controllers)
-   Certificate server (on systems that provide Certification Authority)
-   Cluster database (on systems that are a node of a Windows cluster)
-   Registry service
-   COM+ class registration database

The system state can be backed up in any order.

However, the restoration of the system state should replace boot files first and commit the system section (hive) of the registry as a final step in the process, and might occur in the following order:

1.  Restore the boot files.
2.  COM+ class registration database
3.  Restore SYSVOL, Certificate Server, and Cluster databases (if needed).
4.  Restore Active Directory (if needed).
5.  Restore the registry.

Some system services, such as the Certification Authority, have conventional VSS writers and follow the VSS backup and restore algorithms. Others, such as the registry, require custom backup or restore operations; for more information, see [Custom Backups and Restores](custom-backups-and-restores.md).

## VSS Backup and Restores of Boot and System Files

The boot and system files should be backed up and restored only as a single entity.

A requester can safely use shadow-copied versions of these files, and should be sure that the system volume and boot device are [*shadow copied*](vssgloss-s.md).

The system and boot files include:

-   The core boot files: <dl> NtLdr.exe  
    Boot.ini  
    NtDetect.com  
    NtBootDD.sys (if present)  
    </dl>
-   The WFP service catalog file must be backed up prior to backing up the WFP files, and it is found under: <dl> %SystemRoot%\\System32\\CatRoot\\{F750E6C3-38EE-11D1-85E5-00C04FC295EE}  
    </dl>
-   All files protected by [*System File Protection*](vssgloss-s.md) and enumerated by [**SfcGetNextProtectedFile**](/windows/win32/api/sfc/nf-sfc-sfcgetnextprotectedfile) (see VSS Restore Operations of WFP Protected Files)
-   The Performance Counter Configuration files: <dl> %SystemRoot%\\System32\\Perf?00?.dat  
    %SystemRoot%\\System32\\Perf?00?.bak  
    </dl>
-   If present, the Internet Information Server (IIS) metabase file should be included in backup and restore operations because it contains state that is used by Microsoft Exchange and other network applications. This file can be found at: <dl> %SystemRoot%\\System32\\InetSrv\\Metabase.bin  
    </dl>
-   If the IIS metabase file is backed up, keys to enable applications to read certain encrypted entries should be restored as part of the system state. The files can be found under: <dl> %SystemRoot%\\System32\\Microsoft\\Protect\\\*  
    %AllUsersProfile%\\Microsoft\\Crypto\\RSA\\MachineKeys\\\*  
    </dl>
-   When backing up boot and system files, it may become necessary to determine the DOS boot device by doing the following:
    1.  Find the system partition under **HKEY\_LOCAL\_MACHINE**\\**System**\\**Setup**\\**SystemPartition**.
    2.  Pass the System Root environment variable (%SystemRoot%) to the mount manager to obtain the NT device name.

## VSS Restore Operations of WFP Protected Files

The WFP service is designed to prevent accidental or piecemeal replacement of system files. Therefore, special steps need to be undertaken to restore WFP data.

The means the WFP writer should specify the **VSS\_RME\_RESTORE\_AT\_REBOOT** restore method when defining its Writer Metadata Document. If a requester determines that the WFP writer has failed to specify this restore method, it indicates a writer error.

A requester should implement a restore method of **VSS\_RME\_RESTORE\_AT\_REBOOT** using the Win32 function [**MoveFileEx**](/windows/win32/api/winbase/nf-winbase-movefileexa) with the **MOVEFILE\_DELAY\_UNTIL\_REBOOT** parameter to replace system files. The restored files are not copied into the actual system file directories until after system reboot. The overwriting of protected system files will occur only if the value of the following **REG\_WORD** registry entry is set to 1:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**Session Manager**\\**AllowProtectedRenames** = 1

This value must be set before any boot where protected files are to be replaced via [**MoveFileEx**](/windows/win32/api/winbase/nf-winbase-movefileexa) and is deleted after reboot.

The system dllcache directory should also be backed up or restored, with boot volume backup and restore, and is located by examining the **REG\_EXPAND\_SZ** registry entry:

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**WinLogon**\\**SfcDllCache**<dl> <dt>

                  Data type
</dt> <dd>                  REG\_EXPAND\_SZ</dd> </dl>

The contents of the system dllcache directory are rebuilt by using the System File Checker (SFC) from the command prompt:

-   The **/SCANONCE** option scans all protected files at the next system boot.
-   The **/SCANNOW** option scans all protected files immediately.

All protected files will be scanned, and any versions that are not valid will be replaced in both the directory and dllcache location.

There are four files that are part of the WFP that cannot be restored with the WFP files:

<dl> Ctl3dv2.dll  
DtcSetup.exe  
NtDll.dll  
Smss.exe  
</dl>

These files help in the process of restoring the WFP files and as such there is a circular dependency. Currently, there is no way to restore these files except to reinstall Windows.

 

 
