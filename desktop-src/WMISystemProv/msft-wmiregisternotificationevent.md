---
title: MSFT\_WmiRegisterNotificationEvent class
description: Represents the creation of an event sink for notification for an event query.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 557a9a5e-0fc5-43fc-8467-23da9990a689
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WmiRegisterNotificationEvent class
- MSFT_WmiRegisterNotificationEvent class, described
topic_type:
- apiref
api_name:
- MSFT_WmiRegisterNotificationEvent
- MSFT_WmiRegisterNotificationEvent.SECURITY_DESCRIPTOR
- MSFT_WmiRegisterNotificationEvent.TIME_CREATED
- MSFT_WmiRegisterNotificationEvent.Namespace
- MSFT_WmiRegisterNotificationEvent.Query
- MSFT_WmiRegisterNotificationEvent.QueryLanguage
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_WmiRegisterNotificationEvent class

The **MSFT\_WmiRegisterNotificationEvent** abstract [troubleshooting class](https://msdn.microsoft.com/library/aa394604) represents the creation of an event sink for notification for an event query.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class MSFT_WmiRegisterNotificationEvent : MSFT_WmiEssEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  string Namespace;
  string Query;
  string QueryLanguage;
};
```

## Members

The **MSFT\_WmiRegisterNotificationEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiRegisterNotificationEvent** class has these properties.

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

The event query used in the call which created the sink.

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

## Examples

The following VBScript code example receives notifications when a sink is created by a call to [**SWbemServices.ExecNotificationQueryAsync**](https://msdn.microsoft.com/library/aa393865) and when the sink is canceled. It can also receive notifications from calls in C++ like, [**IWbemServices::ExecNotificationQueryAsync**](https://msdn.microsoft.com/library/aa392106) or [**IWbemServices::CancelAsyncCall**](https://msdn.microsoft.com/library/aa392094).


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\CIMV2") 
Set MySink = WScript.CreateObject( _
    "WbemScripting.SWbemSink","SINK_")

objWMIservice.ExecNotificationQueryAsync MySink, "SELECT * FROM MSFT_WmiRegisterNotificationSink WITHIN 10"

objWMIservice.ExecNotificationQueryAsync MySink, "SELECT * FROM MSFT_WmiCancelNotificationSink WITHIN 10"

WScript.Echo "Waiting for events..."

While (True)
    Wscript.Sleep(1000)
Wend

Sub SINK_OnObjectReady(objObject, objAsyncContext)
    WScript.Echo "Event has occurred: Event class is " & objObject.Path_.Class & VBNewLine & objObject.Query
 
End Sub

Sub SINK_OnCompleted(objObject, objAsyncContext)
    WScript.Echo "Event call complete."
End Sub
```



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
</dt> </dl>

 

 





