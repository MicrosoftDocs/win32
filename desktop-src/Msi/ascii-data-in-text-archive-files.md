---
description: When a table that contains only ASCII characters is exported to a text archive file, the .idt file adheres to the basic archive file format.
ms.assetid: 105d2b85-c6e1-4719-83b4-1693c14ef4f4
title: ASCII Data in Text Archive Files
ms.topic: article
ms.date: 05/31/2018
---

# ASCII Data in Text Archive Files

When a table that contains only ASCII characters is exported to a [text archive file](text-archive-files.md), the .idt file adheres to the basic [archive file format](archive-file-format.md). If the table contains non-ASCII information, the format of the archive file is extended to include code page information.

## Text archive files that contain only ASCII characters

When a table that contains only ASCII characters is exported to an archive file, the .idt file is in the basic [archive file format](archive-file-format.md). Each stream in the table is exported as a file with an .ibd file name extension. The .ibd files are stored in a folder with the same name as the table. For example, consider the export of the following [Binary](binary-table.md) table.



| Name  | Data      |
|-------|-----------|
| Books | Books.ibd |
| Cars  | Cars.ibd  |



 

The directory structure after exporting this table is as follows. The information in the database table is exported to Binary.idt. The two streams of binary data are exported to Book.ibd and Cars.ibd saved in the folder named Binary.

``` syntax
Binary.idt
[Binary]
    Books.ibd
    Cars.ibd
```

The Binary.idt archive file is in the basic [archive file format](archive-file-format.md) and would look as follows.

``` syntax
Name Data
s72 v0
Binary  Name
Books   Books.ibd
Cars    Cars.ibd
```

## Text archive files that contain non- ASCII characters

If the file contains non-ASCII data, the basic [archive file format](archive-file-format.md) of the .idt file is extended to include code page information. The third row in the .idt table is the numeric code page followed by the table name and primary key column names separated by tabs.

> [!Note]  
> An .idt file that contains non-ASCII information should be saved in the ASCII format. For example, a text archive file can contain the column and table names encoded as UTF-8, but the archive file itself should be ASCII.

 

The following ActionText table localized into French would contain non-ASCII information. The numeric code page used for French strings is 1252.



| Action    | Description                                  | Template |
|-----------|----------------------------------------------|----------|
| ADVERTISE | Publication d'informations sur l'application |          |



 

The exported archive file, ActionText.idt, would be as follows.

``` syntax
Action   Description Template
s72 L0  L0
1252    ActionText  Action
Advertise   Publication d'informations sur l'application
```

> [!Note]  
> If a text archive file contains non-ASCII data, the archive file includes code page information. Archive files with code page information can only be imported back into a database of that exact code page or into a language neutral database. In the case of a language neutral database, the code page is set to the code page of the archive file. For more information about how Windows Installer handles code pages see the section [Code Page Handling (Windows Installer)](code-page-handling-windows-installer-.md).

 

 

 



