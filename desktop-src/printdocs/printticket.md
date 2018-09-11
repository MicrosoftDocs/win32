---
Description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 'fe6bd921-cbf3-4cca-afae-82d3822206ba'
title: PrintTicket
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PrintTicket

This topic is not current. For the most current information, see the [Print Schema Specification](http://go.microsoft.com/?linkid=7141496).

A PrintTicket element is the root element of the PrintTicket document. A PrintTicket element contains all job formatting information required to output a job.

## Element Tag

<PrintTicket>

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

[Print Schema Specification](http://go.microsoft.com/?linkid=7141496)
</dt> </dl>

 

 




