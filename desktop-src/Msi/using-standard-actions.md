---
description: An action is executed in the Windows Installer either by calling the MsiDoAction function or including the action in a sequence table.
ms.assetid: ee5bdc72-adf4-46f4-ae1f-4c41d22a1ed8
title: Using Standard Actions
ms.topic: article
ms.date: 05/31/2018
---

# Using Standard Actions

An action is executed in the Windows Installer either by calling the [**MsiDoAction**](/windows/desktop/api/Msiquery/nf-msiquery-msidoactiona) function or including the action in a sequence table. Because most actions encapsulate a single purpose, the most common way to use actions is to order a series of actions into a sequence to accomplish a larger task. The installer has three standard top-level actions that call an associated set of sequence tables. These associated sequence tables may contain standard actions, custom actions, and user-interface elements. Each action in a sequence table has an associated sequence number and may also have an associated conditional expression. All actions in a sequence table are visited in order and are only executed if the conditional expression evaluates to True.

While a standard action can have any sequence number associated with it, many have sequence restrictions which must be followed for the action to function properly. For example the [FileCost action](filecost-action.md), must be called after the [CostInitialize action](costinitialize-action.md). For more information on standard action sequencing restrictions, see [Actions with Sequencing Restrictions](actions-with-sequencing-restrictions.md), [Actions without Sequencing Restrictions](actions-without-sequencing-restrictions.md), or [Standard Actions Reference](standard-actions-reference.md).

The following topics provide more information about using standard actions.

-   [Publishing Products, Features, and Components](publishing-products-features-and-components.md)
-   [File Searching](file-searching.md)
-   [File Costing](file-costing.md)
-   [File Installation](file-installation.md)
-   [Modifying the Registry](modifying-the-registry.md)
-   [Running Actions](running-actions.md)

See also [About Standard Actions](about-standard-actions.md) or [Standard Actions Reference](standard-actions-reference.md).

 

 



