---
description: The custom actions ProcessAccounts and UninstallAccounts generate the deferred custom actions that create, remove, or rollback user accounts.
ms.assetid: 245b576b-96cc-4eab-8848-5ff78ba32873
title: Authoring the InstallExecuteSequence Table
ms.topic: article
ms.date: 05/31/2018
---

# Authoring the InstallExecuteSequence Table

The custom actions ProcessAccounts and UninstallAccounts generate the deferred custom actions that create, remove, or rollback user accounts. The custom actions ProcessAccounts and UninstallAccounts must be entered into the [InstallExecuteSequence table](installexecutesequence-table.md) to be executed. Add the following entries to the [InstallExecuteSequence table](installexecutesequence-table.md). Because these custom actions must be a part of the script generation, both custom actions must be sequenced after the [InstallInitialize action](installinitialize-action.md).

The condition on ProcessAccounts ensures the following. See [Conditional Statement Syntax](conditional-statement-syntax.md).

-   ProcessAccounts runs only if the component TestAccount is being installed locally on the computer.
-   The component Test Account is currently not installed or is installed to run from the source.

The condition on UninstallAccount ensures the following:

-   UninstallAccounts runs only if the component TestAccount is installed locally on the computer.
-   The component Test Account is being removed or being installed to run from the source.

[InstallExecuteSequence Table](installexecutesequence-table.md)



| Action            | Condition                                                           | Sequence |
|-------------------|---------------------------------------------------------------------|----------|
| ProcessAccounts   | VersionNT AND (?TestAccount=2 OR ?TestAccount=4) AND $TestAccount=3 | 1550     |
| UninstallAccounts | VersionNT AND ?TestAccount=3 AND ($TestAccount=4 OR $TestAccount=2) | 1560     |



 

Continue to [Authoring the user interface for password input](authoring-the-user-interface-for-password-input.md).

 

 



