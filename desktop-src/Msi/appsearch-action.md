---
description: The AppSearch action uses file signatures to search for existing versions of products.
ms.assetid: 56665876-2c74-476b-aa1a-158c6e86418d
title: AppSearch Action
ms.topic: article
ms.date: 05/31/2018
---

# AppSearch Action

The AppSearch action uses file signatures to search for existing versions of products. The AppSearch action may use this information to determine where upgrades are to be installed. The AppSearch action can also be used to set a property to the existing value of an registry or .ini file entry.

## Sequence Restrictions

AppSearch should be authored into the [InstallUISequence table](installuisequence-table.md) and [InstallExecuteSequence table](installexecutesequence-table.md). The installer prevents the AppSearch action from running in the InstallExecuteSequence sequence if the action has already run in InstallUISequence sequence.

## ActionData Messages



| Field | Description of action data      |
|-------|---------------------------------|
| \[1\] | Property holding file location. |
| \[2\] | File signature.                 |



 

## Remarks

The AppSearch action requires that the [Signature](signature-table.md) table be present in the installation package. File signatures are listed in the Signature table. A signature that is not in the Signature table denotes a directory and the action sets the property to the directory path for that signature.

The AppSearch action searches for file signatures using the [CompLocator](complocator-table.md) table first, the [RegLocator](reglocator-table.md) table next, then the [IniLocator](inilocator-table.md) table, and finally the [DrLocator](drlocator-table.md) table.

## Related topics

<dl> <dt>

[AppSearch](appsearch-table.md)
</dt> <dt>

[CompLocator](complocator-table.md)
</dt> <dt>

[IniLocator](inilocator-table.md)
</dt> <dt>

[RegLocator](reglocator-table.md)
</dt> <dt>

[DrLocator](drlocator-table.md)
</dt> </dl>

 

 



