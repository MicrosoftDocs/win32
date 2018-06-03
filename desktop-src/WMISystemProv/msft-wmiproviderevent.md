---
title: MSFT\_WmiProviderEvent class
description: The parent class for all consumer provider events.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3b549d65-5430-498b-900f-de28549667fb
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WmiProviderEvent class
- MSFT_WmiProviderEvent class, described
topic_type:
- apiref
api_name:
- MSFT_WmiProviderEvent
- MSFT_WmiProviderEvent.SECURITY_DESCRIPTOR
- MSFT_WmiProviderEvent.TIME_CREATED
- MSFT_WmiProviderEvent.Namespace
- MSFT_WmiProviderEvent.ProviderName
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_WmiProviderEvent class

The **MSFT\_WmiProviderEvent** class is the parent class for all consumer provider events. The **MSFT\_WmiProviderEvent** is only found in the root\\cimv2 namespace.

The following syntax is simplified from Managed Object format (MOF) code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_WmiProviderEvent : MSFT_WmiEssEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  string Namespace;
  string ProviderName;
};
```

## Members

The **MSFT\_WmiProviderEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiProviderEvent** class has these properties.

<dl> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Namespace where the consumer provider was activated.

</dd> <dt>

**ProviderName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the consumer provider.

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

[**MSFT\_WmiEssEvent**](msft-wmiessevent.md)
</dt> <dt>

[ConsumerProvider Troubleshooting Classes](https://msdn.microsoft.com/library/aa389298)
</dt> <dt>

[WMI Troubleshooting](https://msdn.microsoft.com/library/aa394603)
</dt> <dt>

WMI Troubleshooting
</dt> <dt>

[Receiving a WMI Event](https://msdn.microsoft.com/library/aa393013)
</dt> </dl>

 

 





