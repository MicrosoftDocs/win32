---
description: 'ICE05 validates that certain tables contain required entries. This includes, but is not restricted to, checking the Property table for the required properties: ProductName, ProductLanguage, ProductVersion, ProductCode, and Manufacturer.'
ms.assetid: 90b35758-c9d9-4104-a352-f0b17b04b571
title: ICE05
ms.topic: article
ms.date: 05/31/2018
---

# ICE05

ICE05 validates that certain tables contain required entries. This includes, but is not restricted to, checking the [Property table](property-table.md) for the required properties: [**ProductName**](productname.md), [**ProductLanguage**](productlanguage.md), [**ProductVersion**](productversion.md), [**ProductCode**](productcode.md), and [**Manufacturer**](manufacturer.md).

## Result

ICE05 posts an error if a required entry is missing.

## Example

For the example shown, ICE05 would report that the entry: 'ProductVersion' is required in the 'Property' table.

[Property Table](property-table.md) (partial)



| Property                           | Value     |
|------------------------------------|-----------|
| [**ProductName**](productname.md) | MyProduct |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



