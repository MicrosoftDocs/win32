---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 573c2c82-aeb9-4ef2-8a1b-40b4db6ac6e4
title: PrintTicket Schema and Document Construction
ms.topic: article
ms.date: 05/31/2018
---

# PrintTicket Schema and Document Construction

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

The current method of specifying device configuration information using a DEVMODE structure suffers from several limitations. First, the DEVMODE structure is a binary structure, which can lead to problems of differing versions. Second, it is divided into a nonextensible public portion and a private portion that can be accessed only by drivers, and only then by the specific driver that created it. The PrintTicket format expresses configuration information using the XML-based Print Schema Framework, thereby eliminating these shortcomings of the DEVMODE structure.

The PrintTicket Schema addresses each of the two problems just mentioned. First, the PrintTicket Schema is an XML-based text file, so problems with extensibility and versioning are eliminated. Second, configuration information is available to all clients, meaning that any client or provider can store and retrieve any information contained in a PrintTicket. Options are described using the same technique used by the Print Schema Framework and the derived PrintCapabilities document. For this reason, the PrintTicket provides all of the potential portability benefits of the Option definition model to be realized. See [Print Schema Framework](print-schema-framework.md) for more information. The intended audience for this section includes the following groups:

-   Implementers of a PrintTicket / PrintCapabilities Provider interface

-   Consumers of the PrintTicket

-   Clients of a PrintTicket / PrintCapabilities Provider interface

Members of the first category in the preceding list are referred to as PrintTicket providers in the remainder of this section. Members of the last two categories are referred to as PrintTicket consumers.

## Relationship to Print Schema and PrintCapabilities Schema

The PrintTicket and PrintCapabilities schemas are both specialized parts of the Print Schema. The main structural differences between these subsets of the Print Schema is that the PrintTicket Schema contains Property and ParameterInit instances that are not contained in the PrintCapabilities Schema, while the PrintCapabilities Schema includes Property and ParameterDef instances that are not contained in the PrintTicket Schema. Except for these differences, the PrintCapabilities and PrintTicket schemas generally mirror each other in content, sharing Feature, Option, ScoredProperty, and Value instances. Any such shared content must be kept up-to-date. For example, if a change is made in the MediaSize Feature in the PrintCapabilities Schema, the same change must be made in the PrintTicket Schema.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



