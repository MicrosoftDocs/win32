---
description: Find information about the PrintTicket element. This topic isn't current. For the most current information, see the Print Schema Specification.
ms.assetid: 'fe6bd921-cbf3-4cca-afae-82d3822206ba'
title: PrintTicket
ms.topic: article
ms.date: 05/31/2018
---

# PrintTicket

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

A PrintTicket element is the root element of the PrintTicket document. A PrintTicket element contains all job formatting information required to output a job.

## Element Tag

&lt;PrintTicket&gt;

## XML Attributes

The following table lists the XML attributes that may be pertain to this element.



| XML Attribute      | Details                                                                                                                                                                                   |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| version<br/> | Specifies the version of the schema that defines element types and their structure, a literal of type integer. The current schema version is "1". This attribute is required. <br/> |



 

For more information, please see [XML Attributes](xml-attributes.md) section.

## Element Information

The following table lists the elements that may be parents of this element, the elements that may be children of this element, and any restrictions on the element itself.



| Category                   | Details                                                                                                            |
|----------------------------|--------------------------------------------------------------------------------------------------------------------|
| Parent elements<br/> | Document root only.<br/>                                                                                     |
| Child elements<br/>  | *Feature* (zero or more)<br/> *ParameterInit* (zero or more)<br/> *Property* (zero or more)<br/> |
| This element<br/>    | No character data is permitted.<br/> Duplicate child siblings are not permitted.<br/>                  |



 

## Configuration Dependencies

Configuration dependencies are applicable only to elements in a PrintCapabilities document.

## Example

See [PrintTicket Example](printticket-example.md).

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




