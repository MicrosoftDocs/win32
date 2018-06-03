---
title: MSFT\_WmiProvider\_ComServerLoadOperationFailureEvent class
description: Defines the unsuccessful activation of a COM server instance associated with the provider registration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a80c23e7-e549-4ce3-af3a-3be65e546810
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent class
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent class, described
topic_type:
- apiref
api_name:
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.SECURITY_DESCRIPTOR
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.TIME_CREATED
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.TransactionIdentifer
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.Clsid
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.HostingGroup
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.HostingSpecification
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.InProcServer
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.InProcServerPath
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.Locale
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.LocalServer
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.LocalServerPath
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.Namespace
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.Provider
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.ResultCode
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.ServerName
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.TransactionIdentifier
- MSFT_WmiProvider_ComServerLoadOperationFailureEvent.User
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_WmiProvider\_ComServerLoadOperationFailureEvent class

The **MSFT\_WmiProvider\_ComServerLoadOperationFailureEvent** event class defines the unsuccessful activation of a COM server instance associated with the provider registration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class MSFT_WmiProvider_ComServerLoadOperationFailureEvent : Msft_WmiProvider_OperationEvent
{
  uint8   SECURITY_DESCRIPTOR[];
  uint64  TIME_CREATED;
  String  TransactionIdentifer;
  string  Clsid;
  string  HostingGroup;
  uint32  HostingSpecification;
  boolean InProcServer;
  string  InProcServerPath;
  string  Locale;
  boolean LocalServer;
  string  LocalServerPath;
  string  Namespace;
  string  Provider;
  uint32  ResultCode;
  string  ServerName;
  string  TransactionIdentifier;
  string  User;
};
```

## Members

The **MSFT\_WmiProvider\_ComServerLoadOperationFailureEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiProvider\_ComServerLoadOperationFailureEvent** class has these properties.

<dl> <dt>

**Clsid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

COM **CLSID** associated with server implementation, if applicable. Decoupled providers do not have an associated COM **CLSID**.

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

**InProcServer**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the server supports inproc32 activation.

</dd> <dt>

**InProcServerPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Server inproc32 executable application name, if applicable.

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

**LocalServer**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the server supports localserver32 activation.

</dd> <dt>

**LocalServerPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Server localserver32 executable application name, if applicable.

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

**ResultCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Result code returned from the COM activation procedure, if applicable.

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

**ServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

COM server name present within the unnamed value of the **CLSID** key, if applicable.

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

[**Msft\_WmiProvider\_OperationEvent**](msft-wmiprovider-operationevent.md)
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

 

 





