---
description: Registry_TypeGroup1 class - This class is the event type class for registry events. The following syntax is simplified from MOF code.
ms.assetid: 8d0e9d97-3837-46da-a217-13e943580352
title: Registry_TypeGroup1 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Registry_TypeGroup1
- Registry_TypeGroup1.InitialTime
- Registry_TypeGroup1.Status
- Registry_TypeGroup1.Index
- Registry_TypeGroup1.KeyHandle
- Registry_TypeGroup1.KeyName
api_type: 
- NA
api_location: 
---

# Registry\_TypeGroup1 class

This class is the event type class for registry events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}, EventTypeName{"Create", "Open", "Delete", "Query", "SetValue", "DeleteValue", "QueryValue", "EnumerateKey", "EnumerateValueKey", "QueryMultipleValue", "SetInformation", "Flush", "KCBCreate", "KCBDelete", "KCBRundownBegin", "KCBRundownEnd", "Virtualize", "Close"}]
class Registry_TypeGroup1 : Registry
{
  sint64 InitialTime;
  uint32 Status;
  uint32 Index;
  uint32 KeyHandle;
  string KeyName;
};
```

## Members

The **Registry\_TypeGroup1** class has these types of members:

-   [Properties](#properties)

### Properties

The **Registry\_TypeGroup1** class has these properties.

<dl> <dt>

Index
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

The subkey index for the registry operation (such as EnumerateKey).

</dd> <dt>

InitialTime
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1)
</dt> </dl>

Initial time of the registry operation.

</dd> <dt>

KeyHandle
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4), Pointer
</dt> </dl>

Handle to the registry key.

</dd> <dt>

KeyName
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

Name of the registry key.

</dd> <dt>

Status
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Pointer
</dt> </dl>

NTSTATUS value of the registry operation.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Registry**](registry.md)
</dt> </dl>

 

 




