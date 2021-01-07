---
description: This class is the event type class for ready thread events. The following syntax is simplified from MOF code.
ms.assetid: 861ab070-5536-4897-b523-9b09a7d59b3e
title: ReadyThread class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ReadyThread
- ReadyThread.TThreadId
- ReadyThread.AdjustReason
- ReadyThread.AdjustIncrement
- ReadyThread.Flag
- ReadyThread.Reserved
api_type: 
- NA
api_location: 
---

# ReadyThread class

This class is the event type class for ready thread events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{50}, EventTypeName{"ReadyThread"}]
class ReadyThread : Thread_V2
{
  uint32 TThreadId;
  sint8  AdjustReason;
  sint8  AdjustIncrement;
  sint8  Flag;
  sint8  Reserved;
};
```

## Members

The **ReadyThread** class has these types of members:

-   [Properties](#properties)

### Properties

The **ReadyThread** class has these properties.

<dl> <dt>

AdjustIncrement
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

The value by which the priority is being adjusted.

</dd> <dt>

AdjustReason
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2)
</dt> </dl>

The reason for the priority boost.



| Value                                                                        | Meaning                                                                                                                 |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Ignore the increment.<br/>                                                                                        |
| <dl> <dt>1</dt> </dl> | Apply the increment, which will decay incrementally at the end of each quantum.<br/>                              |
| <dl> <dt>2</dt> </dl> | Apply the increment as a boost that will decay in its entirety at quantum (typically for priority donation).<br/> |



 

</dd> <dt>

Flag
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4)
</dt> </dl>

The following are the possible state flags:



| Value                                                                          | Meaning                                                                    |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt>0x1</dt> </dl> | The thread has been readied from DPC (deferred procedure call).<br/> |
| <dl> <dt>0x2</dt> </dl> | The kernel stack is currently swapped out.<br/>                      |
| <dl> <dt>0x4</dt> </dl> | The process address space is swapped out.<br/>                       |



 

Note that when the kernel stack or the process address space is swapped out, there will be an additional ReadyThread event after the kernel stack or the process address space has been swapped back in and the thread is made ready to be dispatched.

</dd> <dt>

Reserved
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5)
</dt> </dl>

Reserved.

</dd> <dt>

TThreadId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Format("x")
</dt> </dl>

The thread identifier of the thread being readied for execution.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**Thread\_V2**](thread-v2.md)
</dt> </dl>

 

 




