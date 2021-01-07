---
description: The purpose of a deferred execution custom action is to delay the execution of a system change to the time when the installation script is executed.
ms.assetid: 79bf4d0b-624d-4652-8c4f-0ecd928a88e3
title: Deferred Execution Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# Deferred Execution Custom Actions

The purpose of a deferred execution custom action is to delay the execution of a system change to the time when the installation script is executed. This differs from a regular custom action, or a standard action, in which the installer executes the action immediately upon encountering it in a sequence table or in a call to [**MsiDoAction**](/windows/desktop/api/Msiquery/nf-msiquery-msidoactiona). A deferred execution custom action enables a package author to specify system operations at a particular point within the execution of the installation script.

The installer does not execute a deferred execution custom action at the time the installation sequence is processed. Instead the installer writes the custom action into the installation script. The only mode parameter the installer sets in this case is MSIRUNMODE\_SCHEDULED. See [**MsiGetMode**](/windows/desktop/api/Msiquery/nf-msiquery-msigetmode) for a description of the run mode parameters.

A deferred execution custom action must be scheduled in the execute sequence table within the section that performs script generation. Deferred execution custom actions must come after [InstallInitialize](installinitialize-action.md) and come before [InstallFinalize](installfinalize-action.md) in the action sequence.

Custom actions that set properties, feature states, component states, or target directories, or that schedule system operations by inserting rows into sequence tables, can in many cases use immediate execution safely. However, custom actions that change the system directly, or call another system service, must be deferred to the time when the installation script is executed. See [Synchronous and Asynchronous Custom Actions](synchronous-and-asynchronous-custom-actions.md) for more information about potential clashes between their custom actions and the main installation thread.

Because the installation script can be executed outside of the installation session in which it was written, the session may no longer exist during execution of the installation script. This means that the original session handle and property data set during the installation sequence is not available to a deferred execution custom action. Deferred custom actions that call dynamic-link libraries (DLLs) pass a handle which can only be used to obtain a very limited amount of information, as described in [Obtaining Context Information for Deferred Execution Custom Actions](obtaining-context-information-for-deferred-execution-custom-actions.md).

Note that deferred custom actions, including [rollback custom actions](rollback-custom-actions.md) and [commit custom actions](commit-custom-actions.md), are the only types of actions that can run outside the users security context.

## Related topics

<dl> <dt>

[Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md)
</dt> <dt>

[Custom Action Reference](custom-action-reference.md)
</dt> </dl>

 

 



