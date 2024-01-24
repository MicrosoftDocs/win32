---
description: SNMP event providers receive SNMP event packets from the WINSNMP stack and translate the information included in the packets into WMI events.
ms.assetid: 4ae0a734-39b0-4418-b55c-6d8f093806a8
ms.tgt_platform: multiple
title: Choosing Between SNMP Event Providers
ms.topic: article
ms.date: 05/31/2018
---

# Choosing Between SNMP Event Providers

SNMP event providers receive SNMP event packets from the WINSNMP stack and translate the information included in the packets into WMI events.

WMI includes the following two SNMP event providers:

-   SNMP Encapsulated Event provider (SEEP)

    Encapsulated provision means that the event instance has simple properties describing the information mapped directly from the SNMP trap.

-   SNMP Referent Event provider (SREP)

    Referent provision abstracts the information present within the SNMP trap so that properties which share the same class and instance are presented as embedded objects. This allows for the unique instance, with which the trap is associated, to be retrieved after the receipt of the event, using the SNMP \_\_RELPATH.

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

Regardless of whether the SNMP event is an SNMPv1 trap or an SNMPv2C notification, the stack reports it as an SNMPv2 notification. Therefore, the event providers process all SNMP events as SNMPv2 notifications.

To describe the SNMP events to WMI consumers, each event provider supports a hierarchy of classes that derives from the [**\_\_ExtrinsicEvent**](--extrinsicevent.md) system class. The [SNMPNotification](snmpnotification.md) class is the parent class for the SEEP hierarchy; the [SNMPExtendedNotification](snmpextendednotification.md) class is the parent class for the SREP hierarchy.

 

 



