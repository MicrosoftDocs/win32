---
description: The Print Schema and related technologies are available in Microsoft .NET Framework 3.0 and later versions of Microsoft .NET Framework, and in Windows Vista and later versions of Windows.
ms.assetid: 98d5f8ec-54bd-4e88-b632-ed427b599cb6
title: Print Schema
ms.topic: article
ms.date: 05/31/2018
---

# Print Schema

The Print Schema and related technologies are available in Microsoft .NET Framework 3.0 and later versions of Microsoft .NET Framework, and in Windows Vista and later versions of Windows. XPS documents and the XPS Object Model can use the print ticket objects, which are described in the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip), to specify the printing preferences of a document to printers and viewing applications.

The [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip) is a downloadable document that contains information about the Print Schema and how to use it in documents and printing. Additional information is provided online for your information only, at [Legacy Print Schema Reference](print-schema.md); however, it might not accurately reflect the current version of the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip). Refer to the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip) for the most current design information.

## Print Schema Overview

The Print Schema is a hierarchically structured, XML-based schema that is used to organize and describe the properties of a printer or print job. The Print Schema includes two components: the Print Schema Keywords and the Print Schema Framework. The Print Schema Keywords are a set of element instances that describe printer attributes and print job formatting intent. The Print Schema Framework defines a hierarchically structured collection of XML element types and how these element types can be used together.

The Print Schema technologies, called *PrintCapabilities* and *PrintTicket*, are built using the Print Schema Keywords as specified by the Print Schema Framework. The Print Schema Specification supports schema extensions by third parties, so that Print Schema users are not restricted to the Property, Feature, Option, or ParameterInit instances that are defined by the Print Schema Keywords. Third-party element instances can be added to element instances that are defined by the Print Schema Keywords; however, private, third-party Property instances must belong to a namespace that is clearly associated with the third party that created the namespace.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> <dt>

[Legacy Print Schema Reference](print-schema.md)
</dt> <dt>

[Bidirectional printer communications (Hardware Dev Center)](/windows-hardware/drivers/print/bidirectional-communication)
</dt> </dl>

 

 
