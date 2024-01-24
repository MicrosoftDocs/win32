---
description: BETest is a VSS requester that tests advanced backup and restore operations.
ms.assetid: a6cc7308-a9fa-4a84-9e7c-4d0adda28db5
title: BETest Tool
ms.topic: article
ms.date: 05/31/2018
---

# BETest Tool

BETest is a VSS requester that tests advanced backup and restore operations. This tool can be used to test an application's use of complex VSS features such as the following:

-   Incremental and differential backup
-   Complex restore options, such as authoritative restore
-   Rollforward options

> [!Note]  
> BETest is included in the Microsoft Windows Software Development Kit (SDK) for Windows Vista and later. The VSS 7.2 SDK includes a version of BETest that runs only on Windows Server 2003. This topic describes the Windows SDK version of BETest, not the Windows Server 2003 version included in the VSS 7.2 SDK. For information about downloading the Windows SDK and the VSS 7.2 SDK, see [Volume Shadow Copy Service](volume-shadow-copy-service-portal.md).

 

In the Windows SDK installation, the BETest tool can be found in `%Program Files(x86)%\Windows Kits\8.1\bin\x64` (for 64-bit Windows) and `%Program Files(x86)%\Windows Kits\8.1\bin\x86` (for 32-bit Windows).

## Running the BETest Tool

To run the BETest tool from the command line, use the following syntax:

**BETest** *command-line-options*

The following usage example shows how to use the BETest tool together with the [VSS Test Writer tool](vss-test-writer-tool.md), which is a VSS writer.

**BETest Tool Usage Example**

