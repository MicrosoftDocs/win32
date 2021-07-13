---
description: Learn about the Property element in documents and printing. This topic isn't current. For the most current information, see the Print Schema Specification.
ms.assetid: 14631336-adfc-4edf-81ef-63e426d41c87
title: Property (Documents and Printing)
ms.topic: article
ms.date: 05/31/2018
---

# Property (Documents and Printing)

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

A Property element declares a device, job formatting, or other relevant property whose name is given by its name attribute. A Value element is used to assign a value to the Property.

A Property can be complex, possibly containing multiple subproperties. Subproperties are also represented by Property elements.

## Element Tag

<Property>

## XML Attributes

The following table lists the XML attributes that may be pertain to this element.



| XML Attribute   | Details                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------|
| name<br/> | Holds the name attribute of the Property, which is either a standard Property or a privately-defined Property. <br/> |



 

For more information, please see [XML Attributes](xml-attributes.md) section.

## Element Information

The following table lists the elements that may be parents of this element, the elements that may be children of this element, and any restrictions on the element itself.



| Category                   | Details                                                                                                                                                                                                                                                                                                                      |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parent elements<br/> | PrintCapabilities <br/> Feature<br/> PrintTicket<br/> Option<br/> ParameterDef<br/> Property<br/> ScoredProperty<br/>                                                                                                                                                              |
| Child elements<br/>  | The system assigns no significance to the ordering of the elements. If clients choose to ascribe some significance in the ordering of the elements, they are free to do so. <br/> *Property* (one or more) *Value* (zero or more)<br/> or <br/> *Property* (zero or more) *Value* (one or more)<br/> |
| This element<br/>    | No character data is permitted.<br/> Duplicate child Value elements that are siblings are permitted.<br/>                                                                                                                                                                                                        |



 

## Configuration Dependencies

A Property may have configuration dependencies, except when it appears within a ParameterDef element.

## Element Usage

In addition to appearing within Feature and Option elements, Property elements can appear at the root level of the respective underlying technologies. The Print Schema defines a set of Property elements that can be used to describe a device in a portable manner. However, if these properties are insufficient to your needs as a PrintCapabilities provider (typically because the device being supported has novel aspects not anticipated by the Print Schema), you may introduce your own private Property elements. You can enhance or elaborate the information provided by a public Property by adding one or more private subproperties as element content of the public Property.

Property elements are defined by using an XML element tag, <Property>. Each Property is assigned a name by means of its name attribute. The name must be an XML QName and must conform to the Namespace Convention. For details, see [XML Attributes](xml-attributes.md). The Property name attribute and its location within the hierarchy of parent Property elements (if it is a subproperty) uniquely identify the Property within the PrintCapabilities document or PrintTicket.

A Property may contain one or more Value elements, or one or more child Property elements (called subproperties), or a combination of both. Subproperties are useful when the Property itself is composed of multiple components. For example, a "ConsumableColor" Property might have "C", "M", and "Y" components.

## Example

``` syntax
<psf:Property name="psk:DisplayName">
  <psf:Value xsi:type="xs:string">6</psf:Value>
</psf:Property>
```

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




