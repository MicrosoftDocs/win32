---
description: Registers event consumer providers with WMI.
ms.assetid: 31ff43dc-dc70-4ba0-866f-37445912f837
ms.tgt_platform: multiple
title: '__EventConsumerProviderRegistration class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __EventConsumerProviderRegistration
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_EventConsumerProviderRegistration class

The **\_\_EventConsumerProviderRegistration** system class registers event consumer providers with WMI.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __EventConsumerProviderRegistration : __ProviderRegistration
{
  string         ConsumerClassNames[];
  __Provider REF provider;
};
```

## Members

The **\_\_EventConsumerProviderRegistration** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_EventConsumerProviderRegistration** class has these properties.

<dl> <dt>

**ConsumerClassNames**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Array of names of the logical consumer classes that the event consumer provider supports.

</dd> <dt>

**provider**
</dt> <dd> <dl> <dt>

Data type: **\_\_Provider**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Object path to the provider. This property is inherited from [**\_\_ProviderRegistration**](--providerregistration.md).

</dd> </dl>

## Remarks

The **\_\_EventConsumerProviderRegistration** class is derived from [**\_\_ProviderRegistration**](--providerregistration.md).

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

[Registering an Event Consumer Provider](registering-an-event-consumer-provider.md)
</dt> <dt>

[Writing an Event Consumer Provider](writing-an-event-consumer-provider.md)
</dt> </dl>

 

