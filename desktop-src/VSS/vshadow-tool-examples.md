---
description: "Learn more about: VShadow Tool Examples"
ms.assetid: 6a69b75b-ee4a-4613-ba05-d2deb42759b7
title: VShadow Tool Examples
ms.topic: article
ms.date: 05/31/2018
---

# VShadow Tool Examples

The following examples show how to use the VShadow tool to perform the most common tasks:

-   [Accessing Shadow Copy Properties from a CMD Script](#accessing-shadow-copy-properties-from-a-cmd-script)
-   [Accessing Nonpersistent Shadow Copies](#accessing-nonpersistent-shadow-copies)
-   [Copying a File from a Shadow Copy](#copying-a-file-from-a-shadow-copy)
-   [Enumerating All Files on a Shadow Copy Device](#enumerating-all-files-on-a-shadow-copy-device)
-   [Importing a Transportable Shadow Copy](#importing-a-transportable-shadow-copy)
-   [Including Writers or Components](#including-writers-or-components)
-   [Excluding Writers or Components](#excluding-writers-or-components)
-   [Breaking Shadow Copy Sets Using the BreakSnapshotSetEx Method](#breaking-shadow-copy-sets-using-the-breaksnapshotsetex-method)

For a complete list of command-line options and their use, see [VShadow Tool and Sample](vshadow-tool-and-sample.md).

## Accessing Shadow Copy Properties from a CMD Script

If you use the **-script** optional flag when you create shadow copies, VShadow creates a CMD script file containing environment variables related to the newly created shadow copies, such as the following:

-   The shadow copy set ID, which is stored in the %SHADOW\_SET\_ID% environment variable
-   The shadow copy IDs, which are stored in variables of the form %SHADOW\_ID\_*NNN*%, where *NNN* represents the index of the source volume in the VShadow command line
-   The shadow copy device names, which are stored in variables of the form %SHADOW\_DEVICE\_*NNN*%, where *NNN* is the index of the source volume in the VShadow command line

You can use the generated CMD file to perform limited management operations on the shadow copies.

> [!Note]  
> The [**BackupComplete**](/windows/win32/api/VsBackup/nf-vsbackup-ivssbackupcomponents-backupcomplete) writer event is sent after the **-exec** script is executed. VSS calls the **IVssBackupComponents::BackupComplete** method to signal to the writers that the backup is completed, and the writers can potentially truncate logs at this point. Therefore, it is important to verify that the shadow/backup actually completed. If the backup failed, you can cancel the creation process by returning a nonzero exit code in the executed script/command. (See the documentation for the exit command in the [Windows Command Line Reference](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc754340(v=ws.11)).) If the custom command returns with a nonzero exit code, then the shadow copy creation is canceled and **IVssBackupComponents::BackupComplete** will not be called.

 

The following example shows how to create a persistent shadow copy from the command line and use the CMD script to expose it.

1.  **vshadow -p -nw -script=SETVAR1.cmd c:**
2.  **call SETVAR1.cmd**
3.  **C:\\>vshadow -el=%SHADOW\_ID\_1%,c:\\directory1**

## Accessing Nonpersistent Shadow Copies

Nonpersistent shadow copies are automatically deleted when the program that creates them (in this case, VShadow) exits. To access the contents of these shadow copies, VShadow allows you to execute a script after the shadow copies are created but before the VShadow program exits.

The following example shows how to use the -exec command-line option to run a script called "enum.cmd":

**vshadow -nw -exec=enum.cmd c:**

In the executed script, you can also run the generated SETVAR script in this custom command. This allows the script to access the contents of the shadow copies directly. Remember that the shadow device can be retrieved from the SHADOW\_DEVICE\_NNN environment variable.

Here is an example enum.cmd script:

``` syntax
call SETVAR1.cmd
for /R %SHADOW_DEVICE_1%\ %%i in (*.*) do @echo %%i
```

Here is the command line to execute the enum.cmd script:

**vshadow -nw -exec=c:\\enum.cmd -script=setvar1.cmd c:**

## Copying a File from a Shadow Copy

The following example shows how to copy a file from a shadow copy.

1.  **dir > c:\\somefile.txt**
2.  **vshadow -p -nw -script=SETVAR1.cmd c:**
3.  **call SETVAR1.cmd**
4.  **copy %SHADOW\_DEVICE\_1%\\somefile.txt c:\\somefile\_bak.txt**

## Enumerating All Files on a Shadow Copy Device

The following example shows how to enumerate all files on a shadow copy device from a batch file.

1.  **dir > c:\\somefile.txt**
2.  **vshadow -p -nw -script=SETVAR1.cmd c:**
3.  **call SETVAR1.cmd**
4.  **for /R %SHADOW\_DEVICE\_1%\\ %%i in (\*) do @echo %%i**

## Importing a Transportable Shadow Copy

To create a transportable shadow copy on one machine and import it to another machine, you must have two computers that are connected (through a SAN configuration) to a storage array that supports VSS hardware shadow copies. A VSS hardware provider must be installed on each computer.

The following example shows how to create and import the shadow copy.

1.  Create the shadow copy set on computer A (the production server) by typing the following command after the command prompt:

    **vshadow -p -t=bc1.xml**

    This will not expose any shadow copy devices on computer A.

2.  Copy the backup components document (bc1.xml) from computer A to computer B.
3.  Import the shadow set on machine B by typing the following command:

    **vshadow -i=bc1.xml**

Optionally, you could expose these shadow copies as drive letters or mounted folders. Also, you could potentially break the shadow set to make the new shadow copy volumes read-write.

To automate the shadow set management process you might use the **-script** command-line option to generate the CMD script containing the shadow copy IDs. Then you can copy the generated script along with the backup components to the other computer.

The following example shows how to create, expose, and break transportable shadow copies using CMD scripts.

1.  Create the shadow copy set on computer A (the production server) from the command line as follows:

    **vshadow -p -t=bc1.xml -script=sc1.cmd**

    Specify the **-script** option to generate the script containing the proper environment variable definitions. Note that this will not expose any shadow copy devices on computer A.

2.  Copy the backup components document (bc1.xml) and the generated script (sc1.cmd) from computer A to computer B.
3.  Import the shadow set on machine B by typing the following command:

    **vshadow -i=bc1.xml**

    This will surface the created devices on computer B.

4.  Run the generated script to set the environment variables for the shadow copy set by typing the file name at the command prompt as in the following example:

    **sc1.cmd**

    This will set the relevant environment variables as described in Access Shadow Copy Properties from a CMD Script.

5.  Expose the shadow copies on computer B by typing the following commands:
    1.  **rmdir /s c:\\mount\_point**
    2.  **mkdir c:\\mount\_point**
    3.  **vshadow –el=%SHADOW\_ID\_1%,c:\\mount\_point**

    This will surface the created shadow copy devices on computer B.
6.  Break the shadow copy set to make the volumes writable by typing the following command:**C:\\>vshadow –bw=%SHADOW\_SET\_ID%**

Note that nonpersistent transportable shadow copies can also be imported, but they are automatically deleted when the **vshadow** **-i** process exits. To import the shadow copies before they are deleted, you must use the **-exec** command-line option as described in Access Nonpersistent Shadow Copies.

## Including Writers or Components

By default, all writers participate in shadow copy creation. To determine which writers and components will be included in a shadow copy set, use the **-wm** or **-wm2** command-line option as described in [Listing Writer Status and Metadata](vshadow-tool-and-sample.md).

To verify that all of a writer's components are included, use the **-wi** optional flag in any of the following formats:

-   **vshadow** **-wi** *WriterName*
-   **vshadow** **-wi** **"***Writer Name String***"**
-   **vshadow** **-wi** **{***WriterID***}**
-   **vshadow** **-wi** **{***InstanceID***}**

To verify that specific components are included, use the **-wi** optional flag in any of the following formats:

-   **vshadow** **-wi** *WriterName***:\\***LogicalPath***\\***ComponentName*
-   **vshadow** **-wi** **"***Writer Name String***":\\***LogicalPath***\\***ComponentName*
-   **vshadow** **-wi** **{***WriterID***}:\\***LogicalPath***\\***ComponentName*
-   **vshadow** **-wi** **{***InstanceID***}:\\***LogicalPath***\\***ComponentName*

The following examples show how to use the **-wi** optional flag.

-   Specifying *WriterName*:\\*LogicalPath*\\*ComponentName*:

    **vshadow -wi="Registry Writer:\\Registry"**

-   Specifying {*WriterID*}:

    **vshadow -wi={BE000CBE-11FE-4426-9C58-531AA6355FC4}**

-   Specifying more than one writer or component:

    **vshadow -wi="Registry Writer:\\Registry" -wi="COM+ REGDB Writer"**

## Excluding Writers or Components

To exclude all writers, use the **-nw** optional flag when creating the shadow copy.

To exclude all of a writer's components, use the **-wx** optional flag in any of the following formats:

-   **vshadow** **-wx** *WriterName*
-   **vshadow** **-wx** **"***Writer Name String***"**
-   **vshadow** **-wx** **{***WriterID***}**
-   **vshadow** **-wx** **{***InstanceID***}**

To exclude specific components, use the **-wx** optional flag in any of the following formats:

-   **vshadow** **-wx** *WriterName***:\\***LogicalPath***\\***ComponentName*
-   **vshadow** **-wx** **"***Writer Name String***":\\***LogicalPath***\\***ComponentName*
-   **vshadow** **-wx** **{***WriterID***}:\\***LogicalPath***\\***ComponentName*
-   **vshadow** **-wx** **{***InstanceID***}:\\***LogicalPath***\\***ComponentName*

The following examples show how to use the **-wx** optional flag.

-   Specifying *WriterName*:\\*LogicalPath*\\*ComponentName*:

    **vshadow -wx="Registry Writer:\\Registry"**

-   Specifying {*WriterID*}:

    **vshadow -wx={BE000CBE-11FE-4426-9C58-531AA6355FC4}**

-   Specifying more than one writer or component:

    **vshadow -wx="Registry Writer:\\Registry" -wx="COM+ REGDB Writer"**

## Breaking Shadow Copy Sets Using the BreakSnapshotSetEx Method

The following examples show how to use the **-bex** command-line option.

-   Specifying that the shadow copy LUN will be masked from the host:

    **vshadow** **-bex** **-mask**

-   Specifying that the shadow copy LUN will be exposed to the host as a read/write volume:

    **vshadow** **-bex** **-rw**

-   Specifying that the shadow copy LUN will be exposed to the host as a read/write volume, and that none of the disk signatures on the shadow copy LUNs will be reverted to that of the original LUNs:

    **vshadow** **-bex** **-norevert**

 

 
