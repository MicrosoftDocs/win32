---
description: Review Feature elements, which contain a list of Option and Property elements describing a device attribute, job formatting setting, or other relevant characteristic.
ms.assetid: 5a6553c2-f322-47e2-bbc8-44f6541f1288
title: Feature
ms.topic: article
ms.date: 05/31/2018
---

# Feature

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

A Feature element contains a complete list of the Option and Property elements that fully describe a device attribute, job formatting setting, or other relevant characteristic.

## Element Tag

&lt;Feature&gt;

## XML Attributes

The following table lists the XML attributes that may be pertain to this element.



| XML Attribute   | Details                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------|
| name<br/> | Holds the name of the Feature, either a standard Feature or a privately-defined Feature. <br/> |



 

For more information, please see [XML Attributes](xml-attributes.md) section.

## Element Information

The following table lists the elements that may be parents of this element, the elements that may be children of this element, and any restrictions on the element itself.




| Category | Details | 
|----------|---------|
| Parent elements<br /> | PrintCapabilities <br /> PrintTicket <br /> Feature<br /> | 
| Child elements<br /> | One of the following groups:<br /><ul><li><em>Feature</em> (zero or more)<br /></li><li><em>Option</em> (one or more)<br /></li><li><em>Property</em> (zero or more)<br /></li></ul>or <br /><ul><li><em>Feature</em> (one or more)<br /></li><li><em>Option</em> (zero or more)<br /></li><li><em>Property</em> (zero or more)<br /></li></ul> | 
| This element<br /> | No character data is permitted.<br /> Duplicate child Option elements that are siblings are permitted. Duplicate name attribute shortcuts permitted. <br /> | 




 

## Configuration Dependencies

Feature elements may not have any configuration dependencies.

## Element Usage

### Relationship to XML Attributes

In Feature/Option representation, a device attribute is represented by a Feature element. The device attribute is uniquely identified by the name attribute in the device attribute's Feature element, as in the following example. In this example, the device attribute is Resolution.

``` syntax
<Feature name="Resolution" />
```

The Print Schema defines a set of name attributes for certain Feature instances. These name attributes serve to identify a set of predefined Feature instances associated with specific configurable device attributes. These Feature instance names should be used whenever applicable, because they increase the portability of your PrintCapabilities document and the PrintTickets that are derived from them. Privately-defined Feature instances may be introduced if certain device attributes do not correspond to any of the schema-defined Feature instances. For information about the syntax for name attributes and the conventions that apply to schema-defined and privately-defined names, see [XML Attributes](xml-attributes.md).

### Relationship to Option Element

Each of the possible states is represented by an Option element. Each Option definition contains one or more ScoredProperty elements, which taken together uniquely describe or characterize the state that is being represented. The technique used to create Option definitions is described in [Option Definitions](option-definitions.md). All of the Option elements associated with a particular Feature element reside as child elements of the Feature element.

### Subfeatures

The Print Schema Framework also allows Feature elements to be grouped together in a hierarchical manner. That is, a Feature element can itself contain one or more child Feature elements (subfeatures). This can be useful for organizing related Feature elements, or for Feature elements that control aspects of a device feature. One example is a device that supports stapling. Such a device might offer the user a choice of where to locate the staple, such as at the upper left corner, or the upper right corner, or along the top edge, or along the left edge. The user interface (UI) for this device should be able to present the user with the highest level choices first, which in this case is whether to use stapling. Only after the user has decided to use stapling should he or she be presented with a second tier of choices, staple location. A feature hierarchy adds the additional structure that makes such a user interface possible. The Print Schema Framework allows subfeatures to have their own child subfeatures, thereby permitting an unlimited level of nesting.

The Print Schema Framework also allows Option elements to appear at the same level as subfeatures; that is, as siblings within the same parent Feature element. This allows the user to make the high level decision (whether to use stapling) before making the subfeature selections. For this example the root Feature element, "Staple", might contain two Option elements, "On" and "Off", as well as a subfeature named "StapleLocation".

## Example

``` syntax
<psf:Feature name="psk:JobOutputBin">
  <psf:Property name="psf:SelectionType">
    <psf:Value xsi:type="xs:string">psk:PickOne</psf:Value>
  </psf:Property>
  <psf:Option constrained="psk:None">
    <psf:ScoredProperty name="psk:Bin">
      <psf:Value xsi:type="xs:string">SorterBin</psf:Value>
    </psf:ScoredProperty>
    <psf:ScoredProperty name="psk:MediaSheetCapacity">
      <psf:Value xsi:type="xs:integer">100</psf:Value>
    </psf:ScoredProperty>
  </psf:Option>
</psf:Feature>
```

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




