---
description: A requester should select a specific provider only if it has some information about the providers available.
ms.assetid: 1a3bc938-2754-4fa2-bd7f-e9b3e876bf6c
title: Selecting Providers
ms.topic: article
ms.date: 05/31/2018
---

# Selecting Providers

A requester should select a specific provider only if it has some information about the providers available.

Because this will not generally be the case, it is recommended that a requester supply GUID\_NULL as a provider ID to [**IVssBackupComponents::AddToSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addtosnapshotset), which allows the system to choose a provider according to the following algorithm:

1.  If a hardware provider that supports the given volume is available, it is selected.
2.  If no hardware provider is available, then if any software provider specific to the given volume is available, it is selected.
3.  If no hardware provider and no software provider specific to the volumes is available, the system provider is selected.

However, a requester can obtain information about available providers by using [**IVssBackupComponents::Query**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-query). With this information, and only if the backup application has a good understanding of the various providers, a requester can supply a valid provider ID to [**IVssBackupComponents::AddToSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addtosnapshotset).

Note that all volumes do not need to have the same provider.

 

 



