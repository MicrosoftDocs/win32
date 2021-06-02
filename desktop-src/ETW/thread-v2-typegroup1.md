---
description: Thread_V2_TypeGroup1 class - This class is the event type class for thread start and end events. The following syntax is simplified from MOF code.
ms.assetid: c24b4bc9-2a05-444c-be41-b4dfd0511b93
title: Thread_V2_TypeGroup1 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Thread_V2_TypeGroup1
- Thread_V2_TypeGroup1.ProcessId
- Thread_V2_TypeGroup1.TThreadId
- Thread_V2_TypeGroup1.StackBase
- Thread_V2_TypeGroup1.StackLimit
- Thread_V2_TypeGroup1.UserStackBase
- Thread_V2_TypeGroup1.UserStackLimit
- Thread_V2_TypeGroup1.StartAddr
- Thread_V2_TypeGroup1.Win32StartAddr
- Thread_V2_TypeGroup1.TebBase
- Thread_V2_TypeGroup1.SubProcessTag
api_type: 
- NA
api_location: 
---

# Thread\_V2\_TypeGroup1 class

This class is the event type class for thread start and end events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{1, 2, 3, 4}, EventTypeName{"Start", "End", "DCStart", "DCEnd"}]
class Thread_V2_TypeGroup1 : Thread_V2
{
  uint32 ProcessId;
  uint32 TThreadId;
  uint32 StackBase;
  uint32 StackLimit;
  uint32 UserStackBase;
  uint32 UserStackLimit;
  uint32 StartAddr;
  uint32 Win32StartAddr;
  uint32 TebBase;
  uint32 SubProcessTag;
};
```

## Members

The **Thread\_V2\_TypeGroup1** class has these types of members:

-   [Properties](#properties)

### Properties

The **Thread\_V2\_TypeGroup1** class has these properties.

<dl> <dt>

ProcessId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Format("x")
</dt> </dl>

Process identifier of the thread involved in the event.

</dd> <dt>

StackBase
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3), Pointer
</dt> </dl>

Base address of the thread's stack.

</dd> <dt>

StackLimit
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4), Pointer
</dt> </dl>

Limit of the thread's stack.

</dd> <dt>

StartAddr
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(7), Pointer
</dt> </dl>

Memory address at which the trace starts.

</dd> <dt>

SubProcessTag
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(10), Format("x")
</dt> </dl>

Identifies the service if the thread is owned by a service; otherwise, zero.

</dd> <dt>

TebBase
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(9), Pointer
</dt> </dl>

Thread environment block base address.

</dd> <dt>

TThreadId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Format("x")
</dt> </dl>

Thread identifier of the thread involved in the event.

</dd> <dt>

UserStackBase
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5), Pointer
</dt> </dl>

Base address of the thread's user-mode stack.

</dd> <dt>

UserStackLimit
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(6), Pointer
</dt> </dl>

Limit of the thread's user-mode stack.

</dd> <dt>

Win32StartAddr
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(8), Pointer
</dt> </dl>

Starting address of the function to be executed by this thread.

</dd> </dl>

## Remarks

The DCStart and DCEnd event types enumerate the threads that are currently running at the time the kernel session starts and ends, respectively.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Thread**](thread.md)
</dt> <dt>

[**Thread\_V2**](thread-v2.md)
</dt> </dl>

 

 




