---
Description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 925e314c-85ff-4c1b-b3c9-f36aa4b55e01
title: PrintCapabilities
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PrintCapabilities

This topic is not current. For the most current information, see the [Print Schema Specification](http://go.microsoft.com/?linkid=7141496).

A PrintCapabilities element represents the root of the PrintCapabilities document. The PrintCapabilities document contains all of the information needed to describe the supported device attributes, given a particular device configuration.

## Element Tag

&lt;PrintCapabilities&gt;

## XML Attributes

The following table lists the XML attributes that may be pertain to this element.



| XML Attribute      | Details                                                                                                                                                                                                             |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| version<br/> | Specifies the version of the schema that defines element types and their structure. The version attribute is of type integer. The current schema version is designated "1". This attribute is required. <br/> |



 

For more information, please see [XML Attributes](xml-attributes.md) section.

## Element Information

The following table lists the elements that may be parents of this element, the elements that may be children of this element, and any restrictions on the element itself.



| Category                   | Details                                                                                                           |
|----------------------------|-------------------------------------------------------------------------------------------------------------------|
| Parent elements<br/> | Document root only.<br/>                                                                                    |
| Child elements<br/>  | *Feature* (zero or more)<br/> *ParameterDef* (zero or more)<br/> *Property* (zero or more)<br/> |
| This element<br/>    | No character data is permitted.<br/> Duplicate child siblings are not permitted.<br/>                 |



 

## Configuration Dependencies

The root element may not have any configuration dependencies.

## Example

See [PrintCapabilities Document Example](printcapabilities-document-example.md).

## Related topics

<dl> <dt>

[Print Schema Specification](http://go.microsoft.com/?linkid=7141496)
</dt> </dl>

 

 




