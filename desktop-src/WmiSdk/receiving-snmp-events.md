---
description: The SNMP event providers support SNMPv1 traps and SNMPv2 notifications.
ms.assetid: 715b2925-b01d-4631-86e3-a6239ff1dba7
ms.tgt_platform: multiple
title: Receiving SNMP Events
ms.topic: article
ms.date: 05/31/2018
---

# Receiving SNMP Events

The SNMP event providers support SNMPv1 traps and SNMPv2 notifications.

The following three types of SNMPv1 traps and SNMPv2 notifications are supported:

-   Generic

    Generic traps and notifications correspond to named events such as link up and cold start. Generic traps and notifications are represented by classes, such as **SnmpLinkUpNotification** and **SnmpWarmStartExtendedNotification**, that contain the name of the trap in the class name. These classes are subclasses of [SnmpNotification](snmpnotification.md) and [SnmpExtendedNotification](snmpextendednotification.md).

-   Enterprise-specific

    Enterprise specific traps and notifications correspond to events that are represented by a WMI class that is not a subclass of [SnmpNotification](snmpnotification.md) and [SnmpExtendedNotification](snmpextendednotification.md). To support enterprise specific traps and notifications, a consumer must define classes by compiling MIB definitions using the SNMP MIB compiler.

-   Enterprise-nonspecific

    Nonenterprise-specific traps and notifications do not correspond to any of the generic event types or enterprise-specific event types. Nonenterprise-specific traps and notifications have not had their MIB definitions compiled into the SMIR. They are represented by the [SnmpNotification](snmpnotification.md), **SnmpV2Notification**, **SnmpV1ExtendedNotification**, and **SnmpV2ExtendedNotification** classes derived from SnmpNotification and [SnmpExtendedNotification](snmpextendednotification.md).

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

The following sections are discussed in this topic:

-   [Receiving Generic SNMP Events](#receiving-generic-snmp-events)
-   [Receiving Enterprise-Specific Events](#receiving-enterprise-specific-events)
-   [Receiving Enterprise-Nonspecific Events](#receiving-enterprise-nonspecific-events)

## Receiving Generic SNMP Events

The SEEP and SREP support all types of generic SNMPv1 traps and SNMPv2 notifications. Generic SNMP events are represented by subclasses of the [SnmpNotification](snmpnotification.md) and [SnmpExtendedNotification](snmpextendednotification.md) classes.

Each event type is represented by one SEEP class and one SREP class. The SEEP classes derive from [SnmpNotification](snmpnotification.md); the SREP classes derive from [SnmpExtendedNotification](snmpextendednotification.md). The event providers require different classes because they use different mechanisms in the presentation of the SNMP event data.

The SEEP converts the SNMP event data directly to WMI class properties, whereas the SREP does not. The SREP adds a level of indirection to the interpretation required to use the WMI properties. The properties of the SREP [SnmpExtendedNotification](snmpextendednotification.md) subclasses are instances of SNMP classes; the properties of the SEEP [SnmpNotification](snmpnotification.md) subclasses are integers and strings.

The following table lists the types of generic SNMP events and the associated event classes.



| SNMP event                                    | SEEP class                                | SREP class                                        |
|-----------------------------------------------|-------------------------------------------|---------------------------------------------------|
| Authentication failure                        | **SnmpAuthenticationFailureNotification** | **SnmpAuthenticationFailureExtendedNotification** |
| Exterior Gateway Protocol (EGP) neighbor loss | **SnmpEGPNeighborLossNotification**       | **SnmpEGPNeighborLossExtendedNotification**       |
| Cold start                                    | **SnmpColdStartNotification**             | **SnmpColdStartExtendedNotification**             |
| Warm start                                    | **SnmpWarmStartNotification**             | **SnmpWarmStartExtendedNotification**             |
| Link up                                       | **SnmpLinkUpNotification**                | **SnmpLinkUpExtendedNotification**                |
| Link down                                     | **SnmpLinkDownNotification**              | **SnmpLinkDownExtendedNotification**              |



 

For example, the **SnmpLinkUpNotification** and **SnmpLinkUpExtendedNotification** classes describe the link-up event. Both classes include the **ifIndex**, **ifAdminStatus**, and **ifOperStatus** properties, but they have very different types. The properties in the **SnmpLinkUpNotification** class are of type SINT32 and STRING. The properties in the **SnmpLinkUpExtendedNotification** class are the embedded object type IETF\_SNMP\_RFC1213\_MIB\_ifTable.

## Receiving Enterprise-Specific Events

The SEEP and SREP support any enterprise-specific traps and notifications that you have compiled into the SMIR.

The following procedure describes how to receive enterprise-specific events.

**To receive enterprise-specific events**

1.  Compile the MIB definitions from the device responsible for generating the event.

    You can compile the MIB definitions using the SNMP MIB compiler. For more information, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

2.  Determine what types of classes you want mapping to the events.

    When you compile the MIB definition for an enterprise-specific event, you can determine what type of class the compiler generates. Specifically, you can instruct the compiler to create one of the following choices:

    -   [SnmpNotification](snmpnotification.md) subclasses from the definitions.
    -   [SnmpExtendedNotification](snmpextendednotification.md) subclasses from the definitions.
    -   [SnmpNotification](snmpnotification.md) and [SnmpExtendedNotification](snmpextendednotification.md) subclasses from the definitions.

    For more information, see [Compiling MOF Files](compiling-mof-files.md).

If the SNMP event providers receive a specific trap or notification for which there is no class, the providers generate an nonenterprise-specific event. For more information, see [Receiving Enterprise Nonspecific Events](#receiving-enterprise-nonspecific-events).

## Receiving Enterprise-Nonspecific Events

An enterprise-nonspecific event is an event that does not map from an SNMPv1 trap or SNMPv2 notification to any of the subclasses of [SnmpNotification](snmpnotification.md) or [SnmpExtendedNotification](snmpextendednotification.md) or any class that represents an enterprise event.

SEEP uses the **SNMPV1Notification** or **SNMPV2Notification** classes for nonspecific events, whereas SREP uses the **SNMPv1ExtendedNotification** and **SNMPV2ExtendedNotification** classes.

All four enterprise-nonspecific classes derive from either the [SnmpNotification](snmpnotification.md) or [SnmpExtendedNotification](snmpextendednotification.md) classes, and have the same format. Both classes have the single property **VarBindList**. **VarBindList** is an array of instances of the **SnmpVarBind** class. **SnmpVarBind** is a base class supported by the SNMP event providers to represent an instance of an SNMP variable binding. The following table lists the properties of **SnmpVarBind**.



| Property         | Description                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------|
| Encoding         | String that indicates the Abstract Syntax Notation One (ASN.1) type of the variable in the **Value** property. |
| ObjectIdentifier | String that identifies the variable in the **Value** property.                                                 |
| Value            | Raw data in octets.                                                                                            |



 

In the **SnmpV1Notification** and **SnmpV2Notification** classes, the variable binding order from the SNMP event has been preserved except for the first two variable bindings, TimeStamp and SnmpTrapOID. These bindings have been removed and are stored in the **TimeStamp** and **Identification** properties of the [SnmpNotification](snmpnotification.md) or [SnmpExtendedNotification](snmpextendednotification.md) parent class.

 

 



