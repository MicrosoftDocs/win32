---
title: MSFT\_WmiFilterActivated class
description: Defines the successful activation of a permanent event consumer subscription filter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '33022999-1534-4ac2-a3f3-90085153be49'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_WmiFilterActivated class", "MSFT_WmiFilterActivated class, described"]
topic_type:
- apiref
api_name:
- MSFT_WmiFilterActivated
- MSFT_WmiFilterActivated.SECURITY_DESCRIPTOR
- MSFT_WmiFilterActivated.TIME_CREATED
- MSFT_WmiFilterActivated.QueryLanguage
- MSFT_WmiFilterActivated.Name
- MSFT_WmiFilterActivated.Namespace
- MSFT_WmiFilterActivated.Query
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
---

# MSFT\_WmiFilterActivated class

The **MSFT\_WmiFilterActivated** event class defines the successful activation of a permanent event consumer subscription filter.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class MSFT_WmiFilterActivated : MSFT_WmiFilterEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  string QueryLanguage;
  string Name;
  string Namespace;
  string Query;
};
```

## Members

The **MSFT\_WmiFilterActivated** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiFilterActivated** class has these properties.

<dl> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the filter instance.

This property is inherited from [**MSFT\_WmiFilterEvent**](msft-wmifilterevent.md)

</dd> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Namespace of the filter subscription.

This property is inherited from [**MSFT\_WmiFilterEvent**](msft-wmifilterevent.md)

</dd> <dt>

**Query**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Event query for the subscription filter.

This property is inherited from [**MSFT\_WmiFilterEvent**](msft-wmifilterevent.md)

</dd> <dt>

**QueryLanguage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Query language used in the **Query** property. Currently only WMI Query Language (WQL) is supported.

Example: "WQL"

This property is inherited from [**MSFT\_WmiFilterEvent**](msft-wmifilterevent.md).

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
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>System.mof</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>WmiPrvSD.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WmiFilterEvent**](msft-wmifilterevent.md)
</dt> <dt>

[WMI Service Event Troubleshooting Classes](https://msdn.microsoft.com/library/aa394578)
</dt> <dt>

[WMI Troubleshooting](https://msdn.microsoft.com/library/aa394603)
</dt> <dt>

WMI Troubleshooting
</dt> <dt>

[Monitoring Events](https://msdn.microsoft.com/library/aa392396)
</dt> </dl>

 

 





