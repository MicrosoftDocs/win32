---
description: This sample demonstrates how to use custom actions to create user accounts on a local computer when installing a component.
ms.assetid: fc06dd7b-46d7-45a0-85b3-26f808c64f89
title: Using a Custom Action to Create User Accounts on a Local Computer
ms.topic: article
ms.date: 05/31/2018
---

# Using a Custom Action to Create User Accounts on a Local Computer

This sample demonstrates how to use custom actions to create user accounts on a local computer when installing a component. Removal of a component removes the local user accounts created by the custom action. Several custom actions are demonstrated including [Deferred Execution Custom Actions](deferred-execution-custom-actions.md) and [Rollback Custom Actions](rollback-custom-actions.md).

The sample meets the following specifications.

-   The installation creates user accounts only if running Windows 2000.
-   The installation creates user accounts only if the component is being installed to run locally. This precludes creating user accounts during the repair or reinstallation of the component.
-   The Installer removes the accounts when the component is removed.
-   User account information is read from a custom table in the installation database and is not hard-coded into the custom action code.
-   Because the creation or removal of user accounts requires elevated privileges, some of the custom actions must be capable of making changes to the system that require elevated privileges. These custom actions must be deferred custom actions that run when in the execution script.
-   Each account has a rollback custom action to ensure the account is removed on rollback of the component installation. This does not include the rollback of an account deletion during the removal of a component.
-   Custom actions send ActionData messages for each account that is created or removed. This does not include providing progress messages for the ProgressBar.
-   Custom actions report an error if an account cannot be created.
-   The password for the account is obtained through the user interaction with the user interface, or in the case of an installation at the Basic UI or None [User Interface Levels](user-interface-levels.md), as a property passed on the command line.
-   Sensitive data is hidden from the log file.

The sample includes a hypothetical component named TestAccount. The discussion in the following sections assumes that you have already created the resources required by TestAccount and have authored the [Feature](feature-table.md), [Component](component-table.md), [File](file-table.md), [Directory](directory-table.md), and [FeatureComponents](featurecomponents-table.md) tables in the sample database required to install this component. For more information, see [An Installation Example](an-installation-example.md).

The following topics contain information about how to create required custom actions and add them to an installation package.

-   [Authoring the Custom Actions](authoring-the-custom-actions.md)
-   [Adding a Custom CustomUserAccounts Table](adding-a-custom-customuseraccounts-table.md)
-   [Authoring the CustomAction Table](authoring-the-customaction-table.md)
-   [Authoring the ActionText and Error Tables](authoring-the-actiontext-and-error-tables.md)
-   [Authoring the InstallExecuteSequence Table](authoring-the-installexecutesequence-table.md)
-   [Authoring the User Interface for Password Input](authoring-the-user-interface-for-password-input.md)
-   [Securing the installation](securing-the-installation.md)

 

 



