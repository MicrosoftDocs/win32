---
description: ICE07 validates that installation package specifies that fonts be installed into the FontsFolder. If a font is installed to a folder other than the FontsFolder the installer creates a shortcut rather than actually installing the font.
ms.assetid: aa51b077-fb7b-4e09-9de1-ef1905144a94
title: ICE07
ms.topic: article
ms.date: 05/31/2018
---

# ICE07

ICE07 validates that installation package specifies that fonts be installed into the FontsFolder. If a font is installed to a folder other than the FontsFolder the installer creates a shortcut rather than actually installing the font.

The ICE07 custom action does the following for each font in the [Font table](font-table.md).

1.  Finds the font file to which each font title belongs using the [Font table](font-table.md).
2.  Queries the Component\_ column of the [File table](file-table.md) for the component that controls each file.
3.  Queries the Directory\_ column of the [Component table](component-table.md) to obtain a key into the Directory table.
4.  Resolves the [Directory table](directory-table.md) to determine the name of the folder into which the installer is to install the font file
5.  Posts an error if the font file is being installed into a folder other than the FontsFolder.

## Result

ICE07 posts an error if it finds that the database specifies that a font file be installed into a folder other than the FontsFolder.

## Example

IC07 would post the following error message for the example shown.

``` syntax
'Tahoma' is a font and must be installed to the FontsFolder directory. Current Install Directory: 'Sandbar'.
```

[Font Table](font-table.md)



| File\_ | FontTitle |
|--------|-----------|
| Myrtle | Tahoma    |



 

[File Table](file-table.md) (partial)



| File   | Component\_   |
|--------|---------------|
| Myrtle | Myrtle\_Beach |



 

[Component Table](component-table.md) (partial)



| Component     | Directory\_ |
|---------------|-------------|
| Myrtle\_Beach | SandBar     |



 

In this example, the font Tahoma maps to the font file Myrtle. The file Myrtle belongs to the component Myrtle\_Beach. Resolution of the Directory table shows that all the files belonging to Myrtle\_Beach are to be installed in the Sandbar folder. Because this is not the FontsFolder, ICE07 posts an error message.

Note that if the component Myrtle\_Beach really belongs in the Sandbar folder, and not the FontsFolder, then the font Tahoma may not belong in Myrtle\_Beach. A possible fix for the error would be to include Tahoma in another component that does get installed in the FontsFolder directory.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



