---
description: ICE10 validates that the advertise state of child features matches that of its parent feature.
ms.assetid: b0e0d837-245e-4c38-a7c4-06dda0eea25c
title: ICE10
ms.topic: article
ms.date: 05/31/2018
---

# ICE10

ICE10 validates that the advertise state of child features matches that of its parent feature.

A child feature may not disallow advertisement while its parent feature allows advertisement. The following combination of parent and child attributes is therefore invalid.

``` syntax
parent = msidbFeatureAttributesFavorAdvertise 
child = msidbFeatureAttributesDisallowAdvertise
```

This combination is invalid because it would turn off the parent whenever the parent was supposed to be advertised. However, the reverse is allowed. A child can be marked to favor advertisement while the parent is marked to disallow advertisement.

The ICE10 custom action determines the state of parent and child features from the Attributes column of the [Feature](feature-table.md) table. Note that it is valid to set the state of a feature to 0 and have its parent or child set to favor or disallow advertisement.

## Result

ICE10 posts an error if the Attributes column of the [Feature](feature-table.md) table contains a mismatch in the advertise state.

## Example

ICE10 posts the following error message for the example shown.

``` syntax
Conflicting states, one favors, one disallows. Child: Word differs in advertise state 
from Parent: Office.
```

Note for this example that Microsoft Excel and Microsoft Word are child features of Microsoft Office.

[Feature](feature-table.md) table (partial)



| Feature | Feature\_Parent | Attributes |
|---------|-----------------|------------|
| Office  | Null            | 4          |
| Excel   | Office          | 4          |
| Word    | Office          | 8          |



 

In the example, Word is set to disallow advertisement, which conflicts with the allow advertisement state of its parent, Office.

In some cases ICE10 posts the following error:

``` syntax
Parent feature: 'Parent' not found for child feature: 'Child'. This error means 
that for the child feature 'Child', the feature 'Parent' is not listed in the 
Feature table.
```

This refers to an invalid foreign key reference. The fix is to have 'Child' point to its correct parent feature, or add an entry for the parent feature 'Parent' to the [Feature](feature-table.md) table.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



