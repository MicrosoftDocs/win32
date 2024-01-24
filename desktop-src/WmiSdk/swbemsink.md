---
description: The SWbemSink object is implemented by client applications to receive the results of asynchronous operations and event notifications.
ms.assetid: a90777ef-fa26-4bfb-b196-c083a0c92a29
ms.tgt_platform: multiple
title: SWbemSink object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemSink
- ISWbemSinkEvents
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemSink object

The **SWbemSink** object is implemented by client applications to receive the results of asynchronous operations and event notifications. To make an asynchronous call, you must create an instance of an **SWbemSink** object and pass it as the *ObjWbemSink* parameter. The events in your implementation of **SWbemSink** are triggered when status or results are returned, or when the call is complete. The VBScript **CreateObject** call creates this object.

## Members

The **SWbemSink** object has these types of members:

-   [Methods](#methods)

### Methods

The **SWbemSink** object has these methods.



| Method                             | Description                                                                        |
|:-----------------------------------|:-----------------------------------------------------------------------------------|
| [**Cancel**](swbemsink-cancel.md) | Cancels all asynchronous operations that are associated with this sink.<br/> |



 

## Remarks

An asynchronous callback allows a non-authenticated user to provide data to the sink. This poses security risks to your scripts and applications. To eliminate the risks, use either semisynchronous communication or synchronous communication. For more information, see [Calling a Method](calling-a-method.md).

### Events

You can implement subroutines to be called when events are triggered. For example, if you want to process each object that is returned by an asynchronous query call such as [**SWbemServices.ExecQueryAsync**](swbemservices-execqueryasync.md), create a subroutine using the sink that is specified in the asynchronous call, as shown in the following example.


```VB
Sub SinkName_OnObjectReady(objObject, objAsyncContext)
```



Use the following table as a reference to identify events and trigger descriptions.



| Event                                            | Description                                                             |
|--------------------------------------------------|-------------------------------------------------------------------------|
| [**OnCompleted**](swbemsink-oncompleted.md)     | Triggered when an asynchronous operation is complete.                   |
| [**OnObjectPut**](swbemsink-onobjectput.md)     | Triggered when an asynchronous Put operation is complete.               |
| [**OnObjectReady**](swbemsink-onobjectready.md) | Triggered when an object provided by an asynchronous call is available. |
| [**OnProgress**](swbemsink-onprogress.md)       | Triggered to provide the status of a asynchronous operation.            |



 

**Asynchronously Retrieving Event Log Statistics**

WMI supports both asynchronous and semi-synchronous scripts. When retrieving events from the event logs, asynchronous scripts often retrieve this data much faster.

In an asynchronous script, a query is issued and control is immediately returned to the script. The query continues to process on a separate thread while the script begins to immediately act on the information that is returned. Asynchronous scripts are event driven: each time an event record is retrieved, the OnObjectReady event is fired. When the query has completed, the OnCompleted event will fire, and the script can continue based on the fact that all the available records have been returned.

In a semi-synchronous script, by contrast, a query is issued and the script then queues a large amount of retrieved information before acting upon it. For many objects, semi-synchronous processing is adequate; for example, when querying a disk drive for its properties, there might be only a split second between the time the query is issued and the time the information is returned and acted upon. This is due in large part to the fact that the amount of information returned is relatively small.

When querying an event log, however, the interval between the time the query is issued and the time that a semi-synchronous script can finish returning and acting on the information can take hours. On top of that, the script might run out of memory and fail on its own before completing.

For event logs with a large number of records, the difference in processing time can be considerable. On a Windows 2000-based test computer with 2,000 records in the event log, a semi-synchronous query that retrieved all the events and displayed them in a command window took 10 minutes 45 seconds. An asynchronous query that performed the same operation took one minute 54 seconds.

## Examples

The following VBScript asynchronously queries the event logs for all records.


```VB
Const POPUP_DURATION = 10
Const OK_BUTTON = 0
Set objWSHShell = Wscript.CreateObject("Wscript.Shell")
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
 & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set objSink = WScript.CreateObject("WbemScripting.SWbemSink","SINK_")
objWMIService.InstancesOfAsync objSink, "Win32_NTLogEvent"
errReturn = objWshShell.Popup("Retrieving events", POPUP_DURATION, _
"Event Retrieval", OK_BUTTON)
Sub SINK_OnCompleted(iHResult, objErrorObject, objAsyncContext)
 WScript.Echo "Asynchronous operation is done."
End Sub
Sub SINK_OnObjectReady(objEvent, objAsyncContext)
 Wscript.Echo "Category: " & objEvent.Category
 Wscript.Echo "Computer Name: " & objEvent.ComputerName
 Wscript.Echo "Event Code: " & objEvent.EventCode
 Wscript.Echo "Message: " & objEvent.Message
 Wscript.Echo "Record Number: " & objEvent.RecordNumber
 Wscript.Echo "Source Name: " & objEvent.SourceName
 Wscript.Echo "Time Written: " & objEvent.TimeWritten
 Wscript.Echo "Event Type: " & objEvent.Type
 Wscript.Echo "User: " & objEvent.User
End Sub
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wbemdisp.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemSink<br/> CLSID\_SWbemSinkEvents<br/>                           |
| IID<br/>                      | IID\_ISWbemSink<br/> IID\_ISWbemSinkEvents<br/>                             |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 




