---
description: Registers property providers in WMI.
ms.assetid: 24792884-3fb9-4974-83d5-1c5fc1fa72a1
ms.tgt_platform: multiple
title: '__PropertyProviderRegistration class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __PropertyProviderRegistration
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_PropertyProviderRegistration class

The **\_\_PropertyProviderRegistration** system class registers property providers in WMI.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __PropertyProviderRegistration : __ProviderRegistration
{
  __Provider REF provider;
  boolean        SupportsPut = False;
  boolean        SupportsGet = False;
};
```

## Members

The **\_\_PropertyProviderRegistration** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_PropertyProviderRegistration** class has these properties.

<dl> <dt>

**provider**
</dt> <dd> <dl> <dt>

Data type: **\_\_Provider**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to an instance of [**\_\_Provider**](--provider.md) that represents the object path of the property provider. This property is inherited from [**\_\_ProviderRegistration**](--providerregistration.md).

</dd> <dt>

**SupportsGet**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Describes whether the class or instance provider supports data retrieval.

<dt>

True
</dt> <dd>

The provider supports data retrieval by implementing [**IWbemServices::GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync).

</dd> <dt>

False
</dt> <dd>

The provider does not support data retrieval, and returns **WBEM\_E\_PROVIDER\_NOT\_CAPABLE** from [**GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync).

</dd> </dl>

</dd> <dt>

**SupportsPut**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Describes whether the class or instance provider supports data modification.

<dt>

True
</dt> <dd>

The provider supports class or instance modification by implementing one of the following methods:

-   [**IWbemServices::PutClassAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putclassasync) (class providers)
-   [**IWbemServices::PutInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync) (class providers)

</dd> <dt>

False
</dt> <dd>

The provider does not support data modification and returns **WBEM\_E\_PROVIDER\_NOT\_CAPABLE** from [**PutClassAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putclassasync) or [**PutInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync).

</dd> </dl>

</dd> </dl>

## Remarks

The **\_\_PropertyProviderRegistration** class is derived from [**\_\_ProviderRegistration**](--providerregistration.md). Only administrators can register a property provider by creating an instance of [**\_\_Win32Provider**](--win32provider.md) and **\_\_PropertyProviderRegistration**. Only administrators can delete a property provider.

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

[Registering a Property Provider](registering-a-property-provider.md)
</dt> </dl>

 

