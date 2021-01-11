---
description: The LaunchConditions action queries the LaunchCondition table and evaluates each conditional statement recorded there. If any of these conditional statements fail, an error message is displayed to the user and the installation is terminated.
ms.assetid: b356987d-3efe-4a57-a745-91a1b34222e9
title: LaunchConditions Action
ms.topic: article
ms.date: 05/31/2018
---

# LaunchConditions Action

The LaunchConditions action queries the [LaunchCondition table](launchcondition-table.md) and evaluates each conditional statement recorded there. If any of these conditional statements fail, an error message is displayed to the user and the installation is terminated.

## Sequence Restrictions

The LaunchConditions action is optional. This action is normally the first in the sequence, but the [AppSearch Action](appsearch-action.md) may be sequenced before the LaunchConditions action. If there are launch conditions that do not apply to all installation modes, the appropriate installation mode property should be used in a conditional expression in the appropriate sequence table.

## ActionData Messages

There are no ActionData messages.

 

 



