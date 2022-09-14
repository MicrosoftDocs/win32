---
description: ICE48 checks for directories that are hard-coded to local paths in the Property table.
ms.assetid: 9dcc2475-23a3-4f77-8828-4d0a036670d4
title: ICE48
ms.topic: article
ms.date: 05/31/2018
---

# ICE48

ICE48 checks for directories that are hard-coded to local paths in the [Property table](property-table.md).

Do not hard-code directory paths to local drives because computers differ in the setup of the local drive. This practice may be acceptable if deploying an application to a large number of computers on which the relevant portions of the drives are all the same.

## Result

ICE48 posts an error message if there is a directory that is hard-coded to a local path in the Property table.

## Example

ICE48 would report the following warning for the example shown.

``` syntax
Directory 'Dir1' appears to be hardcoded in the property 
    table to a local drive.
```

[Directory Table](directory-table.md) (partial)



| Directory | Directory\_Parent | DefaultDir |
|-----------|-------------------|------------|
| Dir1      |                   | SourceDir  |



 

[Property Table](property-table.md) (partial)



| Property | Value      |
|----------|------------|
| Dir1     | d:\\source |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



