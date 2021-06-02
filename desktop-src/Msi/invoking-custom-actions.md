---
description: Custom actions are invoked in the same manner as standard actions, either by explicit invocation or during the execution of a sequence table.
ms.assetid: 05f15bae-983a-4763-840d-f2590f4e2a7a
title: Invoking Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# Invoking Custom Actions

Custom actions are invoked in the same manner as standard actions, either by explicit invocation or during the execution of a sequence table. There are two methods for calling actions:

-   You call the specified action directly with the [**MsiDoAction**](/windows/desktop/api/Msiquery/nf-msiquery-msidoactiona) function.
-   A top-level action calls the sequence table containing the custom action. For more information about scheduling a custom action in a sequence table, see [Sequencing Custom Actions](sequencing-custom-actions.md).

When the installer obtains an action name from the [**MsiDoAction**](/windows/desktop/api/Msiquery/nf-msiquery-msidoactiona) function, or from a sequence table, it first searches for a standard action of that name. If it cannot find the standard action, then the installer queries the [CustomAction table](customaction-table.md) to check if the specified action is a custom action. If the specified action is not a custom action, then the installer queries the [Dialog table](dialog-table.md) for a dialog box.

 

 



