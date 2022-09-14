---
description: The Verb table contains command-verb information associated with file name extensions that must be generated as a part of product advertisement. Each row generates a set of registry keys and values.
ms.assetid: 3749095c-f0c0-498c-969f-a6c445cfdd62
title: Verb Table
ms.topic: article
ms.date: 05/31/2018
---

# Verb Table

The Verb table contains command-verb information associated with file name extensions that must be generated as a part of product advertisement. Each row generates a set of registry keys and values.

The Verb table has the following columns.



| Column      | Type                       | Key | Nullable |
|-------------|----------------------------|-----|----------|
| Extension\_ | [Text](text.md)           | Y   | N        |
| Verb        | [Text](text.md)           | Y   | N        |
| Sequence    | [Integer](integer.md)     | N   | Y        |
| Command     | [Formatted](formatted.md) | N   | Y        |
| Argument    | [Formatted](formatted.md) | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Extension_"></span><span id="extension_"></span><span id="EXTENSION_"></span>Extension\_
</dt> <dd>

The extension associated with the table row. This column is an external key to the first column of the [Extension table](extension-table.md).

</dd> <dt>

<span id="Verb"></span><span id="verb"></span><span id="VERB"></span>Verb
</dt> <dd>

The verb for the command.

</dd> <dt>

<span id="Sequence"></span><span id="sequence"></span><span id="SEQUENCE"></span>Sequence
</dt> <dd>

The sequence of the commands. Only verbs for which the Sequence column is non-Null are used to prepare an ordered list for the default value of the shell key. The Verb with the lowest value in this column becomes the default verb.

</dd> <dt>

<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>Command
</dt> <dd>

The localizable text displayed on the context menu.

</dd> <dt>

<span id="Argument"></span><span id="argument"></span><span id="ARGUMENT"></span>Argument
</dt> <dd>

Value for the command arguments.

Note that the resolution of properties in the Argument field is limited. A property formatted as \[*Property*\] in this field can only be resolved if the property already has the intended value when the component owning the verb is installed. For example, for the argument "\[\#MyDoc.doc\]" to resolve to the correct value, the same process must be installing the file MyDoc.doc and the component that owns the verb.

</dd> </dl>

## Remarks

This table is referred to when the [RegisterExtensionInfo action](registerextensioninfo-action.md) or the [UnregisterExtensionInfo action](unregisterextensioninfo-action.md) is executed.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE46](ice46.md)  
[ICE69](ice69.md)  
</dl>

 

 



