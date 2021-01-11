---
description: The Win32\_Thread&\#8194;WMI class represents a thread of execution.
ms.assetid: a284616c-1977-441a-9173-dff4f56b2d39
ms.tgt_platform: multiple
title: Win32_Thread class
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Win32_Thread
- Win32_Thread.Caption
- Win32_Thread.CreationClassName
- Win32_Thread.CSCreationClassName
- Win32_Thread.CSName
- Win32_Thread.Description
- Win32_Thread.ElapsedTime
- Win32_Thread.ExecutionState
- Win32_Thread.Handle
- Win32_Thread.InstallDate
- Win32_Thread.KernelModeTime
- Win32_Thread.Name
- Win32_Thread.OSCreationClassName
- Win32_Thread.OSName
- Win32_Thread.Priority
- Win32_Thread.PriorityBase
- Win32_Thread.ProcessCreationClassName
- Win32_Thread.ProcessHandle
- Win32_Thread.StartAddress
- Win32_Thread.Status
- Win32_Thread.ThreadState
- Win32_Thread.ThreadWaitReason
- Win32_Thread.UserModeTime
api_type:
- DllExport
api_location:
- CIMWin32.dll
---

# Win32\_Thread class

The **Win32\_Thread** [WMI class](../wmisdk/retrieving-a-class.md) represents a thread of execution. While a process must have one thread of execution, the process can create other threads to execute tasks in parallel. Threads share the process environment, thus multiple threads under the same process use less memory than the same number of processes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4DD-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_Thread : CIM_Thread
{
  string   Caption;
  string   CreationClassName;
  string   CSCreationClassName;
  string   CSName;
  string   Description;
  uint64   ElapsedTime;
  uint16   ExecutionState;
  string   Handle;
  datetime InstallDate;
  uint64   KernelModeTime;
  string   Name;
  string   OSCreationClassName;
  string   OSName;
  uint32   Priority;
  uint32   PriorityBase;
  string   ProcessCreationClassName;
  string   ProcessHandle;
  uint32   StartAddress;
  string   Status;
  uint32   ThreadState;
  uint32   ThreadWaitReason;
  uint64   UserModeTime;
};
```

## Members

The **Win32\_Thread** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_Thread** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Caption")
</dt> </dl>

Short description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Cim\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Name of the first concrete class to appear in the inheritance chain used in the creation of an instance. When used with the other key properties of the class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_Thread**](cim-thread.md).

</dd> <dt>

**CSCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_Process**](cim-process.md).**CSCreationClassName**"), [**Cim\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Creation class name of the scoping computer system.

This property is inherited from [**CIM\_Thread**](cim-thread.md).

</dd> <dt>

**CSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_Process**](cim-process.md).**CSName**"), [**Cim\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Name of the scoping computer system.

This property is inherited from [**CIM\_Thread**](cim-thread.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Description")
</dt> </dl>

Description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**ElapsedTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Performance Data Structures\|[**PERF\_OBJECT\_TYPE**](/windows/win32/api/winperf/ns-winperf-perf_object_type)\|PerfTime"), [**Units**](../wmisdk/standard-qualifiers.md) ("milliseconds")
</dt> </dl>

Total execution time, in milliseconds, given to this thread since its creation.

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> <dt>

**ExecutionState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current operating condition of the thread.

This property is inherited from [**CIM\_Thread**](cim-thread.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Ready"></span><span id="ready"></span><span id="READY"></span>

**Ready** (2)


</dt> <dd></dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

**Running** (3)


</dt> <dd></dd> <dt>

<span id="Blocked"></span><span id="blocked"></span><span id="BLOCKED"></span>

**Blocked** (4)


</dt> <dd></dd> <dt>

<span id="Suspended_Blocked"></span><span id="suspended_blocked"></span><span id="SUSPENDED_BLOCKED"></span>

**Suspended Blocked** (5)


</dt> <dd></dd> <dt>

<span id="Suspended_Ready"></span><span id="suspended_ready"></span><span id="SUSPENDED_READY"></span>

**Suspended Ready** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**Handle**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (256), [**Override**](../wmisdk/standard-qualifiers.md) ("Handle"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Tool Help Structures\|[**THREADENTRY32**](/windows/win32/api/tlhelp32/ns-tlhelp32-threadentry32)\|th32ThreadID")
</dt> </dl>

Handle to a thread. The handle has full access rights by default. With the correct security access, the handle can be used in any function that accepts a thread handle. Depending on the inheritance flag specified when it is created, this handle can be inherited by child processes.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Install Date")
</dt> </dl>

Object was installed. This property does not need a value to indicate that the object is installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**KernelModeTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("KernelModeTime"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Performance Data Structures\|[**PERF\_OBJECT\_TYPE**](/windows/win32/api/winperf/ns-winperf-perf_object_type)\|PrivilegedTime"), [**Units**](../wmisdk/standard-qualifiers.md) ("100 nanoseconds")
</dt> </dl>

Time in kernel mode, in 100 nanosecond units. If this information is not available, a value of 0 (zero) should be used.

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Name")
</dt> </dl>

Label by which the object is known. When subclassed, the property can be overridden to be a key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**OSCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_Process**](cim-process.md).**OSCreationClassName**"), [**Cim\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Creation class name of the scoping operating system.

This property is inherited from [**CIM\_Thread**](cim-thread.md).

</dd> <dt>

**OSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_Process**](cim-process.md).**OSName**"), [**Cim\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Name of the scoping operating system.

This property is inherited from [**CIM\_Thread**](cim-thread.md).

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("Priority"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Tool Help Structures\|[**THREADENTRY32**](/windows/win32/api/tlhelp32/ns-tlhelp32-threadentry32)\|tpDeltaPri")
</dt> </dl>

Dynamic priority of the thread. Each thread has a dynamic priority that the scheduler uses to determine which thread to execute. Initially, a thread's dynamic priority is the same as its base priority. The system can raise and lower the dynamic priority, to ensure that it is responsive (guaranteeing that no threads are starved for processor time). The system does not boost the priority of threads with a base priority level between 16 and 31. Only threads with a base priority between 0 and 15 receive dynamic priority boosts. Higher numbers indicate higher priorities.

</dd> <dt>

**PriorityBase**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Performance Data Structures\|[**PERF\_OBJECT\_TYPE**](/windows/win32/api/winperf/ns-winperf-perf_object_type)\|PerfPriorityBase")
</dt> </dl>

Current base priority of a thread. The operating system may raise the thread's dynamic priority above the base priority if the thread is handling user input, or lower it toward the base priority if the thread becomes compute-bound. The **PriorityBase** property can have a value between 0 and 31.

</dd> <dt>

**ProcessCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_Process**](cim-process.md).**CreationClassName**"), [**Cim\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Value of the scoping process **CreationClassName** property.

This property is inherited from [**CIM\_Thread**](cim-thread.md).

</dd> <dt>

**ProcessHandle**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (256), [**Override**](../wmisdk/standard-qualifiers.md) ("ProcessHandle"), [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_Process**](cim-process.md).**Handle**"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Tool Help Structures\|[**THREADENTRY32**](/windows/win32/api/tlhelp32/ns-tlhelp32-threadentry32)\|th32OwnerProcessID")
</dt> </dl>

Process that created the thread. The contents of this property can be used by Windows application programming interface (API) elements.

</dd> <dt>

**StartAddress**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WIn32API\|Thread Object\|LPTHREAD\_START\_ROUTINE\|lpStartAddress")
</dt> </dl>

Starting address of the thread. Because any application with appropriate access to the thread can change the thread's context, this value may only be an approximation of the thread's starting address.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (10), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Status")
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

The values are:

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

**ThreadState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Thread State")
</dt> </dl>

Current execution state for the thread.

<dt>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>**Initialized** (0)


</dt> <dd>

Initialized — It is recognized by the microkernel.

</dd> <dt>

<span id="Ready"></span><span id="ready"></span><span id="READY"></span>

<span id="Ready"></span><span id="ready"></span><span id="READY"></span>**Ready** (1)


</dt> <dd>

Ready — It is prepared to run on the next available processor.

</dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>**Running** (2)


</dt> <dd>

Running — It is executing.

</dd> <dt>

<span id="Standby"></span><span id="standby"></span><span id="STANDBY"></span>

<span id="Standby"></span><span id="standby"></span><span id="STANDBY"></span>**Standby** (3)


</dt> <dd>

Standby — It is about to run, only one thread may be in this state at a time.

</dd> <dt>

<span id="Terminated"></span><span id="terminated"></span><span id="TERMINATED"></span>

<span id="Terminated"></span><span id="terminated"></span><span id="TERMINATED"></span>**Terminated** (4)


</dt> <dd>

Terminated — It is finished executing.

</dd> <dt>

<span id="Waiting"></span><span id="waiting"></span><span id="WAITING"></span>

<span id="Waiting"></span><span id="waiting"></span><span id="WAITING"></span>**Waiting** (5)


</dt> <dd>

Waiting — It is not ready for the processor, when ready, it will be rescheduled.

</dd> <dt>

<span id="Transition"></span><span id="transition"></span><span id="TRANSITION"></span>

<span id="Transition"></span><span id="transition"></span><span id="TRANSITION"></span>**Transition** (6)


</dt> <dd>

Transition — The thread is waiting for resources other than the processor,

</dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (7)


</dt> <dd>

Unknown — The thread state is unknown.

</dd> </dl>

</dd> <dt>

**ThreadWaitReason**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Thread Wait Reason")
</dt> </dl>

Reason why the thread is waiting. This value is only valid if the **ThreadState** member is set to Transition (6). Event pairs allow communication with protected subsystems.

<dt>

<span id="Executive"></span><span id="executive"></span><span id="EXECUTIVE"></span>

<span id="Executive"></span><span id="executive"></span><span id="EXECUTIVE"></span>**Executive** (0)


</dt> <dd></dd> <dt>

<span id="FreePage"></span><span id="freepage"></span><span id="FREEPAGE"></span>

<span id="FreePage"></span><span id="freepage"></span><span id="FREEPAGE"></span>**FreePage** (1)


</dt> <dd>

FreePage

</dd> <dt>

<span id="PageIn"></span><span id="pagein"></span><span id="PAGEIN"></span>

<span id="PageIn"></span><span id="pagein"></span><span id="PAGEIN"></span>**PageIn** (2)


</dt> <dd></dd> <dt>

<span id="PoolAllocation"></span><span id="poolallocation"></span><span id="POOLALLOCATION"></span>

<span id="PoolAllocation"></span><span id="poolallocation"></span><span id="POOLALLOCATION"></span>**PoolAllocation** (3)


</dt> <dd></dd> <dt>

<span id="ExecutionDelay"></span><span id="executiondelay"></span><span id="EXECUTIONDELAY"></span>

<span id="ExecutionDelay"></span><span id="executiondelay"></span><span id="EXECUTIONDELAY"></span>**ExecutionDelay** (4)


</dt> <dd></dd> <dt>

<span id="FreePage"></span><span id="freepage"></span><span id="FREEPAGE"></span>

<span id="FreePage"></span><span id="freepage"></span><span id="FREEPAGE"></span>**FreePage** (5)


</dt> <dd></dd> <dt>

<span id="PageIn"></span><span id="pagein"></span><span id="PAGEIN"></span>

<span id="PageIn"></span><span id="pagein"></span><span id="PAGEIN"></span>**PageIn** (6)


</dt> <dd></dd> <dt>

<span id="Executive"></span><span id="executive"></span><span id="EXECUTIVE"></span>

<span id="Executive"></span><span id="executive"></span><span id="EXECUTIVE"></span>**Executive** (7)


</dt> <dd></dd> <dt>

<span id="FreePage"></span><span id="freepage"></span><span id="FREEPAGE"></span>

<span id="FreePage"></span><span id="freepage"></span><span id="FREEPAGE"></span>**FreePage** (8)


</dt> <dd></dd> <dt>

<span id="PageIn"></span><span id="pagein"></span><span id="PAGEIN"></span>

<span id="PageIn"></span><span id="pagein"></span><span id="PAGEIN"></span>**PageIn** (9)


</dt> <dd></dd> <dt>

<span id="PoolAllocation"></span><span id="poolallocation"></span><span id="POOLALLOCATION"></span>

<span id="PoolAllocation"></span><span id="poolallocation"></span><span id="POOLALLOCATION"></span>**PoolAllocation** (10)


</dt> <dd></dd> <dt>

<span id="ExecutionDelay"></span><span id="executiondelay"></span><span id="EXECUTIONDELAY"></span>

<span id="ExecutionDelay"></span><span id="executiondelay"></span><span id="EXECUTIONDELAY"></span>**ExecutionDelay** (11)


</dt> <dd></dd> <dt>

<span id="FreePage"></span><span id="freepage"></span><span id="FREEPAGE"></span>

<span id="FreePage"></span><span id="freepage"></span><span id="FREEPAGE"></span>**FreePage** (12)


</dt> <dd></dd> <dt>

<span id="PageIn"></span><span id="pagein"></span><span id="PAGEIN"></span>

<span id="PageIn"></span><span id="pagein"></span><span id="PAGEIN"></span>**PageIn** (13)


</dt> <dd></dd> <dt>

<span id="EventPairHigh"></span><span id="eventpairhigh"></span><span id="EVENTPAIRHIGH"></span>

<span id="EventPairHigh"></span><span id="eventpairhigh"></span><span id="EVENTPAIRHIGH"></span>**EventPairHigh** (14)


</dt> <dd></dd> <dt>

<span id="EventPairLow"></span><span id="eventpairlow"></span><span id="EVENTPAIRLOW"></span>

<span id="EventPairLow"></span><span id="eventpairlow"></span><span id="EVENTPAIRLOW"></span>**EventPairLow** (15)


</dt> <dd></dd> <dt>

<span id="LPCReceive"></span><span id="lpcreceive"></span><span id="LPCRECEIVE"></span>

<span id="LPCReceive"></span><span id="lpcreceive"></span><span id="LPCRECEIVE"></span>**LPCReceive** (16)


</dt> <dd></dd> <dt>

<span id="LPCReply"></span><span id="lpcreply"></span><span id="LPCREPLY"></span>

<span id="LPCReply"></span><span id="lpcreply"></span><span id="LPCREPLY"></span>**LPCReply** (17)


</dt> <dd></dd> <dt>

<span id="VirtualMemory"></span><span id="virtualmemory"></span><span id="VIRTUALMEMORY"></span>

<span id="VirtualMemory"></span><span id="virtualmemory"></span><span id="VIRTUALMEMORY"></span>**VirtualMemory** (18)


</dt> <dd></dd> <dt>

<span id="PageOut"></span><span id="pageout"></span><span id="PAGEOUT"></span>

<span id="PageOut"></span><span id="pageout"></span><span id="PAGEOUT"></span>**PageOut** (19)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (20)


</dt> <dd></dd> </dl>

</dd> <dt>

**UserModeTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("UserModeTime"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Performance Data Structures\|[**PERF\_OBJECT\_TYPE**](/windows/win32/api/winperf/ns-winperf-perf_object_type)\|UserTime"), [**Units**](../wmisdk/standard-qualifiers.md) ("100 nanoseconds")
</dt> </dl>

Time in user mode, in 100 nanoseconds units. If this information is not available, a value of 0 (zero) should be used.

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> </dl>

## Remarks

The **Win32\_Thread** class is derived from [**CIM\_Thread**](cim-thread.md).

**Overview**

For routine day-to-day monitoring, there is usually little reason to have a detailed list of threads and their associated properties. Computers create and delete thousands of threads during the course of a day, and few of these creations or deletions are meaningful to anyone but the developer who wrote the software.

However, when you are troubleshooting problems with an application, tracking the individual threads for a process allows you to identify when threads are created and when (or if) they are destroyed. Because threads that are created but not destroyed cause memory leaks, tracking individual threads can be useful information for support technicians. Likewise, identifying thread priorities can help pinpoint threads that, by running at an abnormally high priority, are preempting CPU cycles needed by other threads and other processes.

**Using Win32\_Thread**

As implied in the preceding syntax block, the **Win32\_Thread** class does not report the name of the process under which each thread runs. Instead, it reports the ID of the process under which the thread runs. To return the name of a process and a list of all its threads, your script must:

1.  Connect to the [**Win32\_Process**](win32-process.md) class and return the list of processes and their process IDs.
2.  Temporarily store this information in an array or Dictionary object.
3.  For each process ID, return the list of threads for that process, and then display the process name and the list of threads.

## Examples

The following VBScript sample monitors the threads running on a computer.


```VB
Set objDictionary = CreateObject("Scripting.Dictionary")
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colProcesses = objWMIService.ExecQuery("SELECT * FROM Win32_Process")
For Each objProcess in colProcesses
 objDictionary.Add objProcess.ProcessID, objProcess.Name
Next
Set colThreads = objWMIService.ExecQuery("SELECT * FROM Win32_Thread")
For Each objThread in colThreads
 intProcessID = CInt(objThread.ProcessHandle)
 strProcessName = objDictionary.Item(intProcessID)
 Wscript.Echo strProcessName & VbTab & objThread.ProcessHandle & _
              VbTab & objThread.Handle & VbTab & objThread.ThreadState
Next
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Thread**](cim-thread.md)
</dt> <dt>

[Operating System Classes](./operating-system-classes.md)
</dt> </dl>

 

 
