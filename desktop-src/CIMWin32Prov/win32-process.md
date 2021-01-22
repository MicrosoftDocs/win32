---
Description: The Win32\_Process&\#32;WMI class represents a process on an operating system.
ms.assetid: 51206aca-4784-4d18-95ca-bc0a45691f78
ms.tgt_platform: multiple
title: Win32_Process class
ms.topic: reference
ms.custom: snippet-project
ms.date: 07/23/2020
topic_type:
- APIRef
- kbSyntax
api_name:
- Win32_Process
- Win32_Process.CreationClassName
- Win32_Process.Caption
- Win32_Process.CommandLine
- Win32_Process.CreationDate
- Win32_Process.CSCreationClassName
- Win32_Process.CSName
- Win32_Process.Description
- Win32_Process.ExecutablePath
- Win32_Process.ExecutionState
- Win32_Process.Handle
- Win32_Process.HandleCount
- Win32_Process.InstallDate
- Win32_Process.KernelModeTime
- Win32_Process.MaximumWorkingSetSize
- Win32_Process.MinimumWorkingSetSize
- Win32_Process.Name
- Win32_Process.OSCreationClassName
- Win32_Process.OSName
- Win32_Process.OtherOperationCount
- Win32_Process.OtherTransferCount
- Win32_Process.PageFaults
- Win32_Process.PageFileUsage
- Win32_Process.ParentProcessId
- Win32_Process.PeakPageFileUsage
- Win32_Process.PeakVirtualSize
- Win32_Process.PeakWorkingSetSize
- Win32_Process.Priority
- Win32_Process.PrivatePageCount
- Win32_Process.ProcessId
- Win32_Process.QuotaNonPagedPoolUsage
- Win32_Process.QuotaPagedPoolUsage
- Win32_Process.QuotaPeakNonPagedPoolUsage
- Win32_Process.QuotaPeakPagedPoolUsage
- Win32_Process.ReadOperationCount
- Win32_Process.ReadTransferCount
- Win32_Process.SessionId
- Win32_Process.Status
- Win32_Process.TerminationDate
- Win32_Process.ThreadCount
- Win32_Process.UserModeTime
- Win32_Process.VirtualSize
- Win32_Process.WindowsVersion
- Win32_Process.WorkingSetSize
- Win32_Process.WriteOperationCount
- Win32_Process.WriteTransferCount
api_type:
- DllExport
api_location:
- CIMWin32.dll
---

# Win32\_Process class

The **Win32\_Process** [WMI class](../wmisdk/retrieving-a-class.md) represents a process on an operating system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

