---
description: The Integer Format Types of configurable data may be used in either text or integer database fields. The msmConfigItemNonNullable attribute is implicit in this data format and does not need to be set. Null is never a valid value for this type.
ms.assetid: 63fb9c0d-e7f1-4c1d-bb83-2833c5fff18d
title: Integer Format Types
ms.topic: article
ms.date: 05/31/2018
---

# Integer Format Types

The Integer Format Types of configurable data may be used in either text or integer database fields. The msmConfigItemNonNullable attribute is implicit in this data format and does not need to be set. Null is never a valid value for this type.

The following Integer Format type exists.

[Arbitrary Integer Type](arbitrary-integer-type.md)

Configurable items of the Integer Format Type are used in either text or integer columns and in general could be replaced by any positive or negative integer. However, particular configurable items may also have characteristic semantic restrictions. For example, a particular configurable item required to be an integer between 0 and 100 has and additional semantic restriction. Such restrictions are not enforced by Mergemod.dll and therefore module authors should be prepared to handle any string that satisfies the specified Integer Format type.

 

 



