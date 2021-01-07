---
description: ICE50 checks that shortcut icons are specified to display correctly and match their target file's extension.
ms.assetid: 19288c87-fddb-46c9-8145-59e1b870a261
title: ICE50
ms.topic: article
ms.date: 05/31/2018
---

# ICE50

ICE50 checks that shortcut icons are specified to display correctly and match their target file's extension.

## Result

ICE50 posts an error message if the extension of the icon and target files do not match. ICE50 posts a warning if icons are stored in files that do not have an .exe or .ico extension.

## Example

ICE50 reports the following error for the example shown.



| ICE50 error or warning                                                                                                              | Description                                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The extension of Icon 'Icon2.dat' for Shortcut 'Shortcut2' does not match the extension of the Key File for component 'Component2'. | If the extensions of the icon and the target file do not match, the shortcut will not have the correct context menu when the component is advertised. To fix this error, rename the icon to match the extension of the target file.<br/> |
| The extension of Icon 'Icon1.bat' for Shortcut 'Shortcut1' is not "exe" or "ico". The Icon will not be displayed correctly.         | Not all versions of the shell correctly display icons stored in files that do not have extensions of "exe" or "ico". To fix this warning, rename the icon have an extension of "exe" or "ico".<br/>                                      |



 

[File Table](file-table.md) (partial)



| File  | FileName  |
|-------|-----------|
| File1 | File1.bat |
| File2 | File2.pl  |



 

[Feature Table](feature-table.md) (partial)



| Feature  |
|----------|
| Feature1 |



 

[Component Table](component-table.md) (partial)



| Component  | KeyPath |
|------------|---------|
| Component1 | File1   |
| Component2 | File2   |



 

[Icon Table](icon-table.md)



| Name      | Data            |
|-----------|-----------------|
| Icon1.bat | \[Binary Data\] |
| Icon2.dat | \[Binary Data\] |



 

[Shortcut Table](shortcut-table.md) (partial)



| Shortcut  | Component  | Target   | Icon\_    |
|-----------|------------|----------|-----------|
| Shortcut1 | Component1 | Feature1 | Icon1.bat |
| Shortcut2 | Component2 | Feature1 | Icon2.dat |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 




