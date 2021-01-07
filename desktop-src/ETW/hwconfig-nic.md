---
description: The HWConfig\_NIC class is the event type class for network interface card configuration events. The following syntax is simplified from MOF code.
ms.assetid: e544a27b-17f8-402c-9c92-578cf2a38ca8
title: HWConfig_NIC class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- HWConfig_NIC
- HWConfig_NIC.NICName
api_type: 
- NA
api_location: 
---

# HWConfig\_NIC class

The **HWConfig\_NIC** class is the event type class for network interface card configuration events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(13), EventTypeName("NIC")]
class HWConfig_NIC : HWConfig
{
  string NICName;
};
```

## Members

The **HWConfig\_NIC** class has these types of members:

-   [Properties](#properties)

### Properties

The **HWConfig\_NIC** class has these properties.

<dl> <dt>

NICName
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

Name of the network interface card.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                   |



## See also

<dl> <dt>

[**HWConfig**](hwconfig.md)
</dt> </dl>

 

 




