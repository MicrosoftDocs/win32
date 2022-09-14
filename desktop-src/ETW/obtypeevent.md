---
description: Represents the event type class for object type events related to the beginning and end of data collection.
ms.assetid: 16b21f61-e734-4f51-9b11-e507b5957107
title: ObTypeEvent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ObTypeEvent
- ObTypeEvent.ObjectType
- ObTypeEvent.Reserved
- ObTypeEvent.TypeName
api_type: 
- NA
api_location: 
---

# ObTypeEvent class

Represents the event type class for object type events related to the beginning and end of data collection. This event involves the mapping of the type index values to the type names.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, EventType{36,37}, EventTypeName{TypeDCStart,TypeDCEnd}]
class ObTypeEvent : ObTrace
{
  uint16 ObjectType;
  uint16 Reserved;
  string TypeName;
};
```

## Members

The **ObTypeEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **ObTypeEvent** class has these properties.

<dl> <dt>

**ObjectType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](event-tracing-mof-qualifiers.md) (1)
</dt> </dl>

The object type.

</dd> <dt>

**Reserved**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](event-tracing-mof-qualifiers.md) (2)
</dt> </dl>

Reserved.

</dd> <dt>

**TypeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Format**](event-tracing-mof-qualifiers.md) ("w"), [**StringTermination**](event-tracing-mof-qualifiers.md) ("NullTerminated"), [**WmiDataId**](event-tracing-mof-qualifiers.md) (3)
</dt> </dl>

The type name.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                   |
| MOF<br/>                      | <dl> <dt>Wmicore.mof</dt> </dl> |



 

 




