---
description: A text archive file for a Windows Installer database carries an .idt file name extension.
ms.assetid: 91d81fb2-3a41-477a-85c2-e68bfe482b9c
title: Archive File Format
ms.topic: article
ms.date: 05/31/2018
---

# Archive File Format

A [text archive file](text-archive-files.md) for a Windows Installer database carries an .idt file name extension. When an entire database is exported to archive files, each table in the database has a separate .idt file. If a table contains a stream column, each stream in the table is represented by a file with an .ibd file name extension. The .ibd files are stored in a folder with the same name as the table.

## .idt File Format

The .idt file of an exported database table that contains only ASCII characters has the following basic format.

-   The first row contains the table column names separated by tabs.
-   The second row contains the column definitions separated by tabs.
-   If the file contain only ASCII data, the third row is table name and primary key column names separated by tabs.
-   The remaining rows in the file represent rows in the table, with columns separated by tabs.

> [!Note]  
> If the file contains non-ASCII data, the third row is the numeric code page followed by the table name and primary key column names separated by tabs. An .idt file that contains non-ASCII information should be saved in the ASCII format. For example, a text archive file can contain the column and table names encoded as UTF-8, but the archive file itself should be ASCII. See the section [ASCII Data in Text Archive Files](ascii-data-in-text-archive-files.md).

 

> [!Note]  
> The special [\_ForceCodepage](-forcecodepage.md) and [\_SummaryInformation](-summaryinformation.md) .idt files use extended formats. See the \_ForceCodepage and \_SummaryInformation sections for descriptions of their formats.

 

## Column Definitions

Column definitions are indicated by characters.

-   The first character indicates the column type. A lowercase letter indicates a non-nullable column and an uppercase letter indicates that the column can contain null values.

    | Character | Meaning                   |
    |-----------|---------------------------|
    | s, S      | String Column             |
    | l, L      | Localizable String Column |
    | v, V      | Binary Column             |
    | i, I      | Integer Column            |

    

     

-   The second character indicates the column data size.

    > [!Note]  
    > The Windows Installer does not actually use the specified column size to limit the size of the string that can be entered into a string column field. However, some authoring tools do use the specified column size to limit the size of a valid string. It is recommended that strings entered into any column meet the specified size requirement.

     

    

    | Column Definition | Meaning                                    |
    |-------------------|--------------------------------------------|
    | s255              | Non-Nullable String Column 255 long        |
    | L50               | Nullable Localizable String Column 50 long |
    | i2, I2            | Short Integer Column                       |
    | i4, I4            | Long Integer Column                        |

    

     

## Control Character Translation

Exporting a table to a text archive file translates the control characters to avoid conflicts with file delimiters. While writing into the .idt file, the control characters are translated as follows.



| Control Character | Translation in .idt | Meaning         |
|-------------------|---------------------|-----------------|
| NULL              | 21                  | Null            |
| BS                | 27                  | Back Space      |
| HT                | 16                  | Tab             |
| LF                | 25                  | Line Feed       |
| FF                | 24                  | Form Feed       |
| CR                | 17                  | Carriage Return |



 

 

 



