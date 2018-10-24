---
Description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 0552d301-5105-490f-962b-135c8c2e936b
title: ScoredProperty
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScoredProperty

This topic is not current. For the most current information, see the [Print Schema Specification](http://go.microsoft.com/?linkid=7141496).

A ScoredProperty element declares a property that is intrinsic to an Option definition. Such properties should be compared when evaluating how closely a requested Option matches a device-supported Option.

## Element Tag

<ScoredProperty>

## XML Attributes

The following table lists the XML attributes that may be pertain to this element.



| XML Attribute   | Details                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| name<br/> | Holds the name attribute of the ScoredProperty, either a standard property or a privately-defined property. <br/> |



 

For more information, please see [XML Attributes](xml-attributes.md) section.

## Element Information

The following table lists the elements that may be parents of this element, the elements that may be children of this element, and any restrictions on the element itself.



| Category                   | Details                                                                                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parent elements<br/> | *Option*<br/> *ScoredProperty*<br/>                                                                                                                          |
| Child elements<br/>  | Either<br/> *ParameterRef* (one)<br/> or<br/> *Value* (one)<br/> *Property* (zero or more)<br/> *ScoredProperty* (zero or more)<br/> |
| This element<br/>    | No character data is permitted.<br/> Duplicate child siblings are not permitted.<br/>                                                                        |



 

## Configuration Dependencies

A ScoredProperty element may not have any configuration dependencies.

## Example

Declare a ScoredProperty element named MediaSizeWidth with a Value of 11.

``` syntax
<psf:ScoredProperty name="psk:MediaSizeWidth">
   <psf:Value xsi:type="integer">11</psf:Value>
</psf:ScoredProperty>
```

## Related topics

<dl> <dt>

[Print Schema Specification](http://go.microsoft.com/?linkid=7141496)
</dt> </dl>

 

 




