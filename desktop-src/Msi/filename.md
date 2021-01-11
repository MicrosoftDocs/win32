---
description: The Filename data type is a text string containing a file name or folder.
ms.assetid: af59e1b8-0699-4031-895f-415752611e21
title: Filename
ms.topic: article
ms.date: 05/31/2018
---

# Filename

The Filename data type is a text string containing a file name or folder. By default, the file name is assumed to use short file name syntax; that is, eight-character name, period (.), and 3-character extension. A short file name must always be provided because the [**SHORTFILENAMES**](shortfilenames.md) property may be set or the target volume for the installation may only support short file names.

To include a long file name with the short file name, separate it from the short file name with a vertical bar (\|).

For example, the following two strings are valid:

-   status.txt
-   projec~1.txt\|Project Status.txt

Short and long file names must not contain the following characters:

-   slash (/) or (\\)
-   question mark (?)
-   vertical bar (\|)
-   right angle bracket (>)
-   left angle bracket (<)
-   colon (:)
-   asterisk (\*)
-   quotation mark (")

In addition, short file names must not contain the following characters:

-   plus sign (+)
-   comma (,)
-   semicolon (;)
-   equals sign (=)
-   left square bracket (\[)
-   right square bracket (\])

No space is allowed preceding the vertical bar (\|) separator for the short file name/long file name syntax. Short file names may not include a space, although a long file name may. A space can exist after the separator only if the long file name of the file name begins with the space. No full-path syntax is allowed.

> [!Note]  
> The format of the FileName column of the [MsiEmbeddedUI](msiembeddedui-table.md) table is like the format Filename data type except that the vertical bar (\|) separator for the short file name/long file name syntax is not available.

 

 

 



