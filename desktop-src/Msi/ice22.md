---
description: ICE22 uses the FeatureComponents table to validate the mapping of features and components referenced in the PublishComponent table.
ms.assetid: 1aa3e2e6-3f05-411e-829f-aeddbb53445d
title: ICE22
ms.topic: article
ms.date: 05/31/2018
---

# ICE22

ICE22 uses the [FeatureComponents table](featurecomponents-table.md) to validate the mapping of features and components referenced in the [PublishComponent table](publishcomponent-table.md).

## Result

ICE22 posts an error message if the features and components are mapped incorrectly in the [PublishComponent table](publishcomponent-table.md).

## Example

For the following example ICE22 posts an error that {00000003-0004-0000-0000-624474732465} does not have the correct mapping for the Feature\_ and Component\_ columns.

[PublishComponent Table](publishcomponent-table.md) (partial)



| ComponentId                            | Feature\_ | Component\_ |
|----------------------------------------|-----------|-------------|
| {00000002-0003-0000-0000-624474736554} | Feat1     | Comp1       |
| {00000003-0004-0000-0000-624474732465} | Feat1     | Comp2       |



 

[FeatureComponents Table](featurecomponents-table.md) (partial)



| Feature\_ | Component\_ |
|-----------|-------------|
| Feat1     | Comp1       |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



