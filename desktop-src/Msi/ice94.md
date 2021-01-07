---
description: ICE94 checks the Shortcut table, Feature table, and MsiAssembly table and posts a warning if there are any unadvertised shortcuts pointing to an assembly file in the global assembly cache.
ms.assetid: 9b1b25b5-b190-47c2-8d43-fa3964e87a6f
title: ICE94
ms.topic: article
ms.date: 05/31/2018
---

# ICE94

ICE94 checks the [Shortcut table](shortcut-table.md), [Feature table](feature-table.md), and [MsiAssembly table](msiassembly-table.md) and posts a warning if there are any unadvertised shortcuts pointing to an assembly file in the global assembly cache. If the entry in the Target field of the Shortcut table is not a feature in the Feature table, the shortcut is unadvertised. If the entry in the Component\_ field of the Shortcut table is also listed in the MsiAssembly table, the shortcut points to an assembly file. If the entry in the File\_Application field in the MsiAssembly table is empty, the assembly file is in the global assembly cache.

## Result

ICE94 posts the following warning.



| ICE94 warning                                                                                | Description                                                                            |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| The non-advertised shortcut '\[2\]' points to an assembly file in the global assembly cache. | An unadvertised shortcut is pointing to an assembly file in the global assembly cache. |



 

## Example

ICE94 reports the following error for the example:

``` syntax
The non-advertised shortcut 'shortcut1' points to an assembly file in the global assembly cache.
```

[Shortcut Table](shortcut-table.md) (partial)



| Shortcut  | Component\_ | Target    |
|-----------|-------------|-----------|
| shortcut1 | c1          | \[file1\] |
| shortcut2 | c2          | feature1  |
| shortcut3 | c3          | \[file2\] |



 

[Feature Table](feature-table.md) (partial)



| Feature  |
|----------|
| feature1 |



 

[MsiAssembly Table](msiassembly-table.md) (partial)



| Component\_ | File\_Application |
|-------------|-------------------|
| c1          |                   |
| c2          |                   |
| c3          | fa1               |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



