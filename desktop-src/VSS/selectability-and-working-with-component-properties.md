---
Description: 'Working with implicitly selected components requires access to both the Backup Components Document and Writer Metadata Documents.'
ms.assetid: 'ede51931-be50-4286-818b-0e6122247bdd'
title: Selectability and Working with Component Properties
---

# Selectability and Working with Component Properties

Working with implicitly selected components requires access to both the Backup Components Document and Writer Metadata Documents.

There are two reasons for this:

-   The component data stored in the Backup Components Document (represented by the [**IVssComponent**](ivsscomponent.md) interface) lacks access to component file set information—file specification, path, and recursion flag. (See [Working with the Backup Components Document](working-with-the-backup-components-document.md).)
-   Only components that are [*included explicitly*](vssgloss-e.md#base-vssgloss-explicit-component-inclusion) in the Backup Components Document during backup have their information directly stored in the Backup Components Document. Requesters and writers must use the information available through the [**IVssComponent**](ivsscomponent.md) interface, in conjunction with [*logical path*](vssgloss-l.md#base-vssgloss-logical-path) information and Writer Metadata Documents to obtain information about, and set properties of, [*implicitly included*](vssgloss-i.md#base-vssgloss-implicit-component-inclusion) components.

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

While examining a writer's Writer Metadata Document (see [**IVssBackupComponents::GetWriterMetadata**](ivssbackupcomponents-getwritermetadata.md)) during backup, a requester should be storing a list of all components, their [*logical paths*](vssgloss-l.md#base-vssgloss-logical-path), and their file set information.

File set and excluded file information will be needed to determine a list of files for any (explicitly or implicitly) included component.

For nonselectable for backup components with no selectable for backup ancestors and selectable for backup components that do not define a [*component set*](vssgloss-c.md#base-vssgloss-component-set), only file set and excluded file information will be needed to identify all the component's candidates for backup, because these components do not define subcomponents.

For explicitly included selectable for backup components that define a component set, the file sets and exclude file information both for the defining component and all [*subcomponents*](vssgloss-s.md#base-vssgloss-subcomponent) needs to be used to select files for backup.

This means that backup sets for the components "Executables", "ConfigFiles", and "LicenseInfo" can be found only by examining the writer metadata for just these components using their instances of the [**IVssWMComponent**](ivsswmcomponent.md) interface.

However, if writerData is explicitly included in the backup, you must examine its instance of the [**IVssWMComponent**](ivsswmcomponent.md) interface and those for "Set1", "Jan" (with logical path "writerData\\Set1"), "Dec" (with logical path "writerData\\Set1"), "Set2", "Jan" (with logical path "writerData\\Set2"), "Dec" (with logical path "writerData\\Set2"), "Query", "Usage", "Jan" (with logical path "writerData\\Usage"), and "Dec" (with logical path "writerData\\Usage").

To do this, a requester will have to first identify that the component "writerData" (logical path "") is selectable. It will then have to scan all the other components managed by the writer to determine whether the first element in their logical path is "writerData". Those components that have "writerData" as the leading members of their logical path are identified as being subcomponents of "writerData" and are implicitly selected when it is explicitly selected.

In fact, a similar scan will need to be made to determine that no component has "LicenseInfo" as the leading member of its logical path, and thus that "LicenseInfo" has no subcomponents.

Because of the complexity of this mechanism in VSS, many requester writers may find it useful to create their own structures for storing component and backup set information for both explicitly and implicitly added components.

## Properties of Implicitly Included Components

During restore and backup operations, instances of the [**IVssComponent**](ivsscomponent.md) and [**IVssBackupComponents**](ivssbackupcomponents.md) interfaces are used both to retrieve information about components, and to set or change component properties. However, only components explicitly included will have instances of the **IVssComponent** interface or be accessible to the **IVssBackupComponents** interface.

Some properties are component-set-wide in scope. These properties include the following:

-   Backup and restore status: <dl>

[**IVssBackupComponents::SetBackupSucceeded**](ivssbackupcomponents-setbackupsucceeded.md)  
    [**IVssComponent::GetBackupSucceeded**](ivsscomponent-getbackupsucceeded.md)  
    [**IVssBackupComponents::SetFileRestoreStatus**](ivssbackupcomponents-setfilerestorestatus.md)  
    [**IVssComponent::GetFileRestoreStatus**](ivsscomponent-getfilerestorestatus.md)  
    </dl>
-   Backup and restore options: <dl>

[**IVssBackupComponents::SetBackupOptions**](ivssbackupcomponents-setbackupoptions.md)  
    [**IVssComponent::GetBackupOptions**](ivsscomponent-getbackupoptions.md)  
    [**IVssBackupComponents::SetRestoreOptions**](ivssbackupcomponents-setrestoreoptions.md)  
    [**IVssComponent::GetRestoreOptions**](ivsscomponent-getrestoreoptions.md)  
    </dl>
-   Failure messages: <dl>

[**IVssComponent::SetPostRestoreFailureMsg**](ivsscomponent-setpostrestorefailuremsg.md)  
    [**IVssComponent::SetPreRestoreFailureMsg**](ivsscomponent-setprerestorefailuremsg.md)  
    [**IVssComponent::SetPostRestoreFailureMsg**](ivsscomponent-setpostrestorefailuremsg.md)  
    [**IVssComponent::SetPreRestoreFailureMsg**](ivsscomponent-setprerestorefailuremsg.md)  
    </dl>
-   Restore targets: <dl>

[**IVssComponent::SetRestoreTarget**](ivsscomponent-setrestoretarget.md)  
    [**IVssComponent::GetRestoreTarget**](ivsscomponent-getrestoretarget.md)  
    </dl>
-   Backup stamps: <dl>

[**IVssComponent::SetBackupStamp**](ivsscomponent-setbackupstamp.md)  
    [**IVssComponent::GetBackupStamp**](ivsscomponent-getbackupstamp.md)  
    </dl>
-   Additional metadata: <dl>

[**IVssComponent::SetRestoreMetadata**](ivsscomponent-setrestoremetadata.md)  
    [**IVssComponent::GetRestoreMetadata**](ivsscomponent-getrestoremetadata.md)  
    [**IVssComponent::SetBackupMetadata**](ivsscomponent-setbackupmetadata.md)  
    [**IVssComponent::GetBackupMetadata**](ivsscomponent-getbackupmetadata.md)  
    </dl>

Therefore, you use the instance of the [**IVssComponent**](ivsscomponent.md) interface of a component set's defining member or use the defining member's name, type, and logical path with an [**IVssBackupComponents**](ivssbackupcomponents.md) method to set or retrieve properties for all the component set's members.

For this reason, component sets are treated as units. For instance, a backup of a component set is successful only if the backup of all of the file sets of all of its components is successful.

In the preceding example, suppose one file in the component "Jan" (with logical path "writerData\\Set2") is a member of the component set defined by "writerData". If one of "Jan"'s files failed to back up, a requester would use "writerData"'s information (its name "writerData", its path "", and its component type) as arguments when setting [**IVssBackupComponents::SetBackupSucceeded**](ivssbackupcomponents-setbackupsucceeded.md) with **false** to indicate the component set's failure.

Similarly, the state returned by [**IVssComponent::GetBackupSucceeded**](ivsscomponent-getbackupsucceeded.md) for "writerData"'s instance of the [**IVssComponent**](ivsscomponent.md) interface applies not just to "writerData" but to all its subcomponents as well.

In addition, if a writer chose to change the restore target using [**IVssComponent::SetRestoreTarget**](ivsscomponent-setrestoretarget.md) of "writerData"'s instance of [**IVssComponent**](ivsscomponent.md), that would change the restore target for all the file sets of all of "writerData"'s subcomponents.

The following properties apply not component-wide, but to particular files or file sets:

-   Alternate location mappings: <dl>

[**IVssBackupComponents::AddAlternativeLocationMapping**](ivssbackupcomponents-addalternativelocationmapping.md)  
    [**IVssComponent::GetAlternateLocationMapping**](ivsscomponent-getalternatelocationmapping.md)  
    [**IVssComponent::GetAlternateLocationMappingCount**](ivsscomponent-getalternatelocationmappingcount.md)  
    </dl>
-   Differenced files: <dl>

[**IVssComponent::AddDifferencedFilesByLastModifyTime**](ivsscomponent-adddifferencedfilesbylastmodifytime.md)  
    [**IVssComponent::GetDifferencedFile**](ivsscomponent-getdifferencedfile.md)  
    [**IVssComponent::GetDifferencedFilesCount**](ivsscomponent-getdifferencedfilescount.md)  
    </dl>
-   Partial files: <dl>

[**IVssComponent::AddPartialFile**](ivsscomponent-addpartialfile.md)  
    [**IVssComponent::GetPartialFile**](ivsscomponent-getpartialfile.md)  
    [**IVssComponent::GetPartialFileCount**](ivsscomponent-getpartialfilecount.md)  
    </dl>
-   Directed targets: <dl>

[**IVssComponent::AddDirectedTarget**](ivsscomponent-adddirectedtarget.md)  
    [**IVssComponent::GetDirectedTarget**](ivsscomponent-getdirectedtarget.md)  
    [**IVssComponent::GetDirectedTargetCount**](ivsscomponent-getdirectedtargetcount.md)  
    </dl>
-   New targets: <dl>

[**IVssBackupComponents::AddNewTarget**](ivssbackupcomponents-addnewtarget.md)  
    [**IVssComponent::GetNewTarget**](ivsscomponent-getnewtarget.md)  
    [**IVssComponent::GetNewTargetCount**](ivsscomponent-getnewtargetcount.md)  
    </dl>

When a requester accesses these features for a subcomponent using the [**IVssBackupComponents**](ivssbackupcomponents.md) interface, it uses the component information for the component set's defining component, but the file or file set information for the subcomponent.

Likewise, if the property is accessible through the [**IVssComponent**](ivsscomponent.md) interface, the instance corresponding to the defining subcomponent is used, but the file or file set arguments are taken from the subcomponent.

For instance, suppose the subcomponent "Jan" (with logical path "writerData\\Set2") had a file set with a path of "c:\\fred", a file specification of "\*.dat", and a recursive flag of **true** might have to be restored to an alternate location.

If this was the case, a requester would call [**IVssBackupComponents::AddAlternativeLocationMapping**](ivssbackupcomponents-addalternativelocationmapping.md), using "writerData"'s information (component type, a component name of "writeData", and a logical path of "") along with "Jan"'s file set information (path "c:\\fred", file specification "\*.dat", and recursion equals **true**).

Note that in this case the file set information must exactly match the file set information used by [**IVssCreateWriterMetadata::AddFilesToFileGroup**](ivsscreatewritermetadata-addfilestofilegroup.md), [**IVssCreateWriterMetadata::AddDatabaseFiles**](ivsscreatewritermetadata-adddatabasefiles.md), or [**IVssCreateWriterMetadata::AddDatabaseLogFiles**](ivsscreatewritermetadata-adddatabaselogfiles.md) to add files to Jan.

Similarly, if a writer wanted to add a directed target to a file with a path of "c:\\ethel" and name "lucy.dat" managed by "Jan" (with logical path "writerData\\Set2"), it would use the [**IVssComponent**](ivsscomponent.md) instance corresponding to "writerData", but "Jan"'s file information.

## Implicitly Included Components in the Restore Set

Components that were implicitly included in a backup can be explicitly included in a restore if they are selectable for restore. As noted in [Working with Selectability for Restore and Subcomponents](working-with-selectability-for-restore-and-subcomponents.md), such components are added to the Backup Components Document using the [**IVssBackupComponents::AddRestoreSubcomponent**](ivssbackupcomponents-addrestoresubcomponent.md) method.

However, this does not create a new instance of the [**IVssComponent**](ivsscomponent.md) interface, nor is the component directly accessible through the [**IVssBackupComponents**](ivssbackupcomponents.md) interface.

Instead, a component explicitly included for restore, but implicitly included for backup, must be accessed through an instance of the [**IVssComponent**](ivsscomponent.md) interface corresponding to the component that defined the component set of which it was a member upon backup.

For example, to explicitly include for restore "Set1", a subcomponent of the selectable for backup component "writerData", you would obtain information about it by calling the [**IVssComponent::GetRestoreSubcomponent**](ivsscomponent-getrestoresubcomponent.md) method of "writerData"'s instance of the [**IVssComponent**](ivsscomponent.md) interface.

 

 



