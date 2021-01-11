---
description: The MsiSFCBypass Table contains a list of files that should bypass Windows File Protection when the files are installed on Microsoft Windows Me.
ms.assetid: 86de0dc1-ed8f-410c-a411-6c44c8e5c9fd
title: MsiSFCBypass Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiSFCBypass Table

The MsiSFCBypass Table contains a list of files that should bypass Windows File Protection when the files are installed on Microsoft Windows Me.

The MsiSFCBypass Table has the following column.



| Column | Type                         | Key | Nullable |
|--------|------------------------------|-----|----------|
| File\_ | [Identifier](identifier.md) | Y   | N        |



 

## Columns

<dl> <dt>

<span id="File_"></span><span id="file_"></span><span id="FILE_"></span>File\_
</dt> <dd>

The foreign key to the [File Table](file-table.md) that specifies the file that should bypass Windows File Protection when the file is installed on Windows Me.

</dd> </dl>

 

 



