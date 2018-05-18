---
title: MSFT\_WmiProvider\_PutClassAsyncEvent\_Pre class
description: Represents an event generated immediately prior to calling the provider's implementation of IWbemServices PutClassAsync.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'abbc674f-67db-4c1a-a514-1461c7a9b0bf'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_WmiProvider_PutClassAsyncEvent_Pre class", "MSFT_WmiProvider_PutClassAsyncEvent_Pre class, described"]
topic_type:
- apiref
api_name:
- MSFT_WmiProvider_PutClassAsyncEvent_Pre
- MSFT_WmiProvider_PutClassAsyncEvent_Pre.SECURITY_DESCRIPTOR
- MSFT_WmiProvider_PutClassAsyncEvent_Pre.TIME_CREATED
- MSFT_WmiProvider_PutClassAsyncEvent_Pre.TransactionIdentifer
- MSFT_WmiProvider_PutClassAsyncEvent_Pre.ClassObject
- MSFT_WmiProvider_PutClassAsyncEvent_Pre.Flags
- MSFT_WmiProvider_PutClassAsyncEvent_Pre.HostingGroup
- MSFT_WmiProvider_PutClassAsyncEvent_Pre.HostingSpecification
- MSFT_WmiProvider_PutClassAsyncEvent_Pre.Locale
- MSFT_WmiProvider_PutClassAsyncEvent_Pre.Namespace
- MSFT_WmiProvider_PutClassAsyncEvent_Pre.Provider
- MSFT_WmiProvider_PutClassAsyncEvent_Pre.TransactionIdentifier
- MSFT_WmiProvider_PutClassAsyncEvent_Pre.User
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
---

# MSFT\_WmiProvider\_PutClassAsyncEvent\_Pre class

The **MSFT\_WmiProvider\_PutClassAsyncEvent\_Pre** event class represents an event generated immediately prior to calling the provider's implementation of [**IWbemServices::PutClassAsync**](https://msdn.microsoft.com/library/aa392114).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class MSFT_WmiProvider_PutClassAsyncEvent_Pre : Msft_WmiProvider_OperationEvent_Pre
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  String TransactionIdentifer;
  object ClassObject;
  uint32 Flags;
  string HostingGroup;
  uint32 HostingSpecification;
  string Locale;
  string Namespace;
  string Provider;
  string TransactionIdentifier;
  string User;
};
```

## Members

The **MSFT\_WmiProvider\_PutClassAsyncEvent\_Pre** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiProvider\_PutClassAsyncEvent\_Pre** class has these properties.

<dl> <dt>

**ClassObject**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Class definition.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

One or more of the following values are valid.

<dt>

<span id="WBEM_FLAG_USE_AMENDED_QUALIFIERS"></span><span id="wbem_flag_use_amended_qualifiers"></span>

<span id="WBEM_FLAG_USE_AMENDED_QUALIFIERS"></span><span id="wbem_flag_use_amended_qualifiers"></span>**WBEM\_FLAG\_USE\_AMENDED\_QUALIFIERS**


</dt> <dd>

If this flag is set, WMI does not store any qualifiers with the amended flavor. If this flag is not set, it is assumed that this object is not localized, and all qualifiers are stored with this instance.

</dd> <dt>

<span id="WBEM_FLAG_CREATE_OR_UPDATE"></span><span id="wbem_flag_create_or_update"></span>

<span id="WBEM_FLAG_CREATE_OR_UPDATE"></span><span id="wbem_flag_create_or_update"></span>**WBEM\_FLAG\_CREATE\_OR\_UPDATE**


</dt> <dd>

This flag causes this class to be created if it does not exist or be overwritten if it exists already.

</dd> <dt>

<span id="WBEM_FLAG_UPDATE_ONLY"></span><span id="wbem_flag_update_only"></span>

<span id="WBEM_FLAG_UPDATE_ONLY"></span><span id="wbem_flag_update_only"></span>**WBEM\_FLAG\_UPDATE\_ONLY**


</dt> <dd>

Updates an existing class.

</dd> <dt>

<span id="WBEM_FLAG_CREATE_ONLY"></span><span id="wbem_flag_create_only"></span>

<span id="WBEM_FLAG_CREATE_ONLY"></span><span id="wbem_flag_create_only"></span>**WBEM\_FLAG\_CREATE\_ONLY**


</dt> <dd>

This flag is for class creation only. The call fails if the class already exists.

</dd> <dt>

<span id="WBEM_FLAG_SEND_STATUS"></span><span id="wbem_flag_send_status"></span>

<span id="WBEM_FLAG_SEND_STATUS"></span><span id="wbem_flag_send_status"></span>**WBEM\_FLAG\_SEND\_STATUS**


</dt> <dd>

This flag registers with Windows Management a request to receive intermediate status reports through the client's implementation of [**IWbemObjectSink::SetStatus**](https://msdn.microsoft.com/library/aa391789).

</dd> <dt>

<span id="WBEM_FLAG_OWNER_UPDATE"></span><span id="wbem_flag_owner_update"></span>

<span id="WBEM_FLAG_OWNER_UPDATE"></span><span id="wbem_flag_owner_update"></span>**WBEM\_FLAG\_OWNER\_UPDATE**


</dt> <dd>

Push providers must specify this flag when calling [**PutClassAsync**](https://msdn.microsoft.com/library/aa392114) to indicate that this class has changed.

</dd> <dt>

<span id="WBEM_FLAG_UPDATE_COMPATIBLE"></span><span id="wbem_flag_update_compatible"></span>

<span id="WBEM_FLAG_UPDATE_COMPATIBLE"></span><span id="wbem_flag_update_compatible"></span>**WBEM\_FLAG\_UPDATE\_COMPATIBLE**


</dt> <dd>

This flag allows a class to be updated if there are no derived classes and there are no instances for that class. It also allows updates in all cases if the change is just to non-important qualifiers (for example, the **Description** qualifier). This is the default behavior for this call and is used for compatibility with previous versions of WMI. If the class has instances or changes are to important qualifiers, the update fails.

</dd> <dt>

<span id="WBEM_FLAG_UPDATE_SAFE_MODE"></span><span id="wbem_flag_update_safe_mode"></span>

<span id="WBEM_FLAG_UPDATE_SAFE_MODE"></span><span id="wbem_flag_update_safe_mode"></span>**WBEM\_FLAG\_UPDATE\_SAFE\_MODE**


</dt> <dd>

This flag allows updates of classes even if there are child classes, as long as the change does not cause any conflicts with child classes. An example of an update this flag would allow would be to add a new property to the base class that was not previously mentioned in any of the child classes. If the class has instances, the update fails.

</dd> <dt>

<span id="WBEM_FLAG_UPDATE_FORCE_MODE"></span><span id="wbem_flag_update_force_mode"></span>

<span id="WBEM_FLAG_UPDATE_FORCE_MODE"></span><span id="wbem_flag_update_force_mode"></span>**WBEM\_FLAG\_UPDATE\_FORCE\_MODE**


</dt> <dd>

This flag forces updates of classes when conflicting child classes exist. An example of an update this flag would force would be if a class qualifier were defined in a child class, and the base class tried to add the same qualifier which conflicted with the existing one. In force mode, this conflict would be resolved by deleting the conflicting qualifier in the child class.

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

**Provider**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name associated with a particular provider instance. The name is identical to the [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) property.

This property is inherited from [**Msft\_WmiProvider\_OperationEvent**](msft-wmiprovider-operationevent.md)

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

[**Msft\_WmiProvider\_OperationEvent\_Pre**](msft-wmiprovider-operationevent-pre.md)
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

 

 





