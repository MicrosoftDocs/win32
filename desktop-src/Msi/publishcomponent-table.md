---
description: The PublishComponent table associates components listed in the Component table with a qualifier text-string and a category ID GUID.
ms.assetid: 4a6be647-3e73-47a1-acfa-7d6d0a2fb2f4
title: PublishComponent Table
ms.topic: article
ms.date: 05/31/2018
---

# PublishComponent Table

The PublishComponent table associates components listed in the [Component table](component-table.md) with a qualifier text-string and a category ID GUID. Components with parallel functionality that have been grouped together in this way are referred to as qualified components. See [Qualified Components](qualified-components.md). This provides the installer with a method for single-level indirection when referring to components. See [Using Qualified Components](using-qualified-components.md).

The PublishComponent table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| ComponentId | [GUID](guid.md)             | Y   | N        |
| Qualifier   | [Text](text.md)             | Y   | N        |
| Component\_ | [Identifier](identifier.md) | Y   | N        |
| AppData     | [Text](text.md)             | N   | Y        |
| Feature\_   | [Identifier](identifier.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="ComponentId"></span><span id="componentid"></span><span id="COMPONENTID"></span>ComponentId
</dt> <dd>

A string [GUID](guid.md) that represents the category of components being grouped together. Note that this column's title is misleading. This is the GUID for the category of qualified components and is not the same GUID appearing in the ComponentId column of the [Component table](component-table.md). Here it refers to a server that provides the functionality of a component to external clients rather than the component itself.

</dd> <dt>

<span id="Qualifier"></span><span id="qualifier"></span><span id="QUALIFIER"></span>Qualifier
</dt> <dd>

A text string that qualifies the value in the ComponentId column. A qualifier is used to distinguish multiple forms of the same component, such as a component that is implemented in multiple languages. These are the qualifier text-strings returned by [**MsiEnumComponentQualifiers**](/windows/desktop/api/Msi/nf-msi-msienumcomponentqualifiersa).

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key into column one of the [Component table](component-table.md). This identifier refers to the qualified component's record in the Component table.

</dd> <dt>

<span id="AppData"></span><span id="appdata"></span><span id="APPDATA"></span>AppData
</dt> <dd>

An optional localizable text describing the qualified component of this record. The string is commonly parsed by the application and can be displayed to the user. It should describe the qualified component. This can be retrieved with [**MsiEnumComponentQualifiers**](/windows/desktop/api/Msi/nf-msi-msienumcomponentqualifiersa).

</dd> <dt>

<span id="Feature_"></span><span id="feature_"></span><span id="FEATURE_"></span>Feature\_
</dt> <dd>

External key into column one of the [Feature table](feature-table.md). This is the feature using this qualified component.

</dd> </dl>

## Remarks

This table is referred to when the [PublishComponents action](publishcomponents-action.md) or the [UnpublishComponents action](unpublishcomponents-action.md) is executed.

Note that the name of this table is misleading. This table is not required in order to author advertisement. See the Attributes column of the [Component table](component-table.md) and [Feature table](feature-table.md) for information on how to set the installation state of components to advertise.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE19](ice19.md)  
[ICE22](ice22.md)  
[ICE32](ice32.md)  
</dl>

 

 



