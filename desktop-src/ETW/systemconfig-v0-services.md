---
description: SystemConfig_V0_Services class - This class is the event type class for service configuration events.
ms.assetid: 1e6c2061-f1a2-4253-a0c4-4b45b2feceda
title: SystemConfig_V0_Services class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SystemConfig_V0_Services
- SystemConfig_V0_Services.ServiceName
- SystemConfig_V0_Services.DisplayName
- SystemConfig_V0_Services.ProcessName
- SystemConfig_V0_Services.ProcessId
api_type: 
- NA
api_location: 
---

# SystemConfig\_V0\_Services class

This class is the event type class for service configuration events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(15), EventTypeName("Services")]
class SystemConfig_V0_Services : SystemConfig_V0
{
  char16 ServiceName[];
  char16 DisplayName[];
  char16 ProcessName[];
  uint32 ProcessId;
};
```

## Members

The **SystemConfig\_V0\_Services** class has these types of members:

-   [Properties](#properties)

### Properties

The **SystemConfig\_V0\_Services** class has these properties.

<dl> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **char16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (2), **Max** (256)
</dt> </dl>

Display name of the service. The name is case-preserved in the Service Control Manager. However, display name comparisons are always case-insensitive.

</dd> <dt>

**ProcessId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4)
</dt> </dl>

Identifier of the process in which the service runs.

</dd> <dt>

**ProcessName**
</dt> <dd> <dl> <dt>

Data type: **char16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (3), **Max** (34)
</dt> </dl>

Name of the process in which the service runs.

</dd> <dt>

**ServiceName**
</dt> <dd> <dl> <dt>

Data type: **char16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (1), **Max** (34)
</dt> </dl>

Unique identifier of the service. The identifier provides an indication of the functionality the service provides.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SystemConfig\_V0**](systemconfig-v0.md)
</dt> </dl>

 

 




