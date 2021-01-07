---
description: Serves as the parent class for classes that are used to register class and instance providers in WMI.
ms.assetid: f7c569be-8927-42a4-b96a-abe4b7e3e23c
ms.tgt_platform: multiple
title: '__ObjectProviderRegistration class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __ObjectProviderRegistration
- All
- All
- All
- All
- All
- All
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_ObjectProviderRegistration class

The **\_\_ObjectProviderRegistration** abstract system class serves as the parent class for classes that are used to register class and instance providers in WMI.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract]
class __ObjectProviderRegistration : __ProviderRegistration
{
  sint32         InteractionType = 0;
  __Provider REF provider;
  string         QuerySupportLevels[];
  boolean        SupportsBatching;
  boolean        SupportsDelete = False;
  boolean        SupportsEnumeration = False;
  boolean        SupportsGet = False;
  boolean        SupportsPut = False;
  boolean        SupportsTransactions;
};
```

## Members

The **\_\_ObjectProviderRegistration** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_ObjectProviderRegistration** class has these properties.

<dl> <dt>

**InteractionType**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether or not the class or instance provider supplies its own data, or relies on WMI and the Common Information Model (CIM) repository. Pull providers support dynamic access to their data, and push providers store their data in the CIM repository, and rely on WMI to provide access to it. For more information, see [Determining Push or Pull Status](determining-push-or-pull-status.md). The default value is 0 (zero).

<dt>

<span id="Pull"></span><span id="pull"></span><span id="PULL"></span>

<span id="Pull"></span><span id="pull"></span><span id="PULL"></span>**Pull** (0)


</dt> <dd>

Provider is a pull provider.

</dd> <dt>

<span id="Push"></span><span id="push"></span><span id="PUSH"></span>

<span id="Push"></span><span id="push"></span><span id="PUSH"></span>**Push** (1)


</dt> <dd>

Provider is a push provider.

</dd> <dt>

<span id="PushVerify"></span><span id="pushverify"></span><span id="PUSHVERIFY"></span>

<span id="PushVerify"></span><span id="pushverify"></span><span id="PUSHVERIFY"></span>**PushVerify** (2)


</dt> <dd>

Provider is a push-verify provider. Note that push-verify is not supported at this time.

</dd> </dl>

</dd> <dt>

**provider**
</dt> <dd> <dl> <dt>

Data type: **\_\_Provider**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to an instance of [**\_\_Provider**](--provider.md) that represents an object path to the object provider. This property is inherited from [**\_\_ProviderRegistration**](--providerregistration.md).

</dd> <dt>

**QuerySupportLevels**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Array of the types of provider-included support for query processing. Class providers do not support any type of queries. Instance providers can set **QuerySupportLevels** to **NULL** if they do not support query processing. Providers that support queries implement the [**IWbemServices::ExecQueryAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execqueryasync) method, and set this property to one or more of the following values (the property type is an array).

"WQL:UnarySelect"

"WQL:References"

"WQL:Associators"

"WQL:V1ProviderDefined"

</dd> <dt>

**SupportsBatching**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> <dt>

**SupportsDelete**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, the provider supports data deletion.

<dt>

True
</dt> <dd>

The provider supports class or instance deletion by implementing one of either [**IWbemServices::DeleteClassAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteclassasync) (class providers), or [**IWbemServices::DeleteInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteinstanceasync) (instance providers).

</dd> <dt>

False
</dt> <dd>

The provider does not support data deletion, and returns **WBEM\_E\_PROVIDER\_NOT\_CAPABLE** from [**DeleteClassAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteclassasync) or [**DeleteInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteinstanceasync).

</dd> </dl>

</dd> <dt>

**SupportsEnumeration**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, the provider supports data enumeration.

<dt>

True
</dt> <dd>

The provider supports data enumeration by implementing one of either [**IWbemServices::CreateClassEnumAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createclassenumasync) (class providers), or [**IWbemServices::CreateInstanceEnumAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createinstanceenumasync) (instance providers).

</dd> <dt>

False
</dt> <dd>

The provider does not support data enumeration, and returns **WBEM\_E\_PROVIDER\_NOT\_CAPABLE** from [**CreateClassEnumAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createclassenumasync) or [**CreateInstanceEnumAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createinstanceenumasync).

</dd> </dl>

</dd> <dt>

**SupportsGet**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, the class or instance provider supports data retrieval.

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

If **True**, the class or instance provider supports data modification.

<dt>

True
</dt> <dd>

The provider supports class or instance modification by implementing one of either [**IWbemServices::PutClassAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putclassasync) (class providers), or [**IWbemServices::PutInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync) (class providers).

</dd> <dt>

False
</dt> <dd>

The provider does not support data modification and returns **WBEM\_E\_PROVIDER\_NOT\_CAPABLE** from [**PutClassAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putclassasync) or [**PutInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync).

</dd> </dl>

</dd> <dt>

**SupportsTransactions**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> </dl>

## Remarks

The **\_\_ObjectProviderRegistration** class is derived from [**\_\_ProviderRegistration**](--providerregistration.md).

Class providers must set the **SupportsEnumeration** property to **True** because the providers must be able to supply WMI with a list of their classes. If a class provider attempts to set this property to **False**, WMI flags the registration as illegal. Instance providers are not required to support enumeration, and can choose to set **SupportsEnumeration** to either **True** or **False**.

A provider that sets **QuerySupportLevels** to "WQL:UnarySelect" can accept a query that consists of the basic SELECT statement as supported in WMI version 1.0. Both class and instance providers are expected to be able to handle the **\_\_CLASS** system property. Class providers are also expected to process the **\_\_SUPERCLASS** system property and the ISA operator. The ISA operator is used to expand a result set to derived classes. If a provider is given a query that it cannot interpret, it requests that WMI handle it by returning the **WBEM\_E\_TOO\_COMPLEX** error value. For a description of valid WQL syntax, see [Querying with WQL](querying-with-wql.md).

A provider that sets **QuerySupportLevels** to **WQL:V1ProviderDefined** can try to support a larger set of the SQL syntax at its own risk, such as the `ORDER BY` clause. WMI does not interpret the additional clauses, or attempt to ensure that the result set is correct.

Only administrators can register or delete a provider by creating an instance of [**\_\_Win32Provider**](--win32provider.md) and registering it.

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

[Registering a Provider](registering-a-provider.md)
</dt> </dl>

 

