---
description: The Windows operating system includes a set of VSS writers that are responsible for enumerating the data that is required by various Windows features. These are referred to as &\#0034;in-box&\#0034; writers.
ms.assetid: e20a303d-9440-42be-b383-85f6fad89157
title: In-Box VSS Writers
ms.topic: article
ms.date: 05/31/2018
---

# In-Box VSS Writers

The Windows operating system includes a set of VSS writers that are responsible for enumerating the data that is required by various Windows features. These are referred to as "in-box" writers.

> [!Note]  
> The MSDE in-box writer is not available in Windows Vista, Windows Server 2008, and later. Instead, the SQL Writer should be used to back up SQL Server databases. Only SQL Server 2005 SP2 and later are supported on Windows Vista, Windows Server 2008, and later.

 

-   [Active Directory Domain Services (NTDS) VSS Writer](#active-directory-domain-services-ntds-vss-writer)
-   [Active Directory Federation Services Writer](#active-directory-federation-services-writer)
-   [Active Directory Lightweight Directory Services (LDS) VSS Writer](#active-directory-lightweight-directory-services-lds-vss-writer)
-   [Active Directory Rights Management Services (AD RMS) Writer](#active-directory-rights-management-services-ad-rms-writer)
-   [Automated System Recovery (ASR) Writer](#automated-system-recovery-asr-writer)
-   [Background Intelligent Transfer Service (BITS) Writer](#background-intelligent-transfer-service-bits-writer)
-   [Certificate Authority Writer](#certificate-authority-writer)
-   [Cluster Service Writer](#cluster-service-writer)
-   [Cluster Shared Volume (CSV) VSS Writer](#cluster-shared-volume-csv-vss-writer)
-   [COM+ Class Registration Database Writer](#com-class-registration-database-writer)
-   [Data Deduplication Writer](#data-deduplication-writer)
-   [Distributed File System Replication (DFSR)](#distributed-file-system-replication-dfsr)
-   [Dynamic Host Configuration Protocol (DHCP) Writer](#dynamic-host-configuration-protocol-dhcp-writer)
-   [File Replication Service (FRS)](#file-replication-service-frs)
-   [File Server Resource Manager (FSRM) Writer](#file-server-resource-manager-fsrm-writer)
-   [Hyper-V Writer](#hyper-v-writer)
-   [IIS Configuration Writer](#iis-configuration-writer)
-   [IIS Metabase Writer](#iis-metabase-writer)
-   [Microsoft Message Queuing (MSMQ) Writer](#microsoft-message-queuing-msmq-writer)
-   [MSSearch Service Writer](#mssearch-service-writer)
-   [NPS VSS Writer](#nps-vss-writer)
-   [Performance Counters Writer](#performance-counters-writer)
-   [Registry Writer](#registry-writer)
-   [Remote Desktop Services (Terminal Services) Gateway VSS Writer](#remote-desktop-services-terminal-services-gateway-vss-writer)
-   [Remote Desktop Services (Terminal Services) Licensing VSS Writer](#remote-desktop-services-terminal-services-licensing-vss-writer)
-   [Shadow Copy Optimization Writer](#shadow-copy-optimization-writer)
-   [Sync Share Service Writer](#sync-share-service-writer)
-   [System Writer](#system-writer)
-   [Task Scheduler Writer](#task-scheduler-writer)
-   [VSS Metadata Store Writer](#vss-metadata-store-writer)
-   [Windows Deployment Services (WDS) Writer](#windows-deployment-services-wds-writer)
-   [Windows Internal Database (WID) Writer](#windows-internal-database-wid-writer)
-   [Windows Internet Name Service (WINS) Writer](#windows-internet-name-service-wins-writer)
-   [WMI Writer](#wmi-writer)

## Active Directory Domain Services (NTDS) VSS Writer

This writer reports the NTDS database file (ntds.dit) and the associated log files. These files are required to restore the Active Directory correctly.

There is only one ntds.dit file per domain controller, and it is reported in the writer metadata as in the following example:

``` syntax
    <DATABASE_FILES path="C:\Windows\NTDS" 
                     filespec="ntds.dit" 
                     filespecBackupType="3855"/>
```

Here is an example that shows how to list components in the writer's metadata:

``` syntax
    <BACKUP_LOCATIONS>
        <DATABASE logicalPath="C:_Windows_NTDS" 
                     componentName="ntds" 
                     caption="" restoreMetadata="no" 
                     notifyOnBackupComplete="no" 
                     selectable="no" 
                     selectableForRestore="no" 
                     componentFlags="3">
        <DATABASE_FILES path="C:\Windows\NTDS" 
                     filespec="ntds.dit" 
                     filespecBackupType="3855"/>
        <DATABASE_LOGFILES path="C:\Windows\NTDS" 
                     filespec="edb*.log" 
                     filespecBackupType="3855"/> 
        <DATABASE_LOGFILES path="C:\Windows\NTDS" 
                     filespec="edb.chk" 
                     filespecBackupType="3855"/>
        </DATABASE>
    </BACKUP_LOCATIONS>
```

At backup time, the writer sets the backup expiration time in the writer's backup metadata. Requesters should retrieve this metadata by using [**IVssComponent::GetBackupMetadata**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getbackupmetadata) to determine whether the database has expired. Expired databases cannot be restored.

If the computer that contains the NTDS database is a domain controller, the backup application should always perform a system state backup across all volumes containing critical system state information. At restore time, the application should first restart the computer in Directory Services Restore Mode and then perform a system state restore.

The writer name string for this writer is "NTDS".

The writer ID for this writer is B2014C9E-8711-4C5C-A5A9-3CF384484757.

## Active Directory Federation Services Writer

This writer reports the Active Directory Federation Services (ADFS) data files.

**Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This writer is not supported.

The writer name string for this writer is "ADFS VSS Writer".

The writer ID for this writer is 772C45F8-AE01-4F94-940C-94961864ACAD.

## Active Directory Lightweight Directory Services (LDS) VSS Writer

This writer reports the ADAM database file (adamntds.dit) and the associated log files for each instance in %program files%\\Microsoft ADAM\\instance*N*\\data, where *N* is the ADAM instance number. These database log files are required to restore ADAM instances.

**Windows XP:** This writer is not supported.

Here is an example that shows how to list components in the writer's metadata:

``` syntax
    <BACKUP_LOCATIONS>
        <DATABASE logicalPath="C:_Program Files_Microsoft ADAM_instance1_data" 
                     componentName="adamntds" 
                     caption="" 
                     restoreMetadata="no" 
                     notifyOnBackupComplete="no" 
                     selectable="no" 
                     selectableForRestore="no" 
                     componentFlags="3">
        <DATABASE_FILES path="C:\Program Files\Microsoft ADAM\instance1\data" 
                     filespec="adamntds.dit" 
                     filespecBackupType="3855"/>
        <DATABASE_LOGFILES path="C:\Program Files\Microsoft ADAM\instance1\data" 
                     filespec="edb*.log" 
                     filespecBackupType="3855"/>
        <DATABASE_LOGFILES path="C:\Program Files\Microsoft ADAM\instance1\data" 
                     filespec="edb.chk" 
                     filespecBackupType="3855"/>
        </DATABASE>
    </BACKUP_LOCATIONS>
```

At backup time, the writer sets the backup expiration time in the backup metadata. Backup applications should retrieve this metadata by using the [**IVssComponent::GetBackupMetadata**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getbackupmetadata) method to determine whether the database has expired. Expired databases cannot be restored.

The writer name string for this writer is "ADAM (instance*N*) Writer", where *N* is the ADAM instance number, for example, "ADAM (instance1) Writer", "ADAM (instance2) Writer", and so on.

The writer ID for this writer is DD846AAA-A1B6-42A8-AAF8-03DCB6114BFD. This writer ID is the same for all instances.

## Active Directory Rights Management Services (AD RMS) Writer

This writer reports the Active Directory Rights Management Service (AD RMS) data files.

**Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This writer is not supported.

The writer name string for this writer is "AD RMS Writer".

The writer ID for this writer is 886C43B1-D455-4428-A37F-4D6B9E43F50F.

## Automated System Recovery (ASR) Writer

The ASR writer stores the configuration of disks on the system. This writer reports the Boot Configuration Database (BCD) and is also responsible for dismounting the registry hive that represents the BCD during shadow copy creation. The ASR writer must be included in any backups required for bare-metal recovery. For more information about ASR, see [Using VSS Automated System Recovery for Disaster Recovery](using-vss-automated-system-recovery-for-disaster-recovery.md).

**Windows Server 2003 and Windows XP:** This writer is not supported.

The writer name string for this writer is "ASR Writer".

The writer ID for the ASR writer is BE000CBE-11FE-4426-9C58-531AA6355FC4.

## Background Intelligent Transfer Service (BITS) Writer

The BITS writer uses the **FilesNotToBackup** registry key to exclude files from the BITS cache folder. The default cache location is %AllUsersProfile%\\Microsoft\\Network\\Downloader\\Cache.

**Windows Server 2003 and Windows XP:** This writer is not supported.

In addition, the BITS writer excludes the following files from backup: the BITS state files (qmgr0.dat and qmgr1.dat), the BITS debug log file, and BITS partially downloaded files.

If the BITS download destination file is an SMB file, the client account must have a trust relationship to the server, or else backups may fail.

The writer name string for this writer is "BITS Writer".

The writer ID for the BITS writer is 4969D978-BE47-48B0-B100-F328F07AC1E0.

## Certificate Authority Writer

This writer is responsible for enumerating the data files for the Certificate Server.

The writer name string for this writer is "Certificate Authority".

**Windows XP:** The writer name string for this writer is "Certificate Server Writer".

The writer ID for the writer is 6F5B15B5-DA24-4D88-B737-63063E3A1F86.

## Cluster Service Writer

The Cluster Service VSS writer is documented in the [Cluster Service](/previous-versions/windows/desktop/mscs/backing-up-and-restoring-the-failover-cluster-configuration-using-vss) API documentation.

**Windows Vista, Windows Server 2003 and Windows XP:** This writer is not supported until Windows Vista with Service Pack 1 (SP1) and Windows Server 2008.

## Cluster Shared Volume (CSV) VSS Writer

This writer reports the Cluster Shared Volume (CSV) data files. This writer is an in-box writer for Windows Server operating system versions; it does not ship in Windows Client.

**Windows Server 2008 R2, Windows Server 2008 and Windows Server 2003:** This writer is not supported.

The writer name string for this writer is "Cluster Shared Volume VSS Writer".

The writer ID for the writer is 1072AE1C-E5A7-4EA1-9E4A-6F7964656570.

## COM+ Class Registration Database Writer

This writer is responsible for the contents of the %SystemRoot%\\Registration directory. The COM+ catalog is a file in %SystemRoot%\\Registration with a name that follows the pattern R*xxxxxxxxxxxx*.clb, where *xxxxxxxxxxxx* is a 12-digit hexadecimal number. There can potentially be multiple such files if COM+ applications have been configured on the computer. The file that contains the current COM+ catalog is the file with the largest value of *xxxxxxxxxxxx*.

**Windows Server 2003 and Windows XP:** This writer is not supported.

The COM+ class registration database depends on a registry key being backed up and hence needs to be backed up and restored together with the registry.

To restore the COM+ Registration Database, a backup application (requester) must call the [**ICOMAdminCatalog::RestoreREGDB**](/windows/win32/api/comadmin/nf-comadmin-icomadmincatalog-restoreregdb) method.

The writer name string for this writer is "COM+ REGDB Writer".

The writer ID for the COM+ class registration database writer is 542DA469-D3E1-473C-9F4F-7847F01FC64F.

## Data Deduplication Writer

The Data Deduplication VSS writer is documented in the [Data Deduplication](/previous-versions/windows/desktop/dedup/backup-and-restore-of-data-deduplication-enabled-volumes) API documentation. This writer is an in-box writer for Windows Server operating system versions; it does not ship in Windows Client.

**Windows Server 2008 R2, Windows Server 2008 and Windows Server 2003:** This writer is not supported.

## Distributed File System Replication (DFSR)

The following component includes a VSS writer: [Distributed File System Replication (DFSR)](/previous-versions/windows/desktop/dfsr/dfsr-replicated-folders)

**Windows Vista, Windows Server 2003 and Windows XP:** This writer is not supported until Windows Vista with SP1 and Windows Server 2008.

## Dynamic Host Configuration Protocol (DHCP) Writer

This writer is responsible for enumerating files required for the DHCP server role. This writer is an in-box writer for Windows Server operating system versions; it does not ship in Windows Client.

The writer name string for this writer is "Dhcp Jet Writer".

The writer ID for this writer is BE9AC81E-3619-421F-920F-4C6FEA9E93AD.

## File Replication Service (FRS)

The File Replication Service writer is documented in [Backing Up and Restoring an FRS-Replicated SYSVOL Folder](backing-up-and-restoring-an-frs-replicated-sysvol-folder.md).

**Windows Vista, Windows Server 2003 and Windows XP:** This writer is not supported until Windows Vista with SP1 and Windows Server 2008.

## File Server Resource Manager (FSRM) Writer

This writer enumerates the FSRM configuration files that are used for system state backup. During restore operations it prevents changes in FSRM configuration and temporarily halts enforcement of quotas and file screens. After the restore is complete, the writer refreshes FSRM with the configuration that was restored. This writer is only present when FSRM (part of File Services role) is both installed and running. This writer is an in-box writer for Windows Server operating system versions; it does not ship in Windows Client.

**Windows Server 2003:** This writer is not supported until Windows Server 2003 R2.

The writer name string for this writer is "FSRM Writer".

The writer ID for this writer is 12CE4370-5BB7-4C58-A76A-E5D5097E3674.

## Hyper-V Writer

The Hyper-V VSS writer is documented in the [Hyper-V](/previous-versions/windows/desktop/virtual/backing-up-and-restoring-virtual-machines) API documentation. This writer is an in-box writer for Windows Server operating system versions; it does not ship in Windows Client.

**Windows Server 2003:** This writer is not supported until Windows Server 2008.

## IIS Configuration Writer

The IIS configuration writer is responsible for enumerating the IIS configuration files.

**Windows Vista, Windows Server 2003 and Windows XP:** This writer is not supported until Windows Vista with SP1 and Windows Server 2008. Requesters are required to back up the IIS configuration files, including the .NET FX machine.config file or the ASP.NET root web.config file.

This writer does not back up the .NET FX machine.config file or the ASP.NET root web.config file because these files are enumerated by the System Writer.

This writer backs up all files that are in the %windir%\\system32\\inetsrv\\config\\schema and %windir%\\system32\\inetsrv\\config directories, except for files that are enumerated by the System Writer.

The writer ID for the IIS configuration writer is 2A40FD15-DFCA-4aa8-A654-1F8C654603F6.

## IIS Metabase Writer

The Internet Information Server (IIS) metabase writer is responsible for enumerating the IIS metabase file.

**Windows Vista, Windows Server 2003 and Windows XP:** This writer is not supported until Windows Vista with SP1 and Windows Server 2008. Requesters are required to back up the IIS metabase file.

The writer ID for the IIS metabase writer is 59B1f0CF-90EF-465F-9609-6CA8B2938366.

## Microsoft Message Queuing (MSMQ) Writer

This writer reports the Microsoft Message Queuing (MSMQ) data files.

**Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This writer is not supported.

The writer name string for this writer is "MSMQ Writer (*SvcName*)", where *SvcName* is the name of the MSMQ service the writer is associated with. For default installation, the service name is "MSMQ". For clustered instances, the service name is MSMQ$*ResourceName*, where *ResourceName* is the clustered MSMQ resource name.

The writer ID for this writer is 7E47B561-971A-46E6-96B9-696EEAA53B2A.

## MSSearch Service Writer

This writer exists to delete search index files from shadow copies after creation. This is done to minimize the impact of Copy-on-Write I/O during regular I/O on these files on the shadow-copied volume.

**Windows Server 2003:** This writer is not supported.

To install this writer on the server, you must install the File Services role and enable the Windows Search Service.

The writer name string for this writer is "MSSearch Service Writer".

The writer ID for the MSSearch service writer is CD3F2362-8BEF-46C7-9181-D62844CDC0B2.

## NPS VSS Writer

The NPS writer is responsible for enumerating the Network Policy Server (NPS) configuration files for servers that have the Network Policy and Access Services role installed.

**Windows Vista, Windows Server 2003 and Windows XP:** This writer is not supported until Windows Vista with SP1 and Windows Server 2008.

The writer name string for this writer is "NPS VSS Writer".

The writer ID for the NPS VSS writer is 0x35E81631-13E1-48DB-97FC-D5BC721BB18A.

## Performance Counters Writer

This writer reports the performance counter configuration files. These files are only modified during application installation and should be backed up and restored during system state backups and restores.

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This writer is not supported. Requesters are required to back up these files manually. (See [Backing Up and Restoring System State](locating-additional-system-files.md).)

The writer name string for this writer is "Performance Counters Writer".

The writer ID for the Performance Counters Writer is 0BADA1DE-01A9-4625-8278-69E735F39DD2.

## Registry Writer

The registry writer is reports the Windows registry files to enable in-place backups and restores of the registry. It does not report user hives.

**Windows Server 2003:** In Windows Server 2003, this writer uses an intermediate repository file (sometimes called a "spit file") to store registry data. (See [Registry Backup and Restore Operations Under VSS](registry-backup-and-restore-operations-under-vss.md).)

**Windows XP:** This writer is not supported. (See [Registry Backup and Restore Operations Under VSS](registry-backup-and-restore-operations-under-vss.md).)

The writer name string for this writer is "Registry Writer".

The writer ID for the registry writer is AFBAB4A2-367D-4D15-A586-71DBB18F8485.

## Remote Desktop Services (Terminal Services) Gateway VSS Writer

This writer is responsible for enumerating the Remote Desktop Services (Terminal Services) Gateway files for servers that have Remote Desktop Gateway, a subrole of Remote Desktop Services role, installed.

**Windows Server 2003:** This writer is not supported.

This writer is an in-box writer for Windows Server operating system versions; it does not ship in Windows Client.

The Remote Desktop Services Gateway depends on several registry keys being backed up and therefore needs to be backed up and restored together with the registry.

The writer name string for this writer is "TS Gateway Writer".

The writer ID for this writer is 368753EC-572E-4FC7-B4B9-CCD9BDC624CB.

## Remote Desktop Services (Terminal Services) Licensing VSS Writer

This writer is responsible for enumerating the Remote Desktop Services Licensing (RD Licensing) or Terminal Services Licensing (TS Licensing) files for servers that have Remote Desktop Licensing, a subrole of Remote Desktop Services role, installed.

**Windows Server 2003:** This writer is not supported.

This writer is an in-box writer for Windows Server operating system versions; it does not ship in Windows Client.

Remote Desktop Services Licensing depends on several registry keys being backed up and therefore needs to be backed up and restored together with the registry.

The writer name string for this writer is "TermServLicensing".

The writer ID for this writer is 5382579C-98DF-47A7-AC6C-98A6D7106E09.

## Shadow Copy Optimization Writer

This writer deletes certain files from volume shadow copies. This is done to minimize the impact of Copy-on-Write I/O during regular I/O on these files on the shadow-copied volume. The files that are deleted are typically temporary files or files that do not contain user or system state.

**Windows Server 2003 and Windows XP:** This writer is not supported.

The writer name string for this writer is "Shadow Copy Optimization Writer".

The writer ID for the shadow copy optimization writer is 4DC3BDD4-AB48-4D07-ADB0-3BEE2926FD7F.

## Sync Share Service Writer

**Windows Server 2012 R2:** This writer is included with Windows Server 2012 R2 and newer server versions. It is not compatible with desktop versions.

This writer is responsible for enumerating the sync shares on servers that have the Sync Share Service installed, and for ensuring that their metadata and data remain consistent during backup and restore.

This writer is only present when Sync Share Service is both installed and running.

There will be one VSS writer component for each sync share. This includes the metadata and data paths. These must be backed up together for consistency.

The writer name string is "Sync Share Service VSS writer".

The writer ID is D46BF321-FDBA-4A35-8EC3-454DF03BC86A.

## System Writer

The system writer enumerates all operating system and driver binaries and it is required for a system state backup.

**Windows Server 2003 and Windows XP:** This writer is not supported.

This writer runs as part of the Cryptographic Services (CryptSvc) service. The system writer generates a file list that contains the following files:

-   All static files that have been installed. A static file is a file that is listed in the component manifest with the **writeableType** file attribute set to "static" or "". Static files include all files that are protected by Windows Resource Protection (WRP). However, not all static files are WRP-protected files. For example, game files are static but not WRP-protected so that administrators can change parental control settings.
-   The contents of the Windows Side-by-Side (WinSxS) directory, including all manifests, optional components, and third-party Win32 files.
    > [!Note]  
    > Many of the files in the %windir%\\system32 directory are hard links to files in the WinSxS directory.

     

-   All PnP files for installed drivers (owned by PnP).
-   All user-mode services and non-PnP drivers.
-   All catalogs owned by CryptSvc.

The restore application is responsible for laying down the files and registry and setting ACLs to match the system shadow copy. The appropriate hard links must also be created for a system state restore to succeed.

The writer name string for this writer is "System Writer".

The writer ID for the system writer is E8132975-6F93-4464-A53E-1050253AE220.

## Task Scheduler Writer

This writer reports the task scheduler's task files.

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This writer is not supported. Requesters are required to back up these files manually. (See [Backing Up and Restoring System State](locating-additional-system-files.md).)

The writer name string for this writer is "Task Scheduler Writer".

The writer ID for the writer is D61D61C8-D73A-4EEE-8CDD-F6F9786B7124.

## VSS Metadata Store Writer

This writer reports the writer metadata files for all VSS express writers.

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This writer is not supported.

The writer name string for this writer is "VSS Express Writer Metadata Store Writer".

The writer ID for the writer is 75DFB225-E2E4-4D39-9AC9-FFAFF65DDF06.

## Windows Deployment Services (WDS) Writer

This writer reports the Windows Deployment Services (WDS) data files.

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This writer is not supported.

The writer name string for this writer is "WDS VSS Writer".

The writer ID for this writer is 82CB5521-68DB-4626-83A4-7FC6F88853E9.

## Windows Internal Database (WID) Writer

This writer reports the Windows Internal Database (WID) data files.

**Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This writer is not supported.

The writer name string for this writer is "WIDWriter".

The writer ID for this writer is 8D5194E1-E455-434A-B2E5-51296CCE67DF.

## Windows Internet Name Service (WINS) Writer

This writer is responsible for enumerating files required for WINS.

**Windows XP:** This writer is not supported.

The writer name string for this writer is "WINS Jet Writer".

The writer ID for this writer is F08C1483-8407-4A26-8C26-6C267A629741.

## WMI Writer

This writer is used for identifying WMI-specific state and data during backup operations. The data includes files from the WBEM repository.

**Windows Server 2003 and Windows XP:** This writer is not supported.

The writer name string for this writer is "WMI Writer".

The writer ID for this writer is A6AD56C2-B509-4E6C-BB19-49D8F43532F0.

 

 
