---
description: The PublishFeatures action writes each feature's state into the system registry.
ms.assetid: 8205e865-e625-43b9-8ce9-cff8026b2717
title: PublishFeatures Action
ms.topic: article
ms.date: 05/31/2018
---

# PublishFeatures Action

The PublishFeatures action writes each feature's state into the system registry. The feature state may be either absent, advertised, or installed. The PublishFeatures action also writes the feature-component mapping into the system registry for each installed feature.

The PublishFeatures action queries the [FeatureComponents table](featurecomponents-table.md), [Feature table](feature-table.md), and [Component table](component-table.md).

## Sequence Restrictions

The PublishFeatures action must come before [PublishProduct](publishproduct-action.md).

## ActionData Messages



| Field | Description of action data        |
|-------|-----------------------------------|
| \[1\] | Identifier of advertised feature. |



 

## Remarks

The PublishFeatures action publishes the composition of all features that are selected to be advertised or installed.

 

 



