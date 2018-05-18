---
title: Running a Compiled Help File from the Web
description: Running a Compiled Help File from the Web
ms.assetid: 'AAF72D35-9FBA-40bd-B719-7E7BF0A08355'
---

# Running a Compiled Help File from the Web

You can add a link from a compiled help file to a page on a Web site. When a user clicks the link, a dialog box will appear that gives them the option of saving the compiled help file to their hard disk or opening it from the directory where it's located.

**To open a compiled help file from a Web page or topic file**

1.  [Create an HTML file.](creating-html-files.md)
2.  Use the following syntax to open the compiled help (.chm) file from your HTML file:

    ```
    <A HREF="file name.chm">Link text</a>
    ```

    

    where "file name.chm" is the name of the compiled help file, and "Link text" is the text link.

Make sure that the compiled help file you want to link to is located in the same directory as the topic file you are linking from.

## Note

-   If the compiled help file you are linking to is in a different directory than the topic you are linking from, you will need to enter the path to the compiled help file. For example, if the help file is located in a directory on the Web, you would need to enter the full URL including the HTTP address, &lt;A HREF="http://www.sample.com/example.chm"&gt;

## Related topics

<dl> <dt>

[About Creating a Link to Another Compiled Help File](creating-links-to-other-help-files.md)
</dt> </dl>

 

 




