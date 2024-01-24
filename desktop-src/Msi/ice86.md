---
description: ICE86 issues a warning if the package uses the AdminUser property in database column of the Condition type. Package authors should use the Privileged property in conditional statements.
ms.assetid: c23c2920-3b8b-4cd1-a570-bdeabcf11436
title: ICE86
ms.topic: article
ms.date: 05/31/2018
---

# ICE86

ICE86 issues a warning if the package uses the [**AdminUser**](adminuser.md) property in database column of the [Condition](condition.md) type. Package authors should use the [**Privileged**](privileged.md) property in conditional statements.

## Result

ICE86 posts the following warning.



| ICE86 warning                                                                                               | Description                                                            |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Property \`%s\` found in column \`%s\`.\`%s\` in row %s. \`Privileged\` property is often more appropriate. | [**AdminUser**](adminuser.md) property was used in a Condition field. |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



