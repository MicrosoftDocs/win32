---
description: Restore options allow requesters to communicate customized restore options to writers.
ms.assetid: 364550a1-070a-4f7e-bd62-84672959dc21
title: Setting VSS Restore Options
ms.topic: article
ms.date: 05/31/2018
---

# Setting VSS Restore Options

Restore options allow requesters to communicate customized restore options to writers.

## Restore Options

Standardizing the format of the restore options allow writers and requesters to handle common custom requests. Restore options are set by the requester by calling the [**IVssBackupComponents::SetRestoreOptions**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setrestoreoptions) method up to once per selected-for-backup component before calling the [**IVssBackupComponents::PreRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prerestore) method. The string passed in the *wszRestoreOptions* parameter to the **SetRestoreOptions** method can contain multiple values, as described below.

## Format

The format of restore options, is one or more comma-separated name/value pairs, and the name is optionally prefixed with the name of the subcomponent to which it applies. The component names and option names are case-insensitive. The case-sensitivity of the values is determined by the writer. For example:

``` syntax
"Child1":"Option1"="Value1","Option2"="Value2","Child2\Grandchild3":"Option3"="Value3"
```

In this example, "Option1" only applies to the "Child1" subcomponent and its descendants, "Option2" applies to all components and their descendants, and "Option3" applies only to the "Child2\\Grandchild3" subcomponents and its descendants.

The [**SetRestoreOptions**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setrestoreoptions) method can only be called on components that are selectable for backup, while descendant nodes may not be selectable for backup, they may be selectable for restore.

## Common Restore Options

These common restore options have been defined to increase interoperability between writers and requesters.

-   Authoritative

    The "Authoritative" option supports multiple "Item" values, but only one "All" value.

    This entire component is authoritative.

    ``` syntax
    "Authoritative"="All"
    ```

    Only the specified item is authoritative. The format of the named item is defined by the writer. Common designations are "\*" to indicate all files, "..." to indicate all files and subdirectories of the specified component.

    ``` syntax
    "Authoritative"="Item:XXX"
    ```

-   Roll Forward

    After a database is restored, writers usually roll forward through logs to bring the database up to date. In the case of incremental or differential restores, the requester uses the [**IVssBackupComponents::SetAdditionalRestores**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setadditionalrestores) method to partially control the log-handling behavior - this restore option allows more granular control.

    Do not roll through logs.

    ``` syntax
    "Roll Forward"="None"
    ```

    Roll through all logs.

    ``` syntax
    "Roll Forward"="All"
    ```

    Roll through logs up to specified point. The format of the specified point is defined by the writer.

    ``` syntax
    "Roll Forward"="Partial:XXX"
    ```

-   New Component Name

    A writer may want to restore a component to a new name. For example, restoring a database to a different name to restore an individual item; restoring to the same name would please all data We recommend that writers accept a valid logical path and component name as this options' value. This will often be used with a [*directed target*](vssgloss-d.md).

    ``` syntax
    "New Component Name"="Logical Path\Component Name"
    ```

 

 



