---
Description: You may use the MOF\_FIELD structures to append event data to the EVENT\_TRACE\_HEADER or EVENT\_INSTANCE\_HEADER structures.
ms.assetid: 64ff1191-2177-4d51-afcd-b58d510e9ae8
title: MOF_FIELD structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MOF_FIELD
api_type: 
- HeaderDef
api_location: 
- Evntrace.h
---

# MOF\_FIELD structure

You may use the **MOF\_FIELD** structures to append event data to the [**EVENT\_TRACE\_HEADER**](event-trace-header.md) or [**EVENT\_INSTANCE\_HEADER**](event-instance-header.md) structures.

## Syntax


```C++
typedef struct _MOF_FIELD {
  ULONG64 DataPtr;
  ULONG   Length;
  ULONG   DataType;
} MOF_FIELD, *PMOF_FIELD;
```



## Members

<dl> <dt>

**DataPtr**
</dt> <dd>

Pointer to a event data item.

</dd> <dt>

**Length**
</dt> <dd>

Length of the item pointed to by **DataPtr**, in bytes.

</dd> <dt>

**DataType**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

Be sure to initialize the memory for this structure to zero before setting any members.

If you use **MOF\_FIELD** structures, you must set the **WNODE\_FLAG\_USE\_MOF\_PTR** flag in the **Flags** member of the [**EVENT\_TRACE\_HEADER**](event-trace-header.md) or [**EVENT\_INSTANCE\_HEADER**](event-instance-header.md) structure.

The event tracing session automatically dereferences **MOF\_FIELD** data pointers before passing the data to event trace consumers using [**EVENT\_TRACE**](event-trace.md) structures.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**EVENT\_INSTANCE\_HEADER**](event-instance-header.md)
</dt> <dt>

[**EVENT\_TRACE**](event-trace.md)
</dt> <dt>

[**EVENT\_TRACE\_HEADER**](event-trace-header.md)
</dt> </dl>

 

 




