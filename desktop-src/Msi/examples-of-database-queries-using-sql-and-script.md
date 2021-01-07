---
description: An example of using script-driven database queries is provided in the Windows Installer Software Development Kit (SDK) as the utility WiRunSQL.vbs.
ms.assetid: aa38dbe5-411d-432e-b3fe-09994fc59c75
title: Examples of Database Queries Using SQL and Script
ms.topic: article
ms.date: 05/31/2018
---

# Examples of Database Queries Using SQL and Script

An example of using script-driven database queries is provided in the Windows [Installer Software Development Kit](platform-sdk-components-for-windows-installer-developers.md) (SDK) as the utility WiRunSQL.vbs. This utility handles database queries using the Windows Installer version of SQL described in the section [SQL Syntax](sql-syntax.md).

**Delete a record from a table**

The following command line deletes the record having the primary key RED from the [Feature](feature-table.md) table of the Test.msi database.

**Cscript WiRunSQL.vbs Test.msi "DELETE FROM \`Feature\` WHERE \`Feature\`.\`Feature\`='RED'"**

**Add a table to a database**

The following command line adds the [Directory](directory-table.md) table to the Test.msi database.

**CScript WiRunSQL.vbs Test.msi "CREATE TABLE \`Directory\` (\`Directory\` CHAR(72) NOT NULL, \`Directory\_Parent\` CHAR(72), \`DefaultDir\` CHAR(255) NOT NULL LOCALIZABLE PRIMARY KEY \`Directory\`)"**

**Remove a table from a database**

The following command line removes the [Feature](feature-table.md) table from the Test.msi database.

**Cscript WiRunSQL.vbs Test.msi "DROP TABLE \`Feature\`"**

**Add a new column to a table**

The following command line adds the Test column to the [CustomAction](customaction-table.md) table of the Test.msi database.

**CScript WiRunSQL.vbs Test.msi "ALTER TABLE \`CustomAction\` ADD \`Test\` INTEGER"**

**Insert a new record into a table**

The following command line inserts a new record into the [Feature](feature-table.md) table of the Test.msi database.

**Cscript WiRunSQL.vbs Test.msi "INSERT INTO \`Feature\` (\`Feature\`.\`Feature\`,\`Feature\`.\`Feature\_Parent\`,\`Feature\`.\`Title\`,\`Feature\`.\`Description\`, \`Feature\`.\`Display\`,\`Feature\`.\`Level\`,\`Feature\`.\`Directory\_\`,\`Feature\`.\`Attributes\`) VALUES ('Tennis','Sport','Tennis','Tournament',25,3,'SPORTDIR',2)"**

This inserts the following record into the [Feature](feature-table.md) table of Test.msi.

[Feature](feature-table.md) Table



| Feature | Feature\_Parent | Title  | Description | Display | Level | Directory\_ | Attributes |
|---------|-----------------|--------|-------------|---------|-------|-------------|------------|
| Tennis  | Sport           | Tennis | Tournament  | 25      | 3     | SPORTDIR    | 2          |



 

Note that binary data cannot be inserted into a table directly using the INSERT INTO or UPDATE SQL queries. For information see [Adding Binary Data to a Table Using SQL](adding-binary-data-to-a-table-using-sql.md).

**Modify an existing record in a table**

The following command line changes the existing value in the Title field to "Performances." The updated record has "Arts" as its primary key and is in the Feature table of the Test.msi database.

**Cscript WiRunSQL.vbs Test.msi "UPDATE \`Feature\` SET \`Feature\`.\`Title\`='Performances' WHERE \`Feature\`.\`Feature\`='Arts'"**

**Select a group of records**

The following command line selects the name and type of all controls that belong to the ErrorDialog in the Test.msi database.

**CScript WiRunSQL.vbs Test.msi "SELECT \`Control\`, \`Type\` FROM \`Control\` WHERE \`Dialog\_\`='ErrorDialog' "**

**Hold a table in memory**

The following command line locks the [Component](component-table.md) table of the Test.msi database in memory.

**CScript WiRunSQL.vbs Test.msi "ALTER TABLE \`Component\` HOLD"**

**Free a table in memory**

The following command line frees the [Component](component-table.md) table of the Test.msi database from memory.

**CScript WiRunSQL.vbs Test.msi "ALTER TABLE \`Component\` FREE"**

 

 



