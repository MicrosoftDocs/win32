---
description: Serves as a parent class for classes that control the generation of events, such as timer events.
ms.assetid: 381b06e7-2857-4932-9f52-f1d62efa8b79
ms.tgt_platform: multiple
title: '__EventGenerator class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __EventGenerator
api_type: 
- Schema
api_location: 
- All
---

# \_\_EventGenerator class

The **\_\_EventGenerator** system class is an abstract base class that serves as a parent class for classes that control the generation of events, such as [timer events](receiving-a-timed-or-repeating-event.md).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract]
class __EventGenerator : __IndicationRelated
{
};
```

## Members

The **\_\_EventGenerator** class does not define any members.

## Remarks

The **\_\_EventGenerator** class is derived from [**\_\_IndicationRelated**](--indicationrelated.md), which has no properties.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_IndicationRelated**](/windows/desktop/WmiSdk/--indicationrelated)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 

