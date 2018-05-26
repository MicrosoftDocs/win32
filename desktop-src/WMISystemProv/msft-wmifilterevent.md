---
title: MSFT\_WmiFilterEvent class
description: The parent class for all permanent event consumer filter events.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e6410e73-59a4-4d32-bac7-cbc422ee5904
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WmiFilterEvent class
- MSFT_WmiFilterEvent class, described
topic_type:
- apiref
api_name:
- MSFT_WmiFilterEvent
- MSFT_WmiFilterEvent.SECURITY_DESCRIPTOR
- MSFT_WmiFilterEvent.TIME_CREATED
- MSFT_WmiFilterEvent.Name
- MSFT_WmiFilterEvent.Namespace
- MSFT_WmiFilterEvent.Query
- MSFT_WmiFilterEvent.QueryLanguage
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_WmiFilterEvent class

The **MSFT\_WmiFilterEvent** abstract [troubleshooting class](https://msdn.microsoft.com/library/aa394604) is the parent class for all permanent event consumer filter events.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class MSFT_WmiFilterEvent : MSFT_WmiEssEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  string Name;
  string Namespace;
  string Query;
  string QueryLanguage;
};
```

## Members

The **MSFT\_WmiFilterEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiFilterEvent** class has these properties.

<dl> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the filter instance.

</dd> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Namespace of the filter subscription.

</dd> <dt>

**Query**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Event query for the subscription filter.

</dd> <dt>

**QueryLanguage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Query language used in the **Query** property. Currently only WMI Query Language (WQL) is supported.

Example: "WQL"

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

[WMI Service Event Troubleshooting Classes](https://msdn.microsoft.com/library/aa394578)
</dt> <dt>

[WMI Troubleshooting](https://msdn.microsoft.com/library/aa394603)
</dt> <dt>

WMI Troubleshooting
</dt> <dt>

[Monitoring Events](https://msdn.microsoft.com/library/aa392396)
</dt> <dt>

[Receiving a WMI Event](https://msdn.microsoft.com/library/aa393013)
</dt> </dl>

 

 





