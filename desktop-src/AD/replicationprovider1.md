---
title: ReplicationProvider1 class
description: The base class for the provider instance.
ms.assetid: c3c6efda-faa7-42af-a635-060967fdcc35
ms.tgt_platform: multiple
keywords:
- ReplicationProvider1 class Active Directory
- ReplicationProvider1 class Active Directory , described
topic_type:
- apiref
api_name:
- ReplicationProvider1
- ReplicationProvider1.ClientLoadableCLSID
- ReplicationProvider1.CLSID
- ReplicationProvider1.Concurrency
- ReplicationProvider1.DefaultMachineName
- ReplicationProvider1.Enabled
- ReplicationProvider1.ImpersonationLevel
- ReplicationProvider1.InitializationReentrancy
- ReplicationProvider1.InitializationTimeoutInterval
- ReplicationProvider1.InitializeAsAdminFirst
- ReplicationProvider1.Name
- ReplicationProvider1.OperationTimeoutInterval
- ReplicationProvider1.PerLocaleInitialization
- ReplicationProvider1.PerUserInitialization
- ReplicationProvider1.Pure
- ReplicationProvider1.SecurityDescriptor
- ReplicationProvider1.SupportsExplicitShutdown
- ReplicationProvider1.SupportsExtendedStatus
- ReplicationProvider1.SupportsQuotas
- ReplicationProvider1.SupportsSendStatus
- ReplicationProvider1.SupportsShutdown
- ReplicationProvider1.SupportsThrottling
- ReplicationProvider1.UnloadTimeout
- ReplicationProvider1.Version
- ReplicationProvider1.HostingModel
api_location:
- replprov.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# ReplicationProvider1 class

The base class for the provider instance.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class ReplicationProvider1 : __Win32Provider
{
  string   ClientLoadableCLSID;
  string   CLSID;
  sint32   Concurrency;
  string   DefaultMachineName;
  boolean  Enabled;
  sint32   ImpersonationLevel = 0;
  sint32   InitializationReentrancy = 0;
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
  string   HostingModel;
};
```

## Members

The **ReplicationProvider1** class has these types of members:

-   [Properties](#properties)

### Properties

The **ReplicationProvider1** class has these properties.

<dl> <dt>

**ClientLoadableCLSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Class identifier that WMI uses to determine whether or not to load a high performance provider into the client process or the WMI process. If both the provider and client are located on the same computer, WMI loads the provider in-process to the client by using **ClientLoadableCLSID** as the class identifier. When the provider and client are located on different computers, WMI loads the provider in-process to WMI. WMI also uses **ClientLoadableCLSID** to support refresh operations.

For more information, see [Registering a High-Performance Provider.](/windows/desktop/WmiSdk/registering-a-high-performance-provider)

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**CLSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**GUID** that represents the class identifier (**CLSID**) of the provider COM object. This COM object must contain an implementation of the [**IWbemProviderInit**](/windows/desktop/api/wbemprov/nn-wbemprov-iwbemproviderinit) interface.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**Concurrency**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**DefaultMachineName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Identifies the computer on which to start the provider. If the provider runs on the local computer it is **NULL**.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, this instance is enabled and can be used to complete client requests.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**HostingModel**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**override**](/windows/desktop/WmiSdk/standard-qualifiers) ("HostingModel")
</dt> </dl>

Contains the hosting model of the provider.

</dd> <dt>

**ImpersonationLevel**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Reserved. The default value is zero (0).

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**InitializationReentrancy**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Set of flags that provide information about serialization. The default value is zero (0).

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

All initialization of this provider must be serialized.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

All initializations of this provider in the same namespace must be serialized.

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


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

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**InitializeAsAdminFirst**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**Windows Server 2003:** This property is disabled.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

The provider name.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**OperationTimeoutInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**PerLocaleInitialization**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, the provider is initialized for each locale when a user connects to the same namespace more than one time using different locales. The default value is **FALSE**.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**PerUserInitialization**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, the provider is initialized one time for each NT LAN Manager (NTLM) user that makes requests to the provider. If **FALSE** (default), the provider is initialized one time for all users.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**Pure**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, the provider agrees to prepare to unload by calling [**IUnknown::Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) on all outstanding interface points when WMI calls the **Release** method of its primary interface. Providers that must remain clients of WMI after they do not function as providers should set **Pure** to **FALSE**. The default setting is **TRUE**. For more information, see the Remarks section of this topic.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**SecurityDescriptor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Security descriptor (SD) in the Security Descriptor Definition Language (SDDL) that determines the set of users that can successfully call [**IWbemDecoupledRegistrar:Register**](/windows/desktop/api/wbemprov/nf-wbemprov-iwbemdecoupledregistrar-register) for the decoupled provider. For more information, see the [Security Descriptor Definition Language](/windows/desktop/SecAuthZ/security-descriptor-definition-language) topic in the Security section of the Windows SDK. This security descriptor is used only for decoupled providers, and does not affect other providers. For more information, see [Incorporating a Provider in an Application](/windows/desktop/WmiSdk/incorporating-a-provider-in-an-application).

WMI performs access checks for decoupled providers that use the [**IWbemProviderInit**](/windows/desktop/api/wbemprov/nn-wbemprov-iwbemproviderinit) and [**IWbemObjectSink**](/windows/desktop/WmiSdk/iwbemobjectsink) interfaces. If the security descriptor is **NULL**, then only applications or services that run under the LocalSystem, NetworkService, LocalService accounts can run a decoupled provider.

The following string shows a decoupled provider to be run only by built-in Administrators."O:BAG:BAD:(A;;0x1;;;BA)"

For more information about setting the **SecurityDescriptor** property, see [Maintaining WMI Security](/windows/desktop/WmiSdk/maintaining-wmi-security).

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**SupportsExplicitShutdown**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**SupportsExtendedStatus**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**SupportsQuotas**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**SupportsSendStatus**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**SupportsShutdown**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**SupportsThrottling**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**UnloadTimeout**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

[Date and Time Format](/windows/desktop/WmiSdk/date-and-time-format) that specifies how long WMI allows the provider to remain idle before it is unloaded. Typically, providers request that WMI wait no longer than five minutes.

For the current version of WMI, the value of this property is ignored. WMI unloads the provider based on the time-out value in an internal class in the \\root namespace. It is recommended that providers set **UnloadTimeout**. For more information, see [Unloading a Provider](/windows/desktop/WmiSdk/unloading-a-provider).

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Version of the provider. The supported versions are 1 and 2. Version 2 strengthens validity checks for all associated property registrations, specifically the [**ImpersonationLevel**](/windows/desktop/WmiSdk/swbemsecurity-impersonationlevel) property.

This property is inherited from [**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider).

</dd> </dl>

## Remarks

An instance of this class represents the WMI provider for Active Directory Domain services. The defaults are as follows:

-   Name = "ReplProv1"
-   ClsID = "{29288F43-39B1-40db-B41F-CE899450E911}"
-   HostingModel = "NetworkServiceHost"

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftActiveDirectory<br/>                                               |
| MOF<br/>                      | <dl> <dt>Replprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Replprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**\_\_Win32Provider**](/windows/desktop/WmiSdk/--win32provider)
</dt> </dl>

 

