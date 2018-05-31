---
title: Checking Formatting and Styles
description: You should also test all styles, cascading style sheets, tables, and any other formatting used in your help system.
ms.assetid: 5AD6DF9F-E37E-40df-A2A3-19D0739414DB
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Checking Formatting and Styles

You should also test all styles, cascading style sheets, tables, and any other formatting used in your help system.

## Suggested tasks for testing

-   Make sure that styles appear the way you want them to. Check the length of topics and make sure they match your style guidelines.
-   Make sure all HTML tags have both a start and an end bracket and that expected elements and meta tags are all in place.
-   Check that headings, numbered lists, bulleted lists, and so on are all formatted using the correct tags.
-   Make sure that spacing and margins are correct.
-   View the help file on different monitors and browsers to make sure the formatting, colors, and styles are correct. If any of your styles use the same fonts as the browser you are viewing in, change your default browser font so the difference in styles is immediately apparent.
-   A useful test of whether a cascading style sheet is working or not is to add the style information using the &lt;STYLE&gt; tag with the included styles to a representative file or two. You can then compare these files to the ones using the &lt;LINK&gt; tag.
-   Change your Windows desktop color scheme and make sure the help file is still readable.
-   Test your style sheet in different versions of the same browser. For example, new developments in cascading style sheets cause them to display topics differently in Microsoft Internet Explorer 4.0 than they did in earlier version of Internet Explorer.

## Related topics

<dl> <dt>

[Develop a Process for Testing Help Files](creating-a-process-for-testing.md)
</dt> </dl>

 

 




