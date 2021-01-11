---
description: The Signature table holds the information that uniquely identifies a file signature. For more information regarding signatures see Digital Signatures and Windows Installer.
ms.assetid: '4780356f-e02a-45d9-883c-4f84867dbdea'
title: Signature Table
ms.topic: article
ms.date: 05/31/2018
---

# Signature Table

The Signature table holds the information that uniquely identifies a file signature. For more information regarding signatures see [Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md).

The Signature table has the following columns.



| Column     | Type                               | Key | Nullable |
|------------|------------------------------------|-----|----------|
| Signature  | [Identifier](identifier.md)       | Y   | N        |
| FileName   | [Text](text.md)                   | N   | N        |
| MinVersion | [Text](text.md)                   | N   | Y        |
| MaxVersion | [Text](text.md)                   | N   | Y        |
| MinSize    | [DoubleInteger](doubleinteger.md) | N   | Y        |
| MaxSize    | [DoubleInteger](doubleinteger.md) | N   | Y        |
| MinDate    | [DoubleInteger](doubleinteger.md) | N   | Y        |
| MaxDate    | [DoubleInteger](doubleinteger.md) | N   | Y        |
| Languages  | [Text](text.md)                   | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Signature"></span><span id="signature"></span><span id="SIGNATURE"></span>Signature
</dt> <dd>

The Signature column is a unique file signature.

</dd> <dt>

<span id="FileName"></span><span id="filename"></span><span id="FILENAME"></span>FileName
</dt> <dd>

The name of the file.

</dd> <dt>

<span id="MinVersion"></span><span id="minversion"></span><span id="MINVERSION"></span>MinVersion
</dt> <dd>

The minimum version of the file, with a language comparison. If this field is specified, then the file must have a version that is at least equal to MinVersion. If the file has an equal version to the MinVersion field value but the language specified in the Languages column differs, the file does not satisfy the signature filter criteria.

> [!Note]  
> The language specified in the Languages column is used in the comparison and there is no way to ignore language. If you want a file to meet the MinVersion field requirement regardless of language, you must enter a value in the MinVersion field that is one less than the actual value. For example, if the minimum version for the filter is 2.0.2600.1183, use 2.0.2600.1182 to find the file without matching the language information.

 

</dd> <dt>

<span id="MaxVersion"></span><span id="maxversion"></span><span id="MAXVERSION"></span>MaxVersion
</dt> <dd>

The maximum version of the file. If this field is specified, then the file must have a version that is at most equal to MaxVersion.

</dd> <dt>

<span id="MinSize"></span><span id="minsize"></span><span id="MINSIZE"></span>MinSize
</dt> <dd>

The minimum size of the file. If this field is specified, then the file under inspection must have a size that is at least equal to MinSize. This must be a non-negative number.

</dd> <dt>

<span id="MaxSize"></span><span id="maxsize"></span><span id="MAXSIZE"></span>MaxSize
</dt> <dd>

The maximum size of the file. If this field is specified, then the file under inspection must have a size that is at most equal to MaxSize. This must be a non-negative number.

</dd> <dt>

<span id="MinDate"></span><span id="mindate"></span><span id="MINDATE"></span>MinDate
</dt> <dd>

The minimum modification date and time of the file. If this field is specified, then the file under inspection must have a modification date and time that is at least equal to MinDate. This must be a non-negative number. The format of this field is two packed 16-bit values of type **WORD**. The high order **WORD** value specifies the date in MS-DOS date format. The low order **WORD** value specifies the time in MS-DOS time format. A value of 0 for the time value represents midnight. See the Remarks section.

</dd> <dt>

<span id="MaxDate"></span><span id="maxdate"></span><span id="MAXDATE"></span>MaxDate
</dt> <dd>

The maximum creation date of the file. If this field is specified, then the file under inspection must have a creation date that is at most equal to MaxDate. This must be a non-negative number. The format of this field is two packed 16-bit values of type **WORD**. The high order **WORD** value specifies the date in MS-DOS date format. The low order **WORD** value specifies the time in MS-DOS time format. A value of 0 for the time value represent midnight. See the Remarks section.

</dd> <dt>

<span id="Languages"></span><span id="languages"></span><span id="LANGUAGES"></span>Languages
</dt> <dd>

The languages supported by the file.

</dd> </dl>

## Remarks

This table is used with the [AppSearch Table](appsearch-table.md).

The signature is searched for using the [RegLocator table](reglocator-table.md), the [IniLocator table](inilocator-table.md), the [CompLocator table](complocator-table.md), and the [DrLocator table](drlocator-table.md). This table's columns are generally not localized. If an author decides to search for products in multiple languages, then there can be a separate entry included in the table for each language.

The Signature table generally follows the Windows Installer [File Versioning Rules](file-versioning-rules.md). Languages specified in the Languages column of the Signature table are not evaluated unless the file versions are equivalent. The Languages column will ensure that a file is of a particular language if it is of the requested version. There is no method available to ignore the Languages column. A NULL value entered in the Languages column is treated as a file without a language and does not match the file signature of a file with a language appearing in the Signature table. The following example searches for a particular version of MSI.DLL.

[DrLocator table](drlocator-table.md)

| Signature\_ | Parent | Path                  | Depth |
|-------------|--------|-----------------------|-------|
| MsiDll      | {null} | c:\\windows\\system32 | 0     |



 

[AppSearch Table](appsearch-table.md)



| Property | Signature\_ |
|----------|-------------|
| MSIDLL   | MsiDll      |



 

Signature table



| Signature | FileName | MinVersion    | MaxVersion | MinSize | MaxSize | MinDate | MaxDate | Languages |
|-----------|----------|---------------|------------|---------|---------|---------|---------|-----------|
| MsiDll    | msi.dll  | 2.0.2600.1106 | {null}     | {null}  | {null}  | {null}  | {null}  | 0         |



 

In this case, and on Windows XP SP1, the [AppSearch action](appsearch-action.md) sets MSIDLL to c:\\windows\\system32\\msi.dll because MSI.DLL is a language neutral file. If the value of the Languages column is changed from 0 to 1033, then the AppSearch action fails to find the matching msi.dll and the MSIDLL property is undefined.

You cannot use the Signature table to query on languages alone. To search for different language versions of a file, you must have a separate entry in the Signature table for each language version. If multiple languages are provided in the Languages column, then the search is for a file that supports all of those languages.

The format of MinDate and MaxDate columns are two packed 16-bit values of type **WORD**.

Date **WORD**



| Bits | Content                                             |
|------|-----------------------------------------------------|
| 0–4  | Day of the month (1-31)                             |
| 5-8  | Month (1 = January, 2 = February, and so on)        |
| 9-15 | Year offset from 1980 (add 1980 to get actual year) |



 

Time **WORD**



| Bits  | Content                     |
|-------|-----------------------------|
| 0–4   | Seconds divided by 2        |
| 5-10  | Minutes (0-59)              |
| 11-15 | Hour(0-23 on 24 hour clock) |



 

The formula for calculating the MinDate and MaxDate field values is:

( (Year - 1980) \* 512 + Month \* 32 + Day ) \* 65536 + Hours \* 2048 + Minutes \* 32 + Seconds/2

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
</dl>

 

 



