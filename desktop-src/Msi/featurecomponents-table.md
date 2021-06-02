---
description: The FeatureComponents table defines the relationship between features and components. For each feature, this table lists all the components that make up that feature.
ms.assetid: aff16483-a9ed-4675-8e87-8adf695605ee
title: FeatureComponents Table
ms.topic: article
ms.date: 05/31/2018
---

# FeatureComponents Table

The FeatureComponents table defines the relationship between features and components. For each feature, this table lists all the components that make up that feature.

The FeatureComponents table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Feature\_   | [Identifier](identifier.md) | Y   | N        |
| Component\_ | [Identifier](identifier.md) | Y   | N        |



 

## Columns

<dl> <dt>

<span id="Feature_"></span><span id="feature_"></span><span id="FEATURE_"></span>Feature\_
</dt> <dd>

An external key into the first column of the Feature [table](feature-table.md).

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

An external key into the first column of the [Component table](component-table.md).

</dd> </dl>

## Remarks

There is a maximum limit of 1600 components per feature.

Components can be shared by two or more features, that is, the same component can be referred to by more than one feature.

This table is referred to when the [PublishFeatures action](publishfeatures-action.md) or the [UnpublishFeatures action](unpublishfeatures-action.md) is executed.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE21](ice21.md)  
[ICE22](ice22.md)  
[ICE32](ice32.md)  
[ICE41](ice41.md)  
[ICE47](ice47.md)  
[ICE59](ice59.md)  
[ICE62](ice62.md)  
[ICE69](ice69.md)  
</dl>

 

 



