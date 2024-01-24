---
description: This class is the event type class for context switch events. The following syntax is simplified from MOF code.
ms.assetid: 3f9f84d0-18a9-493c-b104-8236b2bd8404
title: CSwitch class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSwitch
- CSwitch.NewThreadId
- CSwitch.OldThreadId
- CSwitch.NewThreadPriority
- CSwitch.OldThreadPriority
- CSwitch.PreviousCState
- CSwitch.SpareByte
- CSwitch.OldThreadWaitReason
- CSwitch.OldThreadWaitMode
- CSwitch.OldThreadState
- CSwitch.OldThreadWaitIdealProcessor
- CSwitch.NewThreadWaitTime
- CSwitch.Reserved
api_type: 
- NA
api_location: 
---

# CSwitch class

This class is the event type class for context switch events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{36}, EventTypeName{"CSwitch"}]
class CSwitch : Thread_V2
{
  uint32 NewThreadId;
  uint32 OldThreadId;
  sint8  NewThreadPriority;
  sint8  OldThreadPriority;
  uint8  PreviousCState;
  sint8  SpareByte;
  sint8  OldThreadWaitReason;
  sint8  OldThreadWaitMode;
  sint8  OldThreadState;
  sint8  OldThreadWaitIdealProcessor;
  uint32 NewThreadWaitTime;
  uint32 Reserved;
};
```

## Members

The **CSwitch** class has these types of members:

-   [Properties](#properties)

### Properties

The **CSwitch** class has these properties.

<dl> <dt>

**NewThreadId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Format("x")
</dt> </dl>

New thread ID after the switch.

</dd> <dt>

**NewThreadPriority**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

Thread priority of the new thread.

</dd> <dt>

**NewThreadWaitTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(11), Format("x")
</dt> </dl>

Wait time for the new thread.

</dd> <dt>

**OldThreadId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Format("x")
</dt> </dl>

Previous thread ID.

</dd> <dt>

**OldThreadPriority**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4)
</dt> </dl>

Thread priority of the previous thread.

</dd> <dt>

**OldThreadState**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(9)
</dt> </dl>

State of the previous thread. The following are the possible state values:

| State | Description                                   |
|-------|-----------------------------------------------|
| 0     | Initialized                                   |
| 1     | Ready                                         |
| 2     | Running                                       |
| 3     | Standby                                       |
| 4     | Terminated                                    |
| 5     | Waiting                                       |
| 6     | Transition                                    |
| 7     | DeferredReady (added for Windows Server 2003) |



 

</dd> <dt>

**OldThreadWaitIdealProcessor**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(10), Format("x")
</dt> </dl>

Ideal wait time of the previous thread.

</dd> <dt>

**OldThreadWaitMode**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(8)
</dt> </dl>

Wait mode for the previous thread. The following are the possible values:

| State | Description |
|-------|-------------|
| 0     | KernelMode  |
| 1     | UserMode    |



 

</dd> <dt>

**OldThreadWaitReason**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(7)
</dt> </dl>

Wait reason for the previous thread. The following are the possible values:

| State | Description       |
|-------|-------------------|
| 0     | Executive         |
| 1     | FreePage          |
| 2     | PageIn            |
| 3     | PoolAllocation    |
| 4     | DelayExecution    |
| 5     | Suspended         |
| 6     | UserRequest       |
| 7     | WrExecutive       |
| 8     | WrFreePage        |
| 9     | WrPageIn          |
| 10    | WrPoolAllocation  |
| 11    | WrDelayExecution  |
| 12    | WrSuspended       |
| 13    | WrUserRequest     |
| 14    | WrEventPair       |
| 15    | WrQueue           |
| 16    | WrLpcReceive      |
| 17    | WrLpcReply        |
| 18    | WrVirtualMemory   |
| 19    | WrPageOut         |
| 20    | WrRendezvous      |
| 21    | WrKeyedEvent      |
| 22    | WrTerminated      |
| 23    | WrProcessInSwap   |
| 24    | WrCpuRateControl  |
| 25    | WrCalloutStack    |
| 26    | WrKernel          |
| 27    | WrResource        |
| 28    | WrPushLock        |
| 29    | WrMutex           |
| 30    | WrQuantumEnd      |
| 31    | WrDispatchInt     |
| 32    | WrPreempted       |
| 33    | WrYieldExecution  |
| 34    | WrFastMutex       |
| 35    | WrGuardedMutex    |
| 36    | WrRundown         |
| 37    | MaximumWaitReason |



 

</dd> <dt>

**PreviousCState**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5)
</dt> </dl>

The index of the C-state that was last used by the processor. A value of 0 represents the lightest idle state with higher values representing deeper C-states.

</dd> <dt>

**Reserved**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(12)
</dt> </dl>

Reserved.

</dd> <dt>

**SpareByte**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(6)
</dt> </dl>

Not used.

</dd> </dl>

## Remarks

These events produce a high volume of events.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Thread**](thread.md)
</dt> <dt>

[**Thread\_V2**](thread-v2.md)
</dt> </dl>

 

 




