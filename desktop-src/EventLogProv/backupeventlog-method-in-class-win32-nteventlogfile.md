---
Description: Saves the specified event log to a backup file.
ms.assetid: 00575928-a56e-40fd-9cc2-0a547f42a30d
title: BackupEventlog method of the Win32\_NTEventlogFile class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BackupEventlog method of the Win32\_NTEventlogFile class

The **BackupEventLog** method saves the specified event log to a backup file. If a backup file with the same name exists, the method fails.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 BackupEventlog(
  [in] string ArchiveFileName
);
```



## Parameters

<dl> <dt>

*ArchiveFileName* \[in\]
</dt> <dd>

Path and file name of the backup file to be created.

> [!Note]  
> If the *ArchiveFileName* comes from a source that you do not know or trust, then this parameter value should be verified before using it in a call to [**BackupEventlog**](https://msdn.microsoft.com/library/windows/desktop/aa363635).

 

</dd> </dl>

## Return value



| Return code                                                                       | Description                                  |
|-----------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**0**</dt> </dl>  | Success<br/>                           |
| <dl> <dt>**8**</dt> </dl>  | Privilege missing<br/>                 |
| <dl> <dt>**21**</dt> </dl> | Invalid parameter<br/>                 |
| <dl> <dt>**80**</dt> </dl> | Archive file name already exists.<br/> |



 

## Remarks

Event logs maintain a historical record of important events that occur on a computer. These records should be archived, at least temporarily, to help you carry out tasks such as troubleshooting problems (when did the first instance of X occur?) or capacity planning (how does the number of Ys occurring this month compare with the number of Ys that occurred last month?).

The most efficient way to archive event log records is to routinely back up and then clear these logs. Backing up the logs before clearing them ensures that the records will be available if you ever need them; clearing the event logs keeps those logs to a manageable size. Clearing the event logs also ensures that all events will be recorded. If you do not clear the event log before it reaches its maximum size, it either stops recording any new events or starts overwriting older events, depending on how the log has been configured. As a result, events will either be overwritten, and thus lost, or never recorded in the first place.

> [!Note]  
> When you clear an event log, the operating system does not delete the previous event log file. Instead, Windows creates a new 64 KB log file that replaces the old log file. (The new log file is placed on exactly the same sectors of the disk drive as the old log file.) Because the disk drive sectors are overwritten and filled with new information, you cannot retrieve records from a cleared event log using an undelete tool.

 

Before you clear an event log, it is a good idea to create a backup of that log. WMI provides a method for backing up event logs. However, this method comes with two important stipulations. For one, you must use the proprietary event log binary log format. To archive event logs in plain-text format, you need to create a query to extract the records and then write the extracted information to a text file.

In addition, you must make backups to the local computer; you cannot save a backup of the event logs on Computer A to Computer B. Backups are implemented by using the LocalSystem account, which does not have the network credentials necessary to access remote computers. If you want to save backups to a central repository, modify the script to first perform the backup, and then move the backup file to the central repository.

**A technical note on backing up event logs**

Event logs must be backed up separately from any other system files. Although a regular system backup can copy the event log files, the copied event log files will be unusable. If you attempt to open an event log file that has been copied or backed up by using any means other than the Event Log Backup Application Programming Interface (API), you receive an error message stating that the event log file is corrupt.

This error message is the result of a unique characteristic of event log files. When a computer starts, the Event service changes several bits in each event log file header. These changed bits indicate that the event log file is open, and they prevent applications, including backup programs, from accessing the event log file. If you copy an event log file by using the Copy command or a standard backup program, the copied event log file includes these changed bits. If you then try to open the copied file, you receive a message that the event log is corrupt.

Despite the changed bits, you can use Event Viewer to work with the event log files, but only because it does not try to open the event log file itself. Instead, Event Viewer uses the Event service and the Event Logging API to open the event log files.

However, this does not completely solve the problem. For better or worse, the Event service and Event Logging API can be used to open only actual event logs; they cannot open archived event log files. Instead, Event Viewer must directly access backup event log files. If the Event Log Backup API did not produce these backup event log files, these backup files will include the changed bits indicating that the file is open. In that case, any attempt to access the file will fail.

When you use the Event Log Backup method, these header bits are changed to indicate that the file is closed, giving Event Viewer access to the data.

## Examples

The following VBScript sample backs up and then clears the Application event log on a computer.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
 & "{impersonationLevel=impersonate,(Backup)}!\\" & _
 strComputer & "\root\cimv2")
Set colLogFiles = objWMIService.ExecQuery _
 ("SELECT * FROM Win32_NTEventLogFile WHERE LogFileName='Application'")
For Each objLogfile in colLogFiles
 errBackupLog = objLogFile.BackupEventLog("c:\scripts\application.evt")
 If errBackupLog <> 0 Then
 Wscript.Echo "The Application event log could not be backed up."
 Else
 objLogFile.ClearEventLog()
 End If
Next
```



The following VBScript backs up and clears an event log only if the log is larger than 20 megabytes (approximately 20,000,000 bytes). If the log is smaller than 20 megabytes, the script exits without performing the backup.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
 & "{impersonationLevel=impersonate, (Backup, Security)}!\\" _
 & strComputer & "\root\cimv2")
Set colLogFiles = objWMIService.ExecQuery _
 ("SELECT * FROM Win32_NTEventLogFile")
For Each objLogfile in colLogFiles
 If objLogFile.FileSize > 20000000 Then
 strBackupLog = objLogFile.BackupEventLog _
 ("c:\scripts\" & objLogFile.LogFileName & ".evt")
 objLogFile.ClearEventLog()
 End If
Next
```



The following VBScript code sample demonstrates how to backup the entries from the Application event log file on the local machine from instances of Win32\_NTEventLogFile.


```VB
Set LogFileSet = GetObject("winmgmts:{(Backup,Security)}").ExecQuery("select * from Win32_NTEventLogFile where LogfileName='Application'")

for each Logfile in LogFileSet
 RetVal = LogFile.BackupEventlog("c:\BACKUP.LOG")
 if RetVal = 0 then WScript.Echo "Log Backed Up"
next
```



The following Perl code sample demonstrates how to backup the entries from the Application event log file on the local machine from instances of Win32\_NTEventLogFile.


```Perl
use strict;
use Win32::OLE;

close(STDERR);

my ($LogFile, $LogFileSet);
eval { $LogFileSet = Win32::OLE->GetObject("winmgmts:{(Backup,Security)}!\\\\.\\root\\cimv2")->
 ExecQuery("SELECT * FROM Win32_NTEventLogFile WHERE LogfileName='Application'");};

if (!$@ &amp;&amp; defined $LogFileSet) 
{
 foreach $LogFile (in $LogFileSet)
 {
  my $RetVal = $LogFile->BackupEventlog("c:\\BACKUP.LOG");
  if (defined $RetVal &amp;&amp; $RetVal == 0)
  {
   print "\nLog Backed Up\n";
  }
  else
  {
   print Win32::OLE->LastError, "\n";
  }
 }
}
else
{
 print Win32::OLE->LastError, "\n";
}
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                               |
| Header<br/>                   | <dl> <dt>Winbase.h</dt> </dl> |
| MOF<br/>                      | <dl> <dt>Ntevt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntevt.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[**Win32\_NTEventlogFile**](win32-nteventlogfile.md)
</dt> <dt>

[WMI Tasks: Event Logs](https://msdn.microsoft.com/library/aa394593)
</dt> </dl>

 

 




