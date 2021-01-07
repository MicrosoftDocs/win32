---
description: Working with implicitly selected components requires access to both the Backup Components Document and Writer Metadata Documents.
ms.assetid: ede51931-be50-4286-818b-0e6122247bdd
title: Selectability and Working with Component Properties
ms.topic: article
ms.date: 05/31/2018
---

# Selectability and Working with Component Properties

Working with implicitly selected components requires access to both the Backup Components Document and Writer Metadata Documents.

There are two reasons for this:

-   The component data stored in the Backup Components Document (represented by the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface) lacks access to component file set information—file specification, path, and recursion flag. (See [Working with the Backup Components Document](working-with-the-backup-components-document.md).)
-   Only components that are [*included explicitly*](vssgloss-e.md) in the Backup Components Document during backup have their information directly stored in the Backup Components Document. Requesters and writers must use the information available through the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface, in conjunction with [*logical path*](vssgloss-l.md) information and Writer Metadata Documents to obtain information about, and set properties of, [*implicitly included*](vssgloss-i.md) components.

The "MyWriter" case discussed in [Logical Pathing of Components](logical-pathing-of-components.md) can be used to illustrate selectability for backup.



| Component name | Logical path            | Selectable for backup | Selectable for restore | Explicitly included |
|----------------|-------------------------|-----------------------|------------------------|---------------------|
| "Executables"  | ""                      | N                     | N                      | Y                   |
| "ConfigFiles"  | "Executables"           | N                     | N                      | Y                   |
| "LicenseInfo"  | ""                      | Y                     | N                      | Y                   |
| "Security"     | ""                      | Y                     | N                      | Y                   |
| "UserInfo"     | "Security"              | N                     | N                      | N                   |
| "Certificates" | "Security"              | N                     | N                      | N                   |
| "writerData"   | ""                      | Y                     | Y                      | Y                   |
| "Set1"         | "writerData"            | N                     | Y                      | N                   |
| "Jan"          | "writerData\\Set1"      | N                     | N                      | N                   |
| "Dec"          | "writerData\\Set1"      | N                     | N                      | N                   |
| "Set2"         | "writerData"            | N                     | Y                      | N                   |
| "Jan"          | "writerData\\Set2"      | N                     | N                      | N                   |
| "Dec"          | "writerData\\Set2"      | N                     | N                      | N                   |
| "Query"        | "writerData\\QueryLogs" | N                     | N                      | N                   |
| "Usage"        | "writerData"            | Y                     | Y                      | N                   |
| "Jan"          | "writerData\\Usage"     | N                     | N                      | N                   |
| "Dec"          | "writerData\\Usage"     | N                     | N                      | N                   |



 

## Implicitly Included Components in the Backup Set

While examining a writer's Writer Metadata Document (see [**IVssBackupComponents::GetWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritermetadata)) during backup, a requester should be storing a list of all components, their [*logical paths*](vssgloss-l.md), and their file set information.

File set and excluded file information will be needed to determine a list of files for any (explicitly or implicitly) included component.

For nonselectable for backup components with no selectable for backup ancestors and selectable for backup components that do not define a [*component set*](vssgloss-c.md), only file set and excluded file information will be needed to identify all the component's candidates for backup, because these components do not define subcomponents.

For explicitly included selectable for backup components that define a component set, the file sets and exclude file information both for the defining component and all [*subcomponents*](vssgloss-s.md) needs to be used to select files for backup.

This means that backup sets for the components "Executables", "ConfigFiles", and "LicenseInfo" can be found only by examining the writer metadata for just these components using their instances of the [**IVssWMComponent**](/windows/desktop/api/VsBackup/nl-vsbackup-ivsswmcomponent) interface.

However, if writerData is explicitly included in the backup, you must examine its instance of the [**IVssWMComponent**](/windows/desktop/api/VsBackup/nl-vsbackup-ivsswmcomponent) interface and those for "Set1", "Jan" (with logical path "writerData\\Set1"), "Dec" (with logical path "writerData\\Set1"), "Set2", "Jan" (with logical path "writerData\\Set2"), "Dec" (with logical path "writerData\\Set2"), "Query", "Usage", "Jan" (with logical path "writerData\\Usage"), and "Dec" (with logical path "writerData\\Usage").

