---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 35e1ccc2-ffc1-47a6-aba8-5a5cb442e8ae
title: ParameterRef
ms.topic: article
ms.date: 05/31/2018
---

# ParameterRef

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

A ParameterRef element defines a reference to a ParameterInit element. A ScoredProperty element that contains a ParameterRef element does not have an explicitly-set Value element. Instead, the ScoredProperty element receives its value from the ParameterInit element referenced by a ParameterRef element.

## Element Tag

<ParameterRef>

## XML Attributes

The following table lists the XML attributes that may be pertain to this element.



| XML Attribute   | Details                                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| name<br/> | Holds the name attribute of the ParameterDef element that is referenced within the context of the current document.<br/> |



 

For more information, please see [XML Attributes](xml-attributes.md) section.

## Element Information

The following table lists the elements that may be parents of this element, the elements that may be children of this element, and any restrictions on the element itself.



| Category                   | Details                                                                                           |
|----------------------------|---------------------------------------------------------------------------------------------------|
| Parent elements<br/> | ScoredProperty <br/>                                                                        |
| Child elements<br/>  | None permitted.<br/>                                                                        |
| This element<br/>    | No character data is permitted.<br/> Duplicate child siblings are not permitted.<br/> |



 

## Configuration Dependencies

ParameterRef elements may not have any configuration dependencies.

## Example

The following example illustrates how to use ParameterRef elements to enable users to enter custom media size parameters.

``` syntax
<psf:Option name="psk:CustomMediaSize" constrained="psk:None">
  <psf:ScoredProperty name="psk:MediaSizeWidth">
    <psf:ParameterRef name="psk:PageMediaSizeMediaSizeWidth" />
  </psf:ScoredProperty>
  <psf:ScoredProperty name="psk:MediaSizeHeight">
    <psf:ParameterRef name="psk:PageMediaSizeMediaSizeHeight" />
  </psf:ScoredProperty>
  <psf:Property name="psk:DisplayName">
    <psf:Value xsi:type="xs:string">Fabrikam User Custom</psf:Value>
  </psf:Property>
</psf:Option>
```

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




