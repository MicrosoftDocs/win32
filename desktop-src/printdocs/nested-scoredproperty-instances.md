---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 071dc91f-3574-4e0e-b2ba-0e4a56ce4a28
title: Nested ScoredProperty Instances
ms.topic: article
ms.date: 05/31/2018
---

# Nested ScoredProperty Instances

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

Notice that you are not restricted to adding ScoredProperty instances as child elements of an Option instance. ScoredProperty instances may also be nested within other ScoredProperty instances. This is useful when a device property is complex and is best represented by multiple subproperties. Adding subproperties to an existing (or public) Property or ScoredProperty is a good way to enhance an Option, while retaining portability with existing Option instances. For example, the standard Option instances for the MediaType Feature contain a ScoredProperty describing the weight of the media as Light, Medium, Heavy, or ExtraHeavy. If you want more precise descriptions of the weight, you can add a subproperty (GramsPer100Sheets in the following example) that contains the actual weight (in grams) of 100 sheets of media. The enhanced Option might look like the following example.

``` syntax
<!-- Note: The following ScoredProperty is not a Public Print Schema ScoredProperty -->
<!-- This example shows a nested ScoredProperty defined by a Private namespace-->
<!-- It is included for illustration purposes. -->

<psf:ScoredProperty name="FabrikamES500:PaperWeight">
  <psf:Value xsi:type="xs:string">Medium</psf:Value>
  <psf:ScoredProperty name="FabrikamES500:GramsPerSheet">
    <Value xsi:type="decimal">109.5</Value>
  </psf:ScoredProperty>
</psf:ScoredProperty>
```

A comparison of the original and enhanced Option instances produces a near-perfect match, because the enhanced Option is a superset of the original, and the locations and values of each of the original ScoredProperty instances is preserved.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