To do this, a requester will have to first identify that the component "writerData" (logical path "") is selectable. It will then have to scan all the other components managed by the writer to determine whether the first element in their logical path is "writerData". Those components that have "writerData" as the leading members of their logical path are identified as being subcomponents of "writerData" and are implicitly selected when it is explicitly selected.

In fact, a similar scan will need to be made to determine that no component has "LicenseInfo" as the leading member of its logical path, and thus that "LicenseInfo" has no subcomponents.

Because of the complexity of this mechanism in VSS, many requester writers may find it useful to create their own structures for storing component and backup set information for both explicitly and implicitly added components.

## Properties of Implicitly Included Components

During restore and backup operations, instances of the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) and [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interfaces are used both to retrieve information about components, and to set or change component properties. However, only components explicitly included will have instances of the **IVssComponent** interface or be accessible to the **IVssBackupComponents** interface.

Some properties are component-set-wide in scope. These properties include the following:

-   Backup and restore status: <dl>

[**IVssBackupComponents::SetBackupSucceeded**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupsucceeded)  
    [**IVssComponent::GetBackupSucceeded**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getbackupsucceeded)  
    [**IVssBackupComponents::SetFileRestoreStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setfilerestorestatus)  
    [**IVssComponent::GetFileRestoreStatus**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getfilerestorestatus)  
    </dl>
-   Backup and restore options: <dl>

[**IVssBackupComponents::SetBackupOptions**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupoptions)  
    [**IVssComponent::GetBackupOptions**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getbackupoptions)  
    [**IVssBackupComponents::SetRestoreOptions**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setrestoreoptions)  
    [**IVssComponent::GetRestoreOptions**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getrestoreoptions)  
    </dl>
-   Failure messages: <dl>

[**IVssComponent::SetPostRestoreFailureMsg**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setpostrestorefailuremsg)  
    [**IVssComponent::SetPreRestoreFailureMsg**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setprerestorefailuremsg)  
    [**IVssComponent::SetPostRestoreFailureMsg**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setpostrestorefailuremsg)  
    [**IVssComponent::SetPreRestoreFailureMsg**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setprerestorefailuremsg)  
    </dl>
-   Restore targets: <dl>

[**IVssComponent::SetRestoreTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setrestoretarget)  
    [**IVssComponent::GetRestoreTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getrestoretarget)  
    </dl>
-   Backup stamps: <dl>

[**IVssComponent::SetBackupStamp**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setbackupstamp)  
    [**IVssComponent::GetBackupStamp**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getbackupstamp)  
    </dl>
-   Additional metadata: <dl>

[**IVssComponent::SetRestoreMetadata**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setrestoremetadata)  
    [**IVssComponent::GetRestoreMetadata**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getrestoremetadata)  
    [**IVssComponent::SetBackupMetadata**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setbackupmetadata)  
    [**IVssComponent::GetBackupMetadata**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getbackupmetadata)  
    </dl>

Therefore, you use the instance of the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface of a component set's defining member or use the defining member's name, type, and logical path with an [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) method to set or retrieve properties for all the component set's members.

For this reason, component sets are treated as units. For instance, a backup of a component set is successful only if the backup of all of the file sets of all of its components is successful.

In the preceding example, suppose one file in the component "Jan" (with logical path "writerData\\Set2") is a member of the component set defined by "writerData". If one of "Jan"'s files failed to back up, a requester would use "writerData"'s information (its name "writerData", its path "", and its component type) as arguments when setting [**IVssBackupComponents::SetBackupSucceeded**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupsucceeded) with **false** to indicate the component set's failure.

Similarly, the state returned by [**IVssComponent::GetBackupSucceeded**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getbackupsucceeded) for "writerData"'s instance of the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface applies not just to "writerData" but to all its subcomponents as well.

In addition, if a writer chose to change the restore target using [**IVssComponent::SetRestoreTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-setrestoretarget) of "writerData"'s instance of [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent), that would change the restore target for all the file sets of all of "writerData"'s subcomponents.

The following properties apply not component-wide, but to particular files or file sets:

-   Alternate location mappings: <dl>

[**IVssBackupComponents::AddAlternativeLocationMapping**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addalternativelocationmapping)  
    [**IVssComponent::GetAlternateLocationMapping**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getalternatelocationmapping)  
    [**IVssComponent::GetAlternateLocationMappingCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getalternatelocationmappingcount)  
    </dl>
-   Differenced files: <dl>

[**IVssComponent::AddDifferencedFilesByLastModifyTime**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-adddifferencedfilesbylastmodifytime)  
    [**IVssComponent::GetDifferencedFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getdifferencedfile)  
    [**IVssComponent::GetDifferencedFilesCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getdifferencedfilescount)  
    </dl>
-   Partial files: <dl>

[**IVssComponent::AddPartialFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-addpartialfile)  
    [**IVssComponent::GetPartialFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getpartialfile)  
    [**IVssComponent::GetPartialFileCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getpartialfilecount)  
    </dl>
-   Directed targets: <dl>

[**IVssComponent::AddDirectedTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-adddirectedtarget)  
    [**IVssComponent::GetDirectedTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getdirectedtarget)  
    [**IVssComponent::GetDirectedTargetCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getdirectedtargetcount)  
    </dl>
-   New targets: <dl>

[**IVssBackupComponents::AddNewTarget**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addnewtarget)  
    [**IVssComponent::GetNewTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getnewtarget)  
    [**IVssComponent::GetNewTargetCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getnewtargetcount)  
    </dl>

When a requester accesses these features for a subcomponent using the [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface, it uses the component information for the component set's defining component, but the file or file set information for the subcomponent.

Likewise, if the property is accessible through the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface, the instance corresponding to the defining subcomponent is used, but the file or file set arguments are taken from the subcomponent.

For instance, suppose the subcomponent "Jan" (with logical path "writerData\\Set2") had a file set with a path of "c:\\fred", a file specification of "\*.dat", and a recursive flag of **true** might have to be restored to an alternate location.

If this was the case, a requester would call [**IVssBackupComponents::AddAlternativeLocationMapping**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addalternativelocationmapping), using "writerData"'s information (component type, a component name of "writeData", and a logical path of "") along with "Jan"'s file set information (path "c:\\fred", file specification "\*.dat", and recursion equals **true**).

Note that in this case the file set information must exactly match the file set information used by [**IVssCreateWriterMetadata::AddFilesToFileGroup**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-addfilestofilegroup), [**IVssCreateWriterMetadata::AddDatabaseFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabasefiles), or [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles) to add files to Jan.

Similarly, if a writer wanted to add a directed target to a file with a path of "c:\\ethel" and name "lucy.dat" managed by "Jan" (with logical path "writerData\\Set2"), it would use the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) instance corresponding to "writerData", but "Jan"'s file information.

## Implicitly Included Components in the Restore Set

Components that were implicitly included in a backup can be explicitly included in a restore if they are selectable for restore. As noted in [Working with Selectability for Restore and Subcomponents](working-with-selectability-for-restore-and-subcomponents.md), such components are added to the Backup Components Document using the [**IVssBackupComponents::AddRestoreSubcomponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addrestoresubcomponent) method.

However, this does not create a new instance of the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface, nor is the component directly accessible through the [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) interface.

Instead, a component explicitly included for restore, but implicitly included for backup, must be accessed through an instance of the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface corresponding to the component that defined the component set of which it was a member upon backup.

For example, to explicitly include for restore "Set1", a subcomponent of the selectable for backup component "writerData", you would obtain information about it by calling the [**IVssComponent::GetRestoreSubcomponent**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getrestoresubcomponent) method of "writerData"'s instance of the [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) interface.

 

 



