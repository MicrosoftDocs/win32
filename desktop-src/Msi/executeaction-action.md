---
description: The ExecuteAction action initiates the execution sequence using the EXECUTEACTION property to determine which type of installation to perform.
ms.assetid: 61878317-ac87-4f6e-9375-12a78969e29e
title: ExecuteAction Action
ms.topic: article
ms.date: 05/31/2018
---

# ExecuteAction Action

The ExecuteAction action initiates the execution sequence using the [**EXECUTEACTION**](executeaction.md) property to determine which type of installation to perform.

## Sequence Restrictions

This action should be sequenced after all information collection necessary to begin the installation is complete. Additional actions may be sequenced after ExecuteAction action in the [InstallUISequence table](installuisequence-table.md), and [AdminUISequence table](adminuisequence-table.md). A sequence will typically begin with [*costing*](c-gly.md) actions, such as the [CostInitialize action](costinitialize-action.md), followed by the user interface actions, and then the ExecuteAction action.

## ActionData Messages

There are no ActionData messages.

## Remarks

The ExecuteAction action is run with system privileges if the installer service is enabled. The top-level actions, such as the [INSTALL action](install-action.md), [ADVERTISE action](advertise-action.md), and [ADMIN action](admin-action.md) include internal logic that determines whether calling the ExecuteAction action requires either the execution sequence or the user interface sequence to run.

## Related topics

<dl> <dt>

[InstallUISequence table](installuisequence-table.md)
</dt> <dt>

[AdminUISequence table](adminuisequence-table.md)
</dt> <dt>

[CostInitialize action](costinitialize-action.md)
</dt> </dl>

 

 



