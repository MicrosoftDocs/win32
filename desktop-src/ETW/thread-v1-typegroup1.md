---
description: This class is the event type class for thread start events. The following syntax is simplified from MOF code.
ms.assetid: 412de56f-4f54-46e8-ab60-d47371247e79
title: Thread_V1_TypeGroup1 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Thread_V1_TypeGroup1
- Thread_V1_TypeGroup1.ProcessId
- Thread_V1_TypeGroup1.TThreadId
- Thread_V1_TypeGroup1.StackBase
- Thread_V1_TypeGroup1.StackLimit
- Thread_V1_TypeGroup1.UserStackBase
- Thread_V1_TypeGroup1.UserStackLimit
- Thread_V1_TypeGroup1.StartAddr
- Thread_V1_TypeGroup1.Win32StartAddr
- Thread_V1_TypeGroup1.WaitMode
api_type: 
- NA
api_location: 
---

# Thread\_V1\_TypeGroup1 class

This class is the event type class for thread start events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{1, 3}, EventTypeName{"Start", "DCStart"}]
class Thread_V1_TypeGroup1 : Thread_V1
{
  uint32 ProcessId;
  uint32 TThreadId;
  uint32 StackBase;
  uint32 StackLimit;
  uint32 UserStackBase;
  uint32 UserStackLimit;
  uint32 StartAddr;
  uint32 Win32StartAddr;
  sint8  WaitMode;
};
```

## Members

The **Thread\_V1\_TypeGroup1** class has these types of members:

-   [Properties](#properties)

### Properties

The **Thread\_V1\_TypeGroup1** class has these properties.

<dl> <dt>

ProcessId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1)
</dt> </dl>

Process identifier of the thread involved in the event.

**Windows Server 2003:** Contains the Format("x") qualifier.

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

TThreadId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2)
</dt> </dl>

Thread identifier of the thread involved in the event.

**Windows Server 2003:** Contains the Format("x") qualifier.

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

WaitMode
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(9), Format("c")
</dt> </dl>

Not used.

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

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**Thread\_V1**](thread-v1.md)
</dt> </dl>

 

 




