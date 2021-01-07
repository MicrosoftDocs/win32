---
description: ICE47 checks the Feature and FeatureComponents tables for features with 1600 or more components.
ms.assetid: e3101569-4d0b-48c9-8ba2-6f0de0c39e74
title: ICE47
ms.topic: article
ms.date: 05/31/2018
---

# ICE47

ICE47 checks the [Feature](feature-table.md) and [FeatureComponents](featurecomponents-table.md) tables for features with 1600 or more components.

## Result

ICE47 posts an error message if a feature exceeds the maximum limit of 1600 components per feature.

## Example

ICE47 would report the following warning:

``` syntax
Feature 'Feature1' has 1600 components. This could cause 
    problems on Win9X systems. You should try to have less 
    than 800 components per feature."
```

[Feature Table](feature-table.md) (partial)



| Feature  |
|----------|
| Feature1 |



 

[FeatureComponents Table](featurecomponents-table.md) (partial)



| Action   | Condition     |
|----------|---------------|
| Feature1 | Component1    |
| Feature1 | Component1600 |



 

To fix this warning, try splitting the feature into several features

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



