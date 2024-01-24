---
description: The ProgId table contains information for program IDs and version independent program IDs that must be generated as a part of the product advertisement.
ms.assetid: 66a7e170-6f70-4db7-98f4-8a074471b9f2
title: ProgId Table
ms.topic: article
ms.date: 05/31/2018
---

# ProgId Table

The ProgId table contains information for program IDs and version independent program IDs that must be generated as a part of the product advertisement.

The ProgId table has the following columns.



| Column         | Type                         | Key | Nullable |
|----------------|------------------------------|-----|----------|
| ProgId         | [Text](text.md)             | Y   | N        |
| ProgId\_Parent | [Text](text.md)             | N   | Y        |
| Class\_        | [GUID](guid.md)             | N   | Y        |
| Description    | [Text](text.md)             | N   | Y        |
| Icon\_         | [Identifier](identifier.md) | N   | Y        |
| IconIndex      | [Integer](integer.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="ProgId"></span><span id="progid"></span><span id="PROGID"></span>ProgId
</dt> <dd>

The program ID or version independent program ID. ProgIds listed in the ProgId table are registered if the CLSID listed in the Class\_column of this table is scheduled to be advertised or installed. When the ProgId is selected for registration, all ProgIds that refer to this row through the ProgId\_Parent column are also selected for registration.

</dd> <dt>

<span id="ProgId_Parent"></span><span id="progid_parent"></span><span id="PROGID_PARENT"></span>ProgId\_Parent
</dt> <dd>

Defined only for version independent program IDs. This field is a foreign key into the ProgId column. To define a version independent program ID, enter the corresponding ProgId into the ProgId\_Parent column. When the ProgId is selected for installation, the corresponding version-independent ProgIds associated through the ProgId\_Parent column are also selected for registration.

</dd> <dt>

<span id="Class_"></span><span id="class_"></span><span id="CLASS_"></span>Class\_
</dt> <dd>

An optional foreign key into the [Class table](class-table.md). This column must be Null for a version independent ProgId. If the Class\_value for a ProgId is null, the ProgId is registered when it appears in the ProgId column of a row in the [Extension table](extension-table.md) and the extension has at least one Verb associated with it in the [Verb table](verb-table.md). ProgIds selected for registration in this manner do not install other ProgIds that reference the current ProgId through the ProgId\_Default value.

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

An optional localized description of the associated program ID.

</dd> <dt>

<span id="Icon_"></span><span id="icon_"></span><span id="ICON_"></span>Icon\_
</dt> <dd>

An optional foreign key into the [Icon table](icon-table.md) that specifies the icon file associated with this ProgId. This is written under the DefaultIcon key associated with this ProgId. This column must be Null for a version independent ProgId.

</dd> <dt>

<span id="IconIndex"></span><span id="iconindex"></span><span id="ICONINDEX"></span>IconIndex
</dt> <dd>

The Icon index into the icon file. This column must be Null for a version independent ProgId.

</dd> </dl>

## Remarks

The [RegisterProgIdInfo](registerprogidinfo-action.md) and [UnregisterProgIdInfo](unregisterprogidinfo-action.md) actions in [*sequence tables*](s-gly.md) process the information in this table. For information about using *sequence tables*, see [Using a Sequence Table](using-a-sequence-table.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE36](ice36.md)  
[ICE89](ice89.md)  
</dl>

 

 



