---
description: ICE21 validates that every component in the Component table belongs to a feature. It uses the FeatureComponents table to check for this mapping.
ms.assetid: 68983d6a-b807-4730-a645-378001e558ec
title: ICE21
ms.topic: article
ms.date: 05/31/2018
---

# ICE21

ICE21 validates that every component in the [Component table](component-table.md) belongs to a feature. It uses the [FeatureComponents table](featurecomponents-table.md) to check for this mapping.

## Result

ICE21 posts an error message if the installation package contains a component that does not belong to a feature.

## Example

For the following example, ICE21 posts an error message stating that the component Comp1 does not map to any feature.

[Component Table](component-table.md) (partial)



| Component |
|-----------|
| Comp1     |
| Comp2     |



 

[FeatureComponents Table](featurecomponents-table.md) (partial)



| Feature  | Component |
|----------|-----------|
| Feature1 | Comp2     |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



