---
title: MSFT\_WmiProvider\_PutInstanceAsyncEvent\_Post class
description: Represents an event generated immediately following completion of the provider's implementation of IWbemServices PutInstanceAsync.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 93451261-092d-4cac-b64e-3c15aeb9096a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post class
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post class, described
topic_type:
- apiref
api_name:
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.SECURITY_DESCRIPTOR
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.TIME_CREATED
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.TransactionIdentifer
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.Flags
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.HostingGroup
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.HostingSpecification
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.InstanceObject
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.Locale
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.Namespace
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.ObjectParameter
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.Provider
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.ResultCode
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.StringParameter
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.SuperclassName
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.TransactionIdentifier
- MSFT_WmiProvider_PutInstanceAsyncEvent_Post.User
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_WmiProvider\_PutInstanceAsyncEvent\_Post class

The **MSFT\_WmiProvider\_PutInstanceAsyncEvent\_Post** event class represents an event generated immediately following completion of the provider's implementation of [**IWbemServices::PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class MSFT_WmiProvider_PutInstanceAsyncEvent_Post : Msft_WmiProvider_OperationEvent_Post
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  String TransactionIdentifer;
  uint32 Flags;
  string HostingGroup;
  uint32 HostingSpecification;
  object InstanceObject;
  string Locale;
  string Namespace;
  object ObjectParameter;
  string Provider;
  uint32 ResultCode;
  string StringParameter;
  string SuperclassName;
  string TransactionIdentifier;
  string User;
};
```

## Members

The **MSFT\_WmiProvider\_PutInstanceAsyncEvent\_Post** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiProvider\_PutInstanceAsyncEvent\_Post** class has these properties.

<dl> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Creation mode if the instance does not currently exist. This property can have one or more of the following values.

<dt>

<span id="WBEM_FLAG_CREATE_OR_UPDATE"></span><span id="wbem_flag_create_or_update"></span>

<span id="WBEM_FLAG_CREATE_OR_UPDATE"></span><span id="wbem_flag_create_or_update"></span>**WBEM\_FLAG\_CREATE\_OR\_UPDATE**


</dt> <dd>

This flag causes this instance to be created if it does not exist or be overwritten if it exists already.

</dd> <dt>

<span id="WBEM_FLAG_UPDATE_ONLY"></span><span id="wbem_flag_update_only"></span>

<span id="WBEM_FLAG_UPDATE_ONLY"></span><span id="wbem_flag_update_only"></span>**WBEM\_FLAG\_UPDATE\_ONLY**


</dt> <dd>

Updates an existing instance.

</dd> <dt>

<span id="WBEM_FLAG_CREATE_ONLY"></span><span id="wbem_flag_create_only"></span>

<span id="WBEM_FLAG_CREATE_ONLY"></span><span id="wbem_flag_create_only"></span>**WBEM\_FLAG\_CREATE\_ONLY**


</dt> <dd>

This flag is for instance creation only. The call fails if the class already exists.

</dd> <dt>

<span id="WBEM_FLAG_SEND_STATUS"></span><span id="wbem_flag_send_status"></span>

<span id="WBEM_FLAG_SEND_STATUS"></span><span id="wbem_flag_send_status"></span>**WBEM\_FLAG\_SEND\_STATUS**


</dt> <dd>

This flag registers with WMI a request to receive intermediate status reports through the clients implementation of [**IWbemObjectSink::SetStatus**](https://msdn.microsoft.com/library/aa391789).

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

**InstanceObject**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Object instance to be written.

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

**SuperclassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Parent class name if not blank or **NULL**. Only classes that are subclasses of this class are returned. If this property is **NULL** or blank and **Flags** contains **WBEM\_FLAG\_SHALLOW**, only top-level classes (those which have no parent class) are returned. If this property is **NULL** or blank and **Flags** is **WBEM\_FLAG\_DEEP**, all classes within the namespace are returned.

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
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
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

WMI Troubleshooting
</dt> <dt>

[Receiving a WMI Event](https://msdn.microsoft.com/library/aa393013)
</dt> </dl>

 

 





