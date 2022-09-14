---
description: Hardware Provider Interactions and Behaviors
ms.assetid: 059968cf-43e5-4442-b757-80afdd66799f
title: Hardware Provider Interactions and Behaviors
ms.topic: article
ms.date: 05/31/2018
---

# Hardware Provider Interactions and Behaviors

Hardware providers may support copy-on-write and/or full copy mirror (differential and/or plex) shadow copies. Resource allocation for shadow copies should follow the context specified by the requester in [**IVssBackupComponents::SetContext**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setcontext), enumerated by [**\_VSS\_SNAPSHOT\_CONTEXT**](/windows/desktop/api/Vss/ne-vss-vss_snapshot_context), for the shadow copy set.

-   If the requester specifies a shadow copy context that is supported by the provider, the provider should create a shadow copy using that method.
-   If the requester specifies a shadow copy context that is not supported by the provider, then the provider should not attempt to create the shadow copy and return **FALSE** through the *pbIsSupported* parameter in [**IVssHardwareSnapshotProvider::AreLunsSupported**](/windows/desktop/api/VsProv/nf-vsprov-ivsshardwaresnapshotprovider-arelunssupported).
-   If the requester does not explicitly specify a shadow copy context, then the provider should use reasonable default behavior for shadow copy creation.

Hardware providers associated with SAN RAID subsystems should support transportable shadow copies to allow movement between hosts on a SAN.

Hardware providers running on multiple machines on a SAN yet managing the same RAID subsystem do not need to coordinate between providers on a SAN. The coordinator maintains any necessary state. Two kinds of state are recognized:

-   State necessary to support data access to the volumes contained on a hardware shadow copy. This includes any tagging of a volume as read-only or hidden. This state must be on the hardware LUN and travel with the LUN. This state is preserved across boot epochs and/or device discovery. VSS manages this state for the lifetime of the shadow copy.
-   State necessary to recognize a specific volume as part of a shadow copy set. This state is persisted by VSS in conjunction with the requester that originally created the shadow copy set.

For more information, see the following topics:

-   [The Shadow Copy Creation Process](the-shadow-copy-creation-process.md)
-   [Required Behaviors for Shadow Copy Providers](required-behaviors-for-shadow-copy-providers.md)
-   [State Transitions in shadow copy providers](state-transitions-in-shadow-copy-providers.md)
-   [Error Handling in shadow copy providers](error-handling-in-shadow-copy-providers.md)

 

 



