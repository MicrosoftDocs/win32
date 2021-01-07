---
description: ICE56 validates that the directory structure of the .msi file has a single root directory, that the root is the TARGETDIR property, and that the SourceDir property value is in the DefaultDir column of the Directory table.
ms.assetid: 6fbb51ff-64fc-40b7-852f-490c93e592c0
title: ICE56
ms.topic: article
ms.date: 05/31/2018
---

# ICE56

ICE56 validates that the directory structure of the .msi file has a single root directory, that the root is the [**TARGETDIR**](targetdir.md) property, and that the [**SourceDir**](sourcedir.md) property value is in the DefaultDir column of the [Directory table](directory-table.md).

If a .msi file has multiple roots or specifies a root other than [**TARGETDIR**](targetdir.md), an [administrative installation](administrative-installation.md) does not create a correct administrative image.

Note that empty directories are not checked by ICE56. The directory structure passes validation with multiple root directories if the extra directories are empty.

## Result

ICE56 posts an error if the .msi does not have a single root, [**TARGETDIR**](targetdir.md), or if [**SourceDir**](sourcedir.md) is not specified in the DefaultDir column of the [Directory table](directory-table.md).

## Example

ICE56 reports the following errors for the example shown.

``` syntax
Directory 'TARGETDIR' has a bad DefaultDir value. 
Directory 'Root2' is an invalid root Directory.
```

[Directory Table](directory-table.md)



| Directory | Directory\_Parent | DefaultDir |
|-----------|-------------------|------------|
| TARGETDIR |                   | Temp       |
| Root2     | Root2             | SourceDir  |



 

To fix the first error, the [**TARGETDIR**](targetdir.md) root should have a DefaultDir value of [**SourceDir**](sourcedir.md). SOURCEDIR is also accepted. It may be possible to make **TARGETDIR** the parent of the second root, and use the '.' value in the DefaultDir column. See the [Directory table](directory-table.md) for more information.

To fix the second error, the Directory structure should have only one root called [**TARGETDIR**](targetdir.md).

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