1.  Create a test directory named C:\\BETest. Copy the following files into this directory:
    -   betest.exe
    -   vswriter.exe
    -   [BetestSample.xml](#sample-xml-configuration-file-betestsamplexml)
    -   [VswriterSample.xml](#sample-xml-configuration-file-vswritersamplexml)
2.  Create a directory named C:\\TestPath. Put some test data files in this directory.
3.  Create a directory named C:\\BackupDestination. Leave this directory empty.
4.  Open two elevated command windows and set the working directory in each to C:\\BETest.
5.  In the first command window, start the [VSS Test Writer tool](vss-test-writer-tool.md) as follows:

    **vswriter.exe VswriterSample.xml**

    The vswriterSample.xml file configures the VSS Test Writer tool (vswriter) to report the contents of the c:\\TestPath directory in preparation for a backup operation. Note that the VSS Test Writer tool will not produce output until it detects activity from a requester such as BETest. To stop the VSS Test Writer tool, press CTRL+C.

6.  In the second command window, use the BETest tool to perform a backup operation as follows:

    **betest.exe /B /S backup.xml /D C:\\BackupDestination /X BetestSample.xml**

    BETest will back up the files from the C:\\TestPath directory to the C:\\BackupDestination directory. It will save the backup component document to C:\\BETest\\backup.xml.

7.  If the backup operation is successful, delete the contents of the C:\\TestPath directory, and use the BETest tool to perform a restore operation as follows:

    **betest.exe /R /S backup.xml /D C:\\BackupDestination /X BetestSample.xml**

## BETest Tool Command-Line Options

The BETest tool uses the following command-line options to identify the work to perform.

<dl> <dt>

<span id="_Auth"></span><span id="_auth"></span><span id="_AUTH"></span>**/Auth**
</dt> <dd>

Performs an authoritative restore operation for Active Directory or Active Directory Application Mode.

**Windows Server 2003:** This command-line option is not supported.

</dd> <dt>

<span id="_B"></span><span id="_b"></span>**/B**
</dt> <dd>

Performs a backup operation but does not perform a restore.

</dd> <dt>

<span id="_BC"></span><span id="_bc"></span>**/BC**
</dt> <dd>

Performs only the backup complete operation.

**Windows Server 2003:** This command-line option is not supported.

</dd> <dt>

<span id="_C_Filename"></span><span id="_c_filename"></span><span id="_C_FILENAME"></span>**/C** *Filename*
</dt> <dd>

> [!Note]  
> This command-line option is provided only for backward compatibility. The **/X** command-line option should be used instead.

 

Selects the components to be backed up or restored based on the contents of the configuration file specified by *Filename*. This file must contain only ANSI characters in the range from 0 through 127, and it must be no larger than 1 MB. Each line in the file must use the following format:

*WriterId* : *ComponentName*;

Where *WriterId* is the writer ID, and *ComponentName* is the name of one of the writer's components. The writer ID and component names must be in quotation marks, and there must be spaces before and after the colon (:). If two or more components are specified, they must be separated by commas. For example:

"5affb034-969f-4919-8875-88f830d0ef89" : "TestFiles1", "TestFiles2", "TestFiles3";

</dd> <dt>

<span id="_D_Path"></span><span id="_d_path"></span><span id="_D_PATH"></span>**/D** *Path*
</dt> <dd>

Save the backed-up files to or restore them from the backup directory specified by *Path*.

</dd> <dt>

<span id="_NBC"></span><span id="_nbc"></span>**/NBC**
</dt> <dd>

Omits the backup complete operation.

**Windows Server 2003:** This command-line option is not supported.

</dd> <dt>

<span id="_O"></span><span id="_o"></span>**/O**
</dt> <dd>

Specifies that the backup includes a bootable system state.

</dd> <dt>

<span id="_P"></span><span id="_p"></span>**/P**
</dt> <dd>

Creates a persistent shadow copy.

**Windows Server 2003:** This command-line option is not supported.

</dd> <dt>

<span id="_Pre_Filename"></span><span id="_pre_filename"></span><span id="_PRE_FILENAME"></span>**/Pre** *Filename*
</dt> <dd>

If the backup type specified in the **/T** command-line option is INCREMENTAL or DIFFERENTIAL, set the backup document to the file specified by *Filename* for previous full or incremental backup.

**Windows Server 2003 and Windows XP:** This command-line option is not supported.

</dd> <dt>

<span id="_R"></span><span id="_r"></span>**/R**
</dt> <dd>

Performs restore but does not perform backup. Must be used together with the **/S** command-line option.

</dd> <dt>

<span id="_Rollback"></span><span id="_rollback"></span><span id="_ROLLBACK"></span>**/Rollback**
</dt> <dd>

Creates a shadow copy that can be used for application rollback.

**Windows Server 2003:** This command-line option is not supported.

</dd> <dt>

<span id="_S_Filename"></span><span id="_s_filename"></span><span id="_S_FILENAME"></span>**/S** *Filename*
</dt> <dd>

In case of backup, saves the backup document to the file specified by *Filename*. In case of restore only, loads the backup document from this file.

</dd> <dt>

<span id="_Snapshot"></span><span id="_snapshot"></span><span id="_SNAPSHOT"></span>**/Snapshot**
</dt> <dd>

Creates a volume shadow copy but does not perform backup or restore.

**Windows Server 2003:** This command-line option is not supported.

</dd> <dt>

<span id="_StopError"></span><span id="_stoperror"></span><span id="_STOPERROR"></span>**/StopError**
</dt> <dd>

Stops BETest when the first writer error is encountered.

**Windows Server 2003:** This command-line option is not supported.

</dd> <dt>

<span id="_T_BackupType"></span><span id="_t_backuptype"></span><span id="_T_BACKUPTYPE"></span>**/T** *BackupType*
</dt> <dd>

Specifies the backup type. *BackupType* can be FULL, LOG, COPY, INCREMENTAL, or DIFFERENTIAL. For more information about backup types, see [**VSS\_BACKUP\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_backup_type).

</dd> <dt>

<span id="_V"></span><span id="_v"></span>**/V**
</dt> <dd>

Generates verbose output that can be used for troubleshooting.

**Windows Server 2003:** This command-line option is not supported.

</dd> <dt>

<span id="_X_Filename"></span><span id="_x_filename"></span><span id="_X_FILENAME"></span>**/X** *Filename*
</dt> <dd>

Selects the components to be backed up or restored based on the contents of the XML configuration file specified by *Filename*. This file must contain only ANSI characters in the range from 0 through 127. The format of the XML file is defined by the schema in the BETest.xml file. For a sample configuration file, see BetestSample.xml. Both of these files are in the vsstools directory.

> [!Note]  
> You can view the BETest.xml file in Internet Explorer. Before you open this file, make sure that the xdr-schema.xsl file is in the same directory as BETest.xml. The xdr-schema.xsl file contains rendering instructions that make the BETest.xml file more readable.

 

**Windows Server 2003:** This command-line option is not supported.

</dd> </dl>

## Sample XML Configuration File: BetestSample.xml

The following sample configuration file, BetestSample.xml, can be found in the Vsstools directory.

``` syntax
<BETest>
    <Writer writerid="5affb034-969f-4919-8875-88f830d0ef89">
        <Component componentName="TestFiles">
        </Component>
    </Writer>
</BETest>
```

This example of a simple configuration file selects one component to be backed up or restored.

## Sample XML Configuration File: VswriterSample.xml

The following sample configuration file, VswriterSample.xml, can be found in the Vsstools directory.

``` syntax
<TestWriter   usage="USER_DATA"
                    deleteFiles="no">

    <RestoreMethod method="RESTORE_IF_CAN_BE_REPLACED" 
                   writerRestore="always"
                   rebootRequired="no" />
    
    <Component componentType="filegroup" 
               componentName="TestFiles">
               <ComponentFile path="c:\TestPath" filespec="*" recursive="no" />
    </Component>

</TestWriter>
```

The root element in this configuration file is named TestWriter. All other elements are arranged under the TestWriter element.

The first attribute associated with TestWriter is the usage attribute. This attribute specifies the usage type reported through the [**IVssExamineWriterMetadata::GetIdentity**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssexaminewritermetadata-getidentity) method. One of the possible values for this attribute is USER\_DATA.

The second attribute is the deleteFiles attribute. This attribute is described in [Configuring Writer Attributes](vss-test-writer-tool.md).

The first child element of the root element is a RestoreMethod element. This element specifies the following:

-   The restore method (in this case, RESTORE\_IF\_CAN\_BE\_REPLACED)
-   Whether the writer requires restore events (in this case, always)
-   Whether a reboot is required after the writer is restored (in this case, no)

This element can optionally specify an alternate-location mapping. (In this case, no alternate location is specified.) For more information, see [Specifying Alternate Location Mappings](vss-test-writer-tool.md).

The second child element is a Component element. This element causes the writer to add a component to its metadata. A Component element contains attributes to describe the component and child elements to describe the content of the component, such as the following:

-   componentType to indicate whether this is a filegroup or a database (in this case, a filegroup)
-   logicalPath for the component logical path (in this case, none is specified)
-   componentName for the name of the component (in this case, "TestFiles")
-   selectable to indicate selectable-for-backup status

The Component element also has a child element named ComponentFile to add a file specification to this component. (A Component element can have an arbitrary number of ComponentFile elements that can be specified for each component.) This ComponentFile element has the following attributes:

-   path="c:\\TestPath"
-   filespec="\*"
-   recursive="no"

 

 



