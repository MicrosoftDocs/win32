---
description: ICE24 validates the Property table in a Windows Installer database.
ms.assetid: 1250677b-691e-46bd-83e0-e349106c820b
title: ICE24
ms.topic: article
ms.date: 05/31/2018
---

# ICE24

ICE24 validates the following properties in the [Property table](property-table.md):

-   That the [**ProductCode**](productcode.md) Property is a valid [GUID](guid.md) data type.
-   That the [**ProductVersion**](productversion.md) Property is a valid product version.
-   That the [**ProductLanguage**](productlanguage.md) Property is a valid [Language](language.md) data type.

## Result

ICE24 posts an error message if any of these properties are not in the form of a valid data type.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



