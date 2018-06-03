---
title: MSFT\_WmiProvider\_DeleteClassAsyncEvent\_Pre class
description: Represents an event generated immediately prior to calling the provider's implementation of IWbemServices DeleteClassAsync.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8a4fe9b2-9bfa-43f9-a339-9f0773d94cda
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre class
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre class, described
topic_type:
- apiref
api_name:
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre.SECURITY_DESCRIPTOR
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre.TIME_CREATED
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre.TransactionIdentifer
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre.ClassObject
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre.Flags
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre.HostingGroup
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre.HostingSpecification
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre.Locale
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre.Namespace
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre.Provider
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre.TransactionIdentifier
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre.User
- MSFT_WmiProvider_DeleteClassAsyncEvent_Pre.ClassName
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_WmiProvider\_DeleteClassAsyncEvent\_Pre class

The **MSFT\_WmiProvider\_DeleteClassAsyncEvent\_Pre** event class represents an event generated immediately prior to calling the provider's implementation of [**IWbemServices::DeleteClassAsync**](https://msdn.microsoft.com/library/aa392100).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class MSFT_WmiProvider_DeleteClassAsyncEvent_Pre : Msft_WmiProvider_OperationEvent_Pre
{
  uint8  SECURITY_DESCRIPTOR[];
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
  String ClassName;
};
```

## Members

The **MSFT\_WmiProvider\_DeleteClassAsyncEvent\_Pre** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiProvider\_DeleteClassAsyncEvent\_Pre** class has these properties.

<dl> <dt>

**ClassName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **ClassName** property hold the name of the class targeted for deletion.

</dd> <dt>

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

<span id="WBEM_FLAG_SEND_STATUS"></span><span id="wbem_flag_send_status"></span>

<span id="WBEM_FLAG_SEND_STATUS"></span><span id="wbem_flag_send_status"></span>**WBEM\_FLAG\_SEND\_STATUS**


</dt> <dd>

This flag registers with WMI a request to receive intermediate status reports through the client's implementation of [**IWbemObjectSink::SetStatus**](https://msdn.microsoft.com/library/aa391789).

</dd> <dt>

<span id="WBEM_FLAG_OWNER_UPDATE"></span><span id="wbem_flag_owner_update"></span>

<span id="WBEM_FLAG_OWNER_UPDATE"></span><span id="wbem_flag_owner_update"></span>**WBEM\_FLAG\_OWNER\_UPDATE**


</dt> <dd>

Push providers must specify this flag when calling [**DeleteClassAsync**](https://msdn.microsoft.com/library/aa392100) to indicate that this class has changed.

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
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
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

 

 





