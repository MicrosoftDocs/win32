---
Description: WMI contains an event infrastructure that produces notifications about changes in WMI data and services. WMI event classes provide notification when specific events occur.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 347808a7-0f7b-4687-93f4-bea55c96795a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Receiving a WMI Event
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Receiving a WMI Event

WMI contains an event infrastructure that produces notifications about changes in WMI data and services. WMI [*event classes*](gloss-e.md#wmi-gloss-event-class) provide notification when specific events occur.

The following sections are discussed in this topic:

-   [Event Queries](#event-queries)
-   [Example](#example)
-   [Event Consumers](#event-consumers)
-   [Providing Events](#providing-events)
-   [Subscription Quotas](#subscription-quotas)
-   [Related topics](#related-topics)

## Event Queries

You can create a [semisynchronous](receiving-synchronous-and-semisynchronous-event-notifications.md) or [**asynchronous**](receiving-asynchronous-event-notifications.md) query to monitor changes to event logs, process creation, service status, computer availability or disk drive free space, and other entities or events. In scripting, the [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md) method is used to subscribe to events. In C++, [**IWbemServices::ExecNotificationQuery**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationquery) is used. For more information, see [Calling a Method](calling-a-method.md).

Notification of a change in the standard WMI data model is called an [*intrinsic event*](gloss-i.md#wmi-gloss-intrinsic-event). [**\_\_InstanceCreationEvent**](--instancecreationevent.md) or [**\_\_NamespaceDeletionEvent**](--namespacedeletionevent.md) are examples of intrinsic events. Notification of a change that a provider makes to define a provider event is called an [*extrinsic event*](gloss-e.md#wmi-gloss-extrinsic-event). For example, the [System Registry Provider](https://msdn.microsoft.com/library/aa393886), [Power Management Event Provider](https://msdn.microsoft.com/library/aa392747), and [Win32 Provider](https://msdn.microsoft.com/library/aa394388) define their own events. For more information, see [Determining the Type of Event to Receive](determining-the-type-of-event-to-receive.md).

## Example

The following script code example is a query for the intrinsic [**\_\_InstanceCreationEvent**](--instancecreationevent.md) of the event class [**Win32\_NTLogEvent**](https://msdn.microsoft.com/library/aa394226). You can run this program in the background and when there is an event, a message appears. If you close the **Waiting for events** dialog box, the program stops waiting for events. Be aware that the **SeSecurityPrivilege** must be enabled.


```VB
Sub SINK_OnObjectReady(objObject, objAsyncContext)
    WScript.Echo (objObject.TargetInstance.Message)
End Sub

Set objWMIServices = GetObject( _
    "WinMgmts:{impersonationLevel=impersonate, (security)}") 

' Create the event sink object that receives the events
Set sink = WScript.CreateObject("WbemScripting.SWbemSink","SINK_")
 
' Set up the event selection. SINK_OnObjectReady is called when
' a Win32_NTLogEvent event occurs
objWMIServices.ExecNotificationQueryAsync sink,"SELECT * FROM __InstanceCreationEvent " & "WHERE TargetInstance ISA 'Win32_NTLogEvent' "

WScript.Echo "Waiting for events"
```

<span codelanguage="PowerShell"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PowerShell</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code> # Define event Query
$query = &quot;SELECT * FROM __InstanceCreationEvent 
          WHERE TargetInstance ISA &#39;Win32_NTLogEvent&#39; &quot;

# Register for event - also specify an action that
# displays the log event when the event fires.
Register-WmiEvent -Source Demo1 -Query $query -Action {
                Write-Host &quot;Log Event occured&quot;
                $global:myevent = $event
                Write-Host &quot;EVENT MESSAGE&quot;
                Write-Host $event.SourceEventArgs.NewEvent.TargetInstance.Message}
# So wait
&quot;Waiting for events&quot;</code></pre></td>
</tr>
</tbody>
</table>



The following VBScript code example shows the extrinsic event [\_\_RegistryValueChangeEvent](registering-for-system-registry-events.md) that the registry provider defines. The script creates a temporary consumer by using the call to [**SWbemServices.ExecNotificationQueryAsync**](swbemservices-execnotificationqueryasync.md), and only receives events when the script is running. The following script runs indefinitely until the computer is rebooted, WMI is stopped, or the script is stopped. To stop the script manually, use Task Manager to stop the process. To stop it programmatically, use the [**Terminate**](https://msdn.microsoft.com/library/aa393907) method in the Win32\_Process class. For more information, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md).


```VB
strComputer = "."

Set objWMIServices=GetObject( _
    "winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\default")

set objSink = WScript.CreateObject("WbemScripting.SWbemSink","SINK_")


objWMIServices.ExecNotificationQueryAsync objSink, _
    "Select * from RegistryValueChangeEvent Where Hive = 'HKEY_LOCAL_MACHINE' and KeyPath = 'SYSTEM\\ControlSet001\\Control' and ValueName = 'CurrentUser'"

WScript.Echo "Waiting for events..."

While (True) 
     WScript.Sleep (1000)
Wend

 
WScript.Echo "Listening for Registry Change Events..." & vbCrLf 

While(True) 
    WScript.Sleep 1000 
Wend 

Sub SINK_OnObjectReady(wmiObject, wmiAsyncContext) 
    WScript.Echo "Received Registry Value Change Event" & vbCrLf & wmiObject.GetObjectText_() 
End Sub
```



## Event Consumers

You can monitor or consume events using the following consumers while a script or application is running:

-   Temporary event consumers

    A [*temporary consumer*](gloss-t.md#wmi-gloss-temporary-consumer) is a WMI client application that receives a WMI event. WMI includes a unique interface that use to specify the events for WMI to send to a client application. A temporary event consumer is considered temporary because it only works when specifically loaded by a user. For more information, see [Receiving Events for the Duration of Your Application](receiving-events-for-the-duration-of-your-application.md).

-   Permanent event consumers

    A [*permanent consumer*](gloss-p.md#wmi-gloss-permanent-consumer) is a COM object that can receive a WMI event at all times. A permanent event consumer uses a set of persistent objects and filters to capture a WMI event. Like a temporary event consumer, you set up a series of WMI objects and filters that capture a WMI event. When an event occurs that matches a filter, WMI loads the permanent event consumer and notifies it about the event. Because a permanent consumer is implemented in the WMI repository and is an executable file that is registered in WMI, the permanent event consumer operates and receives events after it is created and even after a reboot of the operating system as long as WMI is running. For more information, see [Receiving Events at All Times](receiving-events-at-all-times.md).

Scripts or applications that receive events have special security considerations. For more information, see [Securing WMI Events](securing-wmi-events.md).

An application or script can use a built-in WMI event provider that supplies [standard consumer classes](standard-consumer-classes.md). Each standard consumer class responds to an event with a different action by sending an email message or executing a script. You do not have to write provider code to use a standard consumer class to create a permanent event consumer. For more information, see [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).

## Providing Events

An event provider is a COM component that sends an event to WMI. You can create an event provider to send an event in a C++ or C# application. Most event providers manage an object for WMI, for example, an application or hardware item. For more information, see [Writing an Event Provider](writing-an-event-provider.md).

A timed or repeating event is an event that occurs at a predetermined time.

WMI provides the following ways to create timed or repeating events for your applications:

-   The standard Microsoft event infrastructure.
-   A specialized timer class.

For more information, see [Receiving a Timed or Repeating Event](receiving-a-timed-or-repeating-event.md). When you write an event provider, consider the security information identified in [Providing Events Securely](providing-events-securely.md).

It is recommended that permanent event subscriptions be compiled into the \\root\\subscription namespace. For more information, see [Implementing Cross-Namespace Permanent Event Subscriptions](implementing-cross-namespace-permanent-event-subscriptions.md).

## Subscription Quotas

Polling for events can degrade performance for providers that support queries over huge data sets. Additionally, any user that has read access to a namespace with dynamic providers can perform a denial of service (DoS) attack. WMI maintains quotas for all of the users combined and for each event consumer in the single instance of [**\_\_ArbitratorConfiguration**](--arbitratorconfiguration.md) located in the \\root namespace. These quotas are global rather than for each namespace. You cannot change the quotas.

WMI currently enforces quotas using the properties of [**\_\_ArbitratorConfiguration**](--arbitratorconfiguration.md). Each quota has a per user and a total version that includes all users combined, not per namespace. The following table lists the quotas that apply to the **\_\_ArbitratorConfiguration** properties.



| Total/PerUser                                                                   | Quota                                                                       |
|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| TemporarySubscriptionsTotal<br/> TemporarySubscriptionsPerUser<br/> | 10,000<br/> 1,000<br/>                                          |
| PermanentSubscriptionsTotal<br/> PermanentSubscriptionsPerUser<br/> | 10,000<br/> 1,000<br/>                                          |
| PollingInstructionsTotal<br/> PollingInstructionsPerUser<br/>       | 10,000<br/> 1,000<br/>                                          |
| PollingMemoryTotal<br/> PollingMemoryPerUser<br/>                   | 10,000,000 (0x989680) bytes<br/> 5,000,000 (0x4CB40) bytes<br/> |



 

An administrator or a user with **FULL\_WRITE** permission in the namespace can modify the singleton instance of [**\_\_ArbitratorConfiguration**](--arbitratorconfiguration.md). WMI tracks the per-user quota.

## Related topics

<dl> <dt>

[Using WMI](using-wmi.md)
</dt> </dl>

 

 




