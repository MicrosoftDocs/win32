---
title: Backup
description: Allow backup applications to communicate with other applications and services about backup and restore operations. Perform tape backup, initialize tape, and retrieve tape drive information. Maintain duplicate files with single-instance store (SIS).
ms.assetid: 97c3e2c4-8214-4093-bd13-3c38c91e08bd
keywords:
- backup Backup
- backup Backup , home
- restore operations Backup
ms.topic: article
ms.date: 05/31/2018
---

# Backup

Registry keys for backup and restore allow backup applications to communicate with other applications and services about backup and restore operations. For more information, see [Registry Keys and Values for Backup and Restore](registry-keys-for-backup-and-restore.md).

The tape backup API enables backup applications to read from and write to a tape, initialize a tape, and retrieve tape or tape drive information. For more information, see [Tape Backup](tape-backup.md).

Single-instance store (SIS) is an architecture designed to maintain duplicate files with a minimum of overhead. Backup application use the SIS backup API to access the SIS architecture. For more information, see [Single-Instance Store and SIS Backup](single-instance-store-and-sis-backup.md).

Backup and restore of encrypted files is enabled by the raw encryption API, which reads and writes encrypted files while keeping the data in encrypted format. The API allows the encrypted data in these files to be backed up and restored, while meeting the goals of maintaining the security of the backed up data, and being usable by an application that lacks permission to use the encryption keys on the file. For more information, see [Backup and Restore of Encrypted Files](/windows/desktop/FileIO/backup-and-restore-of-encrypted-files).

The Srdelayed tool can enable system state recovery applications to move, delete, and set the short name of system files. For more information, see [Srdelayed.exe](srdelayed-exe.md).

## Related topics

<dl> <dt>

[Backup Reference](backup-reference.md)
</dt> </dl>

 

 