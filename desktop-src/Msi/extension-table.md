---
description: The Extension table contains information about file name extension servers that must be generated as a part of product advertisement. Each row generates a set of registry keys and values.
ms.assetid: 924858b7-8956-4636-b7c7-c902aa822ee1
title: Extension Table
ms.topic: article
ms.date: 05/31/2018
---

# Extension Table

The Extension table contains information about file name extension servers that must be generated as a part of product advertisement. Each row generates a set of registry keys and values.

The Extension table contains the columns shown in the following table.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Extension   | [Text](text.md)             | Y   | N        |
| Component\_ | [Identifier](identifier.md) | Y   | N        |
| ProgId\_    | [Text](text.md)             | N   | Y        |
| MIME\_      | [Text](text.md)             | N   | Y        |
| Feature\_   | [Identifier](identifier.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="Extension"></span><span id="extension"></span><span id="EXTENSION"></span>Extension
</dt> <dd>

The extension associated with the table row. The extension can be up to 255 characters long. Enter the extension in this field without the preceding period.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

An external key to the first column of the [Component](component-table.md) table. This column references the component that controls the installation of the extension.

</dd> <dt>

<span id="ProgId_"></span><span id="progid_"></span><span id="PROGID_"></span>ProgId\_
</dt> <dd>

The Program ID associated with this extension. This is a foreign key into the [ProgId](progid-table.md) table.

</dd> <dt>

<span id="MIME_"></span><span id="mime_"></span>MIME\_
</dt> <dd>

The Content Type that is to be written for the Extension column.

An external key to the first column of the [MIME](mime-table.md) table.

</dd> <dt>

<span id="Feature_"></span><span id="feature_"></span><span id="FEATURE_"></span>Feature\_
</dt> <dd>

An external key into the first column of the [Feature](feature-table.md) table specifying the feature that provides the extension server.

</dd> </dl>

## Remarks

The Extension table is referred to when the [RegisterExtensionInfo](registerextensioninfo-action.md) action or the [UnRegisterExtensionInfo](unregisterextensioninfo-action.md) action is executed.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE15](ice15.md)  
[ICE19](ice19.md)  
[ICE32](ice32.md)  
[ICE41](ice41.md)  
[ICE69](ice69.md)  
</dl>

 

 



