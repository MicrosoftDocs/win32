---
description: ICE68 checks that all custom action types needed for an installation are valid.
ms.assetid: a37d6d6c-3005-425b-883a-6fe074b9d708
title: ICE68
ms.topic: article
ms.date: 05/31/2018
---

# ICE68

ICE68 checks that all custom action types needed for an installation are valid. Failure to fix the error reported by ICE68 causes an installation that attempts to execute the action to fail. ICE68 issues a warning if the **msidbCustomActionTypeNoImpersonate** attribute is set without also setting the **msidbCustomActionTypeInScript** attribute.

## Result

ICE68 returns an error if an action type needed for an installation is invalid.

## Example

ICE68 posts the following warning if a custom action has the **msidbCustomActionTypeNoImpersonate** bit set in the Type field of the CustomAction table without the **msidbCustomActionTypeInScript** also set.

``` syntax
Even though custom action '[2]' is marked to be elevated (with 
attribute msidbCustomActionTypeNoImpersonate), it will not be run with elevated 
privileges because it's not deferred (with attribute msidbCustomActionTypeInScript).
```

To fix this warning, include **msidbCustomActionTypeInScript** (0x400) if the custom action includes **msidbCustomActionTypeNoImpersonate** (0x800). Otherwise the installer ignores the **msidbCustomActionTypeNoImpersonate** attribute. For more information, see [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md).

ICE68 reports the following error for the example shown:

``` syntax
Invalid custom action type for action 'Action1'.
```

1027 is not a valid action type.

To fix this error, choose a valid custom action type.

[CustomAction Table](customaction-table.md) (partial)



| Action  | Type | Source   | Target     |
|---------|------|----------|------------|
| Action1 | 1027 | Argument | Component1 |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



