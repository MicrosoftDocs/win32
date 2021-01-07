---
description: Selectability for restore allows the requester to determine when a component can be individually restored.
ms.assetid: 684dc50f-5d7b-4c95-85dd-77c320d65fff
title: Working with Selectability For Restore and Subcomponents
ms.topic: article
ms.date: 05/31/2018
---

# Working with Selectability For Restore and Subcomponents

Selectability for restore allows the requester to determine when a component can be individually restored. A component that has been included for backup can appear in one of two ways:

-   A component may have been [*explicitly included*](vssgloss-e.md) in the backup. These components have a corresponding [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) instance in the Backup Components Document. These components are included in a restore using [**IVssBackupComponents::SetSelectedForRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setselectedforrestore).
-   A component may have been [*implicitly included*](vssgloss-i.md) in the backup. These components do not have a corresponding [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) instance in the Backup Components Document; however, there will always be an **IVssComponent** instance for some ancestor component in the document. These components are included in a restore using [**IVssBackupComponents::AddRestoreSubcomponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addrestoresubcomponent).

Any component that has been explicitly included in the backup can always be individually selected for restore, regardless of its selectability-for-restore value. The requester calls [**IVssBackupComponents::SetSelectedForRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setselectedforrestore), passing in the writer ID, logical path, and name of the specific component. Components that have been implicitly included in the backup will be restored when an explicitly included ancestor is restored. Implicitly included components can be individually selected for restore only if they are marked as selectable for restore. The requester first calls **IVssBackupComponents::SetSelectedForRestore** on the closest explicitly included ancestor component, and then calls [**IVssBackupComponents::AddRestoreSubcomponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addrestoresubcomponent) on the ancestor component to select the implicitly included component for restore. After this is done, only the implicitly selected component will be restored; all other components in the component set will not be restored.

Unlike selectability for backup, which must always be explicitly set when a component is added with [**IVssCreateWriterMetadata::AddComponent**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addcomponent), selectability for restore has a default value of false, which can be overridden.

Because top-level components (components with an empty logical path) can only be explicitly included in a backup, selectability for restore has no meaning for these components.

 

 



