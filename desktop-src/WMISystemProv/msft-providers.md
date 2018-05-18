---
title: MSFT\_Providers class
description: The MSFT\_Providers class contains configuration information for providers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '43d18a94-5925-40ed-812d-50b941d040ed'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_Providers class", "MSFT_Providers class, described"]
topic_type:
- apiref
api_name:
- MSFT_Providers
- MSFT_Providers.HostingGroup
- MSFT_Providers.HostingSpecification
- MSFT_Providers.HostingProcessIdentifier
- MSFT_Providers.Locale
- MSFT_Providers.Namespace
- MSFT_Providers.Provider
- MSFT_Providers.ProviderOperation_AccessCheck
- MSFT_Providers.ProviderOperation_CancelQuery
- MSFT_Providers.ProviderOperation_CreateClassEnumAsync
- MSFT_Providers.ProviderOperation_CreateInstanceEnumAsync
- MSFT_Providers.ProviderOperation_CreateRefreshableEnum
- MSFT_Providers.ProviderOperation_CreateRefreshableObject
- MSFT_Providers.ProviderOperation_CreateRefresher
- MSFT_Providers.ProviderOperation_DeleteClassAsync
- MSFT_Providers.ProviderOperation_DeleteInstanceAsync
- MSFT_Providers.ProviderOperation_ExecMethodAsync
- MSFT_Providers.ProviderOperation_ExecQueryAsync
- MSFT_Providers.ProviderOperation_FindConsumer
- MSFT_Providers.ProviderOperation_GetObjectAsync
- MSFT_Providers.ProviderOperation_GetObjects
- MSFT_Providers.ProviderOperation_GetProperty
- MSFT_Providers.ProviderOperation_NewQuery
- MSFT_Providers.ProviderOperation_ProvideEvents
- MSFT_Providers.ProviderOperation_PutClassAsync
- MSFT_Providers.ProviderOperation_PutInstanceAsync
- MSFT_Providers.ProviderOperation_PutProperty
- MSFT_Providers.ProviderOperation_QueryInstances
- MSFT_Providers.ProviderOperation_SetRegistrationObject
- MSFT_Providers.ProviderOperation_StopRefreshing
- MSFT_Providers.ProviderOperation_ValidateSubscription
- MSFT_Providers.TransactionIdentifier
- MSFT_Providers.User
- MSFT_Providers.HostProcessIdentifier
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
---

# MSFT\_Providers class

