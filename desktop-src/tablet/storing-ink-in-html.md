---
description: It is usually desirable to copy a more complicated set of information than can be contained in ink serialized format (ISF).
ms.assetid: 1cef7f91-118c-4a16-802d-bd2ec5d15416
title: Storing Ink in HTML
ms.topic: article
ms.date: 05/31/2018
---

# Storing Ink in HTML

It is usually desirable to copy a more complicated set of information than can be contained in ink serialized format (ISF). HTML is especially useful as an interoperability format because of its strong acceptance as an industry standard and its ability to represent heterogeneous content.

HTML is widely understood, well documented, and familiar to many developers. There are many tools for HTML production. In addition, Microsoft Windows contains application programming interfaces (APIs) for rendering and manipulation of HTML. Finally, the Tablet PC Platform APIs provide the fortified GIF persistence format, which is suitable for embedding in other formats, most importantly HTML. This format consists of a GIF file with Ink Serialized Format (ISF) embedded in an application extension block.

These GIF files are representations of ink objects that:

-   Render in applications that are not ink-enabled, such as browsers or legacy word processors.
-   Contain all the necessary information from the original ink that one would want to maintain for purposes such as editing or recognition.

These GIF files can be produced by using the persistence methods of the Tablet PC Platform APIs. They are GIFs and should use the GIF extension and, to an application that is not ink-enabled, there is nothing different about them from a normal GIF. To an ink-enabled application, however, there is a rich set of data underlying the image.

After it is produced by the Tablet PC Platform APIs, a fortified GIF is referenced by an IMG tag in HTML. The HTML is then stored in the standard CF\_HTML Clipboard slot. This allows the HTML to be visible to other applications, whether they are ink-enabled. The image itself can be stored in the Windows Internet cache and set to age out after an appropriate amount of time.

Specific adornments to the IMG tag are provided or required. These adornments identify the HTML as containing ink. The following example refers to a fortified GIF by using HTML tags:

`<img href="34372423432.gif" />`

If it is necessary to refer to the image by some other means, such as cascading style sheets or Vector Markup Language (VML), there should still be an IMG tag referencing the image. This allows cutting and pasting into and out of any application that accepts HTML representations of ink.

Applications that support ink in HTML should:

-   Generate CF\_HTML when the user executes a copy. When generating CF\_HTML on copy (or save as HTML), use the [Microsoft.Ink.Ink.Save](/previous-versions/dotnet/netframework-3.5/ms571335(v=vs.90)) method, specifying the [Microsoft.Ink.PersistenceFormat](/previous-versions/ms827245(v=msdn.10)) value in the *p* parameter, to generate a fortified GIF image. The alt text should be set to the most accurate recognition result. You can set positioning to either absolute or in-place, as desired.
-   Check all IMG tags to determine if any images they point to contain ink, if the CF\_HTML slot is chosen for a paste. If so, treat the images as [Ink](/previous-versions/aa515768(v=msdn.10)) objects internally. Although only GIF files are supported in this version, your application should check non-GIF images as well, in case additional image formats are supported in the future.
-   Support the copying and pasting of ISF. Applications that support HTML should also support ISF to enhance interoperability with ink-enabled applications that do not recognize HTML. This is similar to the convention that applications that place HTML on the Clipboard also place text.

For more information about fortified GIFs, see [Building Blocks](building-blocks.md).

 

 
