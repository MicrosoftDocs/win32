---
description: Serves as the parent class for registration classes for various types of providers.
ms.assetid: 1e5d95cb-0961-4be8-b80a-37b598c9ccfe
ms.tgt_platform: multiple
title: '__ProviderRegistration class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __ProviderRegistration
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_ProviderRegistration class

The **\_\_ProviderRegistration** abstract system class serves as the parent class for registration classes for various types of providers.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract]
class __ProviderRegistration : __SystemClass
{
  __Provider REF provider;
};
```

## Members

The **\_\_ProviderRegistration** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_ProviderRegistration** class has these properties.

<dl> <dt>

**provider**
</dt> <dd> <dl> <dt>

Data type: **\_\_Provider**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to an instance of [**\_\_Provider**](--provider.md) representing the object path to the provider.

</dd> </dl>

## Remarks

The **\_\_ProviderRegistration** class is derived from [**\_\_SystemClass**](--systemclass.md), which has no properties.

Instances of the **\_\_ProviderRegistration** system class are never created. The classes that providers use to create instances for registration derive either directly or indirectly from this class. These classes are:

[**\_\_ClassProviderRegistration**](--classproviderregistration.md)

[**\_\_EventConsumerProviderRegistration**](--eventconsumerproviderregistration.md)

[**\_\_EventProviderRegistration**](--eventproviderregistration.md)

[**\_\_InstanceProviderRegistration**](--instanceproviderregistration.md)

[**\_\_MethodProviderRegistration**](--methodproviderregistration.md)

[**\_\_ObjectProviderRegistration**](--objectproviderregistration.md)

[**\_\_PropertyProviderRegistration**](--propertyproviderregistration.md)

Only administrators can register or delete a provider by creating an instance of [**\_\_Win32Provider**](--win32provider.md) and registering it.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_SystemClass**](/windows/desktop/WmiSdk/--systemclass)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[Registering a Provider](registering-a-provider.md)
</dt> </dl>

 

