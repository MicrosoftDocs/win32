---
description: The BindImage table contains information about each executable or DLL that needs to be bound to the DLLs imported by it.
ms.assetid: 68bf064c-dd85-4796-8e08-6af307f94ad8
title: BindImage Table
ms.topic: article
ms.date: 05/31/2018
---

# BindImage Table

The BindImage table contains information about each executable or DLL that needs to be bound to the DLLs imported by it.

The BindImage table has the following columns.



| Column | Type                         | Key | Nullable |
|--------|------------------------------|-----|----------|
| File\_ | [Identifier](identifier.md) | Y   | N        |
| Path   | [Paths](paths.md)           | N   | Y        |



 

## Columns

<dl> <dt>

<span id="File_"></span><span id="file_"></span><span id="FILE_"></span>File\_
</dt> <dd>

An external key to column one of the [File table](file-table.md). This must be an executable file or a DLL file.

</dd> <dt>

<span id="Path"></span><span id="path"></span><span id="PATH"></span>Path
</dt> <dd>

A list of paths, separated by semicolons, that represent the paths to be searched to find the imported DLLs. The list is usually a list of properties, with each property enclosed inside square brackets (\[ \]) .

</dd> </dl>

## Remarks

The installer computes the virtual address of each function that is imported from all DLLs, and the computed virtual address is then saved in the importing image's Import Address Table (IAT).

This table is referred to when the [BindImage action](bindimage-action.md) is executed.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE46](ice46.md)  
[ICE76](ice76.md)  
</dl>

 

 



