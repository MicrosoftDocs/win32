---
description: ICE06 checks every table to validate that all the columns listed in the \_Validation table are present in the table. If a table does not exist, any \_Validation entries for that table are ignored.
ms.assetid: 0c3f21ae-49ea-4cfe-b465-6fdc2b19cbb9
title: ICE06
ms.topic: article
ms.date: 05/31/2018
---

# ICE06

ICE06 checks every table to validate that all the columns listed in the [\_Validation table](-validation-table.md) are present in the table. If a table does not exist, any \_Validation entries for that table are ignored.

The purpose of ICE06 is to detect instances in which an author tries to use a new \_Validation table that reflects a schema change with an old database that has not been updated. ICE06 also detects the reverse case of an old \_Validation table being used with an altered database.

Note that the internal validation performed by [ICE03](ice03.md) catches the instance of a table column not defined in the \_Validation table being listed in the columns catalog. The use of both ICE03 and ICE06 therefore ensures every column in the database is tested.

## Result

ICE06 posts an error when there is a table column defined in the \_Validation table that is not listed in the \_Columns table.

## Example

For the following example ICE06 posts the message

Column: Version of Table: ModuleSignature is not defined in database.

[\_Validation Table](-validation-table.md) (partial)



| Table           | Column   |
|-----------------|----------|
| ModuleSignature | ModuleID |
| ModuleSignature | Version  |



 

[\_Columns Table](-columns-table.md) (partial)



| Table           | Number | Name     |
|-----------------|--------|----------|
| ModuleSignature | 1      | ModuleID |



 

The Version column of the ModuleSignature table is not in the database or listed in the \_Columns table.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



