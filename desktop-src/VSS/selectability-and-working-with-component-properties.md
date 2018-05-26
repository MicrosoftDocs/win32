---
Description: Working with implicitly selected components requires access to both the Backup Components Document and Writer Metadata Documents.
ms.assetid: ede51931-be50-4286-818b-0e6122247bdd
title: Selectability and Working with Component Properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Selectability and Working with Component Properties

Working with implicitly selected components requires access to both the Backup Components Document and Writer Metadata Documents.

There are two reasons for this:

-   The component data stored in the Backup Components Document (represented by the [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) interface) lacks access to component file set information—file specification, path, and recursion flag. (See [Working with the Backup Components Document](working-with-the-backup-components-document.md).)
-   Only components that are [*included explicitly*](vssgloss-e.md#base-vssgloss-explicit-component-inclusion) in the Backup Components Document during backup have their information directly stored in the Backup Components Document. Requesters and writers must use the information available through the [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) interface, in conjunction with [*logical path*](vssgloss-l.md#base-vssgloss-logical-path) information and Writer Metadata Documents to obtain information about, and set properties of, [*implicitly included*](vssgloss-i.md#base-vssgloss-implicit-component-inclusion) components.

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

While examining a writer's Writer Metadata Document (see [**IVssBackupComponents::GetWriterMetadata**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritermetadata?branch=master)) during backup, a requester should be storing a list of all components, their [*logical paths*](vssgloss-l.md#base-vssgloss-logical-path), and their file set information.

File set and excluded file information will be needed to determine a list of files for any (explicitly or implicitly) included component.

For nonselectable for backup components with no selectable for backup ancestors and selectable for backup components that do not define a [*component set*](vssgloss-c.md#base-vssgloss-component-set), only file set and excluded file information will be needed to identify all the component's candidates for backup, because these components do not define subcomponents.

For explicitly included selectable for backup components that define a component set, the file sets and exclude file information both for the defining component and all [*subcomponents*](vssgloss-s.md#base-vssgloss-subcomponent) needs to be used to select files for backup.

This means that backup sets for the components "Executables", "ConfigFiles", and "LicenseInfo" can be found only by examining the writer metadata for just these components using their instances of the [**IVssWMComponent**](/windows/win32/VsBackup/nl-vsbackup-ivsswmcomponent?branch=master) interface.

However, if writerData is explicitly included in the backup, you must examine its instance of the [**IVssWMComponent**](/windows/win32/VsBackup/nl-vsbackup-ivsswmcomponent?branch=master) interface and those for "Set1", "Jan" (with logical path "writerData\\Set1"), "Dec" (with logical path "writerData\\Set1"), "Set2", "Jan" (with logical path "writerData\\Set2"), "Dec" (with logical path "writerData\\Set2"), "Query", "Usage", "Jan" (with logical path "writerData\\Usage"), and "Dec" (with logical path "writerData\\Usage").

To do this, a requester will have to first identify that the component "writerData" (logical path "") is selectable. It will then have to scan all the other components managed by the writer to determine whether the first element in their logical path is "writerData". Those components that have "writerData" as the leading members of their logical path are identified as being subcomponents of "writerData" and are implicitly selected when it is explicitly selected.

In fact, a similar scan will need to be made to determine that no component has "LicenseInfo" as the leading member of its logical path, and thus that "LicenseInfo" has no subcomponents.

Because of the complexity of this mechanism in VSS, many requester writers may find it useful to create their own structures for storing component and backup set information for both explicitly and implicitly added components.

## Properties of Implicitly Included Components

During restore and backup operations, instances of the [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) and [**IVssBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) interfaces are used both to retrieve information about components, and to set or change component properties. However, only components explicitly included will have instances of the **IVssComponent** interface or be accessible to the **IVssBackupComponents** interface.

Some properties are component-set-wide in scope. These properties include the following:

-   Backup and restore status: <dl>

[**IVssBackupComponents::SetBackupSucceeded**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupsucceeded?branch=master)  
    [**IVssComponent::GetBackupSucceeded**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getbackupsucceeded?branch=master)  
    [**IVssBackupComponents::SetFileRestoreStatus**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setfilerestorestatus?branch=master)  
    [**IVssComponent::GetFileRestoreStatus**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getfilerestorestatus?branch=master)  
    </dl>
-   Backup and restore options: <dl>

[**IVssBackupComponents::SetBackupOptions**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupoptions?branch=master)  
    [**IVssComponent::GetBackupOptions**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getbackupoptions?branch=master)  
    [**IVssBackupComponents::SetRestoreOptions**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setrestoreoptions?branch=master)  
    [**IVssComponent::GetRestoreOptions**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getrestoreoptions?branch=master)  
    </dl>
-   Failure messages: <dl>

[**IVssComponent::SetPostRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setpostrestorefailuremsg?branch=master)  
    [**IVssComponent::SetPreRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setprerestorefailuremsg?branch=master)  
    [**IVssComponent::SetPostRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setpostrestorefailuremsg?branch=master)  
    [**IVssComponent::SetPreRestoreFailureMsg**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setprerestorefailuremsg?branch=master)  
    </dl>
-   Restore targets: <dl>

[**IVssComponent::SetRestoreTarget**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setrestoretarget?branch=master)  
    [**IVssComponent::GetRestoreTarget**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getrestoretarget?branch=master)  
    </dl>
-   Backup stamps: <dl>

[**IVssComponent::SetBackupStamp**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setbackupstamp?branch=master)  
    [**IVssComponent::GetBackupStamp**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getbackupstamp?branch=master)  
    </dl>
-   Additional metadata: <dl>

[**IVssComponent::SetRestoreMetadata**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setrestoremetadata?branch=master)  
    [**IVssComponent::GetRestoreMetadata**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getrestoremetadata?branch=master)  
    [**IVssComponent::SetBackupMetadata**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setbackupmetadata?branch=master)  
    [**IVssComponent::GetBackupMetadata**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getbackupmetadata?branch=master)  
    </dl>

Therefore, you use the instance of the [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) interface of a component set's defining member or use the defining member's name, type, and logical path with an [**IVssBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) method to set or retrieve properties for all the component set's members.

For this reason, component sets are treated as units. For instance, a backup of a component set is successful only if the backup of all of the file sets of all of its components is successful.

In the preceding example, suppose one file in the component "Jan" (with logical path "writerData\\Set2") is a member of the component set defined by "writerData". If one of "Jan"'s files failed to back up, a requester would use "writerData"'s information (its name "writerData", its path "", and its component type) as arguments when setting [**IVssBackupComponents::SetBackupSucceeded**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-setbackupsucceeded?branch=master) with **false** to indicate the component set's failure.

Similarly, the state returned by [**IVssComponent::GetBackupSucceeded**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getbackupsucceeded?branch=master) for "writerData"'s instance of the [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) interface applies not just to "writerData" but to all its subcomponents as well.

In addition, if a writer chose to change the restore target using [**IVssComponent::SetRestoreTarget**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-setrestoretarget?branch=master) of "writerData"'s instance of [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master), that would change the restore target for all the file sets of all of "writerData"'s subcomponents.

The following properties apply not component-wide, but to particular files or file sets:

-   Alternate location mappings: <dl>

[**IVssBackupComponents::AddAlternativeLocationMapping**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addalternativelocationmapping?branch=master)  
    [**IVssComponent::GetAlternateLocationMapping**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getalternatelocationmapping?branch=master)  
    [**IVssComponent::GetAlternateLocationMappingCount**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getalternatelocationmappingcount?branch=master)  
    </dl>
-   Differenced files: <dl>

[**IVssComponent::AddDifferencedFilesByLastModifyTime**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-adddifferencedfilesbylastmodifytime?branch=master)  
    [**IVssComponent::GetDifferencedFile**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getdifferencedfile?branch=master)  
    [**IVssComponent::GetDifferencedFilesCount**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getdifferencedfilescount?branch=master)  
    </dl>
-   Partial files: <dl>

[**IVssComponent::AddPartialFile**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-addpartialfile?branch=master)  
    [**IVssComponent::GetPartialFile**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getpartialfile?branch=master)  
    [**IVssComponent::GetPartialFileCount**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getpartialfilecount?branch=master)  
    </dl>
-   Directed targets: <dl>

[**IVssComponent::AddDirectedTarget**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-adddirectedtarget?branch=master)  
    [**IVssComponent::GetDirectedTarget**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getdirectedtarget?branch=master)  
    [**IVssComponent::GetDirectedTargetCount**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getdirectedtargetcount?branch=master)  
    </dl>
-   New targets: <dl>

[**IVssBackupComponents::AddNewTarget**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addnewtarget?branch=master)  
    [**IVssComponent::GetNewTarget**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getnewtarget?branch=master)  
    [**IVssComponent::GetNewTargetCount**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getnewtargetcount?branch=master)  
    </dl>

When a requester accesses these features for a subcomponent using the [**IVssBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) interface, it uses the component information for the component set's defining component, but the file or file set information for the subcomponent.

Likewise, if the property is accessible through the [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) interface, the instance corresponding to the defining subcomponent is used, but the file or file set arguments are taken from the subcomponent.

For instance, suppose the subcomponent "Jan" (with logical path "writerData\\Set2") had a file set with a path of "c:\\fred", a file specification of "\*.dat", and a recursive flag of **true** might have to be restored to an alternate location.

If this was the case, a requester would call [**IVssBackupComponents::AddAlternativeLocationMapping**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addalternativelocationmapping?branch=master), using "writerData"'s information (component type, a component name of "writeData", and a logical path of "") along with "Jan"'s file set information (path "c:\\fred", file specification "\*.dat", and recursion equals **true**).

Note that in this case the file set information must exactly match the file set information used by [**IVssCreateWriterMetadata::AddFilesToFileGroup**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-addfilestofilegroup?branch=master), [**IVssCreateWriterMetadata::AddDatabaseFiles**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabasefiles?branch=master), or [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](/windows/win32/VsWriter/nf-vswriter-ivsscreatewritermetadata-adddatabaselogfiles?branch=master) to add files to Jan.

Similarly, if a writer wanted to add a directed target to a file with a path of "c:\\ethel" and name "lucy.dat" managed by "Jan" (with logical path "writerData\\Set2"), it would use the [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) instance corresponding to "writerData", but "Jan"'s file information.

## Implicitly Included Components in the Restore Set

Components that were implicitly included in a backup can be explicitly included in a restore if they are selectable for restore. As noted in [Working with Selectability for Restore and Subcomponents](working-with-selectability-for-restore-and-subcomponents.md), such components are added to the Backup Components Document using the [**IVssBackupComponents::AddRestoreSubcomponent**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponents-addrestoresubcomponent?branch=master) method.

However, this does not create a new instance of the [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) interface, nor is the component directly accessible through the [**IVssBackupComponents**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponents?branch=master) interface.

Instead, a component explicitly included for restore, but implicitly included for backup, must be accessed through an instance of the [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) interface corresponding to the component that defined the component set of which it was a member upon backup.

For example, to explicitly include for restore "Set1", a subcomponent of the selectable for backup component "writerData", you would obtain information about it by calling the [**IVssComponent::GetRestoreSubcomponent**](/windows/win32/VsWriter/nf-vswriter-ivsscomponent-getrestoresubcomponent?branch=master) method of "writerData"'s instance of the [**IVssComponent**](/windows/win32/VsWriter/nl-vswriter-ivsscomponent?branch=master) interface.

 

 