> [!NOTE]
> For a general discussion on Processes and Threads within Windows, please see the topic [Processes and Threads](/ProcThread/processes-and-threads.md).

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), SupportsCreate, CreateBy("Create"), SupportsDelete, DeleteBy("DeleteInstance"), UUID("{8502C4DC-5FBB-11D2-AAC1-006008C78BC7}"), DisplayName("Processes"), AMENDMENT]
class Win32_Process : CIM_Process
{
  string   CreationClassName;
  string   Caption;
  string   CommandLine;
  datetime CreationDate;
  string   CSCreationClassName;
  string   CSName;
  string   Description;
  string   ExecutablePath;
  uint16   ExecutionState;
  string   Handle;
  uint32   HandleCount;
  datetime InstallDate;
  uint64   KernelModeTime;
  uint32   MaximumWorkingSetSize;
  uint32   MinimumWorkingSetSize;
  string   Name;
  string   OSCreationClassName;
  string   OSName;
  uint64   OtherOperationCount;
  uint64   OtherTransferCount;
  uint32   PageFaults;
  uint32   PageFileUsage;
  uint32   ParentProcessId;
  uint32   PeakPageFileUsage;
  uint64   PeakVirtualSize;
  uint32   PeakWorkingSetSize;
  uint32   Priority = NULL;
  uint64   PrivatePageCount;
  uint32   ProcessId;
  uint32   QuotaNonPagedPoolUsage;
  uint32   QuotaPagedPoolUsage;
  uint32   QuotaPeakNonPagedPoolUsage;
  uint32   QuotaPeakPagedPoolUsage;
  uint64   ReadOperationCount;
  uint64   ReadTransferCount;
  uint32   SessionId;
  string   Status;
  datetime TerminationDate;
  uint32   ThreadCount;
  uint64   UserModeTime;
  uint64   VirtualSize;
  string   WindowsVersion;
  uint64   WorkingSetSize;
  uint64   WriteOperationCount;
  uint64   WriteTransferCount;
};
```

## Members

The **Win32\_Process** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_Process** class has these methods.



| Method                                                                   | Description                                                                                                                                                                                                                                                                               |
|:-------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AttachDebugger**](attachdebugger-method-in-class-win32-process.md)   | Launches the currently registered debugger for a process.<br/>                                                                                                                                                                                                                      |
| [**Create**](create-method-in-class-win32-process.md)                   | Creates a new process.<br/>                                                                                                                                                                                                                                                         |
| [**GetAvailableVirtualSize**](getavailablevirtualsize-win32-process.md) | Retrieves the current size, in bytes, of the free virtual address space available to the process.<br/> **Windows Server 2012, Windows 8, Windows 7, Windows Server 2008 and Windows Vista:** This method is not supported before Windows 8.1 and Windows Server 2012 R2.<br/> |
| [**GetOwner**](getowner-method-in-class-win32-process.md)               | Retrieves the user name and domain name under which the process is running.<br/>                                                                                                                                                                                                    |
| [**GetOwnerSid**](getownersid-method-in-class-win32-process.md)         | Retrieves the security identifier (SID) for the owner of a process.<br/>                                                                                                                                                                                                            |
| [**SetPriority**](setpriority-method-in-class-win32-process.md)         | Changes the execution priority of a process.<br/>                                                                                                                                                                                                                                   |
| [**Terminate**](terminate-method-in-class-win32-process.md)             | Terminates a process and all of its threads.<br/>                                                                                                                                                                                                                                   |



 

### Properties

The **Win32\_Process** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Caption")
</dt> </dl>

Short description of an object—a one-line string.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**CommandLine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Command Line To Start Process")
</dt> </dl>

Command line used to start a specific process, if applicable.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Class Name")
</dt> </dl>

Name of the class or subclass used in the creation of an instance. When used with other key properties of the class, this property allows all instances of the class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_Process**](cim-process.md).

</dd> <dt>

**CreationDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](../wmisdk/standard-wmi-qualifiers.md), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("CreationDate")
</dt> </dl>

Date the process begins executing.

This property is inherited from [**CIM\_Process**](cim-process.md).

</dd> <dt>

**CSCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_OperatingSystem**](cim-operatingsystem.md).**CSCreationClassName**"), [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Computer System Class Name")
</dt> </dl>

Creation class name of the scoping computer system.

This property is inherited from [**CIM\_Process**](cim-process.md).

</dd> <dt>

**CSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_OperatingSystem**](cim-operatingsystem.md).**CSName**"), [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Computer System Name")
</dt> </dl>

Name of the scoping computer system.

This property is inherited from [**CIM\_Process**](cim-process.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Description")
</dt> </dl>

Description of an object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**ExecutablePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Privileges**](../wmisdk/standard-wmi-qualifiers.md) ("SeDebugPrivilege"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Tool Help Structures\|[**MODULEENTRY32**](/windows/win32/api/tlhelp32/ns-tlhelp32-moduleentry32)\|szExePath"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Executable Path")
</dt> </dl>

Path to the executable file of the process.

Example: "C:\\Windows\\System\\Explorer.Exe"

</dd> <dt>

**ExecutionState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Execution State")
</dt> </dl>

Current operating condition of the process.

This property is inherited from [**CIM\_Process**](cim-process.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

Unknown

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

Other

</dd> <dt>

<span id="Ready"></span><span id="ready"></span><span id="READY"></span>

<span id="Ready"></span><span id="ready"></span><span id="READY"></span>**Ready** (2)


</dt> <dd></dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>**Running** (3)


</dt> <dd></dd> <dt>

<span id="Blocked"></span><span id="blocked"></span><span id="BLOCKED"></span>

<span id="Blocked"></span><span id="blocked"></span><span id="BLOCKED"></span>**Blocked** (4)


</dt> <dd>

Blocked

</dd> <dt>

<span id="Suspended_Blocked"></span><span id="suspended_blocked"></span><span id="SUSPENDED_BLOCKED"></span>

<span id="Suspended_Blocked"></span><span id="suspended_blocked"></span><span id="SUSPENDED_BLOCKED"></span>**Suspended Blocked** (5)


</dt> <dd></dd> <dt>

<span id="Suspended_Ready"></span><span id="suspended_ready"></span><span id="SUSPENDED_READY"></span>

<span id="Suspended_Ready"></span><span id="suspended_ready"></span><span id="SUSPENDED_READY"></span>**Suspended Ready** (6)


</dt> <dd></dd> <dt>

<span id="Terminated"></span><span id="terminated"></span><span id="TERMINATED"></span>

<span id="Terminated"></span><span id="terminated"></span><span id="TERMINATED"></span>**Terminated** (7)


</dt> <dd></dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (8)


</dt> <dd></dd> <dt>

<span id="Growing"></span><span id="growing"></span><span id="GROWING"></span>

<span id="Growing"></span><span id="growing"></span><span id="GROWING"></span>**Growing** (9)


</dt> <dd></dd> </dl>

</dd> <dt>

**Handle**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](../wmisdk/key-qualifier.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Handle")
</dt> </dl>

Process identifier.

This property is inherited from [**CIM\_Process**](cim-process.md).

</dd> <dt>

**HandleCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|HandleCount"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Handle Count")
</dt> </dl>

Total number of open handles owned by the process. **HandleCount** is the sum of the handles currently open by each thread in this process. A handle is used to examine or modify the system resources. Each handle has an entry in a table that is maintained internally. Entries contain the addresses of the resources and data to identify the resource type.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Install Date")
</dt> </dl>

Date an object is installed. The object may be installed without a value being written to this property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**KernelModeTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("KernelModeTime"), [**Units**](../wmisdk/standard-qualifiers.md) ("100 nanoseconds")
</dt> </dl>

Time in kernel mode, in milliseconds. If this information is not available, use a value of 0 (zero).

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> <dt>

**MaximumWorkingSetSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Privileges**](../wmisdk/standard-wmi-qualifiers.md) ("SeDebugPrivilege"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32\|WINNT.H\|QUOTA\_LIMITS\|MaximumWorkingSetSize"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Maximum Working Set Size"), [**Units**](../wmisdk/standard-qualifiers.md) ("kilobytes")
</dt> </dl>

Maximum working set size of the process. The working set of a process is the set of memory pages visible to the process in physical RAM. These pages are resident, and available for an application to use without triggering a page fault.

Example: 1413120

</dd> <dt>

**MinimumWorkingSetSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Privileges**](../wmisdk/standard-wmi-qualifiers.md) ("SeDebugPrivilege"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32\|WINNT.H\|QUOTA\_LIMITS\|MinimumWorkingSetSize"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Minimum Working Set Size"), [**Units**](../wmisdk/standard-qualifiers.md) ("kilobytes")
</dt> </dl>

Minimum working set size of the process. The working set of a process is the set of memory pages visible to the process in physical RAM. These pages are resident and available for an application to use without triggering a page fault.

Example: 20480

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Name")
</dt> </dl>

Name of the executable file responsible for the process, equivalent to the Image Name property in Task Manager.

When inherited by a subclass, the property can be overridden to be a key property. The name is hard-coded into the application itself and is not affected by changing the file name. For example, even if you rename Calc.exe, the name Calc.exe will still appear in Task Manager and in any WMI scripts that retrieve the process name.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**OSCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_OperatingSystem**](cim-operatingsystem.md).**CreationClassName**"), [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Operating System Class Name")
</dt> </dl>

Creation class name of the scoping operating system.

This property is inherited from [**CIM\_Process**](cim-process.md).

</dd> <dt>

**OSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_OperatingSystem**](cim-operatingsystem.md).**Name**"), [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Operating System Name")
</dt> </dl>

Name of the scoping operating system.

This property is inherited from [**CIM\_Process**](cim-process.md).

</dd> <dt>

**OtherOperationCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|SYSTEM\_PROCESS\_INFORMATION\|OtherOperationCount"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Other Operation Count")
</dt> </dl>

Number of I/O operations performed that are not read or write operations.

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> <dt>

**OtherTransferCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|SYSTEM\_PROCESS\_INFORMATION\|OtherTransferCount"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Other Transfer Count"), [**Units**](../wmisdk/standard-qualifiers.md) ("bytes")
</dt> </dl>

Amount of data transferred during operations that are not read or write operations.

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> <dt>

**PageFaults**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|PageFaultCount"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Number Of Page Faults")
</dt> </dl>

Number of page faults that a process generates.

Example: 10

</dd> <dt>

**PageFileUsage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|PagefileUsage"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Page File Usage"), [**Units**](../wmisdk/standard-qualifiers.md) ("kilobytes")
</dt> </dl>

Amount of page file space that a process is using currently. This value is consistent with the **VMSize** value in TaskMgr.exe.

Example: 102435

</dd> <dt>

**ParentProcessId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|InheritedFromUniqueProcessId"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Parent Process Id")
</dt> </dl>

Unique identifier of the process that creates a process. Process identifier numbers are reused, so they only identify a process for the lifetime of that process. It is possible that the process identified by **ParentProcessId** is terminated, so **ParentProcessId** may not refer to a running process. It is also possible that **ParentProcessId** incorrectly refers to a process that reuses a process identifier. You can use the **CreationDate** property to determine whether the specified parent was created after the process represented by this **Win32\_Process** instance was created.

</dd> <dt>

**PeakPageFileUsage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|PeakPagefileUsage"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Peak Page File Usage"), [**Units**](../wmisdk/standard-qualifiers.md) ("kilobytes")
</dt> </dl>

Maximum amount of page file space used during the life of a process.

Example: 102367

</dd> <dt>

**PeakVirtualSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|PeakVirtualSize"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Peak Virual Address Space Usage"), [**Units**](../wmisdk/standard-qualifiers.md) ("bytes")
</dt> </dl>

Maximum virtual address space a process uses at any one time. Using virtual address space does not necessarily imply corresponding use of either disk or main memory pages. However, virtual space is finite, and by using too much the process might not be able to load libraries.

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> <dt>

**PeakWorkingSetSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|PeakWorkingSetSize"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Peak Working Set Size"), [**Units**](../wmisdk/standard-qualifiers.md) ("kilobytes")
</dt> </dl>

Peak working set size of a process.

Example: 1413120

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("Priority"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|BasePriority"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Priority")
</dt> </dl>

Scheduling priority of a process within an operating system. The higher the value, the higher priority a process receives. Priority values can range from 0 (zero), which is the lowest priority to 31, which is highest priority.

Example: 7

</dd> <dt>

**PrivatePageCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|PrivatePageCount"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Private Page Count")
</dt> </dl>

Current number of pages allocated that are only accessible to the process represented by this **Win32\_Process** instance.

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> <dt>

**ProcessId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|[**PROCESS\_INFORMATION**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-process_information)\|dwProcessId "), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Process Id")
</dt> </dl>

Numeric identifier used to distinguish one process from another. ProcessIDs are valid from process creation time to process termination. Upon termination, that same numeric identifier can be applied to a new process.

This means that you cannot use ProcessID alone to monitor a particular process. For example, an application could have a ProcessID of 7, and then fail. When a new process is started, the new process could be assigned ProcessID 7. A script that checked only for a specified ProcessID could thus be "fooled" into thinking that the original application was still running.

</dd> <dt>

**QuotaNonPagedPoolUsage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|QuotaNonPagedPoolUsage"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Non-Paged Pool Usage Quota")
</dt> </dl>

Quota amount of nonpaged pool usage for a process.

Example: 15

</dd> <dt>

**QuotaPagedPoolUsage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|QuotaPagedPoolUsage"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Paged Pool Usage Quota")
</dt> </dl>

Quota amount of paged pool usage for a process.

Example: 22

</dd> <dt>

**QuotaPeakNonPagedPoolUsage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|QuotaPeakNonPagedPoolUsage"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Peak Non-Paged Pool Usage Quota")
</dt> </dl>

Peak quota amount of nonpaged pool usage for a process.

Example: 31

</dd> <dt>

**QuotaPeakPagedPoolUsage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|QuotaPeakPagedPoolUsage"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Peak Paged Pool Usage Quota")
</dt> </dl>

Peak quota amount of paged pool usage for a process.

Example: 31

</dd> <dt>

**ReadOperationCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|SYSTEM\_PROCESS\_INFORMATION\|ReadOperationCount"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Read Operation Count")
</dt> </dl>

Number of read operations performed.

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> <dt>

**ReadTransferCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|SYSTEM\_PROCESS\_INFORMATION\|ReadTransferCount"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Read Transfer Count"), [**Units**](../wmisdk/standard-qualifiers.md) ("bytes")
</dt> </dl>

Amount of data read.

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> <dt>

**SessionId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|SessionId"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Session Id")
</dt> </dl>

Unique identifier that an operating system generates when a session is created. A session spans a period of time from logon until logoff from a specific system.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (10), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Status")
</dt> </dl>

This property is not implemented and does not get populated for any instance of this class. It is always **NULL**.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

Values include the following:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

</dd> <dt>

**TerminationDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Termination Date")
</dt> </dl>

Process was stopped or terminated. To get the termination time, a handle to the process must be held open. Otherwise, this property returns **NULL**.

This property is inherited from [**CIM\_Process**](cim-process.md).

</dd> <dt>

**ThreadCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|NumberOfThreads"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Thread Count")
</dt> </dl>

Number of active threads in a process. An instruction is the basic unit of execution in a processor, and a thread is the object that executes an instruction. Each running process has at least one thread.

</dd> <dt>

**UserModeTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("UserModeTime"), [**Units**](../wmisdk/standard-qualifiers.md) ("100 nanoseconds")
</dt> </dl>

Time in user mode, in 100 nanosecond units. If this information is not available, use a value of 0 (zero).

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> <dt>

**VirtualSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process Status\|SYSTEM\_PROCESS\_INFORMATION\|VirtualSize"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Virtual Address Space Usage"), [**Units**](../wmisdk/standard-qualifiers.md) ("bytes")
</dt> </dl>

Current size of the virtual address space that a process is using, not the physical or virtual memory actually used by the process. Using virtual address space does not necessarily imply corresponding use of either disk or main memory pages. Virtual space is finite, and by using too much, the process might not be able to load libraries. This value is consistent with what you see in Perfmon.exe.

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> <dt>

**WindowsVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Functions\|GetProcessVersion"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Windows Version")
</dt> </dl>

Version of Windows in which the process is running.

Example: 4.0

</dd> <dt>

**WorkingSetSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Working Set Size"), [**Units**](../wmisdk/standard-qualifiers.md) ("bytes")
</dt> </dl>

Amount of memory in bytes that a process needs to execute efficiently—for an operating system that uses page-based memory management. If the system does not have enough memory (less than the working set size), thrashing occurs. If the size of the working set is not known, use **NULL** or 0 (zero). If working set data is provided, you can monitor the information to understand the changing memory requirements of a process.

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

This property is inherited from [**CIM\_Process**](cim-process.md).

</dd> <dt>

**WriteOperationCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|SYSTEM\_PROCESS\_INFORMATION\|WriteOperationCount"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Write Operation Count")
</dt> </dl>

Number of write operations performed.

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> <dt>

**WriteTransferCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|SYSTEM\_PROCESS\_INFORMATION\|WriteTransferCount"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Write Transfer Count"), [**Units**](../wmisdk/standard-qualifiers.md) ("bytes")
</dt> </dl>

Amount of data written.

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> </dl>

## Remarks

The **Win32\_Process** class is derived from [**CIM\_Process**](cim-process.md). The calling process that uses this class must have the **SE\_RESTORE\_NAME** privilege on the computer in which the registry resides. For more information, see [Executing Privileged Operations](../wmisdk/executing-privileged-operations.md).

### Overview

Processes underlie almost everything that happens on a computer. In fact, the root cause of most computer problems can be traced to processes; for example, too many processes might be running on a computer (and contending for a finite set of resources), or a single process might be using more than its share of resources. These factors make it important to keep a close watch on the processes running on a computer. Process monitoring, the main activity in process management, allows you to determine what a computer actually does, what applications the computer runs, and how those applications are affected by changes in the computing environment.

### Monitoring a Process

Monitoring processes on a regular basis helps you ensure that a computer runs at peak efficiency and that it carries out its appointed tasks as expected. For example, by monitoring processes you can be notified immediately of any application that has stopped responding, and then take steps to end that process. In addition, process monitoring enables you to identify problems before they occur. For example, by repeatedly checking the amount of memory used by a process, you can identify a memory leak. You can then stop the process before the errant application uses all of the available memory and brings the computer to a halt.

Process monitoring also helps minimize the disruptions caused by planned outages for upgrades and maintenance. For example, by checking the status of a database application running on client computers, you can determine the impact of taking the database offline in order to upgrade the software.

Monitoring process availability. Measures the percentage of time that a process is available. Availability is typically monitored by use of a simple probe, which reports whether the process is still running. By keeping track of the results of each probe, you can calculate the availability of the process. For example, a process that is probed 100 times and responds on 95 of those occasions has an availability of 95 percent. This type of monitoring is typically reserved for databases, mail programs, and other applications that are expected to run at all times. It is not appropriate for word processing programs, spreadsheets, or other applications that are routinely started and stopped several times a day.

You can create an instance of the [**Win32\_ProcessStartup**](win32-processstartup.md) class to configure the process.

You can monitor process performance with the [**Win32\_PerfFormattedData\_PerfProc\_Process**](../wmisdk/retrieving-raw-and-formatted-performance-data.md) class and a WMI refresher object, such as [**SWbemRefresher**](../wmisdk/swbemrefresher.md). For more information, see [Monitoring Performance Data](../wmisdk/monitoring-performance-data.md).

## Examples

The [List the Properties of WMI Classes](https://Gallery.TechNet.Microsoft.Com/a7918bf3-bc03-4553-990f-aba13cf196b7) PowerShell code sample on TechNet Gallery describes the **Win32\_Process** class, and outputs the results in Excel format.

The [Terminate running process on multiple servers](https://Gallery.TechNet.Microsoft.Com/698c2512-2bbd-40ee-b3bf-a9cebdad2faf) terminates a process running on a single or multiple computers.

In the [Example: Calling a Provider Method](../wmisdk/example--calling-a-provider-method.md) topic, the code uses C++ to call **Win32\_Process** to create a process.

Availability is the simplest form of process monitoring: with this approach, you simply ensure that the process is running. When you monitor for process availability, you typically retrieve a list of processes running on a computer and then verify that a particular process is still active. If the process is active, it is considered available. If the process is not active, it is not available. The following VBScript sample monitors process availability by checking the list of processes running on a computer and issuing a notification if the Database.exe process is not found.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colProcesses = objWMIService.ExecQuery("SELECT * FROM Win32_Process WHERE Name = 'Database.exe'")
If colProcesses.Count = 0 Then
 Wscript.Echo "Database.exe is not running."
Else
 Wscript.Echo "Database.exe is running."
End If
```



