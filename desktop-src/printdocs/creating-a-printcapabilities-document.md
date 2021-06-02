---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: b49e20b7-bd9e-4b8f-bb4a-bb1e99b0c417
title: Creating a PrintCapabilities Document
ms.topic: article
ms.date: 05/31/2018
---

# Creating a PrintCapabilities Document

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

After a PrintTicket is validated, it can be used to create a snapshot of the PrintCapabilities. The provider must have an internal representation for any Property whose Value is dependent on the device configuration. For example, if SpotDiameter is a Property that is dependent on both the Resolution and MediaType Features, an internal representation of SpotDiameter as it relates to the various values for Resolution and MediaType might appear as in the following table:



| Resolution      | MediaType         | SpotDiameter   |
|-----------------|-------------------|----------------|
| 300<br/>  | Bond<br/>   | 520<br/> |
| 300<br/>  | Glossy<br/> | 350<br/> |
| 600<br/>  | Bond<br/>   | 330<br/> |
| 600<br/>  | Glossy<br/> | 180<br/> |
| 1200<br/> | Bond<br/>   | 250<br/> |
| 1200<br/> | Glossy<br/> | 100<br/> |



 

For this example, the PrintCapabilities provider must use the provided PrintTicket to select the proper entry from the internal table and report that as the Value for the SpotDiameter Property. This process is repeated for every multi-valued Property (for every Property whose Value is dependent on the configuration). The [PrintCapabilities Schema and Document Construction](printcapabilities-schema-and-document-construction.md) section describes the other steps involved in creating a snapshot of the PrintCapabilities.

To create a snapshot of the default PrintCapabilities document, provide a default PrintTicket (rather than an arbitrary PrintTicket) to the method that creates PrintCapabilities documents.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




