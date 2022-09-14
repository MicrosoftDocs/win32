---
description: The text format types of configurable data may be text strings of any length. Embedded nulls are not allowed.
ms.assetid: 71b89f87-43ba-41cd-a969-765d45da4ba4
title: Text Format Types
ms.topic: article
ms.date: 05/31/2018
---

# Text Format Types

The text format types of configurable data may be text strings of any length. Embedded nulls are not allowed.

The following Text Format types exist:

[Arbitrary Text](arbitrary-text-type.md)

[RTF](rtf-type.md)

[Formatted](formatted-type.md)

[Enum](enum-type.md)

[Identifier Type](identifier-type.md)

Configurable items of the Text Format Type are used in non-binary database fields and in general could be replaced by any string of any length. However, particular configurable items also have semantic restrictions. For example, a configurable item that is required to be a foreign key into a specific table has additional semantic restrictions. Such semantic restrictions are not enforced by Mergemod.dll and therefore module authors should be prepared to handle any string that satisfies the specified Text Format type.

 

 



