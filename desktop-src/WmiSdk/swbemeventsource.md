---
description: The SWbemEventSource object retrieves events from an event query in conjunction with SWbemServices.ExecNotificationQuery.
ms.assetid: 7efd5e6a-4311-4d20-8b05-e9208eec098a
ms.tgt_platform: multiple
title: SWbemEventSource object (Wbemdisp.h)
ms.topic: reference
ms.date: 09/25/2020
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemEventSource
- ISWbemEventSource
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemEventSource object

The **SWbemEventSource** object retrieves events from an event query in conjunction with [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md). You get an **SWbemEventSource** object if you make a call to **SWbemServices.ExecNotificationQuery** to make an event query. You can then use the [**NextEvent**](swbemeventsource-nextevent.md) method to retrieve events as they arrive. This object cannot be created by the VBScript [CreateObject](/previous-versions//xzysf6hc(v=vs.85)) call.

## Members

The **SWbemEventSource** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SWbemEventSource** object has these methods.



| Method                                          | Description                                                                                                                                  |
|:------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| [**NextEvent**](swbemeventsource-nextevent.md) | Used to retrieve an event in conjunction with [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md).<br/> |



 

### Properties

The **SWbemEventSource** object has these properties.



| Property                                                    | Access type          | Description                                              |
|:------------------------------------------------------------|:---------------------|:---------------------------------------------------------|
| [**Security\_**](swbemeventsource-security-.md)<br/> | Read-only<br/> | Used to read or change the security settings.<br/> |



 

## Examples

This script uses the methods of the **SWbemEventSource** class and the [**SWbemServices**](swbemservices.md) class in conjunction with a WQL query for application events. For more information about WMI event notification and queries see [Monitoring Events](monitoring-events.md), [Running a Script Based on an Event](running-a-script-based-on-an-event.md), and [Receiving Asynchronous Event Notifications](receiving-asynchronous-event-notifications.md).


```VB
' Connect to WMI, obtaining an SWbemServices object
set svc = _
CreateObject("Wbemscripting.SWbemLocator")._
   ConnectServer(,"root\cimv2")

' Obtain an SWbemEventSource object from the 
' SWbemServices.ExecNotificationQuery method to specify the 
' event source as "Application" events in a Win32_NTLogEvent
set evtsrc = svc.ExecNotificationQuery("SELECT * " _
   & "FROM __InstanceCreationEvent " _
   & "WHERE TargetInstance ISA 'Win32_NTLogEvent'" _
   & "AND TargetInstance.Logfile ='Application'")

' Wait for an event by executing the NextEvent method on the 
' SWbemEventSource object.
while (num < 5)
    set inst = evtsrc.NextEvent(-1)
    Wscript.echo inst.TargetInstance.Logfile
    num = num + 1
wend
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemEventSource<br/>                                                      |
| IID<br/>                      | IID\_ISWbemEventSource<br/>                                                       |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

