---
description: The Test Writer is a utility that you can use to test VSS requester applications.
ms.assetid: 02434cb9-390c-4cf0-9941-b833ace55685
title: VSS Test Writer Tool
ms.topic: article
ms.date: 05/31/2018
---

# VSS Test Writer Tool

The Test Writer is a utility that you can use to test VSS requester applications. This writer can be configured to perform almost all of the actions that a VSS writer can perform. In addition, the Test Writer performs extensive checks to ensure that the requester has dealt with these writer actions correctly.

Each instance of the writer is initialized with an XML configuration file that describes exactly what components the writer will report on, and how the writer behaves. The writer can be configured to report on various types of scenarios, including more complicated scenarios using the incremental and differential interfaces. The writer will perform checks at various points during the process to ensure that the requester is behaving in a proper manner. After the restore is completed, the writer will check that all necessary files have been restored without corruption. The writer can also be configured to perform other operations such as failing specific events.

> [!Note]  
> This tool is included in the Microsoft Windows Software Development Kit (SDK) for Windows Vista and later. You can download the Windows SDK from [https://msdn.microsoft.com/windowsvista](https://msdn.microsoft.com/windows/default.aspx).

 

In the Windows SDK installation, the VssSampleProvider tool can be found in `%Program Files(x86)%\Windows Kits\8.1\bin\x64` (for 64-bit Windows) and `%Program Files(x86)%\Windows Kits\8.1\bin\x86`.

## Running the Test Writer Tool

To start the Test Writer, type the following at the command prompt:

**vswriter.exe** *config-file*

where *config-file* is the path to a configuration file that specifies the behavior of this writer.

To stop the Test Writer, press CTRL+C.

Multiple instances of the Test Writer can be run at the same time. However, each instance of the writer will report the same writer class ID (though a different writer instance ID), so logical paths and component names must be unique across all simultaneously running instances of the writer.

To ensure that the writer can properly check that the requester has honored the exclude file specifications, all files that were backed up should be deleted from the original volume before attempting to restore them. It is recommended that a template of each writer scenario be stored, so the scenario can be easily recreated.

## Using a Configuration File

The following sample configuration file, vswriter\_config.xml, can be found in `%ProgramFiles%\Microsoft SDKs\Windows\v7.0\bin\vsstools` on x86 platforms and `%ProgramFiles%\Microsoft SDKs\Windows\v7.0\bin\x64\vsstools` on x64 platforms.

``` syntax
<TestWriter usage="USER_DATA">

    <RestoreMethod method="RESTORE_IF_CAN_BE_REPLACED"
                   writerRestore="always"
                   rebootRequired="no" />

    <ExcludeFile path="c:\writerData\notTheseFiles" 
                 filespec="excludeThisFile.txt" 
                 recursive="no"/>

    <Component componentType="filegroup"
               componentName="TestFiles">
        <ComponentFile path="c:\writerData\myFilesHere" 
                       filespec="*"
                       recursive="no" />
    </Component>

</TestWriter>
```

The root element in this configuration file is named TestWriter. All other elements are arranged under the TestWriter element.

One of the attributes associated with TestWriter is the usage attribute. This attribute specifies the usage type reported through [**IVssExamineWriterMetadata::GetIdentity**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getidentity). One of the possible values for this attribute is USER\_DATA.

The first child element of the root element must always be a RestoreMethod element. This element specifies the following:

-   The restore method (in this case, RESTORE\_IF\_CAN\_BE\_REPLACED)
-   Whether the writer requires restore events (in this case, always)
-   Whether a reboot is required after the writer is restored (in this case, no)

This element can optionally specify an alternate-location mapping. (In this case, no alternate location is specified.)

The second child element is an ExcludeFile element. This element causes the writer to exclude a file or a set of files from backup.

The third child element is a Component element. This element causes the writer to add a component to its metadata. A Component element contains attributes to describe the component and child elements to describe the content of the component, such as the following:

-   componentType to indicate whether this is a filegroup or a database
-   logicalPath for the component logical path
-   componentName for the name of the component
-   selectable to indicate selectable-for-backup status

The Component element also has a child element named ComponentFile to add a file specification to this component. (A Component element can have an arbitrary number of ComponentFile elements that can be specified for each component.) This ComponentFile element has the following attributes:

-   path="c:\\writerData\\myFilesHere"
-   filespec="\*"
-   recursive="no"

Although the Test Writer verifies requester behavior, it does not verify that the configuration file always maintains the documented semantics for a writer. There are many operations that a well-behaved writer should not do (such as report the same file in multiple components), and it is up to the author of the XML configuration file to maintain these semantics.

## Configuring Writer Attributes

The TestWriter root element contains attributes that determine various behaviors of the writer. Some of the behaviors that can be altered are the following:




| Attribute | Description | 
|-----------|-------------|
| <span id="verbosity"></span><span id="VERBOSITY"></span>verbosity<br /> | The writer prints the status to the console as it receives events and processes them. The level of verbosity displayed is specified by the verbosity attribute. There are three verbosity levels to choose from:<br /><dl><dt><span id="low"></span><span id="LOW"></span>low</dt><dd> Only failures in the writer or incorrect behavior from the requester will be printed.<br /></dd><dt><span id="medium"></span><span id="MEDIUM"></span>medium</dt><dd> Everything at the low verbosity level is printed in addition to extra status information such as when events are received. This is the default level.<br /></dd><dt><span id="high"></span><span id="HIGH"></span>high</dt><dd> Detailed status information about the operation of the writer is reported.<br /></dd></dl> | 
| <span id="deleteFiles"></span><span id="deletefiles"></span><span id="DELETEFILES"></span>deleteFiles<br /> | To perform extra verification, set this attribute to "yes" to cause the writer to delete all of its files immediately after the volume shadow copy is created. The requester must then copy the files from the shadow copy, because they no longer exist on the original volume. <br /><blockquote>[!Note]<br />In the case of spit writers, the files are deleted from the original location after the spit but before the shadow copy is created. After the shadow copy is created, the files are deleted from the spit directory.</blockquote><br /> | 
| <span id="deletePartialFiles"></span><span id="deletepartialfiles"></span><span id="DELETEPARTIALFILES"></span>deletePartialFiles<br /> | To delete partial files, set this attribute to "yes".<br /> | 
| <span id="deleteDifferencedFiles"></span><span id="deletedifferencedfiles"></span><span id="DELETEDIFFERENCEDFILES"></span>deleteDifferencedFiles<br /> | To delete differenced files, set this attribute to "yes".<br /> | 
| <span id="checkIncludes"></span><span id="checkincludes"></span><span id="CHECKINCLUDES"></span>checkIncludes<br /> | Set this attribute to "yes" to cause the writer to check that every file that has been backed up has been restored to an appropriate location, and that the file has not been corrupted. Partial files and differenced files are also correctly handled.<br /> | 
| <span id="checkExcludes"></span><span id="checkexcludes"></span><span id="CHECKEXCLUDES"></span>checkExcludes<br /> | Set this attribute to "yes" to cause the writer to check that files matching a file specification in the exclude list are not restored. For this to function correctly, the restore directories must be emptied prior to restore.<br /> | 




 

## Specifying Alternate Location Mappings

An alternate location mapping specifies a location to restore to if the restore method is VSS\_WRE\_RESTORE\_TO\_ALTERNATE\_LOCATION or if normal restore of a component fails. A writer can report its alternate location mappings to the requester by using the [**IVssExamineWriterMetadata::GetAlternateLocationMapping**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getalternatelocationmapping) method. You can add alternate location mappings to the Test Writer configuration file by adding AlternateLocationMapping subelements to the RestoreMethod element.

The following RestoreMethod element contains a AlternateLocationMapping subelement.

``` syntax
<RestoreMethod method="RESTORE_IF_CAN_REPLACE"
              writerRestore="always"
              rebootRequired="no">
    <AlternateLocationMapping path="c:\files"
                              filespec="*.txt"
                              recursive="no"
                              alternatePath="c:\altfiles"/>
</RestoreMethod>
```

This example specifies that the requester should first attempt to restore all of the files matching c:\\files\\\*.txt to the c:\\files directory. If one of these files cannot be replaced, the requester should restore all the files to the c:\\altfiles directory instead. The requester should save this alternate location mapping by using the [**IVssBackupComponents::AddAlternativeLocationMapping**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addalternativelocationmapping) method. If the Test Writer is configured to check whether files have been restored, it will also check whether the requester has called **AddAlternativeLocationMapping**.

## Specifying Files to Be Excluded

Every writer can specify a list of file specifications that specify files for the requester to exclude from backup. You can add these file specifications to the Test Writer configuration file by adding ExcludeFile subelements to the TestWriter root element.

Here is an example of an ExcludeFile subelement that excludes all files in the C:\\files directory that match C:\\temp\*.\*.

``` syntax
    <ExcludeFile path="c:\files" 
                 filespec="temp*.*" 
                 recursive="no"/>
```

## Backing Up Spit Writers

Many writers act as "spit writers." A spit writer creates intermediate files, or "spit files," based on an original set of files, and puts the spit files in an alternate location at backup time. The writer uses the [**IVssWMFiledesc::GetAlternateLocation**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getalternatelocation) method to notify the requester that it should back these files up from the alternate location. However, these files should still be restored to the active location of the original files. The Test Writer can be configured to act as a spit writer for a particular file specification.

The following ComponentFile element contains an alternatePath attribute:

``` syntax
    <ComponentFile path="c:\files"
                   filespec="*.txt"
                   recursive="no"
                   alternatePath="c:\files\spit" />
```

This example configures the Test Writer to copy all files matching c:\\files\\\*.txt to the c:\\files\\spit directory immediately before the volume shadow copy is created. The requester must back up the files from the c:\\files\\spit directory. If the Test Writer is configured to delete files, it deletes the original files before the shadow copy is created, so they do not appear in the c:\\files directory on the shadow copy volume. In this case, the files in c:\\files\\spit are deleted after the shadow copy is created, so they must be backed up from the c:\\files\\spit directory on the shadow copy volume.

## Reporting Component Dependencies

Writers can specify a dependency between a local component and a component that exists in another writer. These dependencies are reported to the requester using [**IVssWMComponent::GetDependency**](/windows/desktop/api/VsBackup/nf-vsbackup-ivsswmcomponent-getdependency). The Test Writer can be configured to report these dependencies by adding one or more Dependency subelements to the Component element.

The following Component element contains a Dependency subelement:

``` syntax
    <Component componentType="filegroup"
               logicalPath=""
               componentName="WriterComponent"
               selectable="yes">
         <Dependency writerId="<GUID of target writer>"
                     logicalPath="ComponentPath"
                     componentName="Writer2Component" />
    </Component>
```

The dependency is specified as attributes of the Dependency element. writerId is the class id of the writer containing the target of the dependency, logicalPath is the logical path to the component in that writer, and componentName is the name of the component. In this case, if the requester is backing up "WriterComponent" in the current writer, it should also back up the component "ComponentPath\\Writer2Component" in the target writer.

> [!Note]  
> The Test Writer performs no checking to ensure dependencies are honored.

 

## Failing Events

The Test Writer can be configured to fail any of the normal events that a writer receives. These events are as follows:



| Event                                                                                                                                    | Description                                                                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Identify"></span><span id="identify"></span><span id="IDENTIFY"></span>Identify<br/>                                     | Received as a response to a [**IVssBackupComponents::GatherWriterMetadata**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwritermetadata) call. Failure here will cause the writer to not be reported.<br/>                                                                 |
| <span id="PrepareForBackup"></span><span id="prepareforbackup"></span><span id="PREPAREFORBACKUP"></span>PrepareForBackup<br/>     | Received as a response to the requester calling [**IVssBackupComponents::PrepareForBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup).<br/>                                                                                                                 |
| <span id="PrepareForSnapsot"></span><span id="prepareforsnapsot"></span><span id="PREPAREFORSNAPSOT"></span>PrepareForSnapsot<br/> | Received when the requester calls [**IVssBackupComponents::DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset), but before the shadow copy is created.<br/>                                                                                              |
| <span id="Freeze"></span><span id="freeze"></span><span id="FREEZE"></span>Freeze<br/>                                             | Received immediately after [*PrepareForSnapshot*](vssgloss-p.md), but still before the shadow copy is created.<br/>                                                                                                      |
| <span id="Thaw"></span><span id="thaw"></span><span id="THAW"></span>Thaw<br/>                                                     | Received after the shadow copy creation is finished.<br/>                                                                                                                                                                                                     |
| <span id="PostSnapshot"></span><span id="postsnapshot"></span><span id="POSTSNAPSHOT"></span>PostSnapshot<br/>                     | Received after Thaw completes, but before [**IVssBackupComponents::DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset) completes.<br/>                                                                                                                   |
| <span id="Abort"></span><span id="abort"></span><span id="ABORT"></span>Abort<br/>                                                 | Received if too much time elapses between [*Freeze*](vssgloss-f.md) and [*Thaw*](vssgloss-t.md) or if the requester calls [**IVssBackupComponents::AbortBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-abortbackup).<br/> |
| <span id="BackupComplete"></span><span id="backupcomplete"></span><span id="BACKUPCOMPLETE"></span>BackupComplete<br/>             | Received when the requester exits. Failures here will never be reported.<br/>                                                                                                                                                                                 |
| <span id="PreRestore"></span><span id="prerestore"></span><span id="PRERESTORE"></span>PreRestore<br/>                             | Received when the requester calls [**IVssBackupComponents::PreRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prerestore).<br/>                                                                                                                                           |
| <span id="PostRestore"></span><span id="postrestore"></span><span id="POSTRESTORE"></span>PostRestore<br/>                         | Received when the requester calls [**IVssBackupComponents::PostRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-postrestore).<br/>                                                                                                                                         |



 

These failures are configured by adding one or more FailEvent subelements to the TestWriter root element. There are two classes of failures that can be set: retryable and non-retryable. Retryable errors are errors that may go away if the entire backup process is retried, while non-retryable errors are unlikely to disappear. The failure type for the event is chosen based on the retryable attribute.

Here is an example of a basic non-retryable failure:

``` syntax
    <FailEvent writerEvent="Freeze"
               retryable="no" />
```

This example will cause the writer to fail during the [*Freeze*](vssgloss-f.md) event. [**IVssBackupComponents::GatherWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus) will report the writer failure to be VSS\_E\_WRITERERROR\_NONRETRYABLE.

Here is an example of a basic retryable error:

``` syntax
    <FailEvent writerEvent="Freeze"
               retryable="yes"
               numFailures="2"/>
```

This example will cause the writer to fail the first two times it receives a [*Freeze*](vssgloss-f.md) event. After the first two times, the writer will always succeed. The writer failure reported through [**GatherWriterStatus**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-gatherwriterstatus) will be a random retryable error code.

## Declaring Supported Backup Types

Writers communicate what backup types are supported through the requester's calling [**IVssExamineWriterMetadata::GetBackupSchema**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getbackupschema). The TestWriter root element contains attributes for each backup type to indicate support. These attributes are supportsCopy, supportsDifferential, supportsIncremental, and supportsLog. To indicate support for a particular backup type, set the corresponding attribute to "yes".

If the requester sets the backup type to a backup type that is not supported by the writer, the writer will note this fact during [**PrepareForBackup**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prepareforbackup), but otherwise work correctly.

## Indicating the File Backup Type

The [**IVssWMFiledesc::GetBackupTypeMask**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswmfiledesc-getbackuptypemask) method returns a bitmask to the requester indicating how a file should be backed up. This will indicate whether a file is required or not required during specific types of backup, and also whether a shadow copy is required during specific types of backup. The backup types in this bitmask are explained at greater length in the document [Requester Role in Backing Up Complex Stores](requestor-role-in-backing-up-complex-stores.md).

In the Test Writer, the elements of this bitmask are specified by setting attributes in each ComponentFile element. The fullBackupRequired, diffBackupRequired, incBackupRequired, and logBackupRequired attributes specify when a file needs to be backed up. The fullSnapshotRequired, diffSnapshotRequired, incSnapshotRequired, and logSnapshotRequired attributes specify when a file must be backed up from a shadow copy of a volume (and never from the original volume). The default for all of these values is "yes", indicating that a file must always be backed up and must be backed up from a shadow copy of a volume.

## Adding Partial Files

During the processing of [**DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset), a writer has a chance to add partial files to each component. These partial files are reported using [**IVssComponent::GetPartialFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getpartialfile). The Test Writer can be configured to add partial files by specifying PartialFile subelements in a Component element.

Here is an example of a Component element that has two PartialFile subelements:

``` syntax
    <Component componentType="filegroup"
               logicalPath=""
               componentName="WriterComponent"
               selectable="yes">
        <ComponentFile path="c:\files"
                       filespec="*.txt"
                       recursive="no"/>
        <PartialFile path="c:\files"
                     filespec="partial.txt"
                     ranges="0:5,100:20" />
        <PartialFile path="c:\files2"
                     filespec="partial.txt"
                     ranges="0:5,100:20" />
    </Component>
```

Only partial files that partially match an existing ComponentFile (as in the first partial file in the example) or new partial files that are on the same volume as an existing ComponentFile (as in the second partial file) should be specified this way. For this component, the requester must fully back up all files matching c:\\files\\\*.txt except for partial.txt. The requester must then back up the specified ranges (where a range is an offset followed by a length) for the files c:\\files\\partial.txt and c:\\files2\\partial.txt.

If the writer is configured to check file restores, only the backed-up ranges of the partial file will be checked at restore time. Modifications to other portions of the file will go unnoticed. If the deletePartialFiles attribute of the TestWriter root element is set, the partial files are deleted from the original volume immediately after the shadow copy is created.

## Adding Differenced Files

During the processing of [**DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset), a writer can add differenced files to each component. These differenced files are reported using [**IVssComponent::GetDifferencedFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getdifferencedfile). The Test Writer can be configured to add differenced files by specifying DifferencedFile subelements in a Component element.

Here is an example of a Component element that has two DifferencedFile subelements:

``` syntax
    <Component componentType="filegroup"
               logicalPath=""
               componentName="WriterComponent"
               selectable="yes">
        <ComponentFile path="c:\files"
                       filespec="*.txt"
                       recursive="no"/>
        <DifferencedFile path="c:\files"
                         filespec="*.txt"
                         year="2007"
                         month="1"
                         day="22"
                         hour="12"
                         minute="44"
                         second="17" />
        <DifferencedFile path="c:\files2"
                         filespec="*.txt"
                         year="2007"
                         month="1"
                         day="22"
                         hour="12"
                         minute="44"
                         second="17" />
    </Component>
```

Unlike partial files, differenced files should never partially match a ComponentFile specification. The file specification in a DifferencedFile element should either exactly match a ComponentFile (as in the first differenced file in the example) or it should not match it at all, but be on a volume that is referenced in a ComponentFile (as in the second differenced file). The date and time values should be relative to the local time zone, but they will be converted to GMT before being reported to the requester. In the example, only files matching c:\\files\\\*.txt or c:\\files2\\\*.txt that have been modified since 1/22/2003:12:44:17 will be backed up.

If the Test Writer is configured to check file restores, only the modified files will be checked for restore. If the deleteDifferencedFiles attribute of the TestWriter root element is set, the differenced files are deleted from the original volume immediately after the shadow copy is created.

## New Targets

Certain writers allow the requester to inform them that a new location has been chosen to restore certain files to. The writer indicates that it supports this mode as part of the bitmask returned by [**IVssExamineWriterMetadata::GetBackupSchema**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getbackupschema). By default, the Test Writer always supports new targets. This support can be disabled by setting the supportsNewTarget attribute in the TestWriter root element to "no".

If a writer supports new targets, the requester can inform the writer of new targets by calling [**IVssBackupComponents::AddNewTarget**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addnewtarget). The writer will then check the new target location to verify restore rather than the original location.

## More Information

The Test Writer supports more configuration options that are not described here. The full schema for all of the configuration capabilities of the Test Writer is specified in swriter.xml in `%ProgramFiles%\Microsoft SDKs\Windows\v7.0\bin\x64\vsstools` (for 64-bit Windows) and `%ProgramFiles%\Microsoft SDKs\Windows\v7.0\bin\vsstools` (for 32-bit Windows). This file contains an XML schema that completely describes all of the elements and attributes that make up a configuration file. Each element and each attribute in this file is commented with a description that documents that element's or attribute's use.

 

 




