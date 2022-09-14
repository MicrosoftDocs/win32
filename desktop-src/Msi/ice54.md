---
description: ICE54 checks for components that use a companion file as their key path.
ms.assetid: 94fcabfe-4500-42f2-acea-13b9a6681ca6
title: ICE54
ms.topic: article
ms.date: 05/31/2018
---

# ICE54

ICE54 checks for components that use a companion file as their key path.

The key path file of a component must not derive its version from a different file. This can cause some files to fail to install. See the [File table](file-table.md) for more information about companion files.

## Result

ICE54 posts a warning if any component has a key path file that derives its version from another file.

## Example

ICE54 returns the following warning for the example shown.

``` syntax
Component 'Component1' uses file 'File1' as its KeyPath, but the file's version is provided by the file 'File2'.
```

[Component Table](component-table.md) (partial)



| Component  | Attribute | KeyPath |
|------------|-----------|---------|
| Component1 | 0         | File1   |



 

[File Table](file-table.md) (partial)



| File  | Version | Language |
|-------|---------|----------|
| File1 | File2   |          |
| File2 | 1.0.0.0 | 1033     |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



