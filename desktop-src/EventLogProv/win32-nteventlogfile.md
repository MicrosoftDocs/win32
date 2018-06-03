---
Description: Represents a logical file or directory of operating system events.
ms.assetid: 00575928-a56e-40fd-9cc2-0a547f42a30d
title: Win32\_NTEventlogFile class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_NTEventlogFile class

The **Win32\_NTEventlogFile** [WMI class](https://msdn.microsoft.com/library/aa393244)represents a logical file or directory of operating system events. The file is also known as the event log.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MS_NT_EVENTLOG_PROVIDER"), Dynamic]
class Win32_NTEventlogFile : CIM_DataFile
{
  uint32   AccessMask;
  boolean  Archive;
  string   Caption;
  boolean  Compressed;
  string   CompressionMethod;
  string   CreationClassName;
  datetime CreationDate;
  string   CSCreationClassName;
  string   CSName;
  string   Description;
  string   Drive;
  string   EightDotThreeFileName;
  boolean  Encrypted;
  string   EncryptionMethod;
  string   Extension;
  string   FileName;
  uint64   FileSize;
  string   FileType;
  string   FSCreationClassName;
  string   FSName;
  boolean  Hidden;
  datetime InstallDate;
  uint64   InUseCount;
  datetime LastAccessed;
  datetime LastModified;
  string   LogfileName;
  string.  Manufacturer;
  uint32   MaxFileSize;
  string   Name;
  uint32   NumberOfRecords;
  uint32   OverwriteOutDated;
  string   OverWritePolicy;
  string   Path;
  boolean  Readable;
  string   Sources[];
  string   Status;
  boolean  System;
  string   Version;
  boolean  Writeable;
};
```

## Members

The **Win32\_NTEventlogFile** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_NTEventlogFile** class has these methods.



| Method                                                                                                  | Description                                                                                                                                                                                                                            |
|:--------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BackupEventLog**](backupeventlog-method-in-class-win32-nteventlogfile.md)                           | Saves the specified event log to a backup file.<br/>                                                                                                                                                                             |
| [**ChangeSecurityPermissions**](changesecuritypermissions-method-in-class-win32-nteventlogfile.md)     | Class method that changes the security permissions for the logical file specified in the **Name** property.<br/>                                                                                                                 |
| [**ChangeSecurityPermissionsEx**](changesecuritypermissionsex-method-in-class-win32-nteventlogfile.md) | Class method that changes the security permissions for the logical file specified in the **Name** property.<br/>                                                                                                                 |
| [**ClearEventLog**](cleareventlog-method-in-class-win32-nteventlogfile.md)                             | Clears the specified event log.<br/>                                                                                                                                                                                             |
| [**Compress**](compress-method-in-class-win32-nteventlogfile.md)                                       | Class method that compresses the logical file (or directory) specified in the **Name** property.<br/>                                                                                                                            |
| [**CompressEx**](compressex-method-in-class-win32-nteventlogfile.md)                                   | Class method that uses NTFS compression to compress the logical file (or directory) specified in the **Name** property.<br/>                                                                                                     |
| [**Copy**](copy-method-in-class-win32-nteventlogfile.md)                                               | Class method that copies the logical file or directory specified in the **Name** property to the location specified by the input parameter.<br/>                                                                                 |
| [**CopyEx**](copyex-method-in-class-win32-nteventlogfile.md)                                           | Class method that copies the logical file or directory specified in the **Name** property to the location specified by the *FileName* parameter.<br/>                                                                            |
| [**Delete**](delete-method-in-class-win32-nteventlogfile.md)                                           | Class method that deletes the logical file (or directory) specified in the **Name** property.<br/>                                                                                                                               |
| [**DeleteEx**](deleteex-method-in-class-win32-nteventlogfile.md)                                       | Class method that deletes the logical file (or directory) specified in the **Name** property.<br/>                                                                                                                               |
| [**GetEffectivePermission**](geteffectivepermission-method-in-class-win32-nteventlogfile.md)           | Class method that determines whether the caller has the aggregated permissions specified by the *Permission* argument not only on the file object, but on the share the file or directory resides on (if it is on a share).<br/> |
| [**Rename**](rename-method-in-class-win32-nteventlogfile.md)                                           | Class method that renames the logical file (or directory) specified in the **Name** property.<br/>                                                                                                                               |
| [**TakeOwnerShip**](takeownership-method-in-class-win32-nteventlogfile.md)                             | Class method that obtains ownership of the logical file specified in the **Name** property.<br/>                                                                                                                                 |
| [**TakeOwnerShipEx**](takeownershipex-method-in-class-win32-nteventlogfile.md)                         | Class method that obtains ownership of the logical file specified in the **Name** property.<br/>                                                                                                                                 |
| [**Uncompress**](uncompress-method-in-class-win32-nteventlogfile.md)                                   | Class method that uncompresses the logical file (or directory) specified in the **Name** property.<br/>                                                                                                                          |
| [**UncompressEx**](uncompressex-method-in-class-win32-nteventlogfile.md)                               | Class method that uncompresses the logical file (or directory) specified in the **Name** property.<br/>                                                                                                                          |



 

### Properties

The **Win32\_NTEventlogFile** class has these properties.

<dl> <dt>

**AccessMask**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bitmask that represents the access rights required to access or perform specific operations on the event log file. For bit values, see [**File and Directory Access Rights Constants**](https://msdn.microsoft.com/library/aa822867).

> [!Note]  
> On FAT volumes, the **FULL\_ACCESS** value is returned instead, which indicates no security has been set on the object.

 

</dd> <dt>

**Archive**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, a file that contains Windows events should be archived.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short description of the object.

</dd> <dt>

**Compressed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, a file that contains Windows events is compressed.

</dd> <dt>

**CompressionMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Algorithm or tool used to compress the logical file that contains Windows events.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Name of the first concrete class to appear in the inheritance chain used in the creation of an instance. When used with the other key properties of the class, this property allows all instances of this class and its subclasses to be uniquely identified.

</dd> <dt>

**CreationDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date that the file that contains Windows events was created.

</dd> <dt>

**CSCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Class of the computer system.

</dd> <dt>

**CSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the computer system.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the object.

</dd> <dt>

**Drive**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Drive letter (including colon) of the file that contains Windows events.

Example: "C:"

</dd> <dt>

**EightDotThreeFileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DOS-compatible file name for the file that contains Windows events.

Example: "C:\\PROGRA~1"

</dd> <dt>

**Encrypted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

File that contains Windows events is encrypted.

</dd> <dt>

**EncryptionMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Algorithm or tool used to encrypt the logical file.

</dd> <dt>

**Extension**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

File name extension (without the dot) of the file that contains Windows events.

Example: "txt", "mof", "mdb"

</dd> <dt>

**FileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

File name (without extension) of the file that contains Windows events.

Example: "autoexec"

</dd> <dt>

**FileSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size of the file that contains Windows events (in bytes).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**FileType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

File type (indicated by the **Extension** property).

</dd> <dt>

**FSCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Class of the file system.

</dd> <dt>

**FSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the file system.

</dd> <dt>

**Hidden**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, a file that contains Windows events is hidden.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Object is installed. This property does not need a value to indicate that the object is installed.

</dd> <dt>

**InUseCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of "file opens" that are currently active against the file that contains Windows events.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> <dt>

**LastAccessed**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date and time that the file that contains Windows events was last accessed.

</dd> <dt>

**LastModified**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date and time that the file that contains Windows events was last modified.

</dd> <dt>

**LogfileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the file that contains Windows events. Standard log file names include: Application, System, and Security.

To return the actual path and file name of the event log (for example, C:\\Windows\\System32\\Config\\Sysevent.evt), use the Name property instead.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **string.**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Manufacturer from version resource, if one is present.

</dd> <dt>

**MaxFileSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum size (in bytes) permitted for the file that contains Windows events. If the file exceeds its maximum size, its contents are moved to another file and the primary file is emptied. A value of zero indicates no size limit. WMI retrieves the **Maxsize** value from the Event Log Service registry values.

Although event logs can be sized as large as 4 gigabytes, in practice they should be limited to no more than 300 megabytes. Event logs larger than that can be difficult to analyze because of the number of events contained within the log and because event logs are not optimized for data retrieval.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Inherited name that serves as a key of a logical file instance that contains Windows events within a file system. Full path names should be provided.

Example: "c:\\winnt\\system\\win.ini"

</dd> <dt>

**NumberOfRecords**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of records in the file that contains Windows events. This value is determined by calling the Windows function **GetNumberOfEventLogRecords**.

</dd> <dt>

**OverwriteOutDated**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) (Days), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Number of days after which an event can be overwritten.

Possible values for **OverwriteOutDated** include the following.



| Value                                                                                              | Meaning                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl>                 | Any record can be overwritten if necessary. If necessary, all existing events in the event log can be overwritten to make room for new events.<br/>                                                                            |
| <dl> <dt>1 365</dt> </dl>                   | Events older than the specified number of days can be overwritten as needed. If the event log does not contain any records older than the value specified, no new events will be recorded until the log has been cleared.<br/> |
| <dl> <dt>4294967295 (0xFFFFFFFF)</dt> </dl> | No records can be overwritten. If the log reaches its maximum size, no new events will be recorded until the log has been cleared.<br/>                                                                                        |



 

</dd> <dt>

**OverWritePolicy**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current overwrite policy the Event Log service employs for this log file. Data can be never overwritten, or can be overwritten when necessary or when outdated. When data is outdated depends on the **OverwriteOutDated** value.



| Value                                                                                                                                                                            | Meaning                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WhenNeeded"></span><span id="whenneeded"></span><span id="WHENNEEDED"></span><dl> <dt>**WhenNeeded**</dt> </dl> | The value of **OverwriteOutDated** equals 0 (zero). Any record can be overwritten to make room for new records.<br/>                                         |
| <span id="OutDated"></span><span id="outdated"></span><span id="OUTDATED"></span><dl> <dt>**OutDated**</dt> </dl>         | The value of **OverwriteOutDated** ranges from 1 to 365. Records older than a specified number of days can be overwritten to make room for new records.<br/> |
| <span id="Never"></span><span id="never"></span><span id="NEVER"></span><dl> <dt>**Never**</dt> </dl>                     | The value of **OverwriteOutDated** equals 4294967295. Old records are never overwritten.<br/>                                                                |



 

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Path of the file that contains Windows event. This includes leading and trailing backslashes.

Example: "\\windows\\system\\"

</dd> <dt>

**Readable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, a file that contains Windows events can be read.

</dd> <dt>

**Sources**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of applications that are registered to log into this log file.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current status of the object.

The values are:

<dl><span id="_OK_"></span><span id="_ok_"></span><dt>

**"OK"**
</dt><span id="_Error_"></span><span id="_error_"></span><span id="_ERROR_"></span><dt>

**"Error"**
</dt><span id="_Degraded_"></span><span id="_degraded_"></span><span id="_DEGRADED_"></span><dt>

**"Degraded"**
</dt><span id="_Unknown_"></span><span id="_unknown_"></span><span id="_UNKNOWN_"></span><dt>

**"Unknown"**
</dt><span id="_Pred_Fail_"></span><span id="_pred_fail_"></span><span id="_PRED_FAIL_"></span><dt>

**"Pred Fail"**
</dt><span id="_Starting_"></span><span id="_starting_"></span><span id="_STARTING_"></span><dt>

**"Starting"**
</dt><span id="_Stopping_"></span><span id="_stopping_"></span><span id="_STOPPING_"></span><dt>

**"Stopping"**
</dt><span id="_Service_"></span><span id="_service_"></span><span id="_SERVICE_"></span><dt>

**"Service"**
</dt><span id="_Stressed_"></span><span id="_stressed_"></span><span id="_STRESSED_"></span><dt>

**"Stressed"**
</dt><span id="_NonRecover_"></span><span id="_nonrecover_"></span><span id="_NONRECOVER_"></span><dt>

**"NonRecover"**
</dt><span id="_No_Contact_"></span><span id="_no_contact_"></span><span id="_NO_CONTACT_"></span><dt>

**"No Contact"**
</dt><span id="_Lost_Comm_"></span><span id="_lost_comm_"></span><span id="_LOST_COMM_"></span><dt>

**"Lost Comm"**
</dt> </dl>

</dd> <dt>

**System**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, a file that contains Windows event is a system file.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Version string from version resource if one is present.

</dd> <dt>

**Writeable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, a file that contains Windows events can be written.

</dd> </dl>

## Remarks

The **Win32\_NTEventlogFile** class is derived from [**CIM\_DataFile**](https://msdn.microsoft.com/library/aa387236).

Knowing the properties of your event logs can be useful in planning management activities such as backing up and clearing the logs. For example, knowing both the maximum allowable size and the current size of an event log tells you how much space is available in the log. In turn, this helps you decide whether the log needs to be backed up and cleared.

In addition, tracking the number of records in each log is a simple metric that can often trigger alarms regarding potential problems. For example, suppose routine checks of the number of records in an event log show that a specific computer typically records 100 events a day. Today, however, this routine check shows that the computer has recorded 500 events. This might indicate a serious problem that warrants further investigation.

Scripts that retrieve information about the event logs on a computer do not retrieve information about the Security event log unless those scripts include the Security privilege. The ability to manipulate the Security event log is provided by the Manage auditing and security logs user right, which must be explicitly assigned. To manipulate the Security event log, you must include this privilege as part of the GetObject moniker, even if you are an administrator and have been assigned this right by default.

The Security privilege does not grant you the ability to manage auditing and security logs. You must already possess this right (typically assigned through Group Policy), or the script will fail. To access information from or about the Security event log, you must possess the Manage auditing and security logs user right, and the script must include the Security privilege. The following table indicates the results of querying event logs without including the Security privilege.



| If You Attempt to Access -                 | You Will Retrieve                                         |
|--------------------------------------------|-----------------------------------------------------------|
| All the event logs on a computer           | Data for all the event logs except the Security event log |
| Security event log plus a second event log | Data for only the second event log                        |
| Only the Security event log                | No data                                                   |



 

No special user rights are required to access any of the other event logs on a computer.

## Examples

The following VBScript sample retrieves the number of records in and the maximum file size of the Security event log.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate,(Security)}!\\" & _
 strComputer & "\Root\CIMv2")
Set colLogFiles = objWMIService.ExecQuery("SELECT * FROM Win32_NTEventLogFile WHERE LogFileName='Security'")
For Each objLogFile in colLogFiles
 Wscript.Echo objLogFile.NumberOfRecords
 Wscript.Echo "Maximum Size: " & objLogfile.MaxFileSize
Next
```



The following VBScript code sample demonstrates how to retrieve the info about the event log files on the local machine from instances of **Win32\_NTEventlogFile**.

> [!Note]  
> This script only applies to NT-based systems since Win9x does not support event logs.

 


```VB
Set LogFileSet = GetObject("winmgmts:").InstancesOf ("Win32_NTEventLogFile")

for each Logfile in LogFileSet
 WScript.Echo " Log Name: " & Logfile.LogfileName & Chr(13), _
  "Number of Records: " & Logfile.NumberOfRecords & Chr(13), _
  "Max Size: " & Logfile.MaxFileSize & " bytes" & Chr(13), _
  "File name: " & Logfile.Name
next
```



The following Perl code sample demonstrates how to retrieve the info about the event log files on the local machine from instances of **Win32\_NTEventlogFile**.


```Perl
use strict;
use Win32::OLE;

my ( $LogFileSet, $LogFile );

eval { $LogFileSet = Win32::OLE->GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\cimv2")->
      InstancesOf("Win32_NTEventLogFile"); };

unless ($@)
{
 print "\n";
 foreach $LogFile (in $LogFileSet)
 {
  print "Log Name: ", $LogFile->{LogfileName}, "\n";
  if(defined ($LogFile->{NumberOfRecords}))
  {
   print "Number of Records: ", $LogFile->{NumberOfRecords}, "\n";
  }
  else
  {
   print "Number of Records: \n";
  }
  print "Max Size: ", $LogFile->{MaxFileSize}, " bytes", "\n";
  print "File name: ", $LogFile->{Name}, "\n";
  print "\n";
 }
}
else
{
 print STDERR Win32->LastError, "\n";
}
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Ntevt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntevt.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[WMI Tasks: Event Logs](https://msdn.microsoft.com/library/aa394593)
</dt> </dl>

 

 




