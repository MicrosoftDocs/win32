---
title: MSFT\_WmiProvider\_OperationEvent class
description: Root definition of all WMI provider events.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a4b05dec-314d-47df-90db-0ba877cf27b2
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WmiProvider_OperationEvent class
- MSFT_WmiProvider_OperationEvent class, described
topic_type:
- apiref
api_name:
- MSFT_WmiProvider_OperationEvent
- MSFT_WmiProvider_OperationEvent.SECURITY_DESCRIPTOR
- MSFT_WmiProvider_OperationEvent.TIME_CREATED
- MSFT_WmiProvider_OperationEvent.HostingGroup
- MSFT_WmiProvider_OperationEvent.HostingSpecification
- MSFT_WmiProvider_OperationEvent.Locale
- MSFT_WmiProvider_OperationEvent.Namespace
- MSFT_WmiProvider_OperationEvent.Provider
- MSFT_WmiProvider_OperationEvent.TransactionIdentifier
- MSFT_WmiProvider_OperationEvent.User
- MSFT_WmiProvider_OperationEvent.TransactionIdentifer
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_WmiProvider\_OperationEvent class

The **MSFT\_WmiProvider\_OperationEvent** base class is the root definition of all WMI provider events. A provider operation is defined as some execution on behalf of a client using WMI that results in one or more calls to a provider executable file. The properties of this class define the identity of the provider associated with the operation being executed and is uniquely associated with instances of the class [**MSFT\_Providers**](msft-providers.md). Each instance of [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) can have an associated operation and be identified using the properties below.

Internally, WMI can contain any number of objects that refer to a particular instance of [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) because it differentiates each object based on whether the provider supports per user or per locale instantiation and also depending on where the provider is being hosted. Currently, the **TransactionIdentifier** property is always an empty string.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class MSFT_WmiProvider_OperationEvent : MSFT_WmiSelfEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  string HostingGroup;
  uint32 HostingSpecification;
  string Locale;
  string Namespace;
  string Provider;
  string TransactionIdentifier;
  string User;
  String TransactionIdentifer;
};
```

## Members

The **MSFT\_WmiProvider\_OperationEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiProvider\_OperationEvent** class has these properties.

<dl> <dt>

**HostingGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Second component of the [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) **HostingModel** property when the hosting model is one of "LocalSystemHost", "LocalSystemHostOrSelfHost", "NetworkServiceHost", or "LocalServiceHost". The hosting group defines a particular instantiation of a WMI provider host. Providers that share the same hosting model and hosting group share the same surrogate process.

</dd> <dt>

**HostingSpecification**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The first component of the [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) **HostingModel** property. For the possible values of this property, see the **HostingSpecification** property in the [**MSFT\_Providers**](msft-providers.md) class.

</dd> <dt>

**Locale**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Particular instantiation of a provider instance when the provider is configured for per local initialization.

</dd> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Namespace associated with a particular provider instance.

</dd> <dt>

**Provider**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name associated with a particular provider instance. The name is identical to the [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) property.

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

</dd> <dt>

**TransactionIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Internal use only. The current value is "{00000000-0000-0000-0000-000000000000}".

</dd> <dt>

**User**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Particular provider instance, configured for per user initialization.

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

[**MSFT\_WmiSelfEvent**](msft-wmiselfevent.md)
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

 

 





