---
description: The CCPSearch table contains the list of file signatures used for the Compliance Checking Program (CCP). At least one of these files needs to be present on a user's computer for the user to be in compliance with the program.
ms.assetid: 98d21e24-1633-44b7-bfdb-5a40bab8d319
title: CCPSearch Table
ms.topic: article
ms.date: 05/31/2018
---

# CCPSearch Table

The CCPSearch table contains the list of file signatures used for the Compliance Checking Program (CCP). At least one of these files needs to be present on a user's computer for the user to be in compliance with the program.

The CCPSearch table has the following column.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Signature\_ | [Identifier](identifier.md) | Y   | N        |



 

## Column

<dl> <dt>

<span id="Signature_"></span><span id="signature_"></span><span id="SIGNATURE_"></span>Signature\_
</dt> <dd>

The Signature\_ represents a unique file signature and is also the external key into the [Signature](signature-table.md), [RegLocator](reglocator-table.md), [IniLocator](inilocator-table.md), [CompLocator](complocator-table.md), and [DrLocator](drlocator-table.md) tables.

</dd> </dl>

## Remarks

This table is referred to when the [CCPSearch action](ccpsearch-action.md) or the [RMCCPSearch action](rmccpsearch-action.md) is executed.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
</dl>

 

 



