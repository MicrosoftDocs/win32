---
description: ICE51 checks that a title has been provided for font resource files.
ms.assetid: 5a57ba6e-d1fe-44ab-b72d-52b1f212c322
title: ICE51
ms.topic: article
ms.date: 05/31/2018
---

# ICE51

ICE51 checks that a title has been provided for font resource files.

You must provide a title for a font resource that does not have an embedded name. Only .ttc, .ttf, and .otf font resource files do not require a title, because these files contain an embedded name. Do not provide a title for a font resource that contains an embedded name because the system then registers the font twice.

**[Windows Installer 4.5 and earlier](not-supported-in-windows-installer-4-5.md):** ICE51 does not check .otf font resource files.

## Result

ICE51 posts an error if there are any .ttc, .ttf, and .otf font resource files with titles. ICE51 posts a warning if there are any other font resource files without a title.

## Example

ICE51 would report the following warning for the example shown.

``` syntax
Font 'Font1' is a TTC\TTF\OTF font, but also has a title.
```

ICE51 would report the following error message for the example shown.

``` syntax
Font 'Font2' does not have a title. Only TTC\TTF\OTF fonts do not need titles.
```

[File Table](file-table.md) (partial)



| File  | FileName  |
|-------|-----------|
| Font1 | font1.ttf |
| Font2 | font2.fon |



 

[Font Table](font-table.md)



| File\_ | FontTitle          |
|--------|--------------------|
| Font1  | A Really Cool Font |
| Font2  |                    |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



