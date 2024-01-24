---
description: Use SWbemServices.ExecQuery to request all existing events.
ms.assetid: bc99719a-7e33-4e2d-8355-f8fc97c66f71
ms.tgt_platform: multiple
title: Receiving Synchronous and Semisynchronous Event Notifications
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Synchronous and Semisynchronous Event Notifications

Use [**SWbemServices.ExecQuery**](swbemservices-execquery.md) to request all existing events.

The following code example shows how to query for the events in a log.

`Select * from Win32_NTLogEvent`

For more information, see [Determining the Type of Event to Receive](determining-the-type-of-event-to-receive.md), [Receiving Event Notifications](receiving-event-notifications.md), and [WQL (SQL for WMI)](wql-sql-for-wmi.md).

The default call to [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md) uses semisynchronous communication. The *iflags* parameter has the **wbemFlagForwardOnly** and **wbemFlagReturnImmediately** flags set by default. For more information, see [Calling a Method](calling-a-method.md).

The following procedure describes how to receive semisynchronous event notification using VBScript.

**To receive semisynchronous event notification in VBScript**

1.  Create a query for the type of event that you want to receive. For more information, see [Determining the Type of Event to Receive](determining-the-type-of-event-to-receive.md).

2.  If you request an instance type of event such as [**\_\_InstanceCreationEvent**](--instancecreationevent.md), indicate in the query a type of target instance, for example, [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk).

3.  If necessary, specify an instance, for example, the name of a namespace when requesting future [**\_\_NamespaceModificationEvent**](--namespacemodificationevent.md) instances for a specific namespace.

4.  Specify a polling interval for Windows Management Instrumentation (WMI) in a query, such as "WITHIN 10"—to poll every 10 seconds. For more information, see [WITHIN Clause](within-clause.md).

5.  Call [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md) using the query.

6.  Loop through the collection you receive.

The following example shows how to monitor insertion and removal of disks from a floppy disk drive on a local machine. The script requests \_[**\_\_InstanceModificationEvent**](--instancemodificationevent.md) instances for the floppy drive [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) instance and polls every 10 seconds for new instances. This script is an example of a temporary event consumer, and continues running until it is stopped in Task Manager or the system is rebooted. For more information, see [Receiving Events for the Duration of your Application](receiving-events-for-the-duration-of-your-application.md).


```VB
Const FLOPPY_DISK = 2
Set colMonitoredDisks = GetObject("Winmgmts:").ExecNotificationQuery _
    ("Select * from __InstanceModificationEvent within 10 WHERE " _
        & "TargetInstance ISA 'Win32_LogicalDisk'")
i = 0
Do While i = 0
    Set strDiskChange = colMonitoredDisks.NextEvent
    If strDiskChange.TargetInstance.DriveType = FLOPPY_DISK Then
        If strDiskChange.TargetInstance.Size > 0 Then
            Wscript.Echo "A disk has been inserted" & _
                " into the floppy drive."
    Else
            Wscript.Echo "A disk has been removed" & _
                " from the floppy drive."
        End If
    End If
Loop
```



The following procedure describes how to receive semisynchronous event notification using C++.

**To receive semisynchronous event notification in C++**

1.  Set up the application with calls to the [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) and [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) functions.

    Because WMI is COM based, calling [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) and [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) is a required step for a WMI application. For more information, see [Creating a WMI Application or Script](creating-a-wmi-application-or-script.md).

2.  Determine the kind of events that you want to receive.

    WMI supports intrinsic and extrinsic events. An intrinsic event is an event predefined by WMI. An extrinsic event is an event defined by a third party provider. For more information, see [Determining the Type of Event to Receive](determining-the-type-of-event-to-receive.md).

3.  Register to receive a specific class of events with a call to the [**IWbemServices::ExecNotificationQuery**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationquery) method.

    Make each query very specific. The goal of registration is to register to receive only the required notifications. Notifications that are not required waste processing and delivery time.

    You can design an event consumer to receive multiple events. For example, a consumer might require notification of instance modification events for a specific class of device and security violation events. In this case, the tasks a consumer performs when receiving an instance modification event are different for the two events. Thus, the consumer should make one call to [**IWbemServices::ExecNotificationQuery**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationquery) to register for instance modification events, and another call to **ExecNotificationQuery** to register for security violation events.

    In the call to [**ExecNotificationQuery**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationquery), set the *lFlags* parameter to **WBEM\_FLAG\_RETURN\_IMMEDIATELY** and **WBEM\_FLAG\_FORWARD\_ONLY**. The **WBEM\_FLAG\_RETURN\_IMMEDIATELY** flag requests semisynchronous processing, and the **WBEM\_FLAG\_FORWARD\_ONLY** flag requests a forward-only enumerator. For more information, see [Calling a Method](calling-a-method.md). The **ExecNotificationQuery** function returns a pointer to an [**IEnumWbemClassObject**](/windows/desktop/api/Wbemcli/nn-wbemcli-ienumwbemclassobject) interface.

4.  Poll for registered event notifications by making repeated calls to the [**IEnumWbemClassObject::Next**](/windows/desktop/api/Wbemcli/nf-wbemcli-ienumwbemclassobject-next) method.
5.  When finished, release the enumerator that points to the [**IEnumWbemClassObject**](/windows/desktop/api/Wbemcli/nn-wbemcli-ienumwbemclassobject) object.

    You can release the [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) pointer associated with the registration. Releasing the **IWbemServices** pointer causes WMI to stop delivering events to all associated temporary consumers.

 

 
