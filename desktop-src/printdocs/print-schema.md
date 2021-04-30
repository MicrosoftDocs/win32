---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 'd746bdd1-96c2-41f5-ad99-0b51c8ee8731'
title: Legacy Print Schema Reference
ms.topic: article
ms.date: 05/31/2018
---

# Legacy Print Schema Reference

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

The Print Schema and related technologies are available in the Microsoft .NET Framework 3.0, Microsoft Windows Vista, and later releases.

The Print Schema provides an XML-based format for expressing and organizing a large set of properties that describe either a job format or PrintCapabilities in a hierarchically structured manner.

The Print Schema is an umbrella term that includes two components, the Print Schema Keywords and the Print Schema Framework. The Print Schema Keywords document is a public schema that defines a set of element instances that can be used to describe device attributes and print job formatting. The Print Schema Framework is a public schema that defines a hierarchically structured collection of XML element types, and specifies how the element types can be used together.

The Print Schema Keywords and the Print Schema Framework form the foundation for two Print Schema-related technologies, the PrintCapabilities Schema, and the PrintTicket Schema.

It is important to keep in mind that one of the goals of the Print Schema is to support schema extensions by providers. That is, providers are not restricted to using only those Property, Feature, Option, or ParameterInit instances defined in the Print Schema Keywords in the technologies built on the Print Schema Framework. Provider-specific element instances may be freely interspersed within element instances defined in the Print Schema Keywords. The only requirement is that provider-specific (that is, private) Property instances must belong to a namespace that is clearly associated with the provider.

-   [Print Schema Background](print-schema-background.md)

-   [Print Schema-Related Technologies](print-schema-related-technologies.md)

-   [Terms Used in the Print Schema](terms-used-in-the-print-schema.md)

-   [Syntax of the Print Schema](syntax-of-the-print-schema.md)

-   [Summary of Element Types](summary-of-element-types.md)

-   [Print Schema Framework](print-schema-framework.md)

-   [Print Schema Public Keywords](print-schema-public-keywords.md)

-   [PrintCapabilities Schema and Document Construction](printcapabilities-schema-and-document-construction.md)

-   [PrintTicket Schema and Document Construction](printticket-schema-and-document-construction.md)

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