The following VBScript sample monitors process creation using a temporary event consumer.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colMonitoredProcesses = objWMIService.ExecNotificationQuery("SELECT * FROM __InstanceCreationEvent " _
                                                     & "WITHIN 10 WHERE TargetInstance ISA 'Win32_Process'")
i = 0
Do While i = 0
 Set objLatestProcess = colMonitoredProcesses.NextEvent
 Wscript.Echo objLatestProcess.TargetInstance.Name, Now
Loop
```



The following VBScript monitors process performance information.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colProcessList = objWMIService.ExecQuery("SELECT * FROM Win32_Process")
For Each objProcess in colProcessList
 Wscript.Echo "Process: " & objProcess.Name
 Wscript.Echo "Process ID: " & objProcess.ProcessID
 Wscript.Echo "Thread Count: " & objProcess.ThreadCount
 Wscript.Echo "Page File Size: " & objProcess.PageFileUsage
 Wscript.Echo "Page Faults: " & objProcess.PageFaults
 Wscript.Echo "Working Set Size: " & objProcess.WorkingSetSize
Next
```



The following VBScript code example shows how to obtain the owner of each process on a local computer. You can use this script to obtain data from a remote computer, for example, to determine which users have processes running terminal server, substitute the name of the remote computer for "." in the first line. You must also be an administrator on the remote machine.


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")

