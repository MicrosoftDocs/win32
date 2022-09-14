---
description: System administrators can use WMI to monitor events on a network.
ms.assetid: 871d4add-a7b1-4ec9-a202-3821fdf09e9f
ms.tgt_platform: multiple
title: Monitoring Events
ms.topic: article
ms.date: 05/31/2018
---

# Monitoring Events

System administrators can use WMI to monitor events on a network. For example:

-   A service stops unexpectedly.
-   A server becomes unavailable.
-   A disk drive fills to 80% capacity.
-   Security events are reported to an NT Event Log.

WMI supports event detection and delivery to event consumers because some WMI providers are event providers. For more information, see [Receiving a WMI Event](receiving-a-wmi-event.md).

[*Event consumers*](gloss-e.md) are applications or scripts that request notification of events, and then perform tasks when specific events occur. You can create event monitoring scripts or applications that temporarily monitor when events occur. WMI also supplies a set of preinstalled permanent event providers and the permanent consumer classes that enable you to permanently monitor events. For more information, see [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).

The following sections are discussed in this topic:

-   [Using Temporary Event Consumers](#using-temporary-event-consumers)
-   [Using Permanent Event Consumers](#using-permanent-event-consumers)

## Using Temporary Event Consumers

Temporary event consumers are scripts or applications that return the events that match an event query or filter. Temporary event queries usually use either [**IWbemServices::ExecNotificationQuery**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationquery) in C++ applications or [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md) in scripts and Visual Basic.

An event query requests instances of an event class that specifies a certain type of event, such as [**Win32\_ProcessTrace**](/previous-versions/windows/desktop/krnlprov/win32-processtrace) or [**RegistryKeyChangeEvent**](/previous-versions/windows/desktop/regprov/registrykeychangeevent).

The following VBScript code example requests notification when an instance of [**Win32\_ProcessTrace**](/previous-versions/windows/desktop/krnlprov/win32-processtrace) is created. An instance of this class is generated when a process is started or stopped.

To execute the script, copy it to a file named event.vbs and use the following command line: **cscript event.vbs**. You can see output from the script by starting Notepad.exe or any other process. The script stops after five processes have started or stopped.

This script calls [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md), which is the [*semisynchronous*](gloss-s.md) version of the method. See the next script for an example of setting up an asynchronous temporary event subscription by calling [**SWbemServices.ExecNotificationQueryAsync**](swbemservices-execnotificationqueryasync.md). For more information, see [Calling a Method](calling-a-method.md). The script calls [**SWbemEventSource.NextEvent**](swbemeventsource-nextevent.md) to obtain and process each event as it arrives. Save the script in a file with a .vbs extension and run the script on a command line using CScript: **cscript file.vbs**.


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:\\" _
    & strComputer & "\root\CIMV2") 
Set objEvents = objWMIService.ExecNotificationQuery _
    ("SELECT * FROM Win32_ProcessTrace")

Wscript.Echo "Waiting for events ..."
i = 0
Do Until i=5
    Set objReceivedEvent = objEvents.NextEvent
    'report an event
    Wscript.Echo "Win32_ProcessTrace event occurred" & VBNewLine _
        & "Process Name = " _
            & objReceivedEvent.ProcessName & VBNewLine _
        & "Process ID = " _
            & objReceivedEvent.Processid & VBNewLine _
        & "Session ID = " & objReceivedEvent.SessionID 
i = i+ 1
Loop
```



Temporary event consumers must be started manually and must not persist across WMI restarts or operating system restarts. A temporary event consumer can process events only while it is running.

The following procedure describes how to create a temporary event consumer.

**To create a temporary event consumer**

1.  Decide which programming language to use.

    The programming language determines the API to use.

    -   For the C++ programming language, use the [COM API for WMI](com-api-for-wmi.md).
    -   For Visual Basic or scripting languages, use the [Scripting API for WMI](scripting-api-for-wmi.md).

2.  Start coding a temporary event consumer application the same way that you start a WMI application.

    The first steps of coding depend on the programming language. Typically, you log onto WMI and set up the security settings. For more information, see [Creating a WMI Application or Script](creating-a-wmi-application-or-script.md).

3.  Define the event query that you want to use.

    To obtain some types of performance data, you may need to use classes provided by high-performance providers. For more information, see [Monitoring Performance Data](monitoring-performance-data.md), [Determining the Type of Event To Receive](determining-the-type-of-event-to-receive.md), and [Querying with WQL](querying-with-wql.md).

4.  Decide to make either an asynchronous call or an semisynchronous call, and choose the API method.

    Asynchronous calls allow you to avoid the overhead of polling for data. However, semisynchronous calls provide similar performance with greater security. For more information, see [Calling a Method](calling-a-method.md).

5.  Make the asynchronous or semisynchronous method call and include an event query as the *strQuery* parameter.

    For C++ applications, call the following methods:

    -   [**IWbemServices::ExecNotificationQuery**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationquery)
    -   [**IWbemServices::ExecNotificationQueryAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationqueryasync)

    For scripts, call the following methods:

    -   [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md)
    -   [**SWbemServices.ExecNotificationQueryAsync**](swbemservices-execnotificationqueryasync.md)

6.  Write the code to process the returned event object.

    For asynchronous event queries, put the code in the various methods or events of the object sink. For semisynchronous event queries, each object is returned as WMI obtains it, so the code should be in the loop that handles each object.

The following script code example is an asynchronous version of the [**Win32\_ProcessTrace**](/previous-versions/windows/desktop/krnlprov/win32-processtrace) script. Because asynchronous operations return immediately, a dialog box keeps the script active while it is waiting for events.

Rather than call [**SWbemEventSource.NextEvent**](swbemeventsource-nextevent.md) to receive each event, the script has an event handler for the [**SWbemSink OnObjectReady**](swbemsink-onobjectready.md) event.


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:\\" & _
    strComputer & "\root\CIMV2") 
Set EventSink = WScript.CreateObject( _
    "WbemScripting.SWbemSink","SINK_")

objWMIservice.ExecNotificationQueryAsync EventSink, _
    "SELECT * FROM Win32_ProcessTrace WITHIN 10"
WScript.Echo "Waiting for events..."

i = 0
While (True)
    Wscript.Sleep(1000)
Wend

Sub SINK_OnObjectReady(objObject, objAsyncContext)
    Wscript.Echo "Win32_ProcessTrace event has occurred."
    i = i+1
    If i = 3 Then WScript.Quit 0 
End Sub

```



> [!Note]
>
> An asynchronous callback such as a callback handled by the `SINK_OnObjectReady` subroutine, allows a nonauthenticated user to provide data to the sink. For better security, use either semisynchronous communication or synchronous communication. For more information, see the following topics:
>
> -   [Making a Semisynchronous Call with C++](making-a-semisynchronous-call-with-c--.md)
> -   [Making a Semisynchronous Call with VBScript](making-a-semisynchronous-call-with-vbscript.md)
> -   [Making an Asynchronous Call with C++](making-an-asynchronous-call-with-c--.md)
> -   [Making an Asynchronous Call with VBScript](making-an-asynchronous-call-with-vbscript.md)
> -   [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md)
> -   [Securing Scripting Clients](securing-scripting-clients.md)

 

## Using Permanent Event Consumers

A permanent event consumer runs until its registration is explicitly canceled, and then starts up when WMI or the system restarts.

A permanent event consumer is a combination of WMI classes, filters, and COM objects on a system.

The following list identifies the parts required to create a permanent event consumer:

-   A COM object containing the code that implements the permanent consumer.
-   A new permanent consumer class.
-   An instance of the permanent consumer class.
-   A filter that contains the query for events.
-   A link between the consumer and the filter.

For more information, see [Receiving Events At All Times](--filtertoconsumerbinding.md).

WMI supplies several permanent consumers. The consumer classes and COM object containing the code are preinstalled. For example, you can create and configure an instance of the [**ActiveScriptEventConsumer**](activescripteventconsumer.md) class to run a script when an event occurs. For more information, see [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md). For an example of using **ActiveScriptEventConsumer**, see [Running a Script Based on an Event](running-a-script-based-on-an-event.md).

The following procedure describes how to create a permanent event consumer.

**To create a permanent event consumer**

1.  [Register the event provider](registering-a-provider.md) with the namespace that you are using.

    Some event providers can only use a specific namespace. For example, [**\_\_InstanceCreationEvent**](--instancecreationevent.md) is an intrinsic event that is supported by the [Win32 provider](/windows/desktop/CIMWin32Prov/win32-provider) and is registered by default with the \\root\\cimv2 namespace.

    > [!Note]  
    > You can use the **EventNamespace** property of the [**\_\_EventFilter**](--eventfilter.md) used in the registration to create a cross-namespace subscription. For more information, see [Implementing Cross-Namespace Permanent Event Subscriptions](implementing-cross-namespace-permanent-event-subscriptions.md).

     

2.  [Register the event consumer provider](registering-an-event-consumer-provider.md) with the namespace where event classes are located.

    WMI uses an event consumer provider to find an event consumer that is permanent. The permanent event consumer is the application that WMI starts when an event is received. To register event consumer, providers create instances of [**\_\_EventConsumerProviderRegistration**](--eventconsumerproviderregistration.md).

3.  Create an instance of the class that represents the permanent event consumer you want to use.

    Event consumer classes are derived from the class [**\_\_EventConsumer**](--eventconsumer.md). Set the properties that the event consumer instance requires.

4.  Register the consumer with COM by using the **regsvr32** utility.
5.  Create an instance of the event filter class [**\_\_EventFilter**](--eventfilter.md).

    Set the required fields for the event filter instance. The required fields for [**\_\_EventFilter**](--eventfilter.md) are **Name**, **QueryLanguage**, and **Query**. The **Name** property can be any unique name for an instance of this class. The **QueryLanguage** property is always set to "WQL". The **Query** property is a string that contains an event query. An event is generated when a permanent event consumer's query fails. The event's source is WinMgmt, the event ID is 10, and the event type is Error.

6.  Create an instance of the [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md) class to associate a logical event consumer with an event filter.

    WMI uses an association to find the event consumer associated with the event that matches the criteria specified in the event filter. WMI uses the event consumer provider to find the permanent event consumer application to start.

 

 
