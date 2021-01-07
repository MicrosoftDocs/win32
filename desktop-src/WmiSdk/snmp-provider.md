---
description: The Simple Network Management Protocol (SNMP) provider allows client applications to access SNMP information through Windows Management Instrumentation (WMI).
ms.assetid: 71e758d9-2ea6-42f5-93b4-d370a96b10cf
ms.tgt_platform: multiple
title: WMI and SNMP
ms.topic: article
ms.date: 05/31/2018
---

# WMI and SNMP

The Simple Network Management Protocol (SNMP) provider allows client applications to access SNMP information through Windows Management Instrumentation (WMI). The SNMP provider is not installed by default. For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

Simple Network Management Protocol (SNMP) uses a schema to define objects. The schema is different from the schema used in WMI. The SNMPv1 and SNMPv2C schema is called the Structure of Management Information (SMI), and is packaged as Management Information Base (MIB) files. MIB files define objects using a standard language—Abstract Syntax Notation 1 (ASN.1)—and a number of macro definitions that serve as templates for describing the objects. The macros provide information such as the object name, identifier, syntax, description, access rights, protocol operations, and protocol encoding. The following table lists how the SNMP provider handles different aspects of a MIB object.



| Topic                                                    | Description                                                 |
|----------------------------------------------------------|-------------------------------------------------------------|
| [NOTIFICATION-TYPE Macro](notification-type-macro.md)   | How the **NOTIFICATION-TYPE** macro maps from SNMP to WMI.  |
| [OBJECT-TYPE Macro](object-type-macro.md)               | How the **OBJECT-TYPE** macro maps from SNMP to WMI.        |
| [TEXTUAL-CONVENTION Macro](textual-convention-macro.md) | How the **TEXTUAL-CONVENTION** macro maps from SNMP to WMI. |
| [TRAP-TYPE Macro](trap-type-macro.md)                   | How the **TRAP-TYPE** macro maps from SNMP to WMI.          |



 

The SNMP provider comes with a compiler that translates MIB objects into WMI objects. The SNMP compiler can also output error or other messages. For more information, see [SNMP compiler Error Messages](snmp-compiler-error-messages.md) and [General Information Messages](general-information-messages.md).

## Related topics

<dl> <dt>

[WMI Reference](wmi-reference.md)
</dt> <dt>

[WMI Providers](wmi-providers.md)
</dt> </dl>

 

 



