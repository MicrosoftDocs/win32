---
description: Represents the event type class for handle creation or closure events.
ms.assetid: 39d27cdf-fa51-4fb1-8998-7150ca627eff
title: ObHandleEvent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ObHandleEvent
- ObHandleEvent.Handle
- ObHandleEvent.Object
- ObHandleEvent.ObjectName
- ObHandleEvent.ObjectType
api_type: 
- NA
api_location: 
---

# ObHandleEvent class

Represents the event type class for handle creation or closure events.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, EventType{32,33}, EventTypeName{CreateHandle,CloseHandle}]
class ObHandleEvent : ObTrace
{
  uint32 Handle;
  uint32 Object;
  string ObjectName;
  uint16 ObjectType;
};
```

## Members

The **ObHandleEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **ObHandleEvent** class has these properties.

<dl> <dt>

**Handle**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Format**](event-tracing-mof-qualifiers.md) ("x"), [**WmiDataId**](event-tracing-mof-qualifiers.md) (2)
</dt> </dl>

The object handle.

</dd> <dt>

**Object**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Format**](event-tracing-mof-qualifiers.md) ("x"), [**Pointer**](event-tracing-mof-qualifiers.md), [**WmiDataId**](event-tracing-mof-qualifiers.md) (1)
</dt> </dl>

The object.

</dd> <dt>

**ObjectName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Format**](event-tracing-mof-qualifiers.md) ("w"), [**StringTermination**](event-tracing-mof-qualifiers.md) ("NullTerminated"), [**WmiDataId**](event-tracing-mof-qualifiers.md) (4)
</dt> </dl>

The object name.

</dd> <dt>

**ObjectType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](event-tracing-mof-qualifiers.md) (3)
</dt> </dl>

The object type.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                   |
| MOF<br/>                      | <dl> <dt>Wmicore.mof</dt> </dl> |



 

 




