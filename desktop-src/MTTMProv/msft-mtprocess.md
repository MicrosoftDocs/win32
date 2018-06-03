---
title: MSFT\_MTProcess class
description: The process data object. Statistic data is calculated based on current interval seconds setting.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 14d46616-1bde-4d80-9ae6-a98c3630d86e
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_MTProcess class
- MSFT_MTProcess class, described
topic_type:
- apiref
api_name:
- MSFT_MTProcess
- MSFT_MTProcess.InstanceID
- MSFT_MTProcess.Caption
- MSFT_MTProcess.ElementName
- MSFT_MTProcess.Description
- MSFT_MTProcess.ProcessId
- MSFT_MTProcess.Name
- MSFT_MTProcess.ExecutablePath
- MSFT_MTProcess.ProcessStatus
- MSFT_MTProcess.UserName
- MSFT_MTProcess.CommandLine
- MSFT_MTProcess.SessionId
- MSFT_MTProcess.CpuTime
- MSFT_MTProcess.CycleTime
- MSFT_MTProcess.CreationDate
- MSFT_MTProcess.CreationTime
- MSFT_MTProcess.WorkingSetSize
- MSFT_MTProcess.PeakWorkingSetSize
- MSFT_MTProcess.PrivateWorkingSetSize
- MSFT_MTProcess.SharedWorkingSetSize
- MSFT_MTProcess.CommitCharge
- MSFT_MTProcess.PagedPool
- MSFT_MTProcess.NonPagedPool
- MSFT_MTProcess.PageFaults
- MSFT_MTProcess.BasePriority
- MSFT_MTProcess.HandleCount
- MSFT_MTProcess.ThreadCount
- MSFT_MTProcess.UserObjects
- MSFT_MTProcess.GdiObjects
- MSFT_MTProcess.ReadOperationCount
- MSFT_MTProcess.WriteOperationCount
- MSFT_MTProcess.OtherOperationCount
- MSFT_MTProcess.ReadTransferCount
- MSFT_MTProcess.WriteTransferCount
- MSFT_MTProcess.OtherTransferCount
- MSFT_MTProcess.OperatingSystemContext
- MSFT_MTProcess.Platform
- MSFT_MTProcess.Elevated
- MSFT_MTProcess.UACVirtualization
- MSFT_MTProcess.DataExecutionPrevention
- MSFT_MTProcess.IsImmersive
- MSFT_MTProcess.IntervalSeconds
- MSFT_MTProcess.CpuPercent
- MSFT_MTProcess.CyclePercent
- MSFT_MTProcess.DeltaWorkingSetSize
- MSFT_MTProcess.DeltaPageFaults
api_location:
- MtTmProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_MTProcess class

