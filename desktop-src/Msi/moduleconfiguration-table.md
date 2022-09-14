---
description: The ModuleConfiguration table identifies the configurable attributes of the module. This table is not merged into the database.
ms.assetid: 3b77cc23-c104-4adc-868c-3aa2b5794bc7
title: ModuleConfiguration Table
ms.topic: article
ms.date: 05/31/2018
---

# ModuleConfiguration Table

The ModuleConfiguration table identifies the configurable attributes of the module. This table is not merged into the database.

The ModuleConfiguration table has the following columns.



| Column       | Type                         | Key | Nullable |
|--------------|------------------------------|-----|----------|
| Name         | [Identifier](identifier.md) | Y   | N        |
| Format       | [Integer](integer.md)       | N   | N        |
| Type         | [Text](text.md)             | N   | Y        |
| ContextData  | [Text](text.md)             | N   | Y        |
| DefaultValue | [Text](text.md)             | N   | Y        |
| Attributes   | [Integer](integer.md)       | N   | Y        |
| DisplayName  | [Text](text.md)             | N   | Y        |
| Description  | [Text](text.md)             | N   | Y        |
| HelpLocation | [Text](text.md)             | N   | Y        |
| HelpKeyword  | [Text](text.md)             | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

This field defines the name of the configurable item. This name is referenced in the formatting template in the Value column of the [ModuleSubstitution table](modulesubstitution-table.md).

</dd> <dt>

<span id="Format"></span><span id="format"></span><span id="FORMAT"></span>Format
</dt> <dd>

This column specifies the format of the data being changed.



| Format                                       | Value |
|----------------------------------------------|-------|
| [Text](text-format-types.md)                | 0     |
| [Key](key-format-types.md)                  | 1     |
| [Integer](integer-format-types.md)          | 2     |
| [Bitfield Format](bitfield-format-types.md) | 3     |



 

</dd> <dt>

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>Type
</dt> <dd>

This column specifies the type for the data being changed. This type is used to provide a context for any user-interface and is not used in the merge process. The valid values for this column depend on the value in the Format column.

</dd> <dt>

<span id="ContextData"></span><span id="contextdata"></span><span id="CONTEXTDATA"></span>ContextData
</dt> <dd>

This column specifies a semantic context for the requested data. The type is used to provide a context for any user-interface and is not used in the merge process. The valid values for this column depend on the values in the Format and Type columns.

</dd> <dt>

<span id="DefaultValue"></span><span id="defaultvalue"></span><span id="DEFAULTVALUE"></span>DefaultValue
</dt> <dd>

This column specifies a default value for the item in this record if the merge tool declines to provide a value. This value must have the format, type, and context of the item. If this is a "Key" format item, the foreign key must be a valid key into the tables of the module. Null may be a valid value for this column depending on the item. For "Key" format items, this value is in [CMSM special format](cmsm-special-format.md). For all other types, the value is treated literally.

Module authors must ensure that the module is valid in its default state. This ensures that versions of Mergemod.dll earlier than version 2.0 can still use the module in its default state.

</dd> <dt>

<span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes
</dt> <dd>

This column is a bit field containing attributes for this configurable item. Null is equivalent to 0. All other bits in this column are reserved for future use and must be 0.



| Name                             | Decimal | Hexadecimal | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------|---------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| msmConfigurableOptionKeyNoOrphan | 1       | 0x00000001  | This attribute only applies to records that list a foreign key to a module table in their DefaultValue field. The merge tool ignores the attribute for any formats other than the [Key Format Types](key-format-types.md). Items not listed in the [ModuleSubstitution table](modulesubstitution-table.md) are excluded from the following check. The merge tool does not merge the row referenced by the DefaultValue column into the target database if the following conditions are satisfied after completing all configuration options.<br/> Every row in the ModuleConfiguration table with the same DefaultValue has the msmConfigurationItemsKeyNoOrphan set.<br/> No rows use the DefaultValue because the authoring tool declined to provide a value.<br/> The merge tool merges the row if any of the following conditions are satisfied.<br/> The merge tool finds any row that does not have msmConfigItemsKeyNoOrphan set.<br/> If the merge tool finds any row using DefaultValue because the authoring tool declined to provide a value.<br/> |
| msmConfigurableOptionNonNullable | 2       | 0x00000002  | When this attribute is set, null is not a valid response for this item. This attribute has no effect for [Integer Format Types](integer-format-types.md) or [Bitfield Format Types](bitfield-format-types.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |



 

</dd> <dt>

<span id="DisplayName"></span><span id="displayname"></span><span id="DISPLAYNAME"></span>DisplayName
</dt> <dd>

This column provides a short description of this item that the authoring tool may use in the user interface. This column may not be localized. Set this column to null to have the module is request that the authoring tool not expose this property in the UI. The tool may disregard the value in this field.

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

This column provides a description of this item that the authoring tool may use in UI elements. This string may be localized by the module's language transform. This column may be null.

</dd> <dt>

<span id="HelpLocation"></span><span id="helplocation"></span><span id="HELPLOCATION"></span>HelpLocation
</dt> <dd>

This column provides either the name of a help file (without the .chm extension) or a semicolon delimited list of help namespaces. This column can be null if no help is available. This column can be null only if the HelpKeyword column is null.

</dd> <dt>

<span id="HelpKeyword"></span><span id="helpkeyword"></span><span id="HELPKEYWORD"></span>HelpKeyword
</dt> <dd>

This column provides a keyword into the help file or namespace from the HelpLocation column. The interpretation of this keyword depends on the HelpLocation column. This column may be null.

</dd> </dl>

## Remarks

The ModuleConfiguration table is used by [Configurable Merge Modules](configurable-merge-modules.md). Mergemod.dll 2.0 or later is required to create a configurable merge module.

To ensure compatibility with older versions of Mergemod.dll, the ModuleConfiguration table and [ModuleSubstitution table](modulesubstitution-table.md) should be added to the [ModuleIgnoreTable table](moduleignoretable-table.md) of every module.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE25](ice25.md)  
[ICE45](ice45.md)  
</dl>

 

 




