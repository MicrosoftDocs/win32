---
description: Registers class providers in WMI.
ms.assetid: 1af7d9ed-c5e4-47e4-839d-53d579ef7cea
ms.tgt_platform: multiple
title: '__ClassProviderRegistration class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __ClassProviderRegistration
- All
- All
- All
- All
- All
- All
- All
- All
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

# \_\_ClassProviderRegistration class

The **\_\_ClassProviderRegistration** system class registers class providers in WMI.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __ClassProviderRegistration : __ObjectProviderRegistration
{
  boolean        SupportsBatching;
  datetime       CacheRefreshInterval;
  sint32         InteractionType = 0;
  __Provider REF provider;
  boolean        PerUserSchema;
  string         QuerySupportLevels[];
  string         ReferencedSetQueries[];
  string         ResultSetQueries[];
  boolean        ReSynchroniseOnNamespaceOpen;
  boolean        SuppportsBatching;
  boolean        SupportsEnumeration = False;
  boolean        SupportsDelete = False;
  boolean        SupportsGet = False;
  boolean        SupportsPut = False;
  boolean        SupportsTransactions;
  string         UnsupportedQueries[];
  uint32         Version;
};
```

## Members

The **\_\_ClassProviderRegistration** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_ClassProviderRegistration** class has these properties.

<dl> <dt>

**CacheRefreshInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> <dt>

**InteractionType**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether or not the class or instance provider supplies data, or relies on WMI and the Common Information Model (CIM) repository. Pull providers support dynamic access to data, and push providers store data in the CIM repository, and rely on WMI to provide access to it. The default value is 0 (zero). This property is inherited from [**\_\_ObjectProviderRegistration**](--objectproviderregistration.md). For more information, see [Determining Push or Pull Status](determining-push-or-pull-status.md).

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

Provider is a push-verify provider. Note that **PushVerify** providers are not supported at this time.

</dd> </dl>

</dd> <dt>

**PerUserSchema**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> <dt>

**provider**
</dt> <dd> <dl> <dt>

Data type: **\_\_Provider**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Object path to a class provider. This property is inherited from [**\_\_ProviderRegistration**](--providerregistration.md).

</dd> <dt>

**QuerySupportLevels**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Array of the types of provider-included support for query processing. This property is inherited from [**\_\_ObjectProviderRegistration**](--objectproviderregistration.md). Class providers are required to support at least one type of query. Instance providers can set **QuerySupportLevels** to **NULL** if they do not support query processing. Providers that support queries implement the [**IWbemServices::ExecQueryAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execqueryasync) method, and set this property to one or more of the following values:

<dt>



 ("WQL:UnarySelect")


</dt> <dd></dd> <dt>



 ("WQL:References")


</dt> <dd></dd> <dt>



 ("WQL:Associators")


</dt> <dd></dd> <dt>



 ("WQL:V1ProviderDefined")


</dt> <dd></dd> </dl>

</dd> <dt>

**ReferencedSetQueries**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

One or more queries that describe the set of referenced classes that a class provider supports. Providers that can supply association classes must include at least one query in this property.

</dd> <dt>

**ResultSetQueries**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

One or more queries that describe the set of all classes that can be supplied by the class provider, or a superset of those classes. This property never specifies a subset of supported classes.

</dd> <dt>

**ReSynchroniseOnNamespaceOpen**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> <dt>

**SupportsBatching**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_ObjectProviderRegistration**](--objectproviderregistration.md).

</dd> <dt>

**SupportsDelete**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, the provider supports data deletion. This property is inherited from [**\_\_ObjectProviderRegistration**](--objectproviderregistration.md).

<dt>



 (True)


</dt> <dd>

The provider supports class or instance deletion by implementing one of either [**IWbemServices::DeleteClassAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteclassasync) (class providers), or [**IWbemServices::DeleteInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteinstanceasync) (instance providers).

</dd> <dt>



 (False)


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

If **TRUE**, the provider supports data enumeration. This property is inherited from [**\_\_ObjectProviderRegistration**](--objectproviderregistration.md).

<dt>



 (True)


</dt> <dd>

The provider supports data enumeration by implementing one of either [**IWbemServices::CreateClassEnumAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createclassenumasync) (class providers), or [**IWbemServices::CreateInstanceEnumAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createinstanceenumasync) (instance providers).

</dd> <dt>



 (False)


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

If **TRUE**, the class or instance provider supports data retrieval. This property is inherited from [**\_\_ObjectProviderRegistration**](--objectproviderregistration.md).

<dt>



 (True)


</dt> <dd>

The provider supports data retrieval by implementing [**IWbemServices::GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync).

</dd> <dt>



 (False)


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

If **TRUE**, the class or instance provider supports data modification. This property is inherited from [**\_\_ObjectProviderRegistration**](--objectproviderregistration.md).

<dt>



 (True)


</dt> <dd>

The provider supports class or instance modification by implementing one of either [**IWbemServices::PutClassAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putclassasync) (class providers), or [**IWbemServices::PutInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync) (class providers).

</dd> <dt>



 (False)


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

</dd> <dt>

**SuppportsBatching**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> <dt>

**UnsupportedQueries**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

One or more queries that describe the set of classes that the class provider does not support. Use this property to subtract from the set of classes implied by **ResultSetQueries**.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Version of this class provider.

</dd> </dl>

## Remarks

The **\_\_ClassProviderRegistration** class is derived from [**\_\_ObjectProviderRegistration**](--objectproviderregistration.md), which is derived from [**\_\_ProviderRegistration**](--providerregistration.md).

The properties inherited from [**\_\_ObjectProviderRegistration**](--objectproviderregistration.md) indicate whether or not the class provider supports data retrieval, modification, deletion, enumeration and query processing. The **InteractionType** property specifies whether or not the class provider is designed as a pull or push provider. For more information, see [Determining Push or Pull Status](determining-push-or-pull-status.md).

The [**\_\_ProviderRegistration**](--providerregistration.md) class defines the [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) property. Only administrators can register a provider by creating an instance of [**\_\_Win32Provider**](--win32provider.md) and **\_\_ClassProviderRegistration**. Only administrators can delete a provider.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_ObjectProviderRegistration**](/windows/desktop/WmiSdk/--objectproviderregistration)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[Registering a Class Provider](registering-a-class-provider.md)
</dt> <dt>

[Registering an Instance Provider](registering-an-instance-provider.md)
</dt> <dt>

[**\_\_Win32Provider**](--win32provider.md)
</dt> </dl>

 

