---
description: The Key Format Types of configurable data may be used in text fields to provide a key into a database table.
ms.assetid: 9f3ce218-1243-4eba-9866-113200fefa30
title: Key Format Types
ms.topic: article
ms.date: 05/31/2018
---

# Key Format Types

The Key Format Types of configurable data may be used in text fields to provide a key into a database table. The msmConfigItemNonNullable attribute is implicit in this data format and does not need to be set. Null is never a valid value for this type. Responses to all Key format items must be in [CMSM Special Format](cmsm-special-format.md).

The following Key Format types exist:

[Directory Type](directory-type.md)

[File Type](file-type.md)

[Property Type](property-type.md)

[Dialog Type](dialog-type.md)

[Binary Type](binary-type.md)

[Icon Type](icon-type.md)

Configurable items of the Key Format Type are used in text columns to provide a database key and in general could be replaced by any text string. The individual types may have additional syntactic restrictions, but these restrictions are not enforced by Mergemod.dll. Particular configurable items may also have characteristic semantic restrictions. For example, a particular configurable item may be required to be a key into the [Binary table](binary-table.md) to a row containing a bitmap image. Such restrictions are not enforced by Mergemod.dll and therefore module authors should be prepared to handle any string that satisfies the specified Key Format type. Unless otherwise specified by semantic meaning or attributes, null is a valid response.

 

 