The **MSFT\_Providers** class contains configuration information for providers.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("Msft_ProviderSubSystem"), AMENDMENT]
class MSFT_Providers
{
  string HostingGroup;
  uint32 HostingSpecification;
  string HostingProcessIdentifier;
  string Locale;
  string Namespace;
  string Provider;
  uint64 ProviderOperation_AccessCheck;
  uint64 ProviderOperation_CancelQuery;
  uint64 ProviderOperation_CreateClassEnumAsync;
  uint64 ProviderOperation_CreateInstanceEnumAsync;
  uint64 ProviderOperation_CreateRefreshableEnum;
  uint64 ProviderOperation_CreateRefreshableObject;
  uint64 ProviderOperation_CreateRefresher;
  uint64 ProviderOperation_DeleteClassAsync;
  uint64 ProviderOperation_DeleteInstanceAsync;
  uint64 ProviderOperation_ExecMethodAsync;
  uint64 ProviderOperation_ExecQueryAsync;
  uint64 ProviderOperation_FindConsumer;
  uint64 ProviderOperation_GetObjectAsync;
  uint64 ProviderOperation_GetObjects;
  uint64 ProviderOperation_GetProperty;
  uint64 ProviderOperation_NewQuery;
  uint64 ProviderOperation_ProvideEvents;
  uint64 ProviderOperation_PutClassAsync;
  uint64 ProviderOperation_PutInstanceAsync;
  uint64 ProviderOperation_PutProperty;
  uint64 ProviderOperation_QueryInstances;
  uint64 ProviderOperation_SetRegistrationObject;
  uint64 ProviderOperation_StopRefreshing;
  uint64 ProviderOperation_ValidateSubscription;
  string TransactionIdentifier;
  string User;
  Uint32 HostProcessIdentifier;
};
```

## Members

The **MSFT\_Providers** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_Providers** class has these methods.



| Method                                                    | Description                                                                          |
|:----------------------------------------------------------|:-------------------------------------------------------------------------------------|
| [**Load**](load-method-in-class-msft-providers.md)       | Loads a specific instance of a provider.<br/>                                  |
| [**Resume**](resume-method-in-class-msft-providers.md)   | Resumes execution of suspended providers.<br/>                                 |
| [**Suspend**](suspend-method-in-class-msft-providers.md) | Suspends execution of providers.<br/>                                          |
| [**UnLoad**](unload-method-in-class-msft-providers.md)   | Unloads the COM server associated with a specific instance of a provider.<br/> |



 

### Properties

The **MSFT\_Providers** class has these properties.

<dl> <dt>

**HostingGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Defines the second component of the [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) **HostingModel** property when the hosting model is one of the following:

-   **LocalSystemHost**
-   **NetworkServiceHost**
-   **LocalServiceHost**
-   **LocalSystemHostOrSelfHost**
-   **NetworkServiceHostOrSelfHost**

The hosting group defines a grouping of providers in a separate Wmiprvse.exe process. Providers that share the same hosting model and hosting group share the same service host process.

</dd> <dt>

**HostingProcessIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Process identifier that hosts the specific instance of the provider.

</dd> <dt>

**HostingSpecification**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Defines the first component of the [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) **HostingModel** property. The hosting property is defined to be one of these value types.

<dt>

<span id="WmiCore"></span><span id="wmicore"></span><span id="WMICORE"></span>

<span id="WmiCore"></span><span id="wmicore"></span><span id="WMICORE"></span>**WmiCore**


</dt> <dd>

Activate provider in host to the WMI service. This hosting model is only supported for operating system components.

Attempts to register providers with **WmiCore** fail with **WBEM\_E\_ACCESS\_DENIED**.

</dd> <dt>

<span id="WmiCoreOrSelfHost"></span><span id="wmicoreorselfhost"></span><span id="WMICOREORSELFHOST"></span>

<span id="WmiCoreOrSelfHost"></span><span id="wmicoreorselfhost"></span><span id="WMICOREORSELFHOST"></span>**WmiCoreOrSelfHost**


</dt> <dd>

Activate provider in host to the WMI service or as local server. This hosting model is only supported for operating system components.

Attempts to register providers with **WmiCoreOrSelfHost** fail with **WBEM\_E\_ACCESS\_DENIED**.

</dd> <dt>

<span id="SelfHost"></span><span id="selfhost"></span><span id="SELFHOST"></span>

<span id="SelfHost"></span><span id="selfhost"></span><span id="SELFHOST"></span>**SelfHost**


</dt> <dd>

Activate provider as a local server implementation.

</dd> <dt>

<span id="Decoupled_Com"></span><span id="decoupled_com"></span><span id="DECOUPLED_COM"></span>

<span id="Decoupled_Com"></span><span id="decoupled_com"></span><span id="DECOUPLED_COM"></span>**Decoupled:Com**


</dt> <dd>

Activate provider as a decoupled COM provider. For more information about decoupled providers, see [Incorporating a Provider in an Application](https://msdn.microsoft.com/library/aa390882).

</dd> <dt>

<span id="Decoupled_NonCom"></span><span id="decoupled_noncom"></span><span id="DECOUPLED_NONCOM"></span>

<span id="Decoupled_NonCom"></span><span id="decoupled_noncom"></span><span id="DECOUPLED_NONCOM"></span>**Decoupled:NonCom**


</dt> <dd>

Activate provider as a non-COM event provider.

</dd> <dt>

<span id="LocalSystemHost"></span><span id="localsystemhost"></span><span id="LOCALSYSTEMHOST"></span>

<span id="LocalSystemHost"></span><span id="localsystemhost"></span><span id="LOCALSYSTEMHOST"></span>**LocalSystemHost**


</dt> <dd>

Activate provider in the provider host process that is running under the [LocalSystem](https://msdn.microsoft.com/library/windows/desktop/ms684190) account.

</dd> <dt>

<span id="LocalSystemHostOrSelfHost"></span><span id="localsystemhostorselfhost"></span><span id="LOCALSYSTEMHOSTORSELFHOST"></span>

<span id="LocalSystemHostOrSelfHost"></span><span id="localsystemhostorselfhost"></span><span id="LOCALSYSTEMHOSTORSELFHOST"></span>**LocalSystemHostOrSelfHost**


</dt> <dd>

The provider is self-hosted or loaded into the Wmiprvse.exe process running under the [LocalSystem](https://msdn.microsoft.com/library/windows/desktop/ms684190) account.

**Note**  **LocalSystemHostOrSelfHost** is the default configuration that WMI sets when the [**HostingModel**](https://msdn.microsoft.com/library/aa394688) property in **\_\_Win32Provider** is **NULL**. Because [LocalSystem](https://msdn.microsoft.com/library/windows/desktop/ms684190) is a highly privileged account, an entry is generated in the Security Event Log to notify administrators of a provider running in this trusted status.

</dd> <dt>

<span id="NetworkServiceHost"></span><span id="networkservicehost"></span><span id="NETWORKSERVICEHOST"></span>

<span id="NetworkServiceHost"></span><span id="networkservicehost"></span><span id="NETWORKSERVICEHOST"></span>**NetworkServiceHost**


</dt> <dd>

Activate provider in the provider host process that is running under the [NetworkService](https://msdn.microsoft.com/library/windows/desktop/ms684272) account.

</dd> <dt>

<span id="LocalServiceHost"></span><span id="localservicehost"></span><span id="LOCALSERVICEHOST"></span>

<span id="LocalServiceHost"></span><span id="localservicehost"></span><span id="LOCALSERVICEHOST"></span>**LocalServiceHost**


</dt> <dd>

Activate provider in the provider host process that is running under the [LocalService](https://msdn.microsoft.com/library/windows/desktop/ms684188) account.

</dd> <dt>

<span id="NetworkServiceHostOrSelfHost"></span><span id="networkservicehostorselfhost"></span><span id="NETWORKSERVICEHOSTORSELFHOST"></span>

<span id="NetworkServiceHostOrSelfHost"></span><span id="networkservicehostorselfhost"></span><span id="NETWORKSERVICEHOSTORSELFHOST"></span>****NetworkServiceHostOrSelfHost****


</dt> <dd>

The provider is self-hosted or loaded into the Wmiprvse.exe process running under the [NetworkService](https://msdn.microsoft.com/library/windows/desktop/ms684272) account. **NetworkServiceHostOrSelfHost** is the default configuration when the [**HostingModel**](https://msdn.microsoft.com/library/aa394688) property in **\_\_Win32Provider** is **NULL**. Because **NetworkServiceHostOrSelfHost** is the default, providers from earlier operating systems can continue to work in later operating systems.

</dd> </dl>

</dd> <dt>

**HostProcessIdentifier**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **HostProcessIdentifier** property defines the process identifier hosting the particular instance of the provider.

</dd> <dt>

**Locale**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The language locale. For Microsoft locale identifiers, the format of the string is "MS\_xxxx", where xxxx is a string in hexadecimal form that indicates the LCID. For example, the American English locale identifier is "MS\_409".

</dd> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Namespace associated with a specific provider instance.

</dd> <dt>

**Provider**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Name associated with a specific provider instance. The name is identical to the [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) property.

</dd> <dt>

**ProviderOperation\_AccessCheck**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemEventProviderSecurity::AccessCheck**](https://msdn.microsoft.com/library/aa391743).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_CancelQuery**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemEventProviderQuerySink::CancelQuery**](https://msdn.microsoft.com/library/aa391738).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_CreateClassEnumAsync**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemServices::CreateClassEnumAsync**](https://msdn.microsoft.com/library/aa392096).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_CreateInstanceEnumAsync**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemServices::CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_CreateRefreshableEnum**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemHiPerfProvider::CreateRefreshableEnum**](https://msdn.microsoft.com/library/aa391760).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_CreateRefreshableObject**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemHiPerfProvider::CreateRefreshableObject**](https://msdn.microsoft.com/library/aa391762).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_CreateRefresher**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemHiPerfProvider::CreateRefresher**](https://msdn.microsoft.com/library/aa391763).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_DeleteClassAsync**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemServices::DeleteClassAsync**](https://msdn.microsoft.com/library/aa392100).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_DeleteInstanceAsync**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemServices::DeleteInstanceAsync**](https://msdn.microsoft.com/library/aa392102).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_ExecMethodAsync**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemServices::ExecMethodAsync**](https://msdn.microsoft.com/library/aa392104).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_ExecQueryAsync**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemServices::ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_FindConsumer**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemEventConsumerProvider::FindConsumer**](https://msdn.microsoft.com/library/aa391491).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_GetObjectAsync**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemServices::GetObjectAsync**](https://msdn.microsoft.com/library/aa392110).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_GetObjects**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemHiPerfProvider::GetObjects**](https://msdn.microsoft.com/library/aa391764).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_GetProperty**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemPropertyProvider::GetProperty**](https://msdn.microsoft.com/library/aa391848).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_NewQuery**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemEventProviderQuerySink::NewQuery**](https://msdn.microsoft.com/library/aa391739).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_ProvideEvents**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemEventProvider::ProvideEvents**](https://msdn.microsoft.com/library/aa391744).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_PutClassAsync**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemServices::PutClassAsync**](https://msdn.microsoft.com/library/aa392114).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_PutInstanceAsync**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemServices::PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_PutProperty**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemPropertyProvider::PutProperty**](https://msdn.microsoft.com/library/aa391849).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_QueryInstances**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemHiPerfProvider::QueryInstances**](https://msdn.microsoft.com/library/aa391765).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_SetRegistrationObject**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Property currently not set.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_StopRefreshing**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of calls to [**IWbemHiPerfProvider::StopRefreshing**](https://msdn.microsoft.com/library/aa391766).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ProviderOperation\_ValidateSubscription**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Currently not supported.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**TransactionIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Internal use only. The current value is "{00000000-0000-0000-0000-000000000000}".

</dd> <dt>

**User**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Particular provider instance, configured for per user initialization.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>System.mof</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>WmiPrvSD.dll</dt> </dl> |



## See also

<dl> <dt>

[Provider Hosting and Security](https://msdn.microsoft.com/library/aa392783)
</dt> </dl>

 

 