Set colProcesses = objWMIService.ExecQuery("select * from win32_process" )
For Each objProcess in colProcesses

  If objProcess.GetOwner ( User, Domain ) = 0 Then
    Wscript.Echo "Process " & objProcess.Caption & " belongs to " & Domain & "\" & User
  Else
    Wscript.Echo "Problem " & Rtn & " getting the owner for process " & objProcess.Caption
  End If
Next
```



The following VBScript code example shows how to obtain the logon session associated with a running process. A process must be running Notepad.exe before the script starts. The example locates the instances of [**Win32\_LogonSession**](win32-logonsession.md) associated with the **Win32\_Process** that represents Notepad.exe. [**Win32\_SessionProcess**](win32-sessionprocess.md) is specified as the association class. For more information, see [ASSOCIATORS OF Statement.](../wmisdk/associators-of-statement.md).


```VB
On error resume next
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\.\root\cimv2")
Set colProcesses = objWMIService.ExecQuery("Select * from Win32_Process Where Name = 'Notepad.exe'")
For Each objProcess in colProcesses
  ProcessId = objProcess.ProcessId
  Set colLogonSessions = objWMIService.ExecQuery("Associators of {Win32_Process='" & ProcessId & "'} " _
                                               & "Where Resultclass = Win32_LogonSession Assocclass = Win32_SessionProcess", "WQL", 48)
  If Err <> 0 Then
    WScript.Echo "Error on associators query= " & Err.number & " " & Err.Description
    WScript.Quit
  End If
  For Each LogonSession in colLogonSessions
    Wscript.Echo " Logon id is " & LogonSession.LogonId
  Next
Next
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Process**](cim-process.md)
</dt> <dt>

[Operating System Classes](./operating-system-classes.md)
</dt> <dt>

[WMI Tasks: Processes](../wmisdk/wmi-tasks--processes.md)
</dt> </dl>

 

 