The process data object. Statistic data is calculated based on current interval seconds setting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), dynamic, provider("mttmprov"), AMENDMENT]
class MSFT_MTProcess : CIM_ManagedElement
{
  string   InstanceID;
  string   Caption;
  string   ElementName;
  string   Description;
  uint32   ProcessId;
  string   Name;
  string   ExecutablePath;
  uint16   ProcessStatus;
  string   UserName;
  string   CommandLine;
  uint32   SessionId;
  uint64   CpuTime;
  uint64   CycleTime;
  datetime CreationDate;
  uint64   CreationTime;
  uint64   WorkingSetSize;
  uint64   PeakWorkingSetSize;
  uint64   PrivateWorkingSetSize;
  uint64   SharedWorkingSetSize;
  uint64   CommitCharge;
  uint64   PagedPool;
  uint64   NonPagedPool;
  uint32   PageFaults;
  uint32   BasePriority;
  uint32   HandleCount;
  uint32   ThreadCount;
  uint32   UserObjects;
  uint32   GdiObjects;
  uint64   ReadOperationCount;
  uint64   WriteOperationCount;
  uint64   OtherOperationCount;
  uint64   ReadTransferCount;
  uint64   WriteTransferCount;
  uint64   OtherTransferCount;
  uint16   OperatingSystemContext;
  uint16   Platform;
  boolean  Elevated;
  uint16   UACVirtualization;
  boolean  DataExecutionPrevention;
  boolean  IsImmersive;
  uint16   IntervalSeconds;
  real32   CpuPercent;
  real32   CyclePercent;
  sint64   DeltaWorkingSetSize;
  sint32   DeltaPageFaults;
};
```

## Members

The **MSFT\_MTProcess** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_MTProcess** class has these methods.



| Method                                                | Description                                                  |
|:------------------------------------------------------|:-------------------------------------------------------------|
| [**CreateDump**](createdump-msft-mtprocess.md)       | Create process mini dump of the process instance.<br/> |
| [**CreateProcess**](createprocess-msft-mtprocess.md) | Create a new process.<br/>                             |



 

### Properties

The **MSFT\_MTProcess** class has these properties.

<dl> <dt>

**BasePriority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the ranking that determines the order in which threads of a process are scheduled.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**CommandLine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the command line used to start a specific process, if applicable.

</dd> <dt>

**CommitCharge**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the amount of virtual memory reserved, in bytes, by the operating system for the process.

</dd> <dt>

**CpuPercent**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the current processor utilization percentage across cores since last update.

</dd> <dt>

**CpuTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total processor time, in 100 nanosecond units, elapsed since the process began.

</dd> <dt>

**CreationDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the creation date time of the process.

</dd> <dt>

**CreationTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the creation time of the process, in the number of 100-nanosecond intervals since January 1, 1601 (UTC).

</dd> <dt>

**CyclePercent**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the current cycle time utilization percentage since last update.

</dd> <dt>

**CycleTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total cycle time, in 100 nanosecond units, elapsed since the process began.

</dd> <dt>

**DataExecutionPrevention**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether Data Execution Prevention (a security feature) enabled or disabled for the process.

</dd> <dt>

**DeltaPageFaults**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the change in number of page faults in the process since last update.

</dd> <dt>

**DeltaWorkingSetSize**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the change, in bytes, in working set usage by the process since last update.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Description)
</dt> </dl>

Description of process.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. Note that the **Name** property of [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where **Name** exists and is not a Key (such as for instances of [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884)), the same information can be present in both the **Name** and **ElementName** properties. Note that if there is an associated instance of **CIM\_EnabledLogicalElementCapabilities**, restrictions on this properties may exist as defined in **ElementNameMask** and **MaxElementNameLen** properties defined in that class.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Elevated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that specifies whether the process is running elevated or not.

</dd> <dt>

**ExecutablePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the path to the executable file of the process.

</dd> <dt>

**GdiObjects**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the number of GDI objects used by the process.

</dd> <dt>

**HandleCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of open handles owned by the process.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**InstanceID** is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below. To ensure uniqueness within the NameSpace, the value of **InstanceID** should be constructed using the following "preferred" algorithm: "*OrgID*:*LocalID*" Where *OrgID* and *LocalID* are separated by a colon (:), and where *OrgID* must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the **InstanceID** or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, *OrgID* must not contain a colon (:). When using this algorithm, the first colon to appear in **InstanceID** must appear between *OrgID* and *LocalID*. *LocalID* is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting **InstanceID** is not reused across any **InstanceID**s produced by this or other providers for the NameSpace of this instance. If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the *OrgID* set to "CIM".

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**IntervalSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the current data collection interval in seconds.

</dd> <dt>

**IsImmersive**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates whether the process is an App Store application.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of process either executable image name or internal system process name.

</dd> <dt>

**NonPagedPool**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the amount, in bytes, of non-pageable kernel memory allocated by the kernel or drivers on behalf of the process.

</dd> <dt>

**OperatingSystemContext**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the operating system context in which the process is running.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="XP"></span><span id="xp"></span>

**XP** (1)


</dt> <dd></dd> <dt>

<span id="Vista"></span><span id="vista"></span><span id="VISTA"></span>

**Vista** (2)


</dt> <dd></dd> <dt>

<span id="Win7"></span><span id="win7"></span><span id="WIN7"></span>

**Win7** (3)


</dt> <dd></dd> <dt>

<span id="Win8"></span><span id="win8"></span><span id="WIN8"></span>

**Win8** (4)


</dt> <dd></dd> <dt>

<span id="Win8.1"></span><span id="win8.1"></span><span id="WIN8.1"></span>

**Win8.1** (5)


</dt> <dd></dd> <dt>

<span id="Win10"></span><span id="win10"></span><span id="WIN10"></span>

**Win10** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**OtherOperationCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the number of non-read/non-write I/O operations (for instance, control functions) generated by the process since it was started.

</dd> <dt>

**OtherTransferCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes read by the process in I/O operations other than read/write(for instance, control functions).

</dd> <dt>

**PagedPool**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the amount, in bytes, of pageable kernel memory allocated by the kernel or drivers on behalf of the process.

</dd> <dt>

**PageFaults**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the number of page faults generated by the process since it was started.

</dd> <dt>

**PeakWorkingSetSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the maximum amount of physical memory, in bytes, used by the process.

</dd> <dt>

**Platform**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the platform (32 bit or 64 bit) on which the process is running.

<dt>

<span id="32-bit"></span><span id="32-BIT"></span>

**32-bit** (0)


</dt> <dd></dd> <dt>

<span id="64-bit"></span><span id="64-BIT"></span>

**64-bit** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**PrivateWorkingSetSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the amount of physical memory, in bytes, in use by the process that cannot be used by other processes.

</dd> <dt>

**ProcessId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the global process identifier that is used to identify a process. The value is valid from the time a process is created until it is terminated.

</dd> <dt>

**ProcessStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the status of process execution.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

**Running** (1)


</dt> <dd></dd> <dt>

<span id="Suspended"></span><span id="suspended"></span><span id="SUSPENDED"></span>

**Suspended** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**ReadOperationCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the number of read I/O operations generated by the process since it was started.

</dd> <dt>

**ReadTransferCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes read by the process in I/O operations.

</dd> <dt>

**SessionId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the unique identifier that an operating system generates when a session is created. A session spans a period of time from logon until logoff from a specific system.

</dd> <dt>

**SharedWorkingSetSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the amount of physical memory, in bytes, in use by the process that can be shared with other processes.

</dd> <dt>

**ThreadCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the number of active threads in a process.

</dd> <dt>

**UACVirtualization**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the a value that specifies whether User Account Control (UAC) virtualization is enabled, disabled, or not allowed in the process.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (1)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="NotAllowed"></span><span id="notallowed"></span><span id="NOTALLOWED"></span>

**NotAllowed** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the user name of process.

</dd> <dt>

**UserObjects**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the number of windows manager objects (windows, menus, cursors, keyboard layouts, monitors, etc.) used by the process.

</dd> <dt>

**WorkingSetSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the amount of physical memory, in Kilobytes, currently in use by the process.

</dd> <dt>

**WriteOperationCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the number of write I/O operations generated by the process since it was started.

</dd> <dt>

**WriteTransferCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes written by the process in I/O operations.

</dd> </dl>

## Examples

This PowerShell snippet connects to the *TestSrv1* computer and enumerates the processes.


```PowerShell
$option = New-CimSessionOption -Protocol WSMan
$session = New-CimSession -ComputerName TestSrv1 -SessionOption $option -Credential (Get-Credential)
Get-CimInstance -CimSession $session -Namespace Root/Microsoft/Windows/ManagementTools MSFT_MTProcess | Select Name,CpuPercent,ProcessId
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                    |
| MOF<br/>                      | <dl> <dt>MtTmProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MtTmProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> <dt>

[Management Tools Task Manager WMI Provider](management-tools-task-manager-wmi-provider-portal.md)
</dt> </dl>

 

 





