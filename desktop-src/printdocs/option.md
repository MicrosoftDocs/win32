---
description: Get information about the Option element. This topic isn't current. For the most current information, see the Print Schema Specification.
ms.assetid: feda78d9-58e7-4668-8a25-40e5fd8ad456
title: Option
ms.topic: article
ms.date: 05/31/2018
---

# Option

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

An Option element contains all of the Property and ScoredProperty elements associated with this option.

## Element Tag

<Option>

## XML Attributes

The following table lists the XML attributes that may be pertain to this element.



| XML Attribute          | Details                                                                                                                                                                                                                                                                                                                                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| constrained<br/> | This attribute is optional for a PrintCapabilities document.<br/> This attribute indicates whether the Option is available for selection or use. This XML attribute can be set to one of the following values: None, PrintTicketSettings, AdminSetting or DeviceSettings. <br/> See [XML Attributes](xml-attributes.md)<br/> |
| name<br/>        | Holds the name of the Option, either a standard Option or a privately-defined Option. The XML attribute is used this way in order to differentiate between Option instances. <br/>                                                                                                                                                        |



 

For more information, please see [XML Attributes](xml-attributes.md) section.

## Element Information

The following table lists the elements that may be parents of this element, the elements that may be children of this element, and any restrictions on the element itself.



| Category                   | Details                                                                                                                                                                                                                                                                                          |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parent elements<br/> | Feature <br/>                                                                                                                                                                                                                                                                              |
| Child elements<br/>  | *Property* (zero or more)<br/> *ScoredProperty* (zero or more for Options with XML Attribute 'name'; one or more for Options not utilizing XML Attribute 'name'\*)<br/> \* only public Options defined in Print Schema can have no 'name' attribute, such as DocumentNUp)<br/> |
| This element<br/>    | No character data is permitted.<br/> Duplicate child siblings are not permitted.<br/>                                                                                                                                                                                                |



 

## Configuration Dependencies

An Option definition element may not have any configuration dependencies.

## Element Usage

The purpose of the Option element is to characterize one of the states that a device configuration attribute, represented by a Feature element, can assume. Each Option element definition contains one or more ScoredProperty elements that describe an intrinsic or essential characteristic of that Option. To facilitate portability and preservation of intent, the Print Schema defines many common Feature elements and a variety of Option elements for each Feature. It is therefore important to use Print Schema-defined Option elements, if at all possible, before you create your own Option definitions. Understanding the process of defining Option elements provides useful insights into the way the PrintCapabilities document and PrintTickets are used in the Microsoft .NET Framework version 3.0 and Windows Vista printing architecture.

## Example

The following example defines a name for the Option.

``` syntax
<psf:Option name="psk:PrintFront" />
```

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




