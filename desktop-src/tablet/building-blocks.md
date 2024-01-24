---
description: There are several persistence formats the Tablet PC platform generates that are useful as building blocks for the formats listed previously. The following formats are all generated and consumed by using the Ink object's Load and Save methods.
ms.assetid: 76d42a3d-22f5-47f9-89e8-7c5c098ac62e
title: Building Blocks
ms.topic: article
ms.date: 05/31/2018
---

# Building Blocks

There are several persistence formats the Tablet PC platform generates that are useful as building blocks for the formats listed previously. The following formats are all generated and consumed by using the [**Ink**](/previous-versions/ms583670(v=vs.100)) object's [**Load**](/previous-versions/ms569609(v=vs.100)) and [**Save**](/previous-versions/dotnet/netframework-3.5/ms571335(v=vs.90)) methods.

-   Ink serialized format (ISF): Ink Serialized Format (ISF) is the most compact persistent representation of ink. You can embed ISF within a binary document format or move it directly to the Clipboard. Ink stored in ISF should use the default coordinate system, which is HIMETRIC, with the vertical axis inverted.
-   Base-64 Encoded ISF: You can use base-64 encoded ISF to encode ink directly into an Extensible Markup Language (XML) or HTML file.
-   Fortified Graphics Interchange Format (GIF): Fortified GIF is a GIF file that contains ISF as metadata embedded within the file. Ink generated as a fortified GIF can be viewed in applications that do not recognize ink, and all ink data is maintained if the ink returns to an application that does recognize ink. This format is ideal for transporting ink content within an HTML file. The ink is available to any application, regardless of whether the application recognizes ink.
-   Base-64 Encoded Fortified GIF: This format is provided for developers who want to encode ink directly into an XML or HTML file and then convert the file into an image at a later time. You can use this when you want an XML file that is generated to contain all ink information and to be used as a way to generate HTML by using Extensible Stylesheet Language Transformations (XSLT).
    > [!Note]  
    > The LZW compression and decompression technology is allegedly covered by US Patent No. 4,558,302 and its related and foreign counterpart patents (collectively, the LZW Patents) owned by Unisys Corporation. Microsoft Corporation has obtained a license from Unisys under the LZW Patents to use the GIF and the LZW technology in certain Microsoft products. This license, however, does not extend to third-party developers using Microsoft development products, such as Microsoft toolkit and language development products, to provide GIF read/write or any other LZW capabilities in their own products. Third-party developers need to make their own determination as to whether they need a license from Unisys for their products.

     

An application can generate one of these persistent formats by using the [Microsoft.Ink.Stroke.HitTest](/previous-versions/ms828460(v=msdn.10)) or the [Microsoft.Ink.Ink.HitTest](/previous-versions/dotnet/netframework-3.5/ms571330(v=vs.90)) method to generate a strokes collection and either:

-   Adding these strokes to a new [**Ink**](/previous-versions/ms583670(v=vs.100)) object by using the [AddStrokesAtRectangle](/previous-versions/ms569548(v=vs.100)) method.
-   Generating a new [**Ink**](/previous-versions/ms583670(v=vs.100)) object by using the [ExtractStrokes](/previous-versions/dotnet/netframework-3.5/ms571326(v=vs.90)) method.

The first translates the selection rectangle to the origin, while the second does not. The application then uses the [**Save**](/previous-versions/dotnet/netframework-3.5/ms571335(v=vs.90)) method of the [**Ink**](/previous-versions/ms583670(v=vs.100)) object.

## Related topics

<dl> <dt>

[sInk and tInk Objects](sink-and-tink-objects.md)
</dt> </dl>

 

 
