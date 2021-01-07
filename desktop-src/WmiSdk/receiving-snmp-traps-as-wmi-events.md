---
description: WMI automatically maps SNMP traps to WMI events. The system places the data contained in the trap in the corresponding properties of a WMI event instance for access by the WMI host machine.
ms.assetid: 549f58a9-9d3b-41b9-a374-ab83877f63a7
ms.tgt_platform: multiple
title: Receiving SNMP Traps as WMI Events
ms.topic: article
ms.date: 05/31/2018
---

# Receiving SNMP Traps as WMI Events

WMI automatically maps SNMP traps to WMI events. The system places the data contained in the trap in the corresponding properties of a WMI event instance for access by the WMI host machine.

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

Receiving an SNMP trap is nearly identical to receiving events from any other WMI provider. However, the SNMP event filter has several unique classes to be aware of before registering for events. Also, the event provider requires the use of the \\smir namespace exclusively.

The most common classes to register with are [SnmpNotification](snmpnotification.md) and [SnmpExtendedNotification](snmpextendednotification.md). Consumers intent on using event notifications to update values in monitored SNMP devices must register for SnmpExtendedNotification events. The information from SnmpNotification events is not reusable.

The following table lists information about setting up your computer to receive SNMP traps as WMI events.



| Task                                                                               | Description                                                                        |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [Choosing Between SNMP Event Providers](choosing-between-snmp-event-providers.md) | WMI includes two SNMP event providers.                                             |
| [Receiving SNMP Events](receiving-snmp-events.md)                                 | SNMP event providers support three types of SNMPv1 traps and SNMPv2 notifications. |



 

The following example sets up a computer to monitor for the **SnmpLinkUpNotification** event from a managed hub.


```VB
Set objLocator = CreateObject("wbemscripting.swbemlocator")
Set objServices = objLocator.ConnectServer(, "root\snmp\mngd_hub")

set objwbemEventsource = _ 
    objServices.ExecNotificationQuery _
   ("SELECT * FROM SnmpLinkUpNotification")

set objWbemObject = objwbemEventsource.NextEvent()

wscript.echo "Received " & objWbemObject.path_.class

for each prop in objWbemObject.properties_
    wscript.echo prop.name & " -- " & prop.value
next
```



 

 



