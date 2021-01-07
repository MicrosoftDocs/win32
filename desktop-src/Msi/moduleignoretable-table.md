---
description: If a table in the merge module is listed in the ModuleIgnoreTable table, it is not merged into the .msi file.
ms.assetid: 9ff87993-74f6-4436-b0a9-d7ebed6555bd
title: ModuleIgnoreTable Table
ms.topic: article
ms.date: 05/31/2018
---

# ModuleIgnoreTable Table

If a table in the merge module is listed in the ModuleIgnoreTable table, it is not merged into the .msi file. If the table already exists in the .msi file, it is not modified by the merge. The tables in the ModuleIgnoreTable can therefore contain data that is unneeded after the merge.

The ModuleIgnoreTable table has the following columns.



| Column | Type                         | Key | Nullable |
|--------|------------------------------|-----|----------|
| Table  | [Identifier](identifier.md) | Y   | No       |



 

## Columns

<dl> <dt>

<span id="Table"></span><span id="table"></span><span id="TABLE"></span>Table
</dt> <dd>

Name of the table in the merge module that is not to be merged into the .msi file.

</dd> </dl>

## Remarks

To minimize the size of the .msm file, it is recommended that developers remove unused tables from modules intended for redistribution rather than listing these tables in the ModuleIgnoreTable table.

 

 



