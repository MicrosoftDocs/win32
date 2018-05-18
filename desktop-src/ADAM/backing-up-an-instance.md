---
title: Backing Up an Instance
description: You can back up an instance of AD LDS using the operating system interface, the command line, or using a script or program.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '64be837a-4994-4b55-97b8-b341e5602f8f'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-application-mode'
ms.tgt_platform: multiple
keywords: ["AD LDS examples ADAM , backing up an instance"]
---

# Backing Up an Instance

You can back up an instance of AD LDS using the operating system interface, the command line, or using a script or program.

-   [Using the operating system interface](#)
-   [Using a command line](#using-a-command-line-to-back-up-an-instance-of-ad-lds)
-   [Using a script or a program](#to-use-a-script-or-a-program-to-back-up-an-instance-of-ad-lds)

For more information about how to restore an instance backup [Restoring an Instance](restoring-an-instance.md).

For more information about backing up an AD LDS instance using the operating system interface or command line, see *Back up an AD LDS instance to a file or a tape* in the Active Directory Lightweight Directory Services Help. (This resource may not be available in some languages and countries or regions.)

## 

**To use the operating system interface to back up an instance of AD LDS**

1.  Open **Backup**. Click **Start**, point to **All Programs**, point to **Accessories**, point to **System Tools**, and then click **Backup**.

2.  In Backup or Restore Wizard, click the link for **Advanced Mode**.

3.  Click the **Backup** tab, and then, on the **Job** menu, click **New**.

4.  From the **Tools** menu, click **Options**. In the **Restore** tab of Options, click **Always replace the file on my computer**.

5.  To select an instance of AD LDS folders to back up, select the check box to the left of the folders. The following table lists default AD LDS file directories.

    

    | Directory                                                                                                           | Contents                                          |
    |---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
    | %ProgramFiles%\\Microsoft AD LDS\\*instancename* where *instancename* indicates the AD LDS instance name<br/> | Database files and log files<br/>           |
    | %windir%\\AD LDS<br/>                                                                                         | Program files and administration tools<br/> |

    

     

    To back up the system state, select the **System State** check box.

6.  In **Backup destination**:

    -   To back up files and folders to a file, click **File**.

    -   To back up files and folders to a tape, select a tape drive.

    If a tape drive is not connected to the computer, the **Backup destination** option is unavailable and is automatically set to **File**.

7.  In **Backup media or file name**:

    -   When backing up files and folders to a file, type a path and file name for the backup (.bkf) file, or click the Browse button to find a file.

    -   If backing up files and folders to a tape, select the tape to use.

8.  To select another backup option, such as the backup type and the backup log type, on the **Tools** menu, click **Options**.

9.  Click **Start Backup**, and then make any changes in the **Backup Job Information** dialog box.

10. To set advanced backup options, such as data verification or hardware compression, click **Advanced**.

11. Click **Start Backup** to start the backup operation.

> \[!Caution\]  
> If data has been backed up from an NTFS volume, we recommend that you restore the data to an NTFS volume of the same version to prevent loss of data.

 

## Using a command line to back up an instance of AD LDS

Specify a command that requires the following form:

**ntbackup** **backup** **@***bks file name* **/J** *backup job name* \[**/F** *file name*\] \[**/T** *tape name*\] \[**/P** *pool name*\] \[**/G** *guid name*\] \[**/N** *media name*\] \[**/A**\]



| Value                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *bks file name*<br/>          | The name of the backup selection file (.bks file) to be used for this backup operation. The at sign (@) must precede the name of the backup selection file. A backup selection file contains data about the files and folders selected for backup. You have to create the file using the system interface of Backup. As an alternative, you can supply the path to the drive or file to back up, for example, D:\\.<br/> |
| **/J** *backup job name*<br/> | The job name to be used in the backup report. The job name usually describes the files and folders that you are backing up in the current backup job.<br/>                                                                                                                                                                                                                                                               |
| **/F** *file name*<br/>       | The logical disk path and file name of the backup file. Do not use in conjunction with **/T**, **/P**, or **/G**.<br/>                                                                                                                                                                                                                                                                                                   |
| **/T** *tape name*<br/>       | Overwrites or appends to this tape.<br/>                                                                                                                                                                                                                                                                                                                                                                                 |
| **/P** *pool name*<br/>       | The media type to use. This is usually a subpool of the Backup media pool, such as 4mm DDS. Do not use in conjunction with **/T**, **/G**, **/F**, or **/A**.<br/>                                                                                                                                                                                                                                                       |
| **/G** *guid name*<br/>       | Overwrites or appends to this tape. Do not use in conjunction with **/P**.<br/>                                                                                                                                                                                                                                                                                                                                          |
| **/N** *media name*<br/>      | The new tape name. Do not use in conjunction with **/A**.<br/>                                                                                                                                                                                                                                                                                                                                                           |
| **/A**<br/>                   | Performs an append operation. Either **/T** or **/G** must be used in conjunction with this switch. Do not use in conjunction with **/P**.<br/>                                                                                                                                                                                                                                                                          |



 

For example, to back up the files and folders listed in the backup selection file C:\\adaminstance.bks to file C:\\backup.bkf with the job name "Backup Job 1", use the command: "ntbackup backup @C:\\adaminstance.bks /j "Backup Job 1" /f "C:\\Backup.bkf"".

To back up the same files to a tape drive, use the command "ntbackup backup @C:\\backup.bks /n "Media created 11/5/2003 at 1:25 PM" /d "Set created 11/5/2003 at 1:25 PM" /j "Backup Job 1" /p "4mm DDS""

> \[!Important\]
>
> If you do not specify options, the application uses the options in the system interface.
>
> Before you use to command line to perform backup operations, use the system interface to create the initial backup selection file and setting and a scheduled task. You can then use the scheduled task to view the command syntax. Copy the data from the scheduled task, make changes necessary to create a script or command-line syntax, and then delete the scheduled task if the task is not required.
>
> Some tape drives may not support hardware compression.

 

For more information about additional file and tape backup options, see the Help topic on the **ntbackup** command-line utility in Help and Support Center in Windows Server 2003.

## To use a script or a program to back up an instance of AD LDS

The following Visual Basic Scripting Edition code example constructs a command line to run the ntbackup.exe utility to back up a selected instance.


```VB
' Backup AD LDS Instance.

Option Explicit

Const conWindowStyle  =    1
Const conWaitOnReturn = True

Dim objShell             ' Command shell object.
Dim strADAMInstanceName  ' Name of instance to back up.
Dim strADAMInstancePath  ' Path of instance to back up.
Dim strBackupPath        ' Path of backup file.
Dim strCommandLine       ' Backup command line.
Dim strDescription       ' Description of backup.

' Specify name for instance.
' Change "instance1" to name of selected instance.
strADAMInstanceName = "instance1"

' Specify path for AD LDS instance.
' Change "C:\Program Files\Microsoft AD LDS\instance1\data"
' to the path of the data files for the AD LDS instance to back up.
strADAMInstancePath  = _
    "C:\Program Files\Microsoft AD LDS\instance1\data"

' Specify path for backup file.
' Change "C:\Temp\" to the path to store backup file.
strBackupPath  = "C:\Temp\" & strADAMInstanceName & ".bkf"

' Specify description of backup.
strDescription = "Backup of AD LDS instance: " & strADAMInstanceName

strCommandLine = _
    "cmd /c ""ntbackup backup """ & strADAMInstancePath & _
            """ /snap:on /d """ & strDescription & _
            """ /n ""AD LDS Backup"" /m normal /l:f /f """ & _
                strBackupPath & """"""

WScript.Echo "Execute: " & vbNewLine & strCommandLine

Set objShell = WScript.CreateObject("WScript.Shell")

objShell.Run strCommandLine, conWindowStyle, conWaitOnReturn

WScript.Echo
WScript.Echo "To restore this backup:"
WScript.Echo "  1. Use the Services Administrative Tool"
WScript.Echo "     to stop the service for the AD LDS instance."
WScript.Echo "  2. At a command prompt, type ""ntbackup.exe""."
WScript.Echo "  3. If NTBackup starts in Wizard mode,"
WScript.Echo "     click Advanced Mode."
WScript.Echo "  4. In Advanced Mode,"
WScript.Echo "     click the Restore and Manage Media tab."
WScript.Echo "  5. Select the backup file to restore"
WScript.Echo "     by selecting its check box."
WScript.Echo "  6. To start the restore,"
WScript.Echo "     click the Start Restore button."
WScript.Echo "  7. Click OK in the Confirm Restore dialog."
WScript.Echo "  8. When the restore is complete,"
WScript.Echo "     click Close in the Restore Progress dialog."
WScript.Echo "  9. To exit NTBackup, select Exit from the Job menu."
WScript.Echo " 10. Use the Services Administrative Tool"
WScript.Echo "     to restart the service for the AD LDS instance."
WScript.Echo
```



The following Visual Basic .NET code example constructs a command line to run the **ntbackup.exe** utility to back up a selected instance.


```VB
Imports System
Imports System.Diagnostics
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class BackupInstance

        '/ <summary>
        '/ Backup AD LDS Instance.
        '/ </summary>

        <STAThread()>  Shared Sub Main()

            ' Use ntbackup.exe to backup an AD LDS instance.

            Dim strADAMInstanceName As String  ' Name of instance to back up.
            Dim strADAMInstancePath As String  ' Path of instance to back up.
            Dim strBackupPath As String        ' Path of backup file.
            Dim strCommandLine As String       ' Backup command line.
            Dim strDescription As String       ' Description of the backup.

            ' Specify a name for the instance.
            ' Change "instance1" to name of the selected instance.
            strADAMInstanceName = "instance1"

            ' Specify path for AD LDS instance.
            ' Change "C:\Program Files\Microsoft AD LDS\instance1\data"
            '  to the path of the data files for the AD LDS instance
            '  to back up.
            strADAMInstancePath = _
                "C:\Program Files\Microsoft AD LDS\instance1\data"

            ' Specify the path for the backup file.
            ' Change "C:\Temp\" to the path to store backup file.
            strBackupPath = String.Concat( _
                "C:\Temp\", strADAMInstanceName, ".bkf")

            ' Specify a description of the backup.
            strDescription = String.Concat("Backup of AD LDS instance: ", _
                strADAMInstanceName)

            ' Construct the command.
            strCommandLine = String.Concat("/c ""ntbackup backup """, _
                strADAMInstancePath, """ /snap:on /d """, strDescription, _
                """ /n ""AD LDS Backup"" /m normal /l:f /f """, _
                strBackupPath, """""")

            Console.WriteLine("Execute:\n{0}", strCommandLine)

            ' Execute the command.
            Try
                Process.Start("cmd.exe", strCommandLine)
            Catch e As Exception
                Console.WriteLine("Error:   Backup failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            Console.WriteLine()
            Console.WriteLine("To restore this backup:")
            Console.WriteLine("  1. Use the Services Administrative Tool")
            Console.WriteLine("     to stop the service for the AD LDS instance.")
            Console.WriteLine("  2. At a command prompt, type ""ntbackup.exe"".")
            Console.WriteLine("  3. If NTBackup starts in Wizard mode,")
            Console.WriteLine("     click Advanced Mode.")
            Console.WriteLine("  4. In Advanced Mode,")
            Console.WriteLine("     click the Restore and Manage Media tab.")
            Console.WriteLine("  5. Select the backup file to restore")
            Console.WriteLine("     by clicking its check box.")
            Console.WriteLine("  6. To start the restore,")
            Console.WriteLine("     click the Start Restore button.")
            Console.WriteLine("  7. Click OK in the Confirm Restore dialog.")
            Console.WriteLine("  8. When the restore is complete,")
            Console.WriteLine("     click Close in the Restore Progress dialog.")
            Console.WriteLine("  9. To exit NTBackup, select Exit from the Job menu.")
            Console.WriteLine(" 10. Use the Services Administrative Tool")
            Console.WriteLine("     to restart the service for the AD LDS instance.")
            Console.WriteLine()
            Return

        End Sub 'Main
    End Class 'BackupInstance
End Namespace 'ADAM_Examples
```



The following C# code example constructs a command line to run the ntbackup.exe utility to back up a selected instance.


```CSharp
using System;
using System.Diagnostics;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class BackupInstance
    {
        /// <summary>
        /// Backup AD LDS Instance.
        /// </summary>
        [STAThread]
        static void Main()
        {
            //
            // Use ntbackup.exe to backup an AD LDS instance.
            //

            string strADAMInstanceName;  // Name of instance to back up.
            string strADAMInstancePath;  // Path of instance to back up.
            string strBackupPath;        // Path of backup file.
            string strCommandLine;       // Backup command line.
            string strDescription;       // Description of the backup.

            // Specify name for instance.
            // Change "instance1" to name of selected instance.
            strADAMInstanceName = "instance1";

            // Specify path for AD LDS instance.
            // Change "C:\Program Files\Microsoft AD LDS\instance1\data"
            // to the path of the data files for the AD LDS instance
            // to back up.
            strADAMInstancePath  =
                "C:\\Program Files\\Microsoft AD LDS\\instance1\\data";

            // Specify path for backup file.
            // Change "C:\Temp\" to the path to store backup file.
            strBackupPath  = String.Concat(
                "C:\\Temp\\", strADAMInstanceName, ".bkf");

            // Specify description of backup.
            strDescription = String.Concat(
                "Backup of AD LDS instance: ", strADAMInstanceName);

            // Construct the command.
            strCommandLine = String.Concat(
                "/c \"ntbackup backup \"", strADAMInstancePath,
                "\" /snap:on /d \"", strDescription,
                "\" /n \"AD LDS Backup\" /m normal /l:f /f \"",
                strBackupPath, "\"\"");

            Console.WriteLine("Execute:\n{0}", strCommandLine);

            // Execute the command.
            try
            {
                Process.Start("cmd.exe", strCommandLine);
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Backup failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            Console.WriteLine();
            Console.WriteLine("To restore this backup:");
            Console.WriteLine("  1. Use the Services Administrative Tool");
            Console.WriteLine("     to stop the service for the AD LDS instance.");
            Console.WriteLine("  2. At a command prompt, type \"ntbackup.exe\".");
            Console.WriteLine("  3. If NTBackup starts in Wizard mode,");
            Console.WriteLine("     click Advanced Mode.");
            Console.WriteLine("  4. In Advanced Mode,");
            Console.WriteLine("     click the Restore and Manage Media tab.");
            Console.WriteLine("  5. Select the backup file to restore");
            Console.WriteLine("     by selecting its check box.");
            Console.WriteLine("  6. To start the restore,");
            Console.WriteLine("     click the Start Restore button.");
            Console.WriteLine("  7. Click OK in the Confirm Restore dialog.");
            Console.WriteLine("  8. When the restore is complete,");
            Console.WriteLine("     click Close in the Restore Progress dialog.");
            Console.WriteLine("  9. To exit NTBackup, select Exit from the Job menu.");
            Console.WriteLine(" 10. Use the Services Administrative Tool");
            Console.WriteLine("     to restart the service for the AD LDS instance.");
            Console.WriteLine();
            return;
        }
    }
}
```



 

 





