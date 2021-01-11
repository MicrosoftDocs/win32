---
description: This class is the event type class for thread end events. The following syntax is simplified from MOF code.
ms.assetid: c495bf22-04ce-4285-8e7e-152e4ab65823
title: Thread_V1_TypeGroup2 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Thread_V1_TypeGroup2
- Thread_V1_TypeGroup2.ProcessId
- Thread_V1_TypeGroup2.TThreadId
api_type: 
- NA
api_location: 
---

# Thread\_V1\_TypeGroup2 class

This class is the event type class for thread end events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{2, 4}, EventTypeName{"End", "DCEnd"}]
class Thread_V1_TypeGroup2 : Thread_V1
{
  uint32 ProcessId;
  uint32 TThreadId;
};
```

## Members

The **Thread\_V1\_TypeGroup2** class has these types of members:

-   [Properties](#properties)

### Properties

The **Thread\_V1\_TypeGroup2** class has these properties.

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

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Thread\_V1**](thread-v1.md)
</dt> </dl>

 

 




