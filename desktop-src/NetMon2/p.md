---
description: Glossary of Network Monitor terms that begin with the letter P.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: '321398fb-683f-4fb1-b6b7-c7826811cacd'
title: P (Network Monitor)
ms.topic: article
ms.date: 05/31/2018
---

# P (Network Monitor)

<dl> <dt>

<span id="_netmon_packet_gly"></span><span id="_NETMON_PACKET_GLY"></span>**packet**
</dt> <dd>

See [*frame*](f.md).

</dd> <dt>

<span id="_netmon_parser_gly"></span><span id="_NETMON_PARSER_GLY"></span>**parser**
</dt> <dd>

A component that detects a specific protocol in a delayed capture. Each parser can detect one protocol. However, one parser DLL may contain multiple parsers. Also called a protocol parser.

</dd> <dt>

<span id="_netmon_parser.ini_gly"></span><span id="_NETMON_PARSER.INI_GLY"></span>**parser.ini**
</dt> <dd>

A Network Monitor initialization file that contains a list of all the installed parsers. For each parser there is a comment string that describes the parser, the follow set of the parser, and any Help file associated with the parser. The parser INI file is updated when Network Monitor calls **ParserAutoInstallInfo**, or when the parser DLL calls **CreateHandoffTable**.

</dd> <dt>

<span id="_netmon_perfmon_gly"></span><span id="_NETMON_PERFMON_GLY"></span>**Perfmon**
</dt> <dd>

A software tool that allows you to view network performance-related variables that identify the activity of a process.

</dd> <dt>

<span id="_netmon_promiscuous_mode_gly"></span><span id="_NETMON_PROMISCUOUS_MODE_GLY"></span>**promiscuous mode**
</dt> <dd>

A state in which a network adapter card copies all the frames that pass over the network, regardless of the destination address to a local buffer. This mode enables Network Monitor to capture and display all network traffic.

</dd> <dt>

<span id="_netmon_property_gly"></span><span id="_NETMON_PROPERTY_GLY"></span>**property**
</dt> <dd>

A protocol element in a parser that describes a data field within a frame that is sent by using that protocol.

</dd> <dt>

<span id="_netmon_property_database_gly"></span><span id="_NETMON_PROPERTY_DATABASE_GLY"></span>**property database**
</dt> <dd>

An internal database that defines all the properties that a specific protocol supports. The property database contains a **PROPERTYINFO** structure for each property that the parser defines. Network Monitor uses the information in the database when it attaches a property definition to an instance of the property, and when it formats the property data that is displayed in the details pane of the Network Monitor UI.

</dd> <dt>

<span id="_netmon_protocol_level_gly"></span><span id="_NETMON_PROTOCOL_LEVEL_GLY"></span>**protocol level**
</dt> <dd>

A logical grouping of protocol properties.

</dd> </dl>

 

 



