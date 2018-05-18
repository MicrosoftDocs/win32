---
Description: 'The ClearEventLog method clears the specified event log.'
ms.assetid: 'cbc15964-11b3-41d4-a82e-ab10c4947189'
title: 'ClearEventLog method of the Win32\_NTEventlogFile class'
---

# ClearEventLog method of the Win32\_NTEventlogFile class

The **ClearEventLog** method clears the specified event log.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 ClearEventLog(
  [in] string ArchiveFileName
);
```



## Parameters

<dl> <dt>

*ArchiveFileName* \[in\]
</dt> <dd>

Path and file name of the file to be cleared.

> [!Note]  
> If the *ArchiveFileName* comes from a source that you do not know or trust, then this value should be verified before using it in a call to **ClearEventLog**.

 

</dd> </dl>

## Return value



| Return code                                                                       | Description                  |
|-----------------------------------------------------------------------------------|------------------------------|
| <dl> <dt>**0**</dt> </dl>  | Success<br/>           |
| <dl> <dt>**8**</dt> </dl>  | Privilege Missing<br/> |
| <dl> <dt>**21**</dt> </dl> | Invalid Parameter<br/> |



 

## Examples

The following VBScript sample demonstrates how to clear the entries from the System event log file on the local machine from instances of [**Win32\_NTEventlogFile**](win32-nteventlogfile.md).

> [!Note]  
> A backup file can be specified to the **ClearEventLog** method if a backup of the data is desired before clearing the log.

 


```VB
Set LogFileSet = GetObject("winmgmts:{(Backup,Security)}").ExecQuery("select * from Win32_NTEventLogFile where LogfileName='System'")

for each Logfile in LogFileSet
 RetVal = LogFile.ClearEventlog()
 if RetVal = 0 then WScript.Echo "Log Cleared"
next
```



The following perl sample demonstrates how to clear the entries from the System event log file on the local machine from instances of [**Win32\_NTEventlogFile**](win32-nteventlogfile.md).

> [!Note]  
> A backup file can be specified to the **ClearEventLog** method if a backup of the data is desired before clearing the log.

 


```
use strict;
use Win32::OLE;

close(STDERR);

my ($LogFile, $LogFileSet);
eval {$LogFileSet = Win32::OLE->GetObject("winmgmts:{(Backup,Security)}")->
 ExecQuery("SELECT * FROM Win32_NTEventLogFile WHERE LogfileName='System'");};
if(!$@ &amp;&amp; defined $LogFileSet)
{
 foreach $LogFile (in $LogFileSet)
 {
  my $RetVal = $LogFile->ClearEventlog();
  if ($RetVal == 0)
  {
   print "\nLog Cleared\n";
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
| Minimum supported client<br/> | Windows XP<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                       |
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

 

 




