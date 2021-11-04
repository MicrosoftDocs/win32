---
title: PrintCapabilities Schemas and Documents
description: The PrintCapabilities Schema is intended to eliminate many of the limitations of the Win32 DevCaps functions.
ms.assetid: c4727c17-3122-456c-967d-d1d6ce6a5402
ms.topic: article
ms.date: 05/31/2018
---

# PrintCapabilities Schema and Document Construction

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

The current Win32 DevCaps functions (such as GetDeviceCaps or DeviceCapabilities, both described in the Microsoft Platform Software Development Kit (SDK) documentation) severely limit the type of information non-driver components can obtain, with regard to the capabilities and properties of printing devices. There is no support for publishing the capabilities of print processors, nor is there a method to enumerate nonstandard features. Thus there is no way for a component other than a driver to construct a complete user interface. Furthermore, the client or application cannot completely determine the capabilities of devices or print queues beyond those provided by the Win32 DevCaps functions. The current functions are not extensible, so devices cannot publish new properties or features.

The PrintCapabilities Schema is intended to eliminate many of the limitations of the Win32 DevCaps functions by providing a superset of the functionality afforded by these functions. If more functionality is needed, a provider of the PrintCapabilities document can extend the Print Schema Keywords, within the constraints of the Print Schema Framework, by adding privately-defined element instances. Because of its reliance on XML as the medium of interchange, any consumer of a PrintCapabilities document can access all of the data in the document without restriction, and without concern for compatibility with different operating system versions. This section describes the PrintCapabilities Schema and details its use.

The intended audience for this section includes the following groups:

-   Implementers of the PrintTicket/PrintCapabilities Provider interface

-   Consumers of PrintCapabilities

-   Clients of the PrintTicket/PrintCapabilities Provider interface

The first category in the preceding list is referred to as PrintCapabilities providers in the remainder of this section. The second and third categories are referred to as PrintCapabilities consumers.

## Relationship to Print Schema and PrintTicket Schema

The PrintCapabilities and PrintTicket Schemas are both specialized parts of the Print Schema. The main structural differences between these subsets of the Print Schema is that the PrintCapabilities Schema includes Property and ParameterDef instances that are not contained in the PrintTicket Schema, while the PrintTicket Schema contains Property and ParameterInit instances that are not contained in the PrintCapabilities Schema. Except for these differences, the PrintCapabilities and PrintTicket Schemas generally mirror each other in content, sharing Feature, Option, ScoredProperty, and Value instances. Any such shared content must be kept up-to-date. For example, if a change is made in the PageMediaSize Feature in the PrintCapabilities Schema, the same change must be made in the PrintTicket Schema.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



