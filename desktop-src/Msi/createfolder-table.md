---
description: The CreateFolder table contains references to folders that need to be created explicitly for a particular component.
ms.assetid: b17b470b-6971-4124-8ec3-73914fdea95f
title: CreateFolder Table
ms.topic: article
ms.date: 05/31/2018
---

# CreateFolder Table

The CreateFolder table contains references to folders that need to be created explicitly for a particular component.

The CreateFolder table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Directory\_ | [Identifier](identifier.md) | Y   | N        |
| Component\_ | [Identifier](identifier.md) | Y   | N        |



 

## Columns

<dl> <dt>

<span id="Directory_"></span><span id="directory_"></span><span id="DIRECTORY_"></span>Directory\_
</dt> <dd>

External key into the first column of the [Directory table](directory-table.md).

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key into the first column of the [Component table](component-table.md).

</dd> </dl>

## Remarks

The folders in this table are created when the component is installed. An attempt is made to remove these folders only when the component is uninstalled or moved to run-from-source. No automatic removal is triggered if the folders become empty. In contrast, folders created by the installer but not listed in this table are removed when they become empty.

Because folders created by the installer are deleted when they become empty, you must author an entry into the CreateFolder table to install a component that consists of an empty folder.

This table is referred to when the [CreateFolders](createfolders-action.md) action or the [RemoveFolders](removefolders-action.md) action is called.

For information on how to secure a folder see the [MsiLockPermissionsEx Table](msilockpermissionsex-table.md) and [LockPermissions Table](lockpermissions-table.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE18](ice18.md)  
[ICE32](ice32.md)  
[ICE55](ice55.md)  
</dl>

 

 



