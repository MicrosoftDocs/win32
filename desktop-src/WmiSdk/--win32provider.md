---
description: Registers information about the physical implementation of a provider in WMI. Providers that do not set the HostingModel property are loaded, by default, to run in a Wmiprvse.exe process as NetworkServiceHostOrSelfHost.
ms.assetid: 41e0d938-00c6-4f4c-8027-8b8512398dee
ms.tgt_platform: multiple
title: '__Win32Provider class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# \_\_Win32Provider class

The **\_\_Win32Provider** system class registers information about the physical implementation of a provider in WMI. Providers that do not set the **HostingModel** property are loaded, by default, to run in a Wmiprvse.exe process as **NetworkServiceHostOrSelfHost**.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __Win32Provider : __Provider
{
  string   ClientLoadableCLSID;
  string   CLSID;
  sint32   Concurrency;
  string   DefaultMachineName;
  boolean  Enabled;
  string   HostingModel;
  sint32   ImpersonationLevel = 0;
  sint32   InitializationReentrancy;
  datetime InitializationTimeoutInterval;
  boolean  InitializeAsAdminFirst;
  string   Name;
  datetime OperationTimeoutInterval;
  boolean  PerLocaleInitialization = FALSE;
  boolean  PerUserInitialization = FALSE;
  boolean  Pure = TRUE;
  string   SecurityDescriptor;
  boolean  SupportsExplicitShutdown;
  boolean  SupportsExtendedStatus;
  boolean  SupportsQuotas;
  boolean  SupportsSendStatus;
  boolean  SupportsShutdown;
  boolean  SupportsThrottling;
  datetime UnloadTimeout;
  uint32   Version;
};
```

## Members

The **\_\_Win32Provider** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_Win32Provider** class has these properties.

<dl> <dt>

**ClientLoadableCLSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Class identifier that WMI uses to determine whether or not to load a high performance provider into the client process or the WMI process. If both the provider and client are located on the same computer, WMI loads the provider in-process to the client by using **ClientLoadableCLSID** as the class identifier. When the provider and client are located on different computers, WMI loads the provider in-process to WMI. WMI also uses **ClientLoadableCLSID** to support refresh operations.

For more information, see [Registering a High-Performance Provider.](registering-a-high-performance-provider.md)

</dd> <dt>

**CLSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**GUID** that represents the class identifier (**CLSID**) of the provider COM object. This COM object must contain an implementation of the [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) interface.

</dd> <dt>

**Concurrency**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> <dt>

**DefaultMachineName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Identifies the computer on which to start the provider. If the provider runs on the local computer it is **NULL**.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, this instance is enabled and can be used to complete client requests.

</dd> <dt>

**HostingModel**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is composed of values from the [**MSFT\_Providers**](/previous-versions/windows/desktop/wmisystemprov/msft-providers) **HostingGroup** and **HostingSpecification** properties. The value of this property specifies how WMI loads the provider and the security account it runs under. For more information about setting the **HostingModel** property, see [Provider Hosting and Security](provider-hosting-and-security.md) and [Registering a Provider](registering-a-provider.md).

</dd> <dt>

**ImpersonationLevel**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Reserved. The default value is zero (0).

</dd> <dt>

**InitializationReentrancy**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Set of flags that provide information about serialization. The default value is zero (0).

<dt>

0
</dt> <dd>

All initialization of this provider must be serialized.

</dd> <dt>

1
</dt> <dd>

All initializations of this provider in the same namespace must be serialized.

</dd> <dt>

2
</dt> <dd>

No initialization serialization is necessary.

</dd> </dl>

</dd> <dt>

**InitializationTimeoutInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> <dt>

**InitializeAsAdminFirst**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

TBD

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Key**](standard-qualifiers.md)
</dt> </dl>

The provider name.

</dd> <dt>

**OperationTimeoutInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> <dt>

**PerLocaleInitialization**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, the provider is initialized for each locale when a user connects to the same namespace more than one time using different locales. The default value is **FALSE**.

</dd> <dt>

**PerUserInitialization**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, the provider is initialized one time for each NT LAN Manager (NTLM) user that makes requests to the provider. If **FALSE** (default), the provider is initialized one time for all users.

</dd> <dt>

**Pure**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, the provider agrees to prepare to unload by calling [**IUnknown::Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) on all outstanding interface points when WMI calls the **Release** method of its primary interface. Providers that must remain clients of WMI after they do not function as providers should set **Pure** to **FALSE**. The default setting is **TRUE**. For more information, see the Remarks section of this topic.

</dd> <dt>

**SecurityDescriptor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Security descriptor (SD) in the Security Descriptor Definition Language (SDDL) that determines the set of users that can successfully call [**IWbemDecoupledRegistrar:Register**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemdecoupledregistrar-register) for the decoupled provider. For more information, see the [Security Descriptor Definition Language](/windows/desktop/SecAuthZ/security-descriptor-definition-language) topic in the Security section of the Windows SDK. This security descriptor is used only for decoupled providers, and does not affect other providers. For more information, see [Incorporating a Provider in an Application](incorporating-a-provider-in-an-application.md).

WMI performs access checks for decoupled providers that use the [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) and [**IWbemObjectSink**](iwbemobjectsink.md) interfaces. If the security descriptor is **NULL**, then only applications or services that run under the LocalSystem, NetworkService, LocalService accounts can run a decoupled provider.

The following string shows a decoupled provider to be run only by built-in Administrators."O:BAG:BAD:(A;;0x1;;;BA)"

For more information about setting the **SecurityDescriptor** property, see [Maintaining WMI Security](maintaining-wmi-security.md).

</dd> <dt>

**SupportsExplicitShutdown**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> <dt>

**SupportsExtendedStatus**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> <dt>

**SupportsQuotas**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> <dt>

**SupportsSendStatus**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> <dt>

**SupportsShutdown**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> <dt>

**SupportsThrottling**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

</dd> <dt>

**UnloadTimeout**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

[Date and Time Format](date-and-time-format.md) that specifies how long WMI allows the provider to remain idle before it is unloaded. Typically, providers request that WMI wait no longer than five minutes.

For the current version of WMI, the value of this property is ignored. WMI unloads the provider based on the time-out value in an internal class in the \\root namespace. It is recommended that providers set **UnloadTimeout**. For more information, see [Unloading a Provider](unloading-a-provider.md).

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Version of the provider. The supported versions are 1 and 2. Version 2 strengthens validity checks for all associated property registrations, specifically the [**ImpersonationLevel**](swbemsecurity-impersonationlevel.md) property.

</dd> </dl>

## Remarks

The **\_\_Win32Provider** class is derived from [**\_\_Provider**](--provider.md).

Most providers can accept the default values for the **InitializationReentrancy** property. However, if a provider can support simultaneous initialization for separate users, this property can be set to 1 (one). If serialized initialization is necessary, **InitializationReentrancy** remains 0 (zero). In both instances, **PerUserInitialization** is set to **TRUE**.

A pure provider or a provider that sets the **Pure** property to **TRUE**, exists only to service requests from applications and WMI. Most providers are pure providers. A nonpure provider is the exception. Nonpure providers transition to the role of client after they complete servicing requests.

An example of a nonpure provider is a push provider that starts to issue queries, and makes requests of WMI after it completes initialization. A push provider does not have responsibilities except to update the CIM repository with data at initialization time. After updating the repository, a push provider can wait to be unloaded, or transition to the role of client. The push provider that waits to be unloaded is a pure provider. The push provider that participates in client activities is nonpure.

WMI must be able to distinguish pure providers from non-pure providers so that it can determine when it is safe to shut down. WMI must wait for all operations that involve non-pure providers to complete before it can shut down safely.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_Provider**](/windows/desktop/WmiSdk/--provider)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[Registering a Provider](registering-a-provider.md)
</dt> </dl>

 

