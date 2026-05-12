---
title: Backing Up and Restoring an Active Directory Server
description: Active Directory Domain Services provide functions for backing up and restoring data in the directory database.
ms.assetid: d9b9db51-ed1b-4db4-a4de-b8798c9647ac
ms.tgt_platform: multiple
keywords:
- Active Directory Domain Services, using, backing up and restoring
ms.topic: how-to
ms.date: 07/09/2025
# customer intent: As a Windows developer, I want to learn how to back up and restore an Active Directory server so that I can ensure data integrity and availability.
---

# Backing Up and Restoring an Active Directory Server

Active Directory Domain Services provide functions for backing up and restoring data in the directory database. This section describes how to [back up](backing-up-an-active-directory-server.md) and [restore](restoring-an-active-directory-server.md) an Active Directory server. For more information about backing up an Active Directory server using the utilities provided in Windows 2000 and Windows Server 2003 and later operating systems, see the applicable Resource Kit. See [Kits and tools overview](/windows-hardware/get-started/kits-and-tools-overview) and [Backup, restore, and recovery in Windows](https://support.microsoft.com/windows/backup-restore-and-recovery-in-windows-e6d629c4-2568-4406-814f-209a2af06ef7) for more information.

Backup of an Active Directory server must be performed online and must be performed when the Active Directory Domain Services are installed. Active Directory Domain Services are built on a special database and export a set of backup functions that provide the programmatic backup interface. The backup does not support incremental backups when using the built-in Windows Backup Utility. A backup application binds to a local client-side DLL with entry points defined in Ntdsbcli.h.

Restoration of an Active Directory server is always performed offline.

Although the topics in this section describe only how to back up and restore an Active Directory server, be aware that Windows 2000 and the Windows Server 2003 operating systems have several "system state" components that must be backed up and restored together. These system state components consist of:

- Boot files such as ntldr, ntdetect, all files protected by SFP, and performance counter configuration
- The Active Directory Domain Controller
- SysVol (domain controller only)
- Certificate Server (CA only)
- Cluster database (cluster node only)
- Registry
- COM+ class registration database

The system state can be backed up in any order, but restoration of the system state must occur in the following order:

1. Restore the boot files.
1. Restore SysVol, Certificate Server, Cluster database and COM+ class registration database, as applicable.
1. Restore the Active Directory server.
1. Restore the registry.

For more information about backing up and restoring Certificate Services, see [Using the Certificate Services Backup and Restore Functions](/windows/desktop/SecCrypto/using-the-certificate-services-backup-and-restore-functions).

For more information about backing up and restoring Active Directory Domain Services, see:

- [Considerations for Active Directory Domain Services Backup](considerations-for-active-directory-domain-services-backup.md)
- [Backing Up an Active Directory Server](backing-up-an-active-directory-server.md)
- [Restoring an Active Directory Server](restoring-an-active-directory-server.md)
- [Directory Backup Functions](directory-backup-functions.md)
