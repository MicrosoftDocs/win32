---
title: MSFT\_WmiCancelNotificationSink class
description: Generated when an event sink is canceled.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c8dffdab-0ec9-4579-bb99-aec4a3c7a2a4'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_WmiCancelNotificationSink class", "MSFT_WmiCancelNotificationSink class, described"]
topic_type:
- apiref
api_name:
- MSFT_WmiCancelNotificationSink
- MSFT_WmiCancelNotificationSink.SECURITY_DESCRIPTOR
- MSFT_WmiCancelNotificationSink.TIME_CREATED
- MSFT_WmiCancelNotificationSink.Namespace
- MSFT_WmiCancelNotificationSink.Query
- MSFT_WmiCancelNotificationSink.QueryLanguage
- MSFT_WmiCancelNotificationSink.Sink
- MSFT_WmiCancelNotificationSink.UserSID
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
---

# MSFT\_WmiCancelNotificationSink class

An instance of the abstract **MSFT\_WmiCancelNotificationSink** class is generated when an event sink is canceled.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class MSFT_WmiCancelNotificationSink : MSFT_WmiEssEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  string Namespace;
  string Query;
  string QueryLanguage;
  uint64 Sink;
  string UserSID[];
};
```

## Members

The **MSFT\_WmiCancelNotificationSink** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiCancelNotificationSink** class has these properties.

<dl> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Namespace in which the event occurred.

</dd> <dt>

**Query**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The event query asynchronous call which created the sink.

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

**Sink**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Pointer to the sink that is canceled.

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

**UserSID**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

SID of the user for whom this startup command runs. The **User** property can be empty but the **UserSID** can still have a value if the user name cannot be resolved, for example, the case of a deleted user. This property allows distinguishing between commands associated with two different users with unresolved names. The value of **UserSID** may be **NULL** when not actually associated with a user. For example, a startup command may exist for "All Users".

Example: "S-1-5-21-1579938362-1064596589-3161144252-1006"

</dd> </dl>

## Examples

For an example, see [**MSFT\_WmiRegisterNotificationEvent**](msft-wmiregisternotificationevent.md).

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

[**MSFT\_WmiEssEvent**](msft-wmiessevent.md)
</dt> <dt>

[WMI Service Event Troubleshooting Classes](https://msdn.microsoft.com/library/aa394578)
</dt> <dt>

[WMI Troubleshooting](https://msdn.microsoft.com/library/aa394603)
</dt> <dt>

WMI Troubleshooting
</dt> <dt>

[Monitoring Events](https://msdn.microsoft.com/library/aa392396)
</dt> </dl>

 

 





