---
title: Win32\_ProviderEx class
description: Represents the provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bf8a0c6c-5632-4416-8268-17f5fd350e0b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_ProviderEx class
- Win32_ProviderEx class, described
topic_type:
- apiref
api_name:
- Win32_ProviderEx
- Win32_ProviderEx.ClientLoadableCLSID
- Win32_ProviderEx.CLSID
- Win32_ProviderEx.Concurrency
- Win32_ProviderEx.DefaultMachineName
- Win32_ProviderEx.Enabled
- Win32_ProviderEx.ImpersonationLevel
- Win32_ProviderEx.InitializationReentrancy
- Win32_ProviderEx.InitializationTimeoutInterval
- Win32_ProviderEx.InitializeAsAdminFirst
- Win32_ProviderEx.Name
- Win32_ProviderEx.OperationTimeoutInterval
- Win32_ProviderEx.PerLocaleInitialization
- Win32_ProviderEx.PerUserInitialization
- Win32_ProviderEx.Pure
- Win32_ProviderEx.SupportsExplicitShutdown
- Win32_ProviderEx.SupportsExtendedStatus
- Win32_ProviderEx.SupportsQuotas
- Win32_ProviderEx.SupportsSendStatus
- Win32_ProviderEx.SupportsShutdown
- Win32_ProviderEx.SupportsThrottling
- Win32_ProviderEx.UnloadTimeout
- Win32_ProviderEx.HostingModel
- Win32_ProviderEx.SecurityDescriptor
- Win32_ProviderEx.version
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_ProviderEx class

Represents the provider.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Win32_ProviderEx : __Win32Provider
{
  string   ClientLoadableCLSID;
  string   CLSID;
  sint32   Concurrency;
  string   DefaultMachineName;
  boolean  Enabled;
  sint32   ImpersonationLevel = 0;
  sint32   InitializationReentrancy;
  datetime InitializationTimeoutInterval;
  boolean  InitializeAsAdminFirst;
  string   Name;
  datetime OperationTimeoutInterval;
  boolean  PerLocaleInitialization = FALSE;
  boolean  PerUserInitialization = FALSE;
  boolean  Pure = TRUE;
  boolean  SupportsExplicitShutdown;
  boolean  SupportsExtendedStatus;
  boolean  SupportsQuotas;
  boolean  SupportsSendStatus;
  boolean  SupportsShutdown;
  boolean  SupportsThrottling;
  datetime UnloadTimeout;
  string   HostingModel = "Decoupled:Com:FoldIdentity(FALSE)";
  string   SecurityDescriptor;
  UInt32   version = 1;
};
```

## Members

The **Win32\_ProviderEx** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ProviderEx** class has these properties.

<dl> <dt>

**ClientLoadableCLSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Class identifier that WMI uses to determine whether or not to load a high performance provider into the client process or the WMI process. If both the provider and client are located on the same computer, WMI loads the provider in-process to the client by using **ClientLoadableCLSID** as the class identifier. When the provider and client are located on different computers, WMI loads the provider in-process to WMI. WMI also uses **ClientLoadableCLSID** to support refresh operations.

For more information, see [Registering a High-Performance Provider.](https://msdn.microsoft.com/library/aa393031)

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**CLSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**GUID** that represents the class identifier (**CLSID**) of the provider COM object. This COM object must contain an implementation of the [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**Concurrency**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**DefaultMachineName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Identifies the computer on which to start the provider. If the provider runs on the local computer it is **NULL**.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, this instance is enabled and can be used to complete client requests.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**HostingModel**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("HostingModel")
</dt> </dl>

Hosting Model, provides compatibility with Windows XP and Windows Server .NET. Do not override.

</dd> <dt>

**ImpersonationLevel**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Reserved. The default value is zero (0).

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**InitializationReentrancy**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Set of flags that provide information about serialization. The default value is zero (0).

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

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

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**InitializeAsAdminFirst**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The provider name.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**OperationTimeoutInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**PerLocaleInitialization**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, the provider is initialized for each locale when a user connects to the same namespace more than one time using different locales. The default value is **FALSE**.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**PerUserInitialization**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, the provider is initialized one time for each NT LAN Manager (NTLM) user that makes requests to the provider. If **FALSE** (default), the provider is initialized one time for all users.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**Pure**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, the provider agrees to prepare to unload by calling [**IUnknown::Release**](https://www.bing.com/search?q=**IUnknown::Release**) on all outstanding interface points when WMI calls the **Release** method of its primary interface. Providers that must remain clients of WMI after they do not function as providers should set **Pure** to **FALSE**. The default setting is **TRUE**. For more information, see the Remarks section of this topic.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**SecurityDescriptor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("SecurityDescriptor")
</dt> </dl>

The security descriptor of the provider.

</dd> <dt>

**SupportsExplicitShutdown**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**SupportsExtendedStatus**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**SupportsQuotas**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**SupportsSendStatus**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**SupportsShutdown**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**SupportsThrottling**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not used.

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**UnloadTimeout**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

[Date and Time Format](https://msdn.microsoft.com/library/aa389802) that specifies how long WMI allows the provider to remain idle before it is unloaded. Typically, providers request that WMI wait no longer than five minutes.

For the current version of WMI, the value of this property is ignored. WMI unloads the provider based on the time-out value in an internal class in the \\root namespace. It is recommended that providers set **UnloadTimeout**. For more information, see [Unloading a Provider](https://msdn.microsoft.com/library/aa393943).

This property is inherited from [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688).

</dd> <dt>

**version**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Version)
</dt> </dl>

Version of the provider.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688)
</dt> </dl>

 

 





