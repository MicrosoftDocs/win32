---
description: ICEM10 verifies that a merge module contains only properties that are allowed in the Property Table.
ms.assetid: 9ac7a724-ea0e-4caa-bb4f-846bfb802037
title: ICEM10
ms.topic: article
ms.date: 05/31/2018
---

# ICEM10

ICEM10 verifies that a merge module contains only properties that are allowed in the [Property Table](property-table.md). The following product specific properties are not allowed in the Property Table:

-   [**ProductLanguage Property**](productlanguage.md)
-   [**ProductCode Property**](productcode.md)
-   [**ProductVersion Property**](productversion.md)
-   [**ProductName Property**](productname.md)
-   [**Manufacturer Property**](manufacturer.md)

## Result

ICEM10 posts an error when a merge module contains a property that is not allowed in the [Property Table](property-table.md).

## Example

ICEM10 posts the following error messages for a module that contains the database entries shown.

``` syntax
The property 'ProductLanguage' is not allowed in a merge module.

The property 'Manufacturer' is not allowed in a merge module.
```

The following table shows you a partial [Property Table](property-table.md).



| Property                                   | Values    |
|--------------------------------------------|-----------|
| Color                                      | Red       |
| [**Manufacturer**](manufacturer.md)       | Microsoft |
| [**ProductLanguage**](productlanguage.md) | 1033      |



 

The following procedure shows you how to fix errors.

**To fix the errors**

1.  Remove the '[**Manufacturer**](manufacturer.md)' property from the [Property Table](property-table.md).
2.  Remove the '[**ProductLanguage**](productlanguage.md)' property from the [Property Table](property-table.md).

## Table Used During Execution

The [Property Table](property-table.md) is used during execution.

## Related topics

<dl> <dt>

[Merge Module ICE Reference](merge-module-ice-reference.md)
</dt> </dl>

 

 



