---
description: A specification of the sample is that user account information be read from a custom table in the installation database and not hard-coded into the custom action.
ms.assetid: 1545b4f1-3ccf-4745-90d8-15f1f79d8455
title: Adding a Custom CustomUserAccounts Table
ms.topic: article
ms.date: 05/31/2018
---

# Adding a Custom CustomUserAccounts Table

A specification of the sample is that user account information be read from a custom table in the installation database and not hard-coded into the custom action.

Add a custom table to the sample installation database named CustomUserAccounts to hold user account information. See [Examples of Database Queries Using SQL and Script](examples-of-database-queries-using-sql-and-script.md) for an example of how to add a custom table. Use the following schema for the CustomUserAccounts table. See [Column Definition Format](column-definition-format.md) for an explanation of the column types.



| Column     | Type | Key | Nullable | Description                                                                                                                                                                                                                                                                                                |
|------------|------|-----|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UserName   | s72  | Y   | N        | Name of user account being created.                                                                                                                                                                                                                                                                        |
| Password   | s72  |     | N        | Name of property containing the password for the account. This is a [public property](public-properties.md) set on the command line or through an [edit control](edit-control.md) in the user interface. This edit control should have the [Password Control Attribute](password-control-attribute.md). |
| Attributes | i4   |     | Y        | Attributes for account. These are defined as the **DWORD** values for the usri1\_flags member of the USER\_INFO\_1 structure.                                                                                                                                                                              |



 

After the CustomUserAccounts table has been added to the database you may edit this table using Orca, a table editor provided with the Windows Installer SDK, or another editor. Enter the following record in the CustomUserAccounts table to create a password secured user account for a user called TestUser. Note that 512 is the numeric value for UF\_NORMAL\_ACCOUNT.

CustomUserAccounts Table



| UserName | Password         | Attributes |
|----------|------------------|------------|
| TestUser | TESTUSERPASSWORD | 512        |



 

Add the following records to the \_Validation table for the custom table.

[\_Validation Table](-validation-table.md)



| Table              | Column     | Nullable | MinValue | MaxValue   | KeyTable | KeyColumn | Category                     | Set | Description |
|--------------------|------------|----------|----------|------------|----------|-----------|------------------------------|-----|-------------|
| CustomUserAccounts | UserName   | N        |          |            |          |           | [Text](text.md)             |     |             |
| CustomUserAccounts | Password   | N        |          |            |          |           | [Identifier](identifier.md) |     |             |
| CustomUserAccounts | Attributes | Y        | 0        | 2147483647 |          |           | null                         |     |             |



 

Continue to [Authoring the ActionText and Error Tables](authoring-the-actiontext-and-error-tables.md).

 

 



