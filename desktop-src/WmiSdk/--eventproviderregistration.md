---
description: Used to register event providers with Windows Management Instrumentation (WMI).
ms.assetid: d87f61a8-5549-4f33-ba67-31b5d72b5282
ms.tgt_platform: multiple
title: '__EventProviderRegistration class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __EventProviderRegistration
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_EventProviderRegistration class

The **\_\_EventProviderRegistration** system class is used to register event providers with Windows Management Instrumentation (WMI).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __EventProviderRegistration : __ProviderRegistration
{
  string         EventQueryList[];
  __Provider REF provider;
};
```

## Members

The **\_\_EventProviderRegistration** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_EventProviderRegistration** class has these properties.

<dl> <dt>

**EventQueryList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

One or more Windows Management Instrumentation Query Language (WQL) queries that describe the events that the event provider supports.

</dd> <dt>

**provider**
</dt> <dd> <dl> <dt>

Data type: **\_\_Provider**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Object path to the event provider. This property is inherited from [**\_\_ProviderRegistration**](--providerregistration.md).

</dd> </dl>

## Remarks

Only administrators can register or delete an event provider by creating an instance of [**\_\_Win32Provider**](--win32provider.md) and [**\_\_EventProviderRegistration**](--eventconsumerproviderregistration.md). The **\_\_EventProviderRegistration** class is derived from [**\_\_ProviderRegistration**](--providerregistration.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_ProviderRegistration**](/windows/desktop/WmiSdk/--providerregistration)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[Registering an Event Provider](registering-an-event-provider.md)
</dt> <dt>

[Writing an Event Provider](writing-an-event-provider.md)
</dt> </dl>

 

