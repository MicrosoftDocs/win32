---
description: ICE40 does miscellaneous validation.
ms.assetid: 1f2ba2a1-0170-4434-88fd-a5d1ca8b67c4
title: ICE40
ms.topic: article
ms.date: 05/31/2018
---

# ICE40

ICE40 does miscellaneous validation.

## Result

ICE40 posts warnings on the following:

-   The [**REINSTALLMODE**](reinstallmode.md) property has been overridden.
-   The [RemoveIniFile table](removeinifile-table.md) has a Delete Tag entry with no value.
-   The .msi file is missing the [Error table](error-table.md) and the [**Page Count Summary**](page-count-summary.md) Property is less than or equal to 100. This ICE warning is obsolete because Windows Installer does not require the package to have an Error table. Error messages can be retrieved using Msimsg.dll.

## Example

[Property Table](property-table.md)



| Property                               | Value |
|----------------------------------------|-------|
| [**REINSTALLMODE**](reinstallmode.md) | A     |



 

[RemoveIniFile Table](removeinifile-table.md)



| RemoveIniFile                          | Action | Value |
|----------------------------------------|--------|-------|
| [**REINSTALLMODE**](reinstallmode.md) | 4      |       |



 

## Results

ICE40 would report the following errors.



| ICE40 error                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**REINSTALLMODE**](reinstallmode.md) is defined in the Property table. This may cause difficulties. | Defining the [**REINSTALLMODE**](reinstallmode.md) property in .msi file can lead to unexpected behavior. To fix this error, do not define this property.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| RemoveIniFile entry Remove1 must have a value, because the Action is "Delete Tag" (4).                | There is a Delete Tag action in the in the RemoveIniFile column of the [RemoveIniFile table](removeinifile-table.md) without specifying a tag to delete in the Value column.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Error Table is missing. Only numerical error messages will be generated.                              | This ICE warning is obsolete because Windows Installer does not require the package to have an [Error table](error-table.md). Error messages can be retrieved using Msimsg.dll.<br/> This warning means that the .msi file is missing the [Error table](error-table.md) and the [**Page Count Summary**](page-count-summary.md) Property is less than or equal to 100. <br/> To fix this error, use a current version of the Windows Installer, or add an Error table to the installation package and author formatting templates in the Message column for error messages.<br/> |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 




