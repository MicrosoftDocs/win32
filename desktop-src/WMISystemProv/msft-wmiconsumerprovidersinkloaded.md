---
title: MSFT\_WmiConsumerProviderSinkLoaded class
description: Defines the successful activation of the event consumer provider sink object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a3a8f485-9336-4165-91cb-caf6dca9232a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WmiConsumerProviderSinkLoaded class
- MSFT_WmiConsumerProviderSinkLoaded class, described
topic_type:
- apiref
api_name:
- MSFT_WmiConsumerProviderSinkLoaded
- MSFT_WmiConsumerProviderSinkLoaded.SECURITY_DESCRIPTOR
- MSFT_WmiConsumerProviderSinkLoaded.TIME_CREATED
- MSFT_WmiConsumerProviderSinkLoaded.Namespace
- MSFT_WmiConsumerProviderSinkLoaded.ProviderName
- MSFT_WmiConsumerProviderSinkLoaded.Machine
- MSFT_WmiConsumerProviderSinkLoaded.Consumer
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_WmiConsumerProviderSinkLoaded class

The **MSFT\_WmiConsumerProviderSinkLoaded** event class defines the successful activation of the event consumer provider sink object.

The following syntax is simplified from Managed Object Format (MOF) code, and includes all inherited properties.

## Syntax

``` syntax
class MSFT_WmiConsumerProviderSinkLoaded : MSFT_WmiConsumerProviderEvent
{
  uint8               SECURITY_DESCRIPTOR[];
  uint64              TIME_CREATED;
  string              Namespace;
  string              ProviderName;
  string              Machine;
  __EventConsumer REF Consumer;
};
```

## Members

The **MSFT\_WmiConsumerProviderSinkLoaded** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiConsumerProviderSinkLoaded** class has these properties.

<dl> <dt>

**Consumer**
</dt> <dd> <dl> <dt>

Data type: **\_\_EventConsumer**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to an [**\_\_EventConsumer**](https://msdn.microsoft.com/library/aa394635) object.

</dd> <dt>

**Machine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the machine on which the event occurs.

This property is inherited from [**MSFT\_WmiConsumerProviderEvent**](msft-wmiconsumerproviderevent.md)

</dd> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Namespace where the consumer provider was activated.

This property is inherited from [**MSFT\_WmiProviderEvent**](msft-wmiproviderevent.md)

</dd> <dt>

**ProviderName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the consumer provider.

This property is inherited from [**MSFT\_WmiProviderEvent**](msft-wmiproviderevent.md)

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

[**MSFT\_WmiConsumerProviderEvent**](msft-wmiconsumerproviderevent.md)
</dt> <dt>

[ConsumerProvider Troubleshooting Classes](https://msdn.microsoft.com/library/aa389298)
</dt> <dt>

[WMI Troubleshooting](https://msdn.microsoft.com/library/aa394603)
</dt> <dt>

WMI Troubleshooting
</dt> <dt>

[Receiving a WMI Event](https://msdn.microsoft.com/library/aa393013)
</dt> </dl>

 

 





