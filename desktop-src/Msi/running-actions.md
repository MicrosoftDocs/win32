---
description: The installer functions can be used to run specific actions or action sequences.
ms.assetid: ceb4f70b-1179-416a-9030-3d87341cb956
title: Running Actions
ms.topic: article
ms.date: 05/31/2018
---

# Running Actions

The installer functions can be used to run specific actions or action sequences. These actions can either be [standard](standard-actions.md) or [custom](custom-actions.md) actions. The following procedure describes how to run actions:

**To run an action sequence**

1.  Run a sequence of actions defined in a table by calling the [**MsiSequence**](/windows/desktop/api/Msiquery/nf-msiquery-msisequencea) function.

    The installer queries the indicated table and runs each action if its conditional expression evaluates to TRUE.

2.  Check conditional expressions by calling the [**MsiEvaluateCondition**](/windows/desktop/api/Msiquery/nf-msiquery-msievaluateconditiona) function.
3.  Run the action by calling the [**MsiDoAction**](/windows/desktop/api/Msiquery/nf-msiquery-msidoactiona) function. The action can be a standard action, a custom action, or a user interface dialog box.
4.  If an error occurred during the execution of this action, call the [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) function. The installer will process the error.

 

 



