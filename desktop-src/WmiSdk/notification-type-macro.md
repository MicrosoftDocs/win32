---
description: The NOTIFICATION-TYPE macro contains the following elements.
ms.assetid: b7c6ec2b-640b-4373-a1e3-ff6c130b07d0
ms.tgt_platform: multiple
title: NOTIFICATION-TYPE Macro
ms.topic: article
ms.date: 05/31/2018
---

# NOTIFICATION-TYPE Macro

The NOTIFICATION-TYPE macro contains the following elements.

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

## Components

<dl> <dt>

<span id="Object_descriptor"></span><span id="object_descriptor"></span><span id="OBJECT_DESCRIPTOR"></span>Object descriptor
</dt> <dd>

Attaches a name to an SNMP event in a NOTIFICATION-TYPE macro. The following list lists the rules for mapping the object descriptor.



| Type                        | Concatenate                                                                                                                                                                                                                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Encapsulated CIM class name | "SNMP\_"<br/> MIB module identity name<br/> underscore (\_)<br/> object descriptor<br/> "\_Notification"<br/> Example: The **vtpServerDisabled** notification from the **CISCO-VTP-MIB** maps to **SNMP\_CISCO\_VTP\_MIB\_vtpServerDisabled\_Notification**.<br/>                 |
| Referent CIM class name     | "SNMP\_"<br/> MIB module identity name<br/> underscore (\_)<br/> object descriptor<br/> "\_ExtendedNotification"<br/> Example: The **vtpServerDisabled** notification from the **CISCO-VTP-MIB** maps to **SNMP\_CISCO\_VTP\_MIB\_vtpServerDisabled\_ExtendedNotification**.<br/> |



 

</dd> <dt>

<span id="OBJECTS_clause"></span><span id="objects_clause"></span><span id="OBJECTS_CLAUSE"></span>OBJECTS clause
</dt> <dd>

Enumerates the set of objects associated with the notification object.

</dd> <dt>

<span id="REFERENCE_clause"></span><span id="reference_clause"></span><span id="REFERENCE_CLAUSE"></span>REFERENCE clause
</dt> <dd>

Refers to another document that contains more information about the object. It maps to the CIM class qualifier **Reference**, which is of type string.

</dd> <dt>

<span id="DESCRIPTION_clause"></span><span id="description_clause"></span><span id="DESCRIPTION_CLAUSE"></span>DESCRIPTION clause
</dt> <dd>

Describes the object in question. It maps to the CIM class qualifier **Description**, which is of type string

</dd> <dt>

<span id="STATUS_clause"></span><span id="status_clause"></span><span id="STATUS_CLAUSE"></span>STATUS clause
</dt> <dd>

Indicates whether the object must be supported. When the status is either **obsolete** or **deprecated**, the notification is discarded from the mapping. Otherwise, this clause maps to the CIM class qualifier **Status**, which is of type **string**.

For SNMPv1, the preferred value of **Status** is either **mandatory** or **optional**, but the qualifier can contain some other value. For SNMPv2C, the preferred value of **Status** is either **current** or **deprecated**, but the qualifier can contain some other value.

</dd> </dl>

## Remarks

The SNMP provider maps the **NOTIFICATION-TYPE** macro to either an encapsulated or referent class definition.

An encapsulated class definition does not expose the instance information associated with the MIB object. Instead, the class definition encodes the OBJECTS clause as a series of properties of the CIM event class. Each CIM property reflects the name, type, and value of the corresponding MIB object in the OBJECTS clause. If you require instance information, you must map to a referent class. An encapsulated class definition maps to the [SnmpNotification](snmpnotification.md) class.

A referent class defines an MIB object and the instance information used to obtain the object. The class definition encodes the OBJECTS clause as a series of properties of the CIM event class. Each CIM property reflects the name of the corresponding MIB object in the OBJECTS clause and the type as an embedded object that reflects an instance of the class associated with that MIB object. The provider then generates a class associated with the MIB object. For example, **ifIndex** maps to an embedded class named **SNMP\_RFC1213\_MIB\_ifIndex**. For more information about this type of class, see [OBJECT-TYPE Macro](object-type-macro.md).

 

 




