---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: d5419c40-43e9-49ff-a378-9aeb0757e400
title: ParameterInit
ms.topic: article
ms.date: 05/31/2018
---

# ParameterInit

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

Defines a value for an instance of a ParameterDef element. A ParameterInit element is the target of the reference made by a ParameterRef element.

## Element Tag

<ParameterInit>

## XML Attributes

The following table lists the XML attributes that may be pertain to this element.



| XML Attribute   | Details                                                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| name<br/> | Holds the name attribute of the ParameterDef element that is to be initialized within the context of the current document.<br/> |



 

For more information, please see [XML Attributes](xml-attributes.md) section.

## Element Information

The following table lists the elements that may be parents of this element, the elements that may be children of this element, and any restrictions on the element itself.



| Category                   |                                                                                                   |
|----------------------------|---------------------------------------------------------------------------------------------------|
| Parent elements<br/> | PrintTicket (PrintTicket root)<br/>                                                         |
| Child elements<br/>  | Value (one)<br/>                                                                            |
| This element<br/>    | No character data is permitted.<br/> Duplicate child siblings are not permitted.<br/> |



 

## Configuration Dependencies

None

## Example

The following example initializes a parameter to 1. The example in [ParameterDef](parameterdef.md) demonstrates how to set all of the required Property elements for this parameter.

``` syntax
<psf:ParameterInit name="psk:PageCopyCount">
    <psf:Value xsi:type="xs:integer">1</psf:Value>
</psf:ParameterInit>
```

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




