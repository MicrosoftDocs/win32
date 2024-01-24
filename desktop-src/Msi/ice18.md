---
description: ICE18 validates that any empty directories used as a key path for a component are listed in the CreateFolder table.
ms.assetid: de31b893-831b-4a6d-809a-c4a3056b8a66
title: ICE18
ms.topic: article
ms.date: 05/31/2018
---

# ICE18

ICE18 validates that any empty directories used as a key path for a component are listed in the [CreateFolder table](createfolder-table.md).

If the KeyPath column of the [Component table](component-table.md) is Null, this means that directory listed in the Directory\_ column is the key path for that component. Because folders created by the installer are deleted when they become empty, this folder must be listed in the [CreateFolder table](createfolder-table.md) to prevent the installer from attempting to install every time.

Do not make the SystemFolder directory the key path of a component. Because this folder is present on every operating system, the installer always detects the key path whether or not the component is present. In this case, the key path should be a file, registry entry, or ODBC data source.

When performing a validation ICE18 first checks whether the following are all true:

-   The KeyPath column of the [Component table](component-table.md) contains a Null value.
-   That there are no files listed for the component in the [File table](file-table.md).
-   That there are no files for the component listed in the [RemoveFile table](removefile-table.md) and that the value in the DirProperty is the same as the Directory\_ column of the [Component table](component-table.md).
-   That there are no files for the component listed in the [DuplicateFile table](duplicatefile-table.md) and that the value in the DestFolder is the same as the Directory\_ column of the [Component table](component-table.md).
-   That there are no files for the component listed in the [MoveFile table](movefile-table.md) and that the value in the DestFolder is the same as the Directory\_ column of the [Component table](component-table.md).

If these are all true then ICE18 validates the following:

-   That the Component\_ column of the [CreateFolder table](createfolder-table.md) has the same value as the Component column of the [Component table](component-table.md).
-   That the Directory\_ column of the CreateFolder table has the same value as the Directory\_ column of the [Component table](component-table.md).

## Result

ICE18 posts an error message if the installation package specifies a directory as the key path for component that is not listed in the [CreateFolder table](createfolder-table.md).

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



