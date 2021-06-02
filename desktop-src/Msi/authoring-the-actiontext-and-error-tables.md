---
description: The sample specifications include sending ActionData messages when a custom action creates or removes a user account, and reporting an error if an account cannot be created.
ms.assetid: ee90fe3d-51f4-433b-a5ce-950a03e1d8fb
title: Authoring the ActionText and Error Tables
ms.topic: article
ms.date: 05/31/2018
---

# Authoring the ActionText and Error Tables

The sample specifications include sending ActionData messages when a custom action creates or removes a user account, and reporting an error if an account cannot be created.

Enter the following entries into the ActionText table to provide information used by ActionText messages.

[ActionText Table](actiontext-table.md)



| Action            | Description                                                       | Template                          |
|-------------------|-------------------------------------------------------------------|-----------------------------------|
| ProcessAccounts   | Generating actions to create user accounts on the local computer. | Account: \[1\], Attributes: \[2\] |
| CreateAccount     | Creating user account on the local computer.                      | Account: \[1\]                    |
| RemoveAccount     | Removing user account from the local computer.                    | Account: \[1\]                    |
| RollbackAccount   | Rolling back the creation of user accounts on the local computer. | Account: \[1\]                    |
| UninstallAccounts | Generating actions to remove user accounts on the local computer. | Account: \[1\]                    |



 

Enter the following entries into the Error table to provide information used by error reporting.

[Error Table](error-table.md)



| Error | Message                                                                        |
|-------|--------------------------------------------------------------------------------|
| 25001 | Unable to create user account '\[2\]' on the local machine. Error Code: \[3\]. |
| 25002 | User account '\[2\]' already exists on the local machine.                      |
| 25003 | Unable to remove user account '\[2\]' on the local machine. Error Code: \[3\]. |
| 25004 | User account '\[2\]' does not exist on the local machine.                      |



 

Continue to [Authoring the InstallExecuteSequence Table](authoring-the-installexecutesequence-table.md).

 

 



