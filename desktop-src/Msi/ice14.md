---
description: ICE14 validates the Feature table of a Windows Installer database.
ms.assetid: fb1970f8-1dba-4b06-aa03-5b33d213fc79
title: ICE14
ms.topic: article
ms.date: 05/31/2018
---

# ICE14

ICE14 validates the following for features:

-   That root parent features do not have the msidbFeatureAttributesFollowParent bit set in the Attributes column of the [Feature table](feature-table.md). A root feature does not have a parent.
-   That no feature has the same entry in the Feature and Feature\_Parent columns of the [Feature table](feature-table.md). No feature can be its own parent.

## Result

ICE14 posts an error message if it finds a root feature with the msidbFeatureAttributesFollowParent bit set or a feature with identical entries in the Feature and Feature\_Parent columns of the Feature table.

## Example

ICE14 would return the following errors for the following example:

-   The feature Sport has the same value in the Feature and Feature\_Parent columns of the File table.
-   The root feature Sport has the msidbFeatureAttributesFollowParent bit set.

In the feature tree of this example, Sport is the root feature and a parent of the Swimming and Football features. Freestyle is a child feature of Swimming. TouchFootball is a child feature of Football.

[Feature Table](feature-table.md) (partial)



| Feature       | Attributes | Feature\_Parent |
|---------------|------------|-----------------|
| Sport         | 4          | Sport           |
| Swimming      | 1          | Sport           |
| Football      | 4          | Sport           |
| Freestyle     | 1          | Swimming        |
| TouchFootball | 4          | Football        |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



