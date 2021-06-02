---
description: All property names must follow these restrictions.
ms.assetid: 4447013a-86c4-48a9-bfe1-5e758c799a2f
title: Restrictions on Property Names
ms.topic: article
ms.date: 05/31/2018
---

# Restrictions on Property Names

All property names must follow these restrictions.

-   A property name is an [Identifier](identifier.md), which is a text string that must begin with either a letter or an underscore. Identifiers and property names may contain letters, numerals, underscores, or periods; but cannot begin with a numeral or period.
-   [Public property](public-properties.md) names cannot contain lowercase letters.
-   [Private property](private-properties.md) names must contain some lowercase letters.
-   Property names prefixed with % represent system and user environment variables. These are never entered into the [Property table](property-table.md). The permanent settings of environment variables can only be modified using the [Environment Table](environment-table.md).

## Related topics

<dl> <dt>

[Using Properties](using-properties.md)
</dt> </dl>

 

 



