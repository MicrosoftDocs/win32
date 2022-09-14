---
description: The following table describes the four types of components that can be involved with a backup operation.
ms.assetid: d94e015b-6735-4a88-9d24-b73f0b5f6542
title: Working with Selectability for Backup
ms.topic: article
ms.date: 05/31/2018
---

# Working with Selectability for Backup

The following table describes the four types of components that can be involved with a backup operation.



| Component type                                                                                                                                                                                                               | Description                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <span id="Nonselectable-for-backup_components"></span><span id="nonselectable-for-backup_components"></span><span id="NONSELECTABLE-FOR-BACKUP_COMPONENTS"></span>Nonselectable-for-backup components<br/>             | No selectable-for-backup ancestors in their logical paths.<br/>                              |
| <span id="Selectable-for-backup_components"></span><span id="selectable-for-backup_components"></span><span id="SELECTABLE-FOR-BACKUP_COMPONENTS"></span>Selectable-for-backup components<br/>                         | No selectable-for-backup ancestors in their logical paths.<br/>                              |
| <span id="Nonselectable-for-backup_subcomponents"></span><span id="nonselectable-for-backup_subcomponents"></span><span id="NONSELECTABLE-FOR-BACKUP_SUBCOMPONENTS"></span>Nonselectable-for-backup subcomponents<br/> | Nonselectable-for-backup components with selectable-for-backup ancestors in their path.<br/> |
| <span id="Selectable-for-backup_subcomponents"></span><span id="selectable-for-backup_subcomponents"></span><span id="SELECTABLE-FOR-BACKUP_SUBCOMPONENTS"></span>Selectable-for-backup subcomponents<br/>             | Selectable-for-backup components with selectable-for-backup ancestors in their path.<br/>    |



 

In addition, any selectable-for-backup component—regardless of whether it has selectable-for-backup ancestors or not—defines a [*component set*](vssgloss-c.md) if other components have it as an ancestor in their logical paths.

The rules governing the selection of components for backup can be summarized as follows:

-   When any component without a selectable-for-backup ancestor in its logical path—whether the component is selectable-for-backup or nonselectable-for-backup—is included in a backup, it must be [*included explicitly*](vssgloss-e.md). This means that metadata for these components is added to the Backup Components Document.

    Requesters explicitly add these components using the [**IVssBackupComponents::AddComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent) method.

-   Nonselectable-for-backup subcomponents are always [*included implicitly*](vssgloss-i.md) in the backup. This means that metadata for these components is not part of the Backup Components Document.
-   Selectable-for-backup subcomponents are implicitly included if that ancestor is explicitly included in the backup. In this case, metadata for these components is not added to the Backup Components Document. If an implicitly selectable for backup subcomponent defines a component set, the members of that component set are also implicitly selected.
-   Selectable-for-backup subcomponents whose selectable-for-backup ancestor is not explicitly included in the backup can still be included explicitly by the requester using the [**IVssBackupComponents::AddComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent) method. The metadata for the component will then be added to the Backup Components Document. In addition, if a selectable-for-backup subcomponent defines a component set, the members of that component set are implicitly included in the backup.

The "MyWriter" case discussed in [Logical Pathing of Components](logical-pathing-of-components.md) can be used as an example to illustrate selectability for backup.



| Component name | Logical path            | Selectable for backup |
|----------------|-------------------------|-----------------------|
| "Executables"  | ""                      | N                     |
| "ConfigFiles"  | "Executables"           | N                     |
| "LicenseInfo"  | ""                      | Y                     |
| "Security"     | ""                      | Y                     |
| "UserInfo"     | "Security"              | N                     |
| "Certificates" | "Security"              | N                     |
| "writerData"   | ""                      | Y                     |
| "Set1"         | "writerData"            | N                     |
| "Jan"          | "writerData\\Set1"      | N                     |
| "Dec"          | "writerData\\Set1"      | N                     |
| "Set2"         | "writerData"            | N                     |
| "Jan"          | "writerData\\Set2"      | N                     |
| "Dec"          | "writerData\\Set2"      | N                     |
| "Query"        | "writerData\\QueryLogs" | N                     |
| "Usage"        | "writerData"            | Y                     |
| "Jan"          | "writerData\\Usage"     | N                     |
| "Dec"          | "writerData\\Usage"     | N                     |



 

Whenever "MyWriter" is backed up, explicitly including the "Executables" component using the [**IVssBackupComponents::AddComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent) method will implicitly include the "ConfigFiles" component.

The component "LicenseInfo" is a stand-alone selectable-for-backup component. It may be selected using the [**IVssBackupComponents::AddComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent) method at the discretion of the requester, but its selection will select no other components.

The selectable-for-backup component "Security" defines a simple component set containing two nonselectable-for-backup subcomponents, "UserInfo" and "Certificates". If "Security" is explicitly included for backup, then "UserInfo" and "Certificates" are always implicitly included as well. There is no way to include the subcomponents "UserInfo" or "Certificates" in a backup operation unless "Security" is included.

If the component "writerData" is selected, then the nonselectable-for-backup components "Set1", "Set2", and "Query" as well as the selectable-for-backup component "Usage" are implicitly selected. Each of these components has subcomponents that are implicitly selected for backup. None of their metadata will be added to the Backup Components Document.

If the component "writerData" is not selected, the nonselectable-for-backup components "Set1", "Set2", and "Query" are not included for backup.

However, requesters may choose to explicitly include the selectable for backup component "Usage". Metadata for this component will be added to the Backup Components Document. "Usage"'s subcomponents "Jan" and "Dec" will be implicitly added to the backup, but will not have their information added to the Backup Components Document.

Explicitly including a component for backup will create a corresponding [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) instance in the Backup Components Document.

A requester will retrieve information about explicitly included components from its Backup Components Document by examining those writers (using [**IVssBackupComponents::GetWriterComponents**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritercomponents)) included in its document and retrieving the stored [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) objects.

As neither the file set information (file specification, path, and recursion flag) of the components present in the Backup Components Document, nor any information about implicitly added components will be present, requesters will have to query Writer Metadata Documents to obtain full information about all components included in the Backup Components Document.

 

 




