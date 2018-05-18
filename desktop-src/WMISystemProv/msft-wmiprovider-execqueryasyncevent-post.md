---
title: MSFT\_WmiProvider\_ExecQueryAsyncEvent\_Post class
description: Represents an event generated immediately following completion of the provider's implementation of IWbemServices ExecQueryAsync.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a3aae1ee-0747-4025-8cf1-b8266e95bfc6'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_WmiProvider_ExecQueryAsyncEvent_Post class", "MSFT_WmiProvider_ExecQueryAsyncEvent_Post class, described"]
topic_type:
- apiref
api_name:
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.SECURITY_DESCRIPTOR
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.TIME_CREATED
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.TransactionIdentifer
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.Flags
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.HostingGroup
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.HostingSpecification
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.Locale
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.Namespace
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.ObjectParameter
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.Provider
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.Query
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.QueryLanguage
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.ResultCode
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.StringParameter
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.TransactionIdentifier
- MSFT_WmiProvider_ExecQueryAsyncEvent_Post.User
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
---

# MSFT\_WmiProvider\_ExecQueryAsyncEvent\_Post class

The **MSFT\_WmiProvider\_ExecQueryAsyncEvent\_Post** event class represents an event generated immediately following completion of the provider's implementation of [**IWbemServices::ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class MSFT_WmiProvider_ExecQueryAsyncEvent_Post : Msft_WmiProvider_OperationEvent_Post
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  String TransactionIdentifer;
  uint32 Flags;
  string HostingGroup;
  uint32 HostingSpecification;
  string Locale;
  string Namespace;
  object ObjectParameter;
  string Provider;
  string Query;
  string QueryLanguage;
  uint32 ResultCode;
  string StringParameter;
  string TransactionIdentifier;
  string User;
};
```

## Members

The **MSFT\_WmiProvider\_ExecQueryAsyncEvent\_Post** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiProvider\_ExecQueryAsyncEvent\_Post** class has these properties.

<dl> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This parameter can be one of the following values.

<dt>

<span id="WBEM_FLAG_USE_AMENDED_QUALIFIERS"></span><span id="wbem_flag_use_amended_qualifiers"></span>

<span id="WBEM_FLAG_USE_AMENDED_QUALIFIERS"></span><span id="wbem_flag_use_amended_qualifiers"></span>**WBEM\_FLAG\_USE\_AMENDED\_QUALIFIERS**


</dt> <dd>

If this flag is set, WMI retrieves the amended qualifiers stored in the localized namespace of the current connection's locale. If not set, only the qualifiers stored in the immediate namespace are retrieved.

</dd> <dt>

<span id="WBEM_FLAG_BIDIRECTIONAL"></span><span id="wbem_flag_bidirectional"></span>

<span id="WBEM_FLAG_BIDIRECTIONAL"></span><span id="wbem_flag_bidirectional"></span>**WBEM\_FLAG\_BIDIRECTIONAL**


</dt> <dd>

This flag causes WMI to retain pointers to objects of the enumeration until the client releases the enumerator.

</dd> <dt>

<span id="WBEM_FLAG_SEND_STATUS"></span><span id="wbem_flag_send_status"></span>

<span id="WBEM_FLAG_SEND_STATUS"></span><span id="wbem_flag_send_status"></span>**WBEM\_FLAG\_SEND\_STATUS**


</dt> <dd>

This flag registers with WMI a request to receive intermediate status reports through the client's implementation of [**IWbemObjectSink::SetStatus**](https://msdn.microsoft.com/library/aa391789).

</dd> <dt>

<span id="WBEM_FLAG_ENSURE_LOCATABLE"></span><span id="wbem_flag_ensure_locatable"></span>

<span id="WBEM_FLAG_ENSURE_LOCATABLE"></span><span id="wbem_flag_ensure_locatable"></span>**WBEM\_FLAG\_ENSURE\_LOCATABLE**


</dt> <dd>

This flag ensures that any returned objects have enough information in them so that the system properties, such as **\_\_PATH**, **\_\_RELPATH**, and **\_\_SERVER**, are non-**NULL**.

</dd> <dt>

<span id="WBEM_FLAG_PROTOTYPE"></span><span id="wbem_flag_prototype"></span>

<span id="WBEM_FLAG_PROTOTYPE"></span><span id="wbem_flag_prototype"></span>**WBEM\_FLAG\_PROTOTYPE**


</dt> <dd>

This flag is used for prototyping. It does not execute the query and instead returns an object that looks like a typical result object.

</dd> <dt>

<span id="WBEM_FLAG_DIRECT_READ"></span><span id="wbem_flag_direct_read"></span>

<span id="WBEM_FLAG_DIRECT_READ"></span><span id="wbem_flag_direct_read"></span>**WBEM\_FLAG\_DIRECT\_READ**


</dt> <dd>

This flag causes direct access to the provider for the class specified without any regard to its parent class or subclasses.

</dd> </dl>

</dd> <dt>

**HostingGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Second component of the [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) **HostingModel** property when the hosting model is one of "LocalSystemHost", "LocalSystemHostOrSelfHost", "NetworkServiceHost", or "LocalServiceHost". The hosting group defines a particular instantiation of a WMI provider host. Providers that share the same hosting model and hosting group share the same surrogate process.

This property is inherited from [**Msft\_WmiProvider\_OperationEvent**](msft-wmiprovider-operationevent.md)

</dd> <dt>

**HostingSpecification**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The first component of the [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) **HostingModel** property. For the possible values of this property, see the **HostingSpecification** property in the [**MSFT\_Providers**](msft-providers.md) class.

This property is inherited from [**Msft\_WmiProvider\_OperationEvent**](msft-wmiprovider-operationevent.md)

</dd> <dt>

**Locale**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Particular instantiation of a provider instance when the provider is configured for per local initialization.

This property is inherited from [**Msft\_WmiProvider\_OperationEvent**](msft-wmiprovider-operationevent.md)

</dd> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Namespace associated with a particular provider instance.

This property is inherited from [**Msft\_WmiProvider\_OperationEvent**](msft-wmiprovider-operationevent.md)

</dd> <dt>

**ObjectParameter**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Extended status passed through provider's [**IWbemObjectSink::SetStatus**](https://msdn.microsoft.com/library/aa391789) call, possible **NULL**.

</dd> <dt>

**Provider**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name associated with a particular provider instance. The name is identical to the [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) property.

This property is inherited from [**Msft\_WmiProvider\_OperationEvent**](msft-wmiprovider-operationevent.md)

</dd> <dt>

**Query**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Event query filter, which was registered by a logical consumer.

</dd> <dt>

**QueryLanguage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Language of the query filter. For this version of WMI, it is always WQL.

</dd> <dt>

**ResultCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**HRESULT** status code of the operation.

</dd> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor that the event provider uses to determine which users can receive the event. For more information, see [WMI Security Constants](https://msdn.microsoft.com/library/aa394576).

This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634).

</dd> <dt>

**StringParameter**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is currently always **NULL**.

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time the event is generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Time (UTC) format.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634).

</dd> <dt>

**TransactionIdentifer**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **TransactionIdentifer** property is for internal use, currently always empty.

This property is inherited from [**Msft\_WmiProvider\_OperationEvent**](msft-wmiprovider-operationevent.md).

</dd> <dt>

**TransactionIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Internal use only. The current value is "{00000000-0000-0000-0000-000000000000}".

This property is inherited from [**Msft\_WmiProvider\_OperationEvent**](msft-wmiprovider-operationevent.md)

</dd> <dt>

**User**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Particular provider instance, configured for per user initialization.

This property is inherited from [**Msft\_WmiProvider\_OperationEvent**](msft-wmiprovider-operationevent.md)

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

[**Msft\_WmiProvider\_OperationEvent\_Post**](msft-wmiprovider-operationevent-post.md)
</dt> <dt>

[Provider Event Troubleshooting Classes](https://msdn.microsoft.com/library/aa392768)
</dt> <dt>

[**MSFT\_Providers**](msft-providers.md)
</dt> <dt>

[WMI Troubleshooting](https://msdn.microsoft.com/library/aa394603)
</dt> <dt>

[Receiving a WMI Event](https://msdn.microsoft.com/library/aa393013)
</dt> </dl>

 

 





