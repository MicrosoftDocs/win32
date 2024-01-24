---
description: 'The table below lists the five custom actions used to meet the sample specifications: ProcessAccounts, UninstallAccounts, CreateAccounts, RemoveAccounts, and RollbackAccounts.'
ms.assetid: 389ec652-243e-4392-aec9-3a7eb90e6c68
title: Authoring the Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# Authoring the Custom Actions

The table below lists the five custom actions used to meet the sample specifications: ProcessAccounts, UninstallAccounts, CreateAccounts, RemoveAccounts, and RollbackAccounts. All of these custom actions are in [dynamic-link libraries](dynamic-link-libraries.md) stored in the [Binary Table](binary-table.md). The C++ source code for the dynamic-link libraries containing the sample custom actions are provided in the Windows Installer SDK. ProcessAccounts and UninstallAccounts are in the file Process.cpp. CreateAccount is in the file Create.cpp. RemoveAccount and RollbackAccount are in the file Remove.cpp. These source files can be used to create the files Process.dll, Create.dll, and Remove.dll.

Because the creation or removal of a user account requires elevated privileges, [deferred execution custom actions](deferred-execution-custom-actions.md) that run in the context of the system must be used to create, remove, or roll back user accounts. The immediate execution custom actions, ProcessAccounts and UninstallAccounts, generate the deferred custom actions that create, remove, or rollback user accounts: CreateAccount, RemoveAccount, and RollbackAccount.

Because deferred custom actions cannot read information in database tables, ProcessAccounts and UninstallUserAccouts must set a CustomActionData property to pass the information in the UserAccounts table to the deferred custom actions as described in [Obtaining Context Information for Deferred Execution Custom Actions](obtaining-context-information-for-deferred-execution-custom-actions.md). When the installer runs the execution script, the deferred custom actions handle user accounts according to the information in the CustomActionData property.

Because all the custom actions are in dynamic-link libraries stored in the Binary table, they all include the constants msidbCustomActionTypeDll and msidbCustomActionTypeBinaryData in their base numeric type. ProcessAccounts and UninstallAccounts are examples of pure [Custom Action Type 1](custom-action-type-1.md). For information on other custom action types see the [Summary List of All Custom Action Types](summary-list-of-all-custom-action-types.md).

CreateAccount and RemoveAccount are [deferred execution custom actions](deferred-execution-custom-actions.md) that do not allow services to impersonate particular users. These custom actions include the constants msidbCustomActionTypeInScript and msidbCustomActionTypeNoImpersonate to specify these [custom action in-script execution options](custom-action-in-script-execution-options.md).

RollbackAccount is a [rollback custom action](rollback-custom-actions.md) that only removes user accounts during a [rollback installation](rollback-installation.md). RollbackAccount includes the constants msidbCustomActionTypeInScript and msidbCustomActionTypeRollback to specify these [custom action in-script execution options](custom-action-in-script-execution-options.md).

These custom actions may handle sensitive data such as user passwords, which should not be written to the log file. The deferred custom actions should therefore include msidbCustomActionTypeHideTarget in the custom action type. The names of the deferred custom actions also need to be added to the [**MsiHiddenProperties**](msihiddenproperties.md) property list in the [Property table](property-table.md) because of the way immediate custom actions pass data to deferred custom actions using the CustomActionData property.



| Custom action     | DLL entry point                       | Custom action type                                                                                                                                                         |
|-------------------|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ProcessAccounts   | ProcessUserAccounts in Process.dll.   | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData = 1                                                                                                             |
| UninstallAccounts | UninstallUserAccounts in Process.dll. | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData = 1                                                                                                             |
| CreateAccount     | CreateUserAccount in Create.dll.      | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeInScript + msidbCustomActionTypeNoImpersonate + msidbCustomActionTypeHideTarget = 11265. |
| RemoveAccount     | RemoveUserAccount in Remove.dll.      | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeInScript + msidbCustomActionTypeNoImpersonate + msidbCustomActionTypeHideTarget = 11265. |
| RollbackAccount   | RemoveUserAccount in Remove.dll.      | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeInScript + msidbCustomActionTypeRollback + msidbCustomActionTypeHideTarget = 9473.       |



 

Continue to [Authoring the CustomAction Table](authoring-the-customaction-table.md).

 

 